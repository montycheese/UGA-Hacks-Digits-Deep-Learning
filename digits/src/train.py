from clarifai_basic import ClarifaiCustomModel
from json import dumps
from classifications import language

concept = ClarifaiCustomModel()

model = 'letter_k'

for url in language[model]:
	concept.positive(url, model)

for key, value in language.iteritems():
	if key!= model:
		for url in value:
			print url
			concept.negative(url,model)
concept.train(model)



'''
for url in language['letter_c']:
	concept.positive(url, "letter_c")

for neg_url in language['letter_a']:
	concept.negative(neg_url, "letter_c")
	
for neg_url in language['letter_b']:
	concept.negative(neg_url, "letter_c")
for neg_url in language['applause']:
	concept.negative(neg_url, "letter_c")
for neg_url in language['letter_k']:
	concept.negative(neg_url, "letter_c")

concept.train("letter_c")
'''

#this assigns the result of whether or not the predict was successful 
sum = 0.0
for url in language[model]:
	result = concept.predict(url, model)
	sum += result['urls'][0]['score']
	print dumps(result)

#average confidence
print "Average confidence: %.5f" % (sum / len(language[model]))

#output the prediction!
#print dumps(result)

