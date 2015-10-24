from clarifai_basic import ClarifaiCustomModel


concept = ClarifaiCustomModel()

#ENTER THE URL OF THE IMAGE BETWEEN THE QUOTATION MARKS
# eg: url = "www.image.com/cat.jpg"
url = ""


#REPLACE NELLY WITH what we want the neural net to predict when it sees images similar to the one in the url
concept.positive(url, "nelly")
concept.train('nelly')

#this assigns the result of whether or not the predict was successful 
result = concept.predict('url', 'nelly')

#output the prediction!
print result