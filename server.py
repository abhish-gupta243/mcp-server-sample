from mcp.server.fastmcp import FastMCP
from mcp.server.transport_security import TransportSecuritySettings
from starlette.applications import Starlette
from starlette.middleware.cors import CORSMiddleware
from starlette.routing import Mount

# Initialize FastMCP with DNS rebinding protection DISABLED
mcp = FastMCP(
    "OpenShift-Helper",
    transport_security=TransportSecuritySettings(
        enable_dns_rebinding_protection=False,
    )
)

@mcp.tool()
def get_status(): 
    return "The mcp server is running on OpenShift!"

app = Starlette(
    routes=[
        Mount("/", app=mcp.sse_app()), 
    ]
)

# Add CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["GET", "POST", "OPTIONS"],
    allow_headers=["*"],
)