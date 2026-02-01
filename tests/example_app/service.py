from typing import Annotated

from fastapi import Depends
from svcs import Container
from svcs.fastapi import DepContainer
from wheke import WhekeSettings, get_service, get_settings

from wheke_sqlmodel import SQLModelService, get_sqlmodel_service

from .repository import EntryRepository


class EntryService:
    settings: WhekeSettings

    entries: EntryRepository

    def __init__(
        self,
        *,
        settings: WhekeSettings,
        sqlmodel_service: SQLModelService,
    ) -> None:
        self.settings = settings
        self.entries = EntryRepository(sqlmodel_service)


def entry_service_factory(container: Container) -> EntryService:
    return EntryService(
        settings=get_settings(container, WhekeSettings),
        sqlmodel_service=get_sqlmodel_service(container),
    )


def get_entry_service(container: Container) -> EntryService:
    return get_service(container, EntryService)


def _entry_service_injection(container: DepContainer) -> EntryService:
    return get_entry_service(container)


EntryServiceInjection = Annotated[EntryService, Depends(_entry_service_injection)]
