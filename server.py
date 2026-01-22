from mcp.server.fastmcp import FastMCP
from mcp.server.transport_security import TransportSecuritySettings

# Initialize FastMCP with DNS rebinding protection DISABLED
mcp = FastMCP(
    "OpenShift-Helper",
    transport_security=TransportSecuritySettings(
        enable_dns_rebinding_protection=False,
    )
)

@mcp.tool()
def get_status() -> str:
    """Get the current status of the MCP server"""
    return "The MCP server is running on OpenShift!"

@mcp.tool()
def echo(message: str) -> str:
    """Echo back a message"""
    return f"Echo: {message}"

# Use the streamable HTTP app directly
# This is the simplest approach - no extra wrappers needed
app = mcp.streamable_http_app()