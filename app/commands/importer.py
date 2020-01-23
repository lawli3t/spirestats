import time

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
        relics = parser.parse_from_file(f)

    dao = RelicSqlDao()
    dao.insert_all(relics)

