from datetime import datetime, UTC

from . import db

URL = 'http://localhost/'


class URLMap(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    original = db.Column(db.String(length=None), nullable=False)
    short = db.Column(db.String(16), nullable=False, unique=True)
    timestamp = db.Column(db.DateTime, index=True, default=datetime.now(UTC))

    def to_dict(self):
        return dict(
            url=self.original,
            short_link=URL + self.short,
        )

    def from_dict(self, data):
        setattr(self, 'original', data['url'])
        setattr(self, 'short', data['custom_id'])
