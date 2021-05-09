from . import db


class Image(db.Model):
    '''
    TODO: Add documentation
    '''
    id = db.Column(db.Integer, primary_key=True)
    url = db.Column(db.String(256), nullable=False)
    labels = db.Column(db.String(256))
