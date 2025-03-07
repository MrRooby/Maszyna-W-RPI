import uvicorn
from server import WebServer

if __name__ == "__main__":
    server = WebServer()
    print("Starting Raspberry Pi server...")
    uvicorn.run(server.app, host="0.0.0.0", port=8000)
