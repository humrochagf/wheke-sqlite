from collections.abc import Generator
from contextlib import contextmanager

from sqlalchemy import Engine
from sqlmodel import Session, SQLModel, create_engine
from svcs import Container
from wheke import WhekeSettings, get_service, get_settings

from ._settings import SQLModelSettings


class SQLModelService:
    engine: Engine

    def __init__(self, *, sqlmodel_settings: SQLModelSettings) -> None:
        self.engine = create_engine(sqlmodel_settings.connection_string)

    @property
    @contextmanager
    def session(self) -> Generator[Session]:
        with Session(self.engine) as _session:
            yield _session

    def create_db(self) -> None:
        SQLModel.metadata.create_all(self.engine)

    def dispose(self) -> None:
        self.engine.dispose()


def sqlmodel_service_factory(container: Container) -> SQLModelService:
    settings = get_settings(container, WhekeSettings).get_feature(SQLModelSettings)

    return SQLModelService(sqlmodel_settings=settings)


def get_sqlmodel_service(container: Container) -> SQLModelService:
    return get_service(container, SQLModelService)
