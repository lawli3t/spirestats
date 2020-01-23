import sqlite3
from contextlib import contextmanager
from sqlite3 import Cursor, Connection
from typing import Generator, Tuple

from flask import _app_ctx_stack

DATABASE = 'db.db'
DB_ATTRIBUTE = 'db'


def get_db() -> Connection:
    top = _app_ctx_stack.top
    if not hasattr(top, DB_ATTRIBUTE):
        top.db = sqlite3.connect(DATABASE)
        top.db.row_factory = sqlite3.Row
        setup_db(top.db)
    return top.db


def setup_db(connection: Connection) -> None:
    with open('app/tables.sql') as f:
        c = connection.cursor()
        c.execute(f.read())
        connection.commit()
        c.close()


@contextmanager
def open_cursor() -> Generator[Tuple[Connection, Cursor], None, None]:
    connection = get_db()
    cursor = get_db().cursor()

    try:
        yield cursor, connection
    finally:
        cursor.close()
