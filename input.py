from gpiozero import Button
import asyncio
import json
import websockets

class ButtonHandler:
    def __init__(self, ws_url):
        self.buttons = [
            {"pin": 2,  "name": "wec"},
            {"pin": 3,  "name": "wyc"},
            {"pin": 4,  "name": "wyad"},
            {"pin": 17, "name": "wei"},
            {"pin": 27, "name": "weak"},
            {"pin": 22, "name": "dod"},
            {"pin": 10, "name": "ode"},
            {"pin": 9,  "name": "przep"},
            {"pin": 11, "name": "wyak"},
            {"pin": 5,  "name": "weja"},
            {"pin": 6,  "name": "wea"},
            {"pin": 13, "name": "czyt"},
            {"pin": 20, "name": "pisz"},
            {"pin": 26, "name": "wes"},
            {"pin": 14, "name": "wys"},
            {"pin": 15, "name": "icc"},
            {"pin": 21, "name": "clk"},  
        ]
        self.ws_url = ws_url
        self.setup_buttons()

    def setup_buttons(self):
        for button in self.buttons:
            try:
                btn = Button(button["pin"])
                btn.when_pressed = lambda b=button: self.button_pressed(b["name"])
            except Exception as e:
                print(f"Error setting up button {button['name']} on pin {button['pin']}: {e}")

    async def send_button_press(self, button_name):
        async with websockets.connect(self.ws_url) as websocket:
            data = {"type": "button_press", "button": button_name}
            await websocket.send(json.dumps(data))

    def button_pressed(self, button_name):
        asyncio.run(self.send_button_press(button_name))

    def run(self):
        asyncio.get_event_loop().run_forever()
