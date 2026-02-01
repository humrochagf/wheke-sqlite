from collections.abc import Sequence

from fastapi import APIRouter
from starlette.status import HTTP_201_CREATED

from .models import Entry
from .service import EntryServiceInjection

router = APIRouter(tags=["entry"])


@router.get("/entries")
async def list_entries(service: EntryServiceInjection) -> Sequence[Entry]:
    return await service.entries.list()


@router.post("/entries", status_code=HTTP_201_CREATED)
async def create_entries(entry: Entry, service: EntryServiceInjection) -> None:
    await service.entries.create(entry)
