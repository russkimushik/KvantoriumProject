from app.database.models import async_session
from app.database.models import User, Direction
from sqlalchemy import select, update, delete, desc


async def set_user(tg_id, username):
    async with async_session() as session:
        user = await session.scalar(select(User).where(User.tg_id == tg_id).where(User.username == username))

        if not user:
            session.add(User(tg_id=tg_id, username = username))
            await session.commit()


async def get_directions():
    async with async_session() as session:
        return session.scalars(select(Direction))

async def get_direction(direction_id):
    async with async_session() as session:
        return await session.scalar(select(Direction).where(Direction.id == direction_id))