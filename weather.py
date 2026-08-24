from mcp.server import MCPServer
import requests
mcp = MCPServer("Weather_server")

@mcp.tool()             #weather tool
def get_weather(location):
  url=f"https://wttr.in/{location}?format=%t"
  response=requests.get(url)
  # return response.status_code
  return response.text

if __name__ == "__main__":
    mcp.run(transport="stdio")
    