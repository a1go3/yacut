from flask_wtf import FlaskForm
from wtforms import SubmitField, URLField
from wtforms.validators import DataRequired, Length, Optional, URL, Regexp


class URLForm(FlaskForm):
    original_link = URLField(
        'Длинная ссылка',
        validators=[DataRequired(message='Обязательное поле!'),
                    URL(require_tld=True, message='Введите корректный url.')
                    ]
    )
    custom_id = URLField(
        'Ваш вариант короткой ссылки',
        validators=[Optional(),
                    Length(max=16,
                           message='Предложенный вариант ссылки слишком '
                                   'длинный. '
                                   'Введите максимум 16 символов.'),
                    Regexp(r'[A-Za-z0-9_]+$',
                           message='Ссылка может состоять только из латинских '
                                   'букв и цифр.'),
                    ]
    )
    submit = SubmitField('Создать')
