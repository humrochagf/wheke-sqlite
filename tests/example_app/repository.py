from collections.abc import Sequence

from sqlmodel import select

from wheke_sqlmodel import SQLModelRepository

from .models import Entry


class EntryRepository(SQLModelRepository):
    async def create(self, entry: Entry) -> None:
        async with self.db.session as session:
            session.add(entry)
            await session.commit()

    async def list(self) -> Sequence[Entry]:
        async with self.db.session as session:
            return (await session.exec(select(Entry))).all()
