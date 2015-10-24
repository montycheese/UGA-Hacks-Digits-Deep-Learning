from clarifai_basic import ClarifaiCustomModel
from json import dumps
from classifications import language

concept = ClarifaiCustomModel()

image_url = "http://imgur.com/4zAsCti.jpg"
model = "letter_d"
concept.positive(image_url, model)
concept.train(model)


print concept.predict(image_url, model)
