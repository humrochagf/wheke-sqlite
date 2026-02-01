from sqlmodel import Field, SQLModel


class Entry(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    value: str
