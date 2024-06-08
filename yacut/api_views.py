from http import HTTPStatus

from flask import jsonify, request
import re
from . import app, db
from .error_handlers import InvalidAPIUsage
from .models import URLMap
from .views import get_unique_short_id


@app.route('/api/id/<short>/', methods=['GET'])
def get_full_url(short):
    url = URLMap.query.filter_by(short=short).first()
    if url is None:
        raise InvalidAPIUsage('Указанный id не найден', HTTPStatus.NOT_FOUND)
    return jsonify({'url': url.to_dict()['url']}), HTTPStatus.OK


@app.route('/api/id/', methods=['POST'])
def get_short_url():
    try:
        request.get_json()
    except Exception:
        raise InvalidAPIUsage('Отсутствует тело запроса')

    data = request.get_json()

    if data is None:
        raise InvalidAPIUsage('Отсутствует тело запроса')

    if 'custom_id' not in data or data['custom_id'] == '':
        data['custom_id'] = get_unique_short_id()

    if 'url' not in data:
        raise InvalidAPIUsage('"url" является обязательным полем!')

    if URLMap.query.filter_by(short=data['custom_id']).first() is not None:
        raise InvalidAPIUsage(
            'Предложенный вариант короткой ссылки уже существует.')

    if not re.match(r'[A-Za-z0-9_]+$', data['custom_id']) or len(
            data['custom_id']) > 16:
        raise InvalidAPIUsage(
            'Указано недопустимое имя для короткой ссылки')

    url = URLMap()
    url.from_dict(data)
    db.session.add(url)
    db.session.commit()
    return jsonify(url.to_dict()), 201
