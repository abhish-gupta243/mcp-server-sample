from mcp.server.fastmcp import FastMCP
from starlette.applications import Starlette
from starlette.middleware.cors import CORSMiddleware
from starlette.routing import Mount
from starlette.requests import Request
from starlette.responses import Response
from starlette.middleware.base import BaseHTTPMiddleware

# Initialize FastMCP
mcp = FastMCP("OpenShift-Helper")

@mcp.tool()
def get_status(): 
    return "The mcp server is running on OpenShift!"

# Custom middleware to strip/fix host header issues
class HostHeaderFixMiddleware(BaseHTTPMiddleware):
    async def dispatch(self, request: Request, call_next):
        # Allow any host
        return await call_next(request)

app = Starlette(
    routes=[
        Mount("/", app=mcp.sse_app()), 
    ]
)

# Add the host fix middleware FIRST
app.add_middleware(HostHeaderFixMiddleware)

# Add standard CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["GET", "POST", "OPTIONS"],
    allow_headers=["*"],
)