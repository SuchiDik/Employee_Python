from sqlalchemy.orm import Session
import models, schemas


def get_employees(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Employee).offset(skip).limit(limit).all()


def search_employees(db: Session, query: str, skip: int = 0, limit: int = 100):
    return db.query(models.Employee).filter(
        models.Employee.name.contains(query) | models.Employee.dept.contains(query)
    ).offset(skip).limit(limit).all()


def get_employee(db: Session, employee_id: int):
    return db.query(models.Employee).filter(models.Employee.id == employee_id).first()


def create_employee(db: Session, emp: schemas.EmployeeCreate):
    db_emp = models.Employee(**emp.dict())
    db.add(db_emp)
    db.commit()
    db.refresh(db_emp)
    return db_emp


def delete_employee(db: Session, employee_id: int):
    emp = db.query(models.Employee).filter(models.Employee.id == employee_id).first()
    if emp:
        db.delete(emp)
        db.commit()
        return True
    return False