#  test_mcp.py
#
#  Copyright (c) 2025 Junpei Kawamoto
#
#  This software is released under the MIT License.
#
#  http://opensource.org/licenses/mit-license.php
import base64
from collections.abc import AsyncGenerator, Iterator
from unittest.mock import MagicMock, patch
from urllib.parse import urlencode

from mcp import ClientSession, StdioServerParameters, stdio_client
import pytest

from mcp_memos.api.v1.memo_service_pb2 import Visibility
from .mock import MockServicer, API_TOKEN, MockHTTPServer, memos_server, mock_http_server

_ = memos_server
_ = mock_http_server


@pytest.fixture(scope="module")
async def mcp_client_session(memos_server: MockServicer) -> AsyncGenerator[ClientSession, None]:
    params = StdioServerParameters(
        command="uv", args=["run", "mcp-memos", "--endpoint", memos_server.endpoint, "--token", API_TOKEN]
    )
    async with stdio_client(params) as streams:
        async with ClientSession(streams[0], streams[1]) as session:
            await session.initialize()
            yield session


@pytest.fixture
def mock_requests_get() -> Iterator[MagicMock]:
    with patch("requests.get") as mock_get:
        mock_response = MagicMock()
        mock_response.status_code = 200
        mock_response.content = b"mocked http request"
        mock_response.headers = {"Content-Type": "text/plain"}
        mock_get.return_value = mock_response
        yield mock_get


@pytest.mark.anyio
async def test_list_tools(mcp_client_session: ClientSession) -> None:
    res = await mcp_client_session.list_tools()
    tools = set(tool.name for tool in res.tools)

    assert "create_memo" in tools
    assert "attach_file" in tools


@pytest.mark.anyio
@pytest.mark.parametrize(
    "visibility,expected",
    [
        ("public", Visibility.PUBLIC),
        ("protected", Visibility.PROTECTED),
        ("private", Visibility.PRIVATE),
        (None, Visibility.VISIBILITY_UNSPECIFIED),
    ],
)
async def test_create_memo(
    memos_server: MockServicer,
    mcp_client_session: ClientSession,
    visibility: str | None,
    expected: Visibility,
) -> None:
    content = "abc"

    res = await mcp_client_session.call_tool("create_memo", arguments={"content": content, "visibility": visibility})
    assert not res.isError

    memo = memos_server.memos[res.structuredContent.get("result")]
    assert memo.content == content
    assert memo.visibility == expected


@pytest.mark.anyio
async def test_attach_file(
    memos_server: MockServicer,
    mcp_client_session: ClientSession,
) -> None:
    create_meme_res = await mcp_client_session.call_tool("create_memo", arguments={"content": "abc"})
    memo_name = create_meme_res.structuredContent.get("result")

    attachments = [
        ("abc.txt", "text/plain", "text/plain"),
        ("def.txt", None, "text/plain"),
        ("ghi", None, "application/octet-stream"),
    ]
    for f, t, _ in attachments:
        res = await mcp_client_session.call_tool(
            "attach_file",
            arguments={
                "memo_name": memo_name,
                "filename": f,
                "content": base64.b64encode(f.encode("utf-8")),
                "mime_type": t,
            },
        )
        assert not res.isError

    assert len(memos_server.memos[memo_name].attachments) == 3
    for a, e in zip(memos_server.memos[memo_name].attachments, attachments):
        assert a.name in memos_server.attachments
        assert a.filename == e[0]
        assert a.type == e[2]


@pytest.mark.anyio
async def test_attach_file_from_url(
    memos_server: MockServicer,
    mock_http_server: MockHTTPServer,
    mcp_client_session: ClientSession,
) -> None:
    create_meme_res = await mcp_client_session.call_tool("create_memo", arguments={"content": "abc"})
    memo_name = create_meme_res.structuredContent.get("result")

    attachments = [
        ("abc.txt", "text/plain", "text/plain; charset=utf-8", "text/plain"),
        ("def.txt", None, "text/plain; charset=utf-8", "text/plain"),
        ("ghi.txt", None, "text/plain", "text/plain"),
    ]
    for f, t, c, _ in attachments:
        res = await mcp_client_session.call_tool(
            "attach_file",
            arguments={
                "memo_name": memo_name,
                "filename": f,
                "content": f"{mock_http_server.url}/{f}?{urlencode({'ctype': c})}",
                "mime_type": t,
            },
        )
        assert not res.isError

    assert len(memos_server.memos[memo_name].attachments) == 3
    for a, e in zip(memos_server.memos[memo_name].attachments, attachments):
        assert a.name in memos_server.attachments
        assert a.filename == e[0]
        assert a.type == e[3]


@pytest.mark.anyio
async def test_attach_file_not_found(
    memos_server: MockServicer,
    mcp_client_session: ClientSession,
) -> None:
    res = await mcp_client_session.call_tool(
        "attach_file",
        arguments={"name": "memos/not_found", "filename": "test.txt", "content": "dummy data".encode("utf-8")},
    )
    assert res.isError
