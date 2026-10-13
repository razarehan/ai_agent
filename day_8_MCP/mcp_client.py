from fastmcp import Client

async def connect():
  """
  Connect to the MCP server and return the client instance.
  """
  client = Client("server.py")
  await client.__aenter__()
  print("Connected to MCP server.")
  return client

async def disconnect(client):
  """
  Disconnect from the MCP server.
  """
  await client.__aexit__(None, None, None)
  print("Disconnected from MCP server.")

async def discover_tools(client):
  """
  Discover available tools from the MCP server.
  """
  tools = await client.list_tools()
  return tools

async def execute_tool(client, tool_name, arguments = None):
  """
  Execute a tool on the MCP server if the arguments is none and return the result.
  """
  arguments = {}
  result = await client.call_tool(tool_name, arguments)
  return result