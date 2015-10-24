from clarifai_basic import ClarifaiCustomModel
from json import dumps
from classifications import language



def predict(url):
	concept = ClarifaiCustomModel()
	max_confidence = 0.0
	classification = None
	for word in language.keys():
		print word
		result = concept.predict(url, word)
		confidence = result['urls'][0]['score']
		if confidence > max_confidence:
			max_confidence = confidence
			classification = word
	return (classification, max_confidence)
	
print predict(language['letter_b'][3])