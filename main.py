from fastapi import FastAPI
from dotenv import dotenv_values
from pymongo import MongoClient
from contextlib import asynccontextmanager

from routes import router


config = dotenv_values(".env")

async def db_connection():
    db = MongoClient(config["ATLAS_URI"]).sample_restaurants.restaurants
    print(db)
    return db

@asynccontextmanager
async def db_lifespan(app: FastAPI):
    try:
        conn = await db_connection()
        app.restaurants = conn
        print("Conectado ao MongoDB!")
    except Exception as e:
        raise Exception("Erro ao abrir conexão com MongoDB", e)

    yield

    print("Encerrando conexão com MongoDB")

app = FastAPI(lifespan=db_lifespan)

app.include_router(router)