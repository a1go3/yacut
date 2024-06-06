from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, TextAreaField, URLField
from wtforms.validators import DataRequired, Length, Optional


class URLForm(FlaskForm):
    original = StringField(
        'Введите ссылку',
        validators=[DataRequired(message='Обязательное поле'),
                    Length(1, 128)]
    )
    short = TextAreaField(
        'Введите короткую ссылку',
        validators=[DataRequired(message='Обязательное поле')]
    )
    submit = SubmitField('Добавить')