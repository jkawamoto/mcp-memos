# Memos MCP Server
[![Python Application](https://github.com/jkawamoto/mcp-memos/actions/workflows/python-app.yaml/badge.svg)](https://github.com/jkawamoto/mcp-memos/actions/workflows/python-app.yaml)
[![GitHub License](https://img.shields.io/github/license/jkawamoto/mcp-memos)](https://github.com/jkawamoto/mcp-memos/blob/main/LICENSE)
[![pre-commit](https://img.shields.io/badge/pre--commit-enabled-brightgreen?logo=pre-commit)](https://github.com/pre-commit/pre-commit)
[![Ruff](https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/astral-sh/ruff/main/assets/badge/v2.json)](https://github.com/astral-sh/ruff)

An MCP server for interacting with [Memos](https://github.com/usememos/memos).

## Tools
This MCP server provides the following tools:

### `create_memo`
Create a memo and return the name of the memo.

#### Parameters
- **content** *(string)*: The content of the memo in Markdown format.
- **visibility** *(string, optional)*: The visibility of the memo (private, protected, public).

### `attach_file`
Attach a file to a memo.

#### Parameters
- **memo_name** *(string)*: The name of the memo.
- **filename** *(string)*: The name of the file.
- **content** *(string)*: Base64 representation of a file or a URL to a file to attach to the memo.
- **mime_type** *(string, optional)*: The MIME type of the file.

## Installation
> [!NOTE]
> You'll need [`uv`](https://docs.astral.sh/uv) installed on your system to use `uvx` command.


### For Claude Desktop
Download the latest MCP bundle `mcp-memos.mcpb` from
the [Releases](https://github.com/jkawamoto/mcp-memos/releases) page,
then open the downloaded `.mcpb `file or drag it into the Claude Desktop's Settings window.

You can also manually configure this server for Claude Desktop.
Edit the `claude_desktop_config.json` file by adding the following entry under `mcpServers`:

```json
{
  "mcpServers": {
    "bear": {
      "command": "uvx",
      "args": [
        "--from",
        "git+https://github.com/jkawamoto/mcp-memos",
        "mcp-memos",
        "--endpoint",
        "<Memos server address>",
        "--token",
        "<Your token>"
      ]
    }
  }
}
```
After editing, restart the application.
For more information,
see: [For Claude Desktop Users - Model Context Protocol](https://modelcontextprotocol.io/quickstart/user).

### For Goose CLI
To enable the Bear extension in Goose CLI,
edit the configuration file `~/.config/goose/config.yaml` to include the following entry:

```yaml
extensions:
  bear:
    name: Memos
    cmd: uvx
    args: [--from, git+https://github.com/jkawamoto/mcp-memos, mcp-memos]
    envs: {
      "MEMOS_API_ENDPOINT": "<Memos server address>",
      "MEMOS_API_TOKEN": "<Your token>"
    }
    enabled: true
    type: stdio
```

### For Goose Desktop
Add a new extension with the following settings:

- **Type**: Standard IO
- **ID**: memos
- **Name**: Memos MCP Server
- **Description**: An MCP server for interacting with Memos
- **Command**: `uvx --from git+https://github.com/jkawamoto/mcp-memos mcp-memos`
- **Environment Variables**: Add `MEMOS_API_ENDPOINT` with Memos server address and `MEMOS_API_TOKEN` with your api token

For more details on configuring MCP servers in Goose Desktop,
refer to the documentation:
[Using Extensions - MCP Servers](https://block.github.io/goose/docs/getting-started/using-extensions#mcp-servers).

## License

This application is licensed under the MIT License. See the [LICENSE](LICENSE) file for more details.
