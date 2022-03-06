from cgitb import text
from typing import List
import uvicorn

from fastapi import Depends, FastAPI, HTTPException, Request, Form
from sqlalchemy.orm import Session
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles

from . import crud, models, schemas
from .database import SessionLocal, engine

models.Base.metadata.create_all(bind=engine)

app = FastAPI()
templates = Jinja2Templates(directory="templates/")

# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.get("/")
async def root():
    return {"message":"Hello World!"}

@app.post("/admins/", response_model=schemas.Admin)
def create_admin(admin: schemas.AdminCreate, db: Session = Depends(get_db)):
    db_admin = crud.get_admin_by_email(db, email=admin.email)
    if db_admin:
        raise HTTPException(status_code=400, detail="Email already registered")
    return crud.create_user(db=db, admin=admin)


@app.get("/admins/", response_model=List[schemas.Admin])
def read_admins(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    admins = crud.get_admins(db, skip=skip, limit=limit)
    return admins


@app.get("/admins/{admin_id}", response_model=schemas.Admin)
def read_admin(admin_id: int, db: Session = Depends(get_db)):
    db_admin = crud.get_admin(db, admin_id=admin_id)
    if db_admin is None:
        raise HTTPException(status_code=404, detail="User not found")
    return db_admin


@app.post("/admins/{admin_id}/events/", response_model=schemas.Event)
def create_event_for_admin(
    admin_id: int, event: schemas.EventCreate, db: Session = Depends(get_db)
):
    return crud.create_admin_event(db=db, event=event, admin_id=admin_id)


@app.get("/events/", response_model=List[schemas.Event])
def read_events(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    events = crud.get_events(db, skip=skip, limit=limit)
    return events

@app.get("/form", response_class=HTMLResponse)
def get_form(request:Request):
    return templates.TemplateResponse("form.html", {"request": request})

@app.post("/form", response_class=HTMLResponse)
async def post_form(request: Request, organization_name: str = Form(...), college_name: str = Form(...)):
    print(f'organization_name: {organization_name}')
    print(f'college_name: {college_name}')
    return templates.TemplateResponse("form.html", {"request": request})

if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=5049)