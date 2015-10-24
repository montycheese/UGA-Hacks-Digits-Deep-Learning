from clarifai_basic import ClarifaiCustomModel
from json import dumps

concept = ClarifaiCustomModel()

#ENTER THE URL OF THE IMAGE BETWEEN THE QUOTATION MARKS
# eg: url = "www.image.com/cat.jpg"

#APPLAUSE

from classifications import applause, a
#REPLACE NELLY WITH what we want the neural net to predict when it sees images similar to the one in the url

for url in applause:
	concept.positive(url, "applause")

#for url in a:
#	concept.negative(url, "applause")

concept.train('applause')

#this assigns the result of whether or not the predict was successful 
result = concept.predict(applause[0], 'applause')

#output the prediction!
print dumps(result)
