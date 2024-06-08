from flask_wtf import FlaskForm
from wtforms import SubmitField, URLField
from wtforms.validators import DataRequired, Length, Optional, URL, Regexp

from .messages import LONG_URL, REQUIRED_FIELD, CORRECT_URL, SHORT_URL, \
    TOO_LONG_SHORT_URL, ENG_LET_NUM, CREATE

from settings import REGEX


class URLForm(FlaskForm):
    """Форма для создания коротких ссылок."""
    original_link = URLField(
        LONG_URL,
        validators=[DataRequired(message=REQUIRED_FIELD),
                    URL(require_tld=True, message=CORRECT_URL)
                    ]
    )
    custom_id = URLField(
        SHORT_URL,
        validators=[Optional(),
                    Length(max=16,
                           message=TOO_LONG_SHORT_URL),
                    Regexp(REGEX,
                           message=ENG_LET_NUM)
                    ]
    )
    submit = SubmitField(CREATE)
