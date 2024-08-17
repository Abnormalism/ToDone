from fastapi import FastAPI, Depends, HTTPException
from models import TodoTable, CreateTodo
from setup import SessionLocal, Base, engine
from sqlalchemy.orm import Session

app = FastAPI()
Base.metadata.create_all(bind=engine)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.get('/todos')
async def get_todos(db: Session = Depends(get_db)):
    return db.query(TodoTable).all()

@app.post('/todos/create')
async def create_todo(create: CreateTodo, db: Session = Depends(get_db)):
    new_todo = TodoTable(**create.model_dump())

    db.add(new_todo)
    db.commit()
    db.refresh(new_todo)

    return {'message': 'Todo Created', 'todo': create}


@app.delete('/todos/delete')
async def delete_todos(id: int, db: Session = Depends(get_db)):
    todo = db.query(TodoTable).filter(id == TodoTable.id).first()

    if todo is None:
        raise HTTPException(status_code=404, detail='Todo Not Found')

    db.delete(todo)
    db.commit()

    return {'message': 'Todo Deleted', 'todo': todo}
