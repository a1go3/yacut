import re
from http import HTTPStatus

from flask import jsonify, request
from settings import MAX_LENGTH_SHORT_URL, REGEX

from . import app, db
from .error_handlers import InvalidAPIUsage
from .messages import (ID_NOT_FOUND, INV_SHORT_URL, SHORT_URL_EXIST, STAY_OUT,
                       URL_REQ)
from .models import URLMap
from .views import get_unique_short_id


@app.route('/api/id/', methods=['POST'])
def get_short_url():
    """Обработка POST-запроса на создание новой короткой ссылки."""
    try:
        request.get_json()
    except Exception:
        raise InvalidAPIUsage(STAY_OUT)

    data = request.get_json()

    if 'custom_id' not in data or data['custom_id'] == '':
        data['custom_id'] = get_unique_short_id()

    if 'url' not in data:
        raise InvalidAPIUsage(URL_REQ)

    if URLMap.query.filter_by(short=data['custom_id']).first() is not None:
        raise InvalidAPIUsage(SHORT_URL_EXIST)

    if not re.match(REGEX, data['custom_id']) or len(
            data['custom_id']) > MAX_LENGTH_SHORT_URL:
        raise InvalidAPIUsage(INV_SHORT_URL)

    url = URLMap()
    url.from_dict(data)
    db.session.add(url)
    db.session.commit()
    return jsonify(url.to_dict()), HTTPStatus.CREATED


@app.route('/api/id/<short>/', methods=['GET'])
def get_full_url(short):
    """Обработка GET-запроса на получение оригинальной ссылки по указанному
    короткому идентификатору.
    """
    url = URLMap.query.filter_by(short=short).first()
    if url is None:
        raise InvalidAPIUsage(ID_NOT_FOUND, HTTPStatus.NOT_FOUND)
    return jsonify({'url': url.to_dict()['url']}), HTTPStatus.OK
