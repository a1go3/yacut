from flask import flash, redirect, render_template

from . import app, db

from .models import URLMap
from .messages import SHORT_URL_EXIST
from .forms import URLForm
from .utils import get_unique_short_id


@app.route('/', methods=['GET', 'POST'])
def index():
    """Функция отображающая главную страницу сервиса."""
    form = URLForm()
    if form.validate_on_submit():
        if URLMap.query.filter_by(short=form.custom_id.data).first():
            flash(SHORT_URL_EXIST)
            return render_template('index.html', form=form)

        if not form.custom_id.data:
            url = URLMap(
                original=form.original_link.data,
                short=get_unique_short_id()
            )

        else:
            url = URLMap(
                original=form.original_link.data,
                short=form.custom_id.data,
            )

        db.session.add(url)
        db.session.commit()
        return render_template('index.html', form=form, url=url)
    return render_template('index.html', form=form)


@app.route('/<string:short>', methods=['GET'])
def get_original_url(short):
    """Функция перенаправляющая со ссылки сгенерированной сервисом на
    оригинальную, пользовательскую ссылку."""
    url = URLMap.query.filter_by(short=short).first_or_404()
    return redirect(url.original)
