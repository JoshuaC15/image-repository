from . import db


class Image(db.Model):
    """The properties that make up an image passed through the workflow

    Fields
    ------
    id : Ing
        the unique identifier of the image
    url : Str
        the location of the image stored on the web
    labels : Str
        the labels assigned to an image through the machine learning Vision model
    name : Str
        the name given to an image
    """
    id = db.Column(db.Integer, primary_key=True)
    url = db.Column(db.String(256), nullable=False)
    labels = db.Column(db.String(256))
    name = db.Column(db.String(256))
