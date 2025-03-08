import uvicorn
from server import WebServer
from display_manager import DisplayManager

disp_man = DisplayManager(40, 40)

if __name__ == "__main__":
    #server = WebServer()
    #print("Starting Raspberry Pi server...")
    #uvicorn.run(server.app, host="0.0.0.0", port=8000)
    disp_man.czyt.turn_on_line(True)
    disp_man.main_top.data_flow(choice=True)    
