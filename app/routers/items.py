from typing import List
from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession

from app.db import get_session
from app.schemas import ItemCreate, ItemOut
from app.services import items_service as svc

router = APIRouter()


@router.get("/items", response_model=List[ItemOut])
async def list_items(session: AsyncSession = Depends(get_session)):
    rows = await svc.list_items(session)
    return [
        ItemOut(id=r.id, name=r.name, price=float(r.price), in_stock=r.in_stock)
        for r in rows
    ]


@router.post("/items", response_model=ItemOut, status_code=status.HTTP_201_CREATED)
async def create_item(
    payload: ItemCreate, session: AsyncSession = Depends(get_session)
):
    row = await svc.create_item(session, payload.name, payload.price, payload.in_stock)
    return ItemOut(
        id=row.id, name=row.name, price=float(row.price), in_stock=row.in_stock
    )


@router.get("/items/{item_id}", response_model=ItemOut)
async def get_item(item_id: str, session: AsyncSession = Depends(get_session)):
    row = await svc.get_item(session, item_id)
    if not row:
        raise HTTPException(status_code=404, detail="Item not found")
    return ItemOut(
        id=row.id, name=row.name, price=float(row.price), in_stock=row.in_stock
    )


@router.put("/items/{item_id}", response_model=ItemOut)
async def update_item(
    item_id: str, payload: ItemCreate, session: AsyncSession = Depends(get_session)
):
    row = await svc.update_item(
        session, item_id, payload.name, payload.price, payload.in_stock
    )
    if not row:
        raise HTTPException(status_code=404, detail="Item not found")
    return ItemOut(
        id=row.id, name=row.name, price=float(row.price), in_stock=row.in_stock
    )


@router.delete("/items/{item_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_item(item_id: str, session: AsyncSession = Depends(get_session)):
    ok = await svc.delete_item(session, item_id)
    if not ok:
        raise HTTPException(status_code=404, detail="Item not found")
    return None
