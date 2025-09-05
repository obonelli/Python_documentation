from typing import List, Optional
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select

from app.models import Item


async def list_items(session: AsyncSession) -> List[Item]:
    result = await session.execute(select(Item).order_by(Item.name))
    return result.scalars().all()


async def get_item(session: AsyncSession, item_id: int) -> Optional[Item]:
    return await session.get(Item, item_id)


async def create_item(
    session: AsyncSession, name: str, price: float, in_stock: bool
) -> Item:
    # ⬇️ NO setees id: deja que MySQL lo autogenere
    row = Item(name=name, price=price, in_stock=in_stock)
    session.add(row)
    await session.commit()
    await session.refresh(row)
    return row


async def update_item(
    session: AsyncSession, item_id: int, name: str, price: float, in_stock: bool
) -> Optional[Item]:
    row = await session.get(Item, item_id)
    if not row:
        return None
    row.name = name
    row.price = price
    row.in_stock = in_stock
    await session.commit()
    await session.refresh(row)
    return row


async def delete_item(session: AsyncSession, item_id: int) -> bool:
    row = await session.get(Item, item_id)
    if not row:
        return False
    await session.delete(row)
    await session.commit()
    return True
