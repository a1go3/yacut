from flask import jsonify, request

from . import app, db
from .error_handlers import InvalidAPIUsage
from .models import URLMap
from .views import index


@app.route('/api/id/<short>/', methods=['GET'])
def get_full_url(short):
    url = URLMap.query.filter_by(short=short).first()
    if url is None:
        raise InvalidAPIUsage('Указанный id не найден', 404)
    return jsonify({'url': url.to_dict()['url']}), 200


@app.route('/api/id/', methods=['POST'])
def get_short_url():
    data = request.get_json()
    url = URLMap()
    url.from_dict(data)
    db.session.add(url)
    db.session.commit()
    return jsonify(url.to_dict()), 201
