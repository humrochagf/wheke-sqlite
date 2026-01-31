from typing import ClassVar

from wheke import FeatureSettings


class SQLModelSettings(FeatureSettings):
    __feature_name__: ClassVar[str] = "sqlmodel"

    connection_string: str = "sqlite:///database.db"

    echo_operations: bool = False
