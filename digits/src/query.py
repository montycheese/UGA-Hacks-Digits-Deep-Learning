__author__ = 'montanawong'
from clarifai.client import ClarifaiApi

clarifai_api = ClarifaiApi() # assumes environment variables are set.
url = "http://cdn.hitfix.com/photos/5621843/Grumpy-Cat.jpg"

#result = clarifai_api.tag_images(open('images/cat.jpg'))

result = clarifai_api.tag_image_urls(url)
print result