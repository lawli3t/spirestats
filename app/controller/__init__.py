from flask import Blueprint, jsonify

from app.dao import RelicSqlDao

relic = Blueprint('relic', __name__, url_prefix='/relic')


@relic.route('/', methods=['GET'])
def get_relics():
    return jsonify(RelicSqlDao().get_all())
