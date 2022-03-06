from fastapi import FastAPI, Request
app = FastAPI()

import os
import src

from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

from src.database import endpoints

BASE_DIR = os.path.dirname(__file__)
static_abs_file_path = os.path.join(BASE_DIR, "static/")
app.mount("/static", StaticFiles(directory=static_abs_file_path), name="static")

templates_abs_file_path = os.path.join(BASE_DIR, "templates/")
templates = Jinja2Templates(directory=templates_abs_file_path)


@app.get("/", response_class=HTMLResponse)
async def home_page(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})


@app.get("/about", response_class=HTMLResponse)
async def about_page(request: Request):
    return templates.TemplateResponse("about.html", {"request": request})


@app.get("/add_event", response_class=HTMLResponse)
async def add_event_page(request: Request):
    return templates.TemplateResponse("add_event.html", {"request": request})


# if __name__ == "__main__":
#     import uvicorn
#
#     uvicorn.run(src, host="127.0.0.1", port=5049)
