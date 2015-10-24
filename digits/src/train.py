from clarifai_basic import ClarifaiCustomModel
from json import dumps

concept = ClarifaiCustomModel()

#ENTER THE URL OF THE IMAGE BETWEEN THE QUOTATION MARKS
# eg: url = "www.image.com/cat.jpg"

#APPLAUSE
url = "http://www.churchleaders.com/wp-content/uploads/files/article_images/clap_or_not_937398406.jpg
"
url2= "http://i3.mirror.co.uk/incoming/article4764746.ece/ALTERNATES/s615/Grumpy-Cat.jpg"

url3="http://media3.popsugar-assets.com/files/2014/08/04/788/n/1922398/6159171bee954510_thumb_temp_image8451461407171002/i/Grumpy-Cat-Releases-Second-Book.jpg"


#REPLACE NELLY WITH what we want the neural net to predict when it sees images similar to the one in the url
concept.positive(url, "nelly")
concept.positive(url2, "nelly")
concept.positive(url3, "nelly")
#concept.negative(url, 'pet' )
concept.train('nelly')

#this assigns the result of whether or not the predict was successful 
result = concept.predict(url3, 'nelly')

#output the prediction!
print dumps(result)
