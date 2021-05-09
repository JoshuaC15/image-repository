import sqlite3 as sql
from flask import Blueprint, render_template, request, flash, redirect, url_for
from .utils.extract import detect_labels_url
from .imageModel import Image


views = Blueprint('views', __name__)


@views.route('/')
def home():
    return render_template('home.html')


@views.route('/add', methods=['GET', 'POST'])
def add():
    if request.method == 'POST':
        imageURL = request.form.get('imageURL')
        imageName = request.form.get('name')
        # check if image is valid?

        labels = detect_labels_url(imageURL)

        from . import db

        labelStrings = " ".join(labels)
        image = Image(url=imageURL, labels=labelStrings, name=imageName)
        db.session.add(image)
        db.session.commit()

        flash(f'Image: {image.name} added!', category='success')
        return redirect(url_for('views.add'))

    return render_template('add.html')


@views.route('/search', methods=['GET', 'POST'])
def search():
    if request.method == 'POST':
        label = request.form.get('label')

        if label == 'Everything':
            results = Image.query.all()
        else:
            results = Image.query.filter(Image.labels.contains(label)).all()

        flash(f'Showing similar images to: {label}', category='success')
        return render_template('search.html', images=results)

    return render_template('search.html')
