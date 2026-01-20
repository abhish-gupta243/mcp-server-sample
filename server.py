from mcp.server.fastmcp import FastMCP
from starlette.applications import Starlette
from starlette.middleware.cors import CORSMiddleware
from starlette.routing import Mount

mcp = FastMCP("OpenShift-Helper")

@mcp.tool()
def get_status(): 
    return "The mcp server is running on OpenShift!"

app = Starlette(
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