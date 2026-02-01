from ._service import SQLModelService


class SQLModelRepository:
    db: SQLModelService

    def __init__(self, sqlmodel_service: SQLModelService) -> None:
        self.db = sqlmodel_service
