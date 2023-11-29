import logging
import os
import sys
import uvicorn
from dotenv import load_dotenv
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from lib.core.asyncio_core import gather_tasks
from lib.routes import api_router


load_dotenv(dotenv_path=os.path.join(os.path.dirname(__file__), '.env.' + os.environ['FASTAPI_ENV']))
app = FastAPI()
app.mount('/assets', StaticFiles(directory='assets'), name='assets')
app.mount('/static', StaticFiles(directory='static'), name='static')

# todo: test this out
origins = [
    # 'http://localhost',
    # 'https://localhost',
    '*'
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=[
        'GET',
        'POST'
    ],
    allow_headers=[
        '*'
    ]
)

log_level = os.environ['CHATBOT_UI_LOG_LEVEL'].lower()
logger = logging.getLogger('chatbot_ui_logger')
logging.basicConfig(
    stream=sys.stdout,
    format='%(asctime)s - %(name)s %(levelname)s - %(message)s',
    level=(10 if log_level == 'debug' else 20)
)

app.include_router(api_router)

@app.on_event('startup')
async def startup_event():
    # tasks = []
    # await gather_tasks(tasks)
    pass


@app.on_event('shutdown')
async def shutdown_event():
    # tasks = []
    # await gather_tasks(tasks)
    pass


@app.get('/full-page', response_class=HTMLResponse)
async def chatbot_full_page():
    with open('static/chatbot_full_page.html', 'r') as file:
        html = file.read()
    return html


@app.get('/widget', response_class=HTMLResponse)
async def chatbot_widget():
    with open('static/chatbot_widget.html', 'r') as file:
        html = file.read()
    return html


if __name__ == '__main__':
    uvicorn.run(
        'chatbot_ui:app',
        host='0.0.0.0',
        port=int(os.environ['CHATBOT_UI_PORT']),
        workers=int(os.environ['CHATBOT_UI_WORKERS']),
        log_level=log_level,
        reload=True
    )