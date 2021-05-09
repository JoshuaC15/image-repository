# Machine Learning Image Repository - Shopify Image Repository Submission Joshua Cheng

This project is my submission for the Shopify Image Repository challenge. This project incorporates a powerful general machine learning model that generates a description for any input image. This allows us to automatically label images added to this repository to be searched. No more manual labelling!

## Project Flow
### Add Image
1. Enter a name for your image as well as an image URL. Image URL's can be obtained by right clicking on an image in Google Images and selecting `Copy Image Address` on MacOS or a Windows/Linux equivalent.
1. After submitting a valid image, it will be passed through Google's `Vision AI` model, which will assign labels to that inputted image.
1. The image will then be added to the database

### Search Image
1. Enter some keyword to search for similar images. Some sample labels I tested with include:  
`Food`  
`Water`  
`Sport`  
`Home`  
`Car`
1. Images with matching labels will then be queried and displayed to the user, along with the original assigned image name.

## Stack
1. [Python 3](https://www.python.org)
1. [Flask](https://flask.palletsprojects.com/en/1.1.x/)
1. [Google Vision API](https://cloud.google.com/vision)
1. [SQLite3](https://www.sqlite.org/index.html)

## Quickstart Setup For Image Search
1. Install the required dependencies through the `requirements.txt` file provided:
```bash
pip install -r requirements.txt
```
1. From there, launch the `Flask` server:
```bash
python3 main.py
```
1. That's it, you will now be able to navigate to the `search` tab through the navigation window to search for images related to some label!

## Setup for Image Add
Some additional steps need to be taken to setup adding images need to be taken, namely in setting up Google Vision.

### Google Vision AI
1. First, create a project in GCP to enable billing, the vision API, and create a service account. Steps to do each of these tasks can be found [here](https://cloud.google.com/vision/docs/quickstart-client-libraries#client-libraries-usage-python), as per Google's documentation.  
1. From there, after following those steps you should now have an api key as a json file. you can now set an the required environment variable with the following line:
```
export GOOGLE_APPLICATION_CREDENTIALS="path/to/your/apiJsonKey"
```
1. Install the client library to use the API:
```
pip install --upgrade google-cloud-vision
```
1. That's it, now you will be able to add images and have them passed through the Google Vision API!
