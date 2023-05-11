from fastapi import FastAPI, HTTPException
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, Column, Integer, String, Boolean
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

Base = declarative_base()


#Todo model
class Todo(Base):
    __tablename__ = "todos"
    id = Column(Integer, primary_key=True)
    title = Column(String(255))
    completed = Column(Boolean, default=False)



engine = create_engine("sqlite:///todos.db")
Base.metadata.create_all(engine)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

app = FastAPI()
templates = Jinja2Templates(directory="templates")


@app.exception_handler(HTTPException)
async def http_exception_handler(request, exc):
    return HTMLResponse(content=str(exc.detail), status_code=exc.status_code)


@app.get("/")
async def read_todos(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    todos = db.query(Todo).offset(skip).limit(limit).all()
    return templates.TemplateResponse("todos.html", {"request": request, "todos": todos})


@app.post("/")
async def create_todo(todo: TodoCreate, db: Session = Depends(get_db)):
    db_todo = Todo(title=todo.title)
    db.add(db_todo)
    db.commit()
    db.refresh(db_todo)
    return {"todo": db_todo}


@app.put("/{todo_id}")
async def update_todo(todo_id: int, todo: TodoUpdate, db: Session = Depends(get_db)):
    db_todo = db.query(Todo).filter(Todo.id == todo_id).first()
    if not db_todo:
        raise HTTPException(status_code=404, detail="Todo not found")
    if todo.title:
        db_todo.title = todo.title
    if todo.completed is not None:
        db_todo.completed = todo.completed
    db.commit()
    db.refresh(db_todo)
    return {"todo": db_todo}


@app.delete("/{todo_id}")
async def delete_todo(todo_id: int, db: Session = Depends(get_db)):
    db_todo = db.query(Todo).filter(Todo.id == todo_id).first()
    if not db_todo:
        raise HTTPException(status_code=404, detail="Todo not found")
    db.delete(db_todo)
    db.commit()
    return {"result": "Todo deleted successfully"}
