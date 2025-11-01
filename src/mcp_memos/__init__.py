#  __init__.py
#
#  Copyright (c) 2025 Junpei Kawamoto
#
#  This software is released under the MIT License.
#
#  http://opensource.org/licenses/mit-license.php
from collections.abc import AsyncIterator
from contextlib import asynccontextmanager
from dataclasses import dataclass
from functools import partial
from typing import Any, Literal

from mcp.server import FastMCP
from mcp.server.fastmcp import Context
from pydantic import Field

from .api.v1.memo_service_pb2 import Visibility
from .client import Memos


@dataclass
class AppContext:
    client: Memos


@asynccontextmanager
async def app_lifespan(_server: FastMCP, target: str, token: str) -> AsyncIterator[AppContext]:
    async with Memos(target, token) as cli:
        yield AppContext(client=cli)


def server(target: str, token: str) -> FastMCP:
    mcp = FastMCP("Memos", lifespan=partial(app_lifespan, target=target, token=token))

    @mcp.tool()
    async def create_memo(
        ctx: Context[Any, AppContext],
        content: str = Field(description="the content of the memo in Markdown format."),
        visibility: Literal["private", "protected", "public"] | None = Field(
            description="the visibility of the memo.", default=None
        ),
    ) -> str:
        """Create a memo and return the name of the memo."""
        if visibility == "private":
            v = Visibility.PRIVATE
        elif visibility == "protected":
            v = Visibility.PROTECTED
        elif visibility == "public":
            v = Visibility.PUBLIC
        else:
            v = Visibility.VISIBILITY_UNSPECIFIED
        res = await ctx.request_context.lifespan_context.client.create_memo(content, v)
        return res.name

    return mcp
