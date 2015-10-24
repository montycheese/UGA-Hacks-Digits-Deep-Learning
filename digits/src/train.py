from clarifai_basic import ClarifaiCustomModel
from json import dumps
from classifications import language

concept = ClarifaiCustomModel()

#for url in language['applause']:
#	concept.positive(url, "applause")

for neg_url in language['letter_k']:
	concept.negative(neg_url, "applause")

concept.train("applause")

#this assigns the result of whether or not the predict was successful 
sum = 0.0
for url in language['applause']:
	result = concept.predict(url, 'applause')
	sum += result['urls'][0]['score']
	print dumps(result)

#average confidence
print "Average confidence: %.5f" % (sum / len(language['applause']))

#output the prediction!
#print dumps(result)

