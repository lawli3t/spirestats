from typing import Sequence, Iterable

from pypika import Query

from app.models import Relic
from app.database import open_cursor

import dataclasses


class RelicDao:
    def insert_all(self, relics: Sequence[Relic]):
        raise NotImplementedError

    def get_all(self) -> Sequence[Relic]:
        raise NotImplementedError


class RelicSqlDao(RelicDao):
    def get_all(self) -> Sequence[Relic]:
        relic_table = Relic.table()
        query = Query.from_(relic_table).select('*')

        with open_cursor() as (cursor, connection):
            cursor.execute(str(query))
            return [Relic(**row) for row in cursor]

    def insert_all(self, relics: Iterable[Relic]):
        if not relics:
            return []

        fields = Relic.fields()

        query = Query.into(Relic.table()) \
            .columns(*fields) \

        for relic in relics:
            query = query.insert(*(getattr(relic, field) for field in fields))

        with open_cursor() as (cursor, connection):
            cursor.execute(str(query))
            connection.commit()
