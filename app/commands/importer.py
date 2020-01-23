from flask import Blueprint

from app.parser import RelicParser
import click

from app.dao import RelicSqlDao

blueprint = Blueprint('import', __name__)


@blueprint.cli.command('relics')
@click.argument('filename')
def parse_relics(filename):
    parser = RelicParser()

    with open(filename, 'r') as f:
        relics = [relic for relic in parser.parse_from_file(f)]

    dao = RelicSqlDao()
    print(len(relics))
    dao.insert_all(relics)
    print(dao.get_all())

