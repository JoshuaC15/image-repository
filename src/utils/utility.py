import requests

class Utilities:
    """Utility class that provides useful functions that are used throughout the project
    """

    @staticmethod
    def is_url_image(image_url):
        r = requests.head(image_url)
        return r.status_code == requests.codes.ok
