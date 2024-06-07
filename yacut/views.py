from random import randrange

from flask import abort, flash, redirect, render_template, url_for

from . import app, db

from .models import URLMap
from .forms import URLForm


@app.route('/', methods=['GET', 'POST'])
def get_short_url():
    form = URLForm()
    if form.validate_on_submit():
        url = URLMap(
            original=form.original_link.data,
            short=form.custom_id.data,
        )
        db.session.add(url)
        db.session.commit()
        return render_template('url_cut.html', form=form, url=url)
    return render_template('url_cut.html', form=form)


@app.route('/<string:short>')
def get_original_url(short):
    url = URLMap.query.filter_by(short=short).first_or_404()
    return redirect(url.original)
