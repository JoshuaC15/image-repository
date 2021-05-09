def detect_labels_url(url):
    """Detects labels in an image url, by passing it through Google Cloud's
    Vision API
    """
    from google.cloud import vision
    client = vision.ImageAnnotatorClient()
    image = vision.Image()
    image.source.image_uri = url

    response = client.label_detection(image=image)
    labels = response.label_annotations

    labelNames = list()
    for label in labels:
        labelNames.append(label.description)

    return labelNames
