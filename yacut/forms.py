from flask_wtf import FlaskForm
from settings import MAX_LENGTH_SHORT_URL, REGEX
from wtforms import SubmitField, URLField
from wtforms.validators import URL, DataRequired, Length, Optional, Regexp

from .messages import (CORRECT_URL, CREATE, ENG_LET_NUM, LONG_URL,
                       REQUIRED_FIELD, SHORT_URL, TOO_LONG_SHORT_URL)


class URLForm(FlaskForm):
    """Форма для создания коротких ссылок."""
    original_link = URLField(
        LONG_URL,
        validators=[
            DataRequired(message=REQUIRED_FIELD),
            URL(require_tld=True, message=CORRECT_URL)
        ]
    )
    custom_id = URLField(
        SHORT_URL,
        validators=[
            Optional(),
            Length(max=MAX_LENGTH_SHORT_URL, message=TOO_LONG_SHORT_URL),
            Regexp(REGEX, message=ENG_LET_NUM)
        ]
    )
    submit = SubmitField(CREATE)
