from mcp.server.fastmcp import FastMCP
from starlette.applications import Starlette
from starlette.middleware.cors import CORSMiddleware
from starlette.routing import Mount
import uvicorn

# 1. Initialize FastMCP
mcp = FastMCP("OpenShift-Helper")

@mcp.tool()
def get_cluster_status() -> str:
    """Returns a simple status message from the cluster."""
    return "The mcp server is working."

app = Starlette(
    debug=True,
    routes=[
        Mount("/", app=mcp.sse_app()), 
    ]
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["GET", "POST", "OPTIONS"],
    allow_headers=["*"],
)

if __name__ == "__main__":
    # Use the 'app' instance, not 'mcp.run()'
    uvicorn.run(app, host="0.0.0.0", port=8000)