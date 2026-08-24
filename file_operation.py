from mcp.server import MCPServer

mcp = MCPServer("file_operation")


@mcp.tool()
def write_file(filename: str, content: str) -> str:
    """Write content into a file."""

    with open(filename, "w") as file:
        file.write(content)

    return f"Content successfully written to {filename}"


@mcp.tool()
def read_file(filename: str) -> str:
    """Read and return the content of a file."""

    with open(filename, "r") as file:
        content = file.read()

    return content

if __name__ == "__main__":
    mcp.run(transport="stdio")