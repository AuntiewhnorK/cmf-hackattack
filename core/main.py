from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

opportunity_star_app = FastAPI()

opportunity_star_app.mount("/static", StaticFiles(directory="static"), name="static")

templates = Jinja2Templates(directory="templates")


@opportunity_star_app.get("/", response_class=HTMLResponse)
async def home_page(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})


@opportunity_star_app.get("/add_event", response_class=HTMLResponse)
async def add_event_page(request: Request):
    return templates.TemplateResponse("add_event.html", {"request": request})