from datetime import datetime

from settings import MAX_LENGTH_SHORT_URL, URL

from . import db


class URLMap(db.Model):
    """Модель приложения. Хранит в себе связь оригинальных и укороченных
    ссылок, а также дату их создания.
    """
    id = db.Column(db.Integer, primary_key=True)
    original = db.Column(db.String(length=None), nullable=False)
    short = db.Column(db.String(MAX_LENGTH_SHORT_URL), nullable=False,
                      unique=True)
    timestamp = db.Column(db.DateTime, index=True, default=datetime.utcnow)

    def to_dict(self):
        return dict(
            url=self.original,
            short_link=URL + self.short,
        )

    def from_dict(self, data):
        setattr(self, 'original', data['url'])
        setattr(self, 'short', data['custom_id'])
