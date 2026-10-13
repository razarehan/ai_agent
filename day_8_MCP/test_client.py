import asyncio
from mcp_client import *

# async def main():
#     # Connect to the MCP server
#     client = await connect()

#     # Discover available tools
#     tools = await discover_tools(client)
#     print("Available tools:", tools)

#     # Execute a tool (e.g., "current_time") and get the result
#     tool_name = "current_time"
#     result = await execute_tool(client, tool_name)
#     print(f"Result from '{tool_name}': {result}")

#     # Disconnect from the MCP server
#     await disconnect(client)

# if __name__ == "__main__":
#     asyncio.run(main())