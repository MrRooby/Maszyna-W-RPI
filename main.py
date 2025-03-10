import uvicorn
from server import WebServer
from display_manager import DisplayManager

# Initialize both led strips (lenght left side, right side, brightness)
disp_man = DisplayManager(40, 7, 40)

if __name__ == "__main__":
    server = WebServer()
    print("Starting Raspberry Pi server...")
    uvicorn.run(server.app, host="0.0.0.0", port=8000)
