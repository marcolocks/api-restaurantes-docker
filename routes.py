from http.client import responses
from bson import ObjectId
from fastapi import APIRouter, Body, Request, Response, HTTPException, status, Query
from fastapi.encoders import jsonable_encoder
from typing import List, Annotated

from models import Restaurant

router = APIRouter(prefix="", tags=['Restaurants'])

@router.get("/")
async def default():
    res = {"message": "API de Restaurantes"}
    return res

@router.get("/restaurants")
async def restaurants(request: Request)->list[Restaurant]:
    db = request.app.restaurants
    response = list(db.find(limit=10))
    for item in response:
        item["_id"] = str(item["_id"])
    return response
