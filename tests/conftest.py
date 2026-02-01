from collections.abc import Generator
from pathlib import Path

import pytest
from fastapi.testclient import TestClient
from typer.testing import CliRunner
from wheke import WhekeSettings

from wheke_sqlmodel import SQLITE_DRIVER, SQLModelSettings

from .example_app import build_wheke


@pytest.fixture
def settings(tmp_path: Path) -> WhekeSettings:
    sqlmodel_settings = SQLModelSettings(
        connection_string=f"{SQLITE_DRIVER}:///{tmp_path / 'test.db'}",
        echo_operations=True,
    )
    return WhekeSettings(
        features={
            sqlmodel_settings.__feature_name__: sqlmodel_settings.model_dump(),
        }
    )


@pytest.fixture
def client(settings: WhekeSettings) -> Generator[TestClient]:
    wheke = build_wheke(settings)
    runner = CliRunner()
    cli = wheke.create_cli()

    # setup
    result = runner.invoke(cli, ["sqlmodel", "create-db"])
    assert result.exit_code == 0

    with TestClient(build_wheke(settings).create_app()) as client:
        yield client

    # teardown
    result = runner.invoke(cli, ["sqlmodel", "drop-db"])
    assert result.exit_code == 0
