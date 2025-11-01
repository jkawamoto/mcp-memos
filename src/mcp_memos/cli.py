#  cli.py
#
#  Copyright (c) 2025 Junpei Kawamoto
#
#  This software is released under the MIT License.
#
#  http://opensource.org/licenses/mit-license.php
import logging

import rich_click as click

from . import server


@click.command()
@click.option("--endpoint", required=True, help="Address to Memos server", default="localhost:5230")
@click.option("--token", envvar="MEMOS_API_TOKEN", required=True, help="Memos API token")
@click.version_option()
def main(endpoint: str, token: str) -> None:
    """Memos MCP server."""
    logging.basicConfig(level=logging.INFO)
    logger = logging.getLogger(__name__)

    logger.info("Starting MCP server (Press CTRL+D to quit)")
    server(endpoint, token).run()
    logger.info("MCP server stopped")
