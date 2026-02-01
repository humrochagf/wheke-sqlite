from collections.abc import Sequence

from sqlmodel import select

from wheke_sqlmodel import SQLModelService

from .models import Entry


class EntryRepository:
    db: SQLModelService

    def __init__(self, sqlmodel_service: SQLModelService) -> None:
        self.db = sqlmodel_service

    async def create(self, entry: Entry) -> None:
        async with self.db.session as session:
            session.add(entry)
            await session.commit()

    async def list(self) -> Sequence[Entry]:
        async with self.db.session as session:
            return (await session.exec(select(Entry))).all()
