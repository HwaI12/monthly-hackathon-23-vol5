import os
from fastapi import FastAPI, Depends, Query, status
from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder
from sqlalchemy import Column, TIMESTAMP, Integer, String, create_engine,Text
from sqlalchemy.orm import sessionmaker
from starlette.middleware.cors import CORSMiddleware
from sqlalchemy import Column, TIMESTAMP, Integer, String,Text
from sqlalchemy.ext.declarative import declarative_base
import uvicorn
from schema import *


ROOT_PATH="/api"

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=['*'],
    allow_credentials=True,
    allow_methods=['*'],
    allow_headers=['*']
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
Session = sessionmaker(autocommit=False, autoflush=False, bind=engine)

def session():
    db = Session()
    try:
        yield db
    finally:
        db.close()

Base = declarative_base(bind=engine)
class User(Base):
    __tablename__ = "users"
    __table_args__ = {"autoload": True}
    id = Column(Integer, primary_key = True, nullable=False)
    name = Column(Text, nullable=False)
    password = Column(Text,nullable=False)

# GetItemByName
@app.get('%s/item' % ROOT_PATH)
def get_items(db: Session = Depends(session)):
    result_set = db.query(User).all()    
    response_body = jsonable_encoder({"list": result_set})
    return JSONResponse(status_code=status.HTTP_200_OK, content=response_body)

# CreateItem
@app.post('%s/item' % ROOT_PATH)
def create_item(request: UserRequest, db: Session = Depends(session)):
    item = User(
                name = request.name,
                price = request.password
            )
    db.add(item)
    db.commit()
    response_body = jsonable_encoder({"item_id" : item.id})
    return JSONResponse(status_code=status.HTTP_200_OK, content=response_body)

# UpdateItem
# passwordをupdateするのは良くないのでこれは参考程度
@app.put('%s/item/{id}' % ROOT_PATH)
def update_item(id: int, request: UserRequest, db: Session = Depends(session)):
    item = db.query(User).filter(User.id == id).first()
    if item is None:
            return JSONResponse(status_code=status.HTTP_404_NOT_FOUND)
    item.name = request.name
    item.price = request.password
    db.commit()
    return JSONResponse(status_code=status.HTTP_200_OK)

# DeleteItem
@app.delete('%s/item/{id}' % ROOT_PATH)
def delete_item(id: int, db: Session = Depends(session)):
    db.query(User).filter(User.id == id).delete()
    db.commit()
    return JSONResponse(status_code=status.HTTP_200_OK)

@app.get("/api/hoge")
def index1():
    return {"message": "hogehoge"}


@app.get("/api/fuga")
def index2():
    return {"message": "fugafuga"}


# Dockerfileからuvicorn(FastAPIサーバー）を起動する
if __name__ == "__main__":
    uvicorn.run(
        app="main:app",
        host="0.0.0.0",
        reload=True,
        port=3000,
        log_level="debug",)
