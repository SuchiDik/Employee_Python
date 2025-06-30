from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
import crud, models, schemas
from database import SessionLocal, engine
from auth import verify_token

models.Base.metadata.create_all(bind=engine)

router = APIRouter(
    tags=["Employees"],
    prefix="/employees",
    dependencies=[Depends(verify_token)]
)


# ✅ Dependency to get DB session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.get("/", response_model=list[schemas.Employee])
def read_employees(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    return crud.get_employees(db, skip=skip, limit=limit)


@router.get("/search/", response_model=list[schemas.Employee])
def search_employees(query: str, skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    return crud.search_employees(db, query=query, skip=skip, limit=limit)


@router.post("/", response_model=schemas.Employee)
def create_employee(emp: schemas.EmployeeCreate, db: Session = Depends(get_db)):
    return crud.create_employee(db, emp)


@router.delete("/{emp_id}")
def delete_employee(emp_id: int, db: Session = Depends(get_db)):
    success = crud.delete_employee(db, emp_id)
    if not success:
        raise HTTPException(status_code=404, detail="Employee not found")
    return {"detail": "Employee deleted successfully"}