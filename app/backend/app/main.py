import os
from fastapi import FastAPI, Depends, status
from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder
from sqlalchemy import Column, Integer, String, create_engine, Text
from sqlalchemy.orm import sessionmaker
from starlette.middleware.cors import CORSMiddleware
from sqlalchemy.ext.declarative import declarative_base
import uvicorn
from schema import UserRequest


ROOT_PATH = "/api"

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)

print(os.getenv("PATH"))
SQLALCHEMY_DATABASE_URI = 'postgresql://{user}:{password}@{host}:{port}/{name}'.format(**{
    # 'user': os.environ.get("DB_USER"),
    # 'password':os.environ.get("DB_PASSWORD"),
    # 'host': os.environ.get("DB_HOST"),
    # 'name': os.environ.get("DB_NAME")
    'user': 'postgres',
    'password':'password',
    'host': 'host.docker.internal',
    'port': 5432,
    'name': 'users'
})

engine = create_engine(SQLALCHEMY_DATABASE_URI)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base(bind=engine)


class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, nullable=False)
    name = Column(Text, nullable=False)
    password = Column(Text, nullable=False)

    def __init__(self, name: str, password: str):
        self.name = name
        self.password = password


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.get(f"{ROOT_PATH}/item")
def get_items(db=Depends(get_db)):
    result_set = db.query(User).all()
    response_body = jsonable_encoder({"list": result_set})
    return JSONResponse(status_code=status.HTTP_200_OK, content=response_body)


@app.post(f"{ROOT_PATH}/item")
def create_item(request: UserRequest, db=Depends(get_db)):
    item = User(name=request.name, password=request.password)
    db.add(item)
    db.commit()
    response_body = jsonable_encoder({"item_id": item.id})
    return JSONResponse(status_code=status.HTTP_200_OK, content=response_body)


@app.put(f"{ROOT_PATH}/item/{id}")
def update_item(id: int, request: UserRequest, db=Depends(get_db)):
    item = db.query(User).filter(User.id == id).first()
    if item is None:
        return JSONResponse(status_code=status.HTTP_404_NOT_FOUND)
    item.name = request.name
    item.password = request.password
    db.commit()
    return JSONResponse(status_code=status.HTTP_200_OK)


@app.delete(f"{ROOT_PATH}/item/{id}")
def delete_item(id: int, db=Depends(get_db)):
    db.query(User).filter(User.id == id).delete()
    db.commit()
    return JSONResponse(status_code=status.HTTP_200_OK)


@app.get(f"{ROOT_PATH}/hoge")
def index1():
    return {"message": "hogehoge"}


@app.get(f"{ROOT_PATH}/fuga")
def index2():
    return {"message": "fugafuga"}


if __name__ == "__main__":
    uvicorn.run(
        app="main:app",
        host="0.0.0.0",
        reload=True,
        port=3000,
        log_level="debug",
    )
