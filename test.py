import typing
import sqlite3


class Parent(typing.NamedTuple):
    id: int
    name: str

    def test(self):
        return self.name * 2


class Child(typing.NamedTuple):
    id: int
    parent_id: int
    name: str


connection = sqlite3.connect(':memory:')
connection.row_factory = sqlite3.Row

cursor = connection.cursor()

cursor.execute("""
    CREATE TABLE parent (
        id INTEGER PRIMARY KEY,
        name TEXT NOT NULL
    )
""")

cursor.execute("""
    CREATE TABLE child (
        id INTEGER PRIMARY KEY,
        parent_id INTEGER,
        name TEXT NOT NULL
    );
""")

parent = Parent(None, 'qq')

cursor.execute("""
    INSERT INTO parent VALUES(:id, :name)
""", parent._asdict())

cursor.execute("""
    INSERT INTO child VALUES(:id, :parent_id, :name)
""", [1, 1, 'asdasd'])

cursor.execute('SELECT * FROM parent')
print(Parent(**cursor.fetchone()))

