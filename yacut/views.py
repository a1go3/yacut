import string
from random import choices

from flask import abort, flash, redirect, render_template, url_for

from . import app, db

from .models import URLMap
from .forms import URLForm


@app.route('/', methods=['GET', 'POST'])
def index():
    form = URLForm()
    if form.validate_on_submit() and form.custom_id.data == '':
        url = URLMap(
            original=form.original_link.data,
            short=get_short_url()
        )
        return add_data(form, url)
    elif form.validate_on_submit():
        if URLMap.query.filter_by(
                short=form.custom_id.data).first() is not None:
            flash('Предложенный вами вариант короткой ссылки уже существует.')
            return render_template('index.html', form=form)
        url = URLMap(
            original=form.original_link.data,
            short=form.custom_id.data,
        )
        return add_data(form, url)
    return render_template('index.html', form=form)


@app.route('/<string:short>')
def get_original_url(short):
    url = URLMap.query.filter_by(short=short).first_or_404()
    return redirect(url.original)


def get_short_url():
    return ''.join(choices(string.digits + string.ascii_letters, k=6))


def add_data(form, url):
    db.session.add(url)
    db.session.commit()
    return render_template('index.html', form=form, url=url)
