__author__ = 'montanawong'
from clarifai.client import ClarifaiApi
from json import dumps

clarifai_api = ClarifaiApi() # assumes environment variables are set.
url = "http://www.churchleaders.com/wp-content/uploads/files/article_images/clap_or_not_937398406.jpg"

#result = clarifai_api.tag_images(open('images/cat.jpg'))

result = clarifai_api.tag_image_urls(url)
for result in result['results'][0]['result']['tag']['classes']:
	print dumps(result)