# Load your usual SpaCy model (one of SpaCy English models)
import spacy
'''
NOTE: the following code crashes or gives Seg fault with spacy version 2.1.4
Downgrade to spacy 2.1.3 by running the following on the command line:
pip install -U spacy==2.1.3
'''
import neuralcoref  #the MAIN import required : supplements spacy's built in coreference
nlp = spacy.load('en') # load the model change this to en_web_core_sm if necessary choose appropriately
coref = neuralcoref.NeuralCoref(nlp.vocab) # initialize the neuralcoref with spacy's vocabulary
nlp.add_pipe(coref, name='neuralcoref') #add the coref model to pipe

def resolve_co_reference(text):
	'''
	The coref model calculates the probabilities of links between The main occurence and a reference of that
	main occurence and on the basis of that replaces every reference with the main occurence it is referring to
	'''
	doc = nlp(text)
	if doc._.has_coref: ## if coreference is possible
		return doc._.coref_resolved ##return the sentence with all references replaced
	else:
		return text ##else return text as it is 

print(resolve_co_reference('Donald Trump is a bad president.Mr Trump has been a formidable candidate in the elections'))