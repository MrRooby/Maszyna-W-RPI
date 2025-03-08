from fastapi import FastAPI, WebSocket
from fastapi.staticfiles import StaticFiles
import json
from rpi_ws281x import *
from display_manager import DisplayManager

class WebServer:
    def __init__(self):
        self.app = FastAPI()
        self.display_manager = DisplayManager(led_count=60, brightness=50)
        
        # Mount static files (your Vue.js build)
        self.app.mount("/static", StaticFiles(directory="dist", html=True), name="static")
        
        # WebSocket route
        @self.app.websocket("/ws")
        async def websocket_endpoint(websocket: WebSocket):
            await websocket.accept()
            try:
                await websocket.send_text("Connected to Raspberry Pi")
                while True:
                    data = await websocket.receive_text()
                    await self.handle_websocket_message(websocket, data)
            except Exception as e:
                print(f"WebSocket error: {e}")
    
    async def handle_websocket_message(self, websocket: WebSocket, data: str):
        try:
            message = json.loads(data)
            if message["type"] == "values":
                acc_value = message.get("ACC", 0)
                a_value = message.get("A", 0)
                s_value = message.get("S", 0)
                c_value = message.get("C", 0)
                i_value = message.get("I", 0)

                print(f"Received values:")
                print(f"ACC: {acc_value}")
                print(f"A: {a_value}")
                print(f"S: {s_value}")
                print(f"C: {c_value}")
                print(f"I: {i_value}")
                
                self.display_manager.update_small_display("acc", acc_value)
                await websocket.send_text(json.dumps({"status": "ok"}))

        except json.JSONDecodeError:
            print("Failed to parse JSON")
            await websocket.send_text(json.dumps({"status": "error", "message": "Invalid JSON"}))
