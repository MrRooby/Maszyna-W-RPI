from fastapi import FastAPI, WebSocket
from fastapi.staticfiles import StaticFiles
import json
from rpi_ws281x import *
from display_manager import DisplayManager

class WebServer:
    def __init__(self):
        self.app = FastAPI()
        self.disp_man = DisplayManager(7, 60, 50)
        
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
                acc_value = message["ACC"]
                a_value = message["A"]
                s_value = message["S"]
                c_value = message["C"]
                i_value = message["I"]
                icc_value = message["icc"]
                wec_value = message["wec"]
                wyc_value = message["wyc"]
                busA_value = message["busA"]
                busS_value = message["busS"]
                wyad_value = message["wyad"]
                wei_value = message["wei"]
                iak_value = message["iak"]
                dak_value = message["dak"]
                weak_value = message["weak"]
                weja_value = message["weja"]
                wyak_value = message["wyak"]
                czyt_value = message["czyt"]
                pisz_value = message["pisz"]
                pao_addrs = message["addrs"]
                pao_args = message["args"]
                pao_vals = message["vals"]

                print("Received values:")
                print(f"ACC:  {acc_value}")
                print(f"A:    {a_value}")
                print(f"S:    {s_value}")
                print(f"C:    {c_value}")
                print(f"I:    {i_value}")
                print(f"icc:  {icc_value}")
                print(f"wec:  {wec_value}")
                print(f"wyc:  {wyc_value}")
                print(f"busA: {busA_value}")
                print(f"busS: {busS_value}")
                print(f"wyad: {wyad_value}")
                print(f"wei:  {wei_value}")
                print(f"iak:  {iak_value}")
                print(f"dak:  {dak_value}")
                print(f"weak: {weak_value}")
                print(f"weja: {weja_value}")
                print(f"wyak: {wyak_value}")
                print(f"czyt: {czyt_value}")
                print(f"pisz: {pisz_value}")
                print(f"pao_addrs: {pao_addrs}")
                print(f"pao_args: {pao_args}")
                print(f"pao_vals: {pao_vals}")

                # Left side LEDs
                self.disp_man.busA.data_flow(choice=busA_value)
                self.disp_man.icc.turn_on_line(icc_value)
                self.disp_man.wec.turn_on_line(wec_value)
                self.disp_man.wyc.turn_on_line(wyc_value)
                self.disp_man.c.display_value(c_value)
                self.disp_man.wyad.turn_on_line(wyad_value)
                self.disp_man.i.display_value(i_value)
                self.disp_man.wei.turn_on_line(wei_value)
                self.disp_man.weja.turn_on_line(weja_value)
                self.disp_man.przep.turn_on_line(przep_value)
                self.disp_man.dak.turn_on_line(dak_value)
                self.disp_man.iak.turn_on_line(iak_value)
                self.disp_man.weak.turn_on_line(weak_value)
                self.disp_man.acc.display_value(acc_value)

                # Right side LEDs
                self.disp_man.wea.turn_on_line(wea_value)
                self.disp_man.a.display_value(a_value)
                self.disp_man.PaO_0.display_line(pao_addrs[0], pao_args[0], pao_vals[0])
                self.disp_man.PaO_1.display_line(pao_addrs[1], pao_args[1], pao_vals[1])
                self.disp_man.czyt.turn_on_line(czyt_value)
                self.disp_man.PaO_2.display_line(pao_addrs[2], pao_args[2], pao_vals[2])
                self.disp_man.pisz.turn_on_line(pisz_value)
                self.disp_man.PaO_3.display_line(pao_addrs[3], pao_args[3], pao_vals[3])
                self.disp_man.wyak.turn_on_line(wyak_value)
                self.disp_man.s.display_value(s_value)
                self.disp_man.wes.turn_on_line(wes_value)
                self.disp_man.wys.turn_on_line(wys_value)
                self.disp_man.busS.data_flow(choice=busS_value)

                await websocket.send_text(json.dumps({"status": "ok"}))

        except json.JSONDecodeError:
            print("Failed to parse JSON")
            await websocket.send_text(json.dumps({"status": "error", "message": "Invalid JSON"}))
