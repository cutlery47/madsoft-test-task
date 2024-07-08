from src.abstract.abstract_repository import AbstractCRUDRepository
from src.exceptions.repository_exc import DatabaseMemeNotFoundException, InternalRepositoryException
from src.storage.models.meme import Meme

from sqlalchemy.ext.asyncio import AsyncEngine, async_sessionmaker, create_async_engine
from sqlalchemy import select, update, delete
from sqlalchemy.exc import SQLAlchemyError

from loguru import logger
from typing import List

import os

DRIVER = os.getenv('DB_DRIVER')
USERNAME = os.getenv('DB_USERNAME')
PASSWD = os.getenv('DB_PASSWORD')
HOST = os.getenv('DB_HOST')
PORT = os.getenv('DB_PORT')
NAME = os.getenv('DB_NAME')

class Repository(AbstractCRUDRepository):

    def __init__(self):
        self.engine = create_async_engine(f"{DRIVER}://{USERNAME}:{PASSWD}@{HOST}:{PORT}/{NAME}")
        self.sessionmaker = async_sessionmaker(bind=self.engine, expire_on_commit=False)

    async def read(self, *filters) -> List[Meme]:
        async with self.sessionmaker() as session:
            try:
                query = select(Meme).where(*filters)
                result = await session.execute(query)
                if len(result.scalars().all()) == 0:
                    raise DatabaseMemeNotFoundException()
            except SQLAlchemyError as exc:
                logger.error(f'{type(exc)} raised {exc.args[0]}')
                raise InternalRepositoryException()
            else:
                return [meme for meme in result.scalars().all()]

    async def create(self, item: Meme):
        async with self.sessionmaker() as session:
            try:
                session.add(item)
            except SQLAlchemyError as exc:
                logger.error(f'{type(exc)} raised {exc.args[0]}')
                await session.rollback()
                raise InternalRepositoryException()
            else:
                await session.commit()

    async def update(self, meme: Meme, *filters):
        async with self.sessionmaker() as session:
            try:
                dict_meme = meme_to_dict(meme)
                query = update(Meme).where(*filters).values(dict_meme)
                result = await session.execute(query)
                if result.rowcount == 0:
                    raise DatabaseMemeNotFoundException()
            except SQLAlchemyError as exc:
                logger.error(f'{type(exc)} raised {exc.args[0]}')
                await session.rollback()
                raise InternalRepositoryException()
            else:
                await session.commit()

    async def delete(self, *filters):
        async with self.sessionmaker() as session:
            try:
                query = delete(Meme).where(*filters)
                result = await session.execute(query)
                if result.rowcount == 0:
                    raise DatabaseMemeNotFoundException()
            except SQLAlchemyError as exc:
                logger.error(f'{type(exc)} raised {exc.args[0]}')
                await session.rollback()
                raise InternalRepositoryException()
            else:
                await session.commit()

def meme_to_dict(meme: Meme) -> dict:
    dict_meme = meme.__dict__
    dict_meme.pop('_sa_instance_state', None)
    return dict_meme
