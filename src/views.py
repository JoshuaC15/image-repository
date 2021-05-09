from flask import Blueprint, render_template, request, flash, redirect, url_for
from .utils.extract import detect_labels_url
import sqlite3 as sql
from .imageModel import Image


views = Blueprint('views', __name__)


@views.route('/')
def home():
    return render_template('home.html')


@views.route('/add', methods=['GET', 'POST'])
def add():
    if request.method == 'POST':
        imageURL = request.form.get('imageURL')
        # check if image is valid?

        labels = detect_labels_url(imageURL)

        from . import db

        labelStrings = " ".join(labels)
        image = Image(url=imageURL, labels=labelStrings)
        db.session.add(image)
        db.session.commit()

        flash('Image added!', category='success')
        return redirect(url_for('views.add'))

    return render_template('add.html')


def get_cursor():
    conn = sql.connect("database.db")
    cursor = conn.cursor()
    return cursor, conn


@views.route('/search', methods=['GET', 'POST'])
def search():
    if request.method == 'POST':
        cursor, conn = get_cursor()
        label = request.form.get('label')

        if label == 'Everything':
            results = Image.query.all()
        else:
            results = Image.query.filter(Image.labels.contains(label)).all()

        data = list()
        for result in results:
            data.append(result.url)

        return render_template('search.html', data=data)

    return render_template('search.html')
