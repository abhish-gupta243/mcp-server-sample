from mcp.server.fastmcp import FastMCP
from starlette.applications import Starlette
from starlette.middleware.cors import CORSMiddleware
from starlette.routing import Mount
import uvicorn

# 1. Initialize FastMCP
mcp = FastMCP("OpenShift-Helper")

@mcp.tool()
def get_status(): 
    return "The mcp server is running on OpenShift!"

app = Starlette(
    routes=[
        Mount("/", app=mcp.sse_app()), 
    ]
)

# 3. Add standard CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["GET", "POST", "OPTIONS"],
    allow_headers=["*"],
)

if __name__ == "__main__":
    uvicorn.run(
        app, 
        host="0.0.0.0", 
        port=8000, 
        proxy_headers=True, 
        forwarded_allow_ips="*"
    )