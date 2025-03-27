# URL routing and view functions

from flask import Blueprint, render_template, request, redirect, url_for, abort
from app import db
from app.models import URL
from app.forms import URLForm

main = Blueprint('main', __name__)

@main.route('/', methods=['GET', 'POST'])
def index():
    form = URLForm()
    if form.validate_on_submit():
        original_url = form.original_url.data
        existing_url = URL.query.filter_by(original_url=original_url).first()
        
        if existing_url:
            short_url = existing_url.short_url
        else:
            short_url = URL.generate_short_url()
            new_url = URL(original_url=original_url, short_url=short_url)
            db.session.add(new_url)
            db.session.commit()
        
        return render_template('index.html', form=form, short_url=request.host_url + short_url)
    
    return render_template('index.html', form=form)

@main.route('/<short_url>')
def redirect_to_url(short_url):
    url = URL.query.filter_by(short_url=short_url).first()
    if url:
        url.clicks += 1
        db.session.commit()
        return redirect(url.original_url)
    abort(404)

@main.route('/stats')
def stats():
    urls = URL.query.order_by(URL.clicks.desc()).limit(10).all()
    return render_template('stats.html', urls=urls)