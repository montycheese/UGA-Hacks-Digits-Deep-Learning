from clarifai_basic import ClarifaiCustomModel
from json import dumps
from classifications import language

concept = ClarifaiCustomModel()


image_url = "http://imgur.com/18mJQcx.jpg"
model = "letter_f"
concept.positive(image_url, model)
concept.train(model)

for word in language:
	if word != model:
		print word
		concept.negative(image_url, word)
		concept.train(word)
	
print concept.predict(image_url, model)