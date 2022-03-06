from sqlalchemy.orm import Session

from src.database import models, schemas


def get_admin(db: Session, admin_id: int):
    return db.query(models.Admin).filter(models.Admin.id == admin_id).first()


def get_admin_by_email(db: Session, email: str):
    return db.query(models.Admin).filter(models.Admin.email == email).first()


def get_admins(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Admin).offset(skip).limit(limit).all()


def create_admin(db: Session, admin: schemas.AdminCreate):
    fake_hashed_password = admin.password + "notreallyhashed"
    db_admin = models.Admin(email=admin.email, hashed_password=fake_hashed_password)
    db.add(db_admin)
    db.commit()
    db.refresh(db_admin)
    return db_admin

def get_organization(db: Session, admin_id: int):
    return db.query(models.Organization).filter(models.Admin.id == admin_id).first()


def get_organizations(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Organization).offset(skip).limit(limit).all()

def get_events(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Event).offset(skip).limit(limit).all()


def create_admin_event(db: Session, event: schemas.EventCreate, admin_id: int):
    db_event = models.Event(**event.dict(), owner_id=admin_id)
    db.add(db_event)
    db.commit()
    db.refresh(db_event)
    return db_event
