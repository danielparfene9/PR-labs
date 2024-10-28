from libs.third_party_lib import FastAPI, Path, CORSMiddleware
from libs.third_party_lib import asynccontextmanager, uvicorn
from libs.standard_lib import os
from database import connect_db, disconnect_db
from app.routes import router
from fastapi import WebSocket, WebSocketDisconnect
from threading import Thread
from fastapi.staticfiles import StaticFiles
from fastapi.responses import HTMLResponse

class ConnectionManager:
    def __init__(self):
        self.active_connections: dict[str, list[WebSocket]] = {}

    async def connect(self, websocket: WebSocket, room: str):
        await websocket.accept()
        if room not in self.active_connections:
            self.active_connections[room] = []
        self.active_connections[room].append(websocket)

    def disconnect(self, websocket: WebSocket, room: str):
        self.active_connections[room].remove(websocket)

    async def send_message(self, message: str, room: str):
        for connection in self.active_connections.get(room, []):
            await connection.send_text(message)

manager = ConnectionManager()

@asynccontextmanager
async def lifespan(app: FastAPI):
    await connect_db()
    yield
    await disconnect_db()

app = FastAPI(lifespan=lifespan)

app.include_router(router)

app_ws = FastAPI()

@app_ws.websocket("/ws/{room}")
async def websocket_endpoint(websocket: WebSocket, room: str):
    await manager.connect(websocket, room)
    try:
        while True:
            data = await websocket.receive_text()
            await manager.send_message(f"{data}", room)
    except WebSocketDisconnect:
        manager.disconnect(websocket, room)
        await manager.send_message("A user has left the chat", room)
        
@app_ws.get("/", response_class=HTMLResponse)
async def get_chat_page():
    with open("room.html") as f:
        return HTMLResponse(content=f.read())

def run_websocket_server():
    uvicorn.run("main:app_ws", host="0.0.0.0", port=8000, reload=False)

def run_http_server():
    uvicorn.run("main:app", host="0.0.0.0", port=8001, reload=False)

if __name__ == "__main__":
    websocket_thread = Thread(target=run_websocket_server)
    http_thread = Thread(target=run_http_server)

    websocket_thread.start()
    http_thread.start()

    websocket_thread.join()
    http_thread.join()
