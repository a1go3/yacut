from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, TextAreaField, URLField
from wtforms.validators import DataRequired, Length, Optional, URL

class URLForm(FlaskForm):
    original_link = URLField(
        'Длинная ссылка',
        validators=[DataRequired(message='Обязательное поле'), URL(require_tld=True, message='Введите корректный url'),
                    Length(1, 128)]
    )
    custom_id = StringField(
        'Ваш вариант короткой ссылки',
        validators=[DataRequired(message='Обязательное поле'),
                    Length(6)]
    )
    submit = SubmitField('Создать')