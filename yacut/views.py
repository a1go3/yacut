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
            original=form.original.data,
            short=form.short.data,
        )
        db.session.add(url)
        db.session.commit()
    return render_template('urlcut.html')



@app.route('/<string:short>')
def get_original_url(short):
    url = URLMap.query.filter_by(short=short).first()
    return render_template('original_url.html', url=url)