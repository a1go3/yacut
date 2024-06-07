from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, URLField
from wtforms.validators import DataRequired, Length, Optional, URL, Regexp


class URLForm(FlaskForm):
    original_link = URLField(
        'Длинная ссылка',
        validators=[DataRequired(message='Обязательное поле!'),
                    URL(require_tld=True, message='Введите корректный url.'),
                    Length(max=128)]
    )
    custom_id = StringField(
        'Ваш вариант короткой ссылки',
        validators=[Optional(),
                    Length(min=6,
                           message='Предложенный вариант ссылки слишком '
                                   'короткий. '
                                   'Введите минимум 6 символов.'),
                    Regexp(r'[A-Za-z0-9]',
                           message='Ссылка может состоять только из латинских '
                                   'букв и цифр.'),
                    ]
    )
    submit = SubmitField('Создать')
