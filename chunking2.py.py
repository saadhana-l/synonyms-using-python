from nltk.corpus import stopwords
import nltk
#nltk.download('stopwords')
from nltk.stem import PorterStemmer 
from nltk.tokenize import word_tokenize 
ps = PorterStemmer() 
sent="These stories concern the origin and the nature of the world, the lives and activities of deities, heroes, and the origins and significance of the ancient Greeks' own cult and ritual practices and mythological creatures"
##sent="producers produce items and food and their by-products and they can sleep"
# #sent= "Boys go to eat and beautiful girls come to play"
# #sent="women eat meat and some food for fun and boys go to dance on the sofa and beautifully sing while some cute girls go to eat inside"
# #sent="surface water gets heated up and evaporates into water vapour and forms clouds and they come back as rain" #DOESNT WORK
# #sent="ram keeps his bag on the shelf and book in the kitchen"
# #sent="boys and girls like playing while children sing"
# #sent="Dasarath had four sons and they are Ram, Lakshman, Bharat and Shatrugun"
# #sent="Monsoon failed which led to severe water crisis" #doesnt work
# #sent="We couldn't get tickets to Bangalore so we had to book in Thatkal"
# #sent="Rama missed the bus but he was on time"
# #sent="SVC maam was a good teacher and a good person but ate slowly"
# #sent="Ram goes to play and eats fast"
# #sent="i have prepared tea and samosa and kept it in the kitchen"
# #sent="i buy bread and butter"
# #sent="i like playing and reading" #doesnt work
# #sent="Ram and sita play with their bat and ball and sing songs and some small kids and annoying children go to eat and dance"
# sent="Kids and children like to play and they like to eat"
# #sent="The ball is rolling and the award was given to Obama and the pen was given to me and my friend and was played with by me"
# #sent="Plants take in so much of oxygen and carbondioxide and die. Trees give us shade but they are short sometimes"
# #sent="The book was writing a boy and a letter was given to a girl and rewritten"
# sent="A smart man goes to eat food"
# #sent="Krishna goes to work and does dance. He is very smart."
# sent="A strong man and beautiful woman and a good boy eat food and drink milk"
# sent="Water evaporates into vapor and forms clouds and dries up"
# sent="A man buys some bread and butter"
# #sent="Water heats and rises into vapor"
# #sent="Ram and Sita buy a bat and play happily"
sent="Ram buys some bread and butter and Sita sings songs and can dance well"
#sent="Sita sings songs and can dance well"
#sent="A green plant takes in oxygen and water and gives out carbondioxide and water"
#sent="Sita dances and swims"
#sent="Sita was thirsty so she drank juice and water after lunch"
#sent="Ram buys a bat and ball and Sita plays the keyboard"
sent="Trump and the girl have been bad presidents.They have been formidable candidates in the elections."
words = word_tokenize(sent) 
arr=[]
   
for w in words: 
    arr.append(w) 
li=[word for word in arr]
#print(li)
# stop_words = set(stopwords.words('english'))
conj = set(('and', 'or' ,'but','while','so','because'))
# operators=set(('were','is','are','was','which','since','not','for','to','of'))
# #retain_operators=set(('so','because','since'))
# stop = stop_words - operators - conj
# #li=[word for word in arr if word not in stop] #WE ARE NOT USING STOP WORDS BEFORE CHUNKING
# #print(li)


#CO REF
import spacy
nlp = spacy.load('en_core_web_sm')
import neuralcoref
doc=nlp(sent)
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

sent=resolve_co_reference(sent)
l=[1,2,3]
tagged_list=[[]]
i=0
doc=nlp(sent)
print(sent)
for token in doc:
	if (token.lemma_=="be"):
		l[0]="be"
	else:
		l[0]=token.text
	l[1]=token.tag_
	if(token.dep_=='nsubj'):
		l[2]=1
	else:
		l[2]=0
	tagged_list.insert(i,l)
	l=[1,2,3]
	i=i+1
#print(tagged_list)
#to find subjects in passive sentence
noun=-1
i=0
while(i<len(tagged_list)-1):
	if(tagged_list[i][1].find("NN")!=-1):
		noun=i
	if(tagged_list[i][0]=='be'):
		if(i<len(tagged_list)-2 and tagged_list[i+1][1].startswith("V") and not tagged_list[i+1][1].startswith("VBG")):
			tagged_list[noun][2]=1
	i=i+1
print(tagged_list)


n=[[]]
ind=0
ind2=-1
i=0
subj=""
lis=[]
flag=-1
find=-1
while(i<len(tagged_list)-1):
	if(tagged_list[i][2]==1 and tagged_list[i][1]!="PRP" ):
		subj=tagged_list[i][0]
	if(tagged_list[i][1]=="CC"  or tagged_list[i][0] in conj or tagged_list[i][0]=="," or tagged_list[i][0]==";" or tagged_list[i][0]=="."):
		j=i+1
		while(j<len(tagged_list)-1 and tagged_list[j][1].find("NN")==-1 and tagged_list[j][1].find("VB")==-1):
			j=j+1
		if(j<len(tagged_list)-1and tagged_list[j][1].find("NN")!=-1):
			if(tagged_list[i-1][2]==1 or tagged_list[i-1][2]==2):
				tagged_list[j][2]=2
				subj=subj+" "+tagged_list[i][0]+" "+tagged_list[j][0]
			elif(tagged_list[j][2]==1):
				if(ind2!=-1 and ind2!=ind):
					find=find+1					
					while(find<len(tagged_list)-1 and (tagged_list[find][1]!="CC"  and tagged_list[find][0] not in conj and tagged_list[find][0]!="," and tagged_list[find][0]!=";" and tagged_list[find][0]!=".")):
						find=find+1
					n.append([tagged_list[x][0] for x in range(ind2,i) if(x not in range(ct,find+1))])
					ind2=-1
				else:
					for x in range(ind,i):
						if(tagged_list[x][1]=="CC"  or tagged_list[x][0] in conj or tagged_list[x][0]=="," or tagged_list[x][0]==";" or tagged_list[x][0]=="."):
							if(x>ind and x<i-1):
								if((tagged_list[x-1][2]== 1 or tagged_list[x-1][2]==2)):
									y=x+1
									while(y<len(tagged_list)-1 and tagged_list[y][1].find("NN")==-1 and tagged_list[y][1].find("VB")==-1):
										y=y+1
									if(tagged_list[y][2]==1 or tagged_list[y][2]==2):
										if(len(lis)==0):
											lis.append(x-1)
										lis.append(y)
					for l in range(len(lis)):
						n.append([tagged_list[x][0] for x in range(ind,i) if(x == lis[l] or x>lis[len(lis)-1]) or (l==0 and x<lis[0]) or (l>0 and x>lis[l-1]) and x<=lis[l]])
					if(len(lis)==0):
						n.append([tagged_list[x][0] for x in range(ind,i)])
				lis=[]
				ind =i+1

			else:
				if(ind2==-1):
					ind2=ind
				ct=ind2
				while(ct<i-1 and ((tagged_list[ct][1].find("NN")==-1) or (tagged_list[ct][2]==1 or tagged_list[ct][2]==2 ))):
					ct=ct+1
				if(flag!=ind2):
					n.append([tagged_list[x][0] for x in range(ind2,i)])
					flag=ind2
					find=ct
				else:
					find=find+1					
					while(find<len(tagged_list)-1 and (tagged_list[find][1]!="CC"  and tagged_list[find][0] not in conj and tagged_list[find][0]!="," and tagged_list[find][0]!=";" and tagged_list[find][0]!=".")):
						find=find+1
					n.append([tagged_list[x][0] for x in range(ind2,i) if(x not in range(ct,find+1))])
				ind=i+1 #ADDED NOW



		elif(j<len(tagged_list)-1 and tagged_list[j][1].find("VB")!=-1):
			# if(i+1<len(tagged_list)-1 and tagged_list[i+1][1]!="PRP"):
			# 	tagged_list[i][0]=subj
			#print(2,tagged_list[i][0],i)
			if(ind2!=-1 and ind2!=ind):
				find=find+1					
				while(find<len(tagged_list)-1 and (tagged_list[find][1]!="CC"  and tagged_list[find][0] not in conj and tagged_list[find][0]!="," and tagged_list[find][0]!=";" and tagged_list[find][0]!=".")):
					find=find+1
				n.append([tagged_list[x][0] for x in range(ind2,i) if(x not in range(ct,find+1))])
				ind2=-1
			else:
				for x in range(ind,i): #TO SEPARATE SUBJECTS
					if(tagged_list[x][1]=="CC"  or tagged_list[x][0] in conj or tagged_list[x][0]=="," or tagged_list[x][0]==";" or tagged_list[x][0]=="."):
						if(x>ind and x<i-1):
							if((tagged_list[x-1][2]== 1 or tagged_list[x-1][2]==2)):
								y=x+1
								while(y<len(tagged_list)-1 and tagged_list[y][1].find("NN")==-1 and tagged_list[y][1].find("VB")==-1):
									y=y+1
								if(tagged_list[y][2]==1 or tagged_list[y][2]==2):
									if(len(lis)==0):
										lis.append(x-1)
									lis.append(y)
				for l in range(len(lis)):
					n.append([tagged_list[x][0] for x in range(ind,i) if(x == lis[l] or x>lis[len(lis)-1]) or (l==0 and x<lis[0]) or (l>0 and x>lis[l-1]) and x<=lis[l]])
				if(len(lis)==0):
					n.append([tagged_list[x][0] for x in range(ind,i)])
			lis=[]
			ind=i;

	#print(subj)
	# if(tagged_list[i][1]=="PRP"):
	# 	tagged_list[i][0]=subj
	i=i+1
if(ind2!=-1 and ind2!=ind):
	#print("ind= ",ind,"ind2=",ind2," i=",i)
	find=find+1					
	while(find<len(tagged_list)-1 and (tagged_list[find][1]!="CC"  and tagged_list[find][0] not in conj and tagged_list[find][0]!="," and tagged_list[find][0]!=";" and tagged_list[find][0]!=".")):
		find=find+1
	n.append([tagged_list[x][0] for x in range(ind2,i) if(x not in range(ct,find+1))])
	ind2=-1;
else:	
	for x in range(ind,i):
		if(tagged_list[x][1]=="CC"  or tagged_list[x][0] in conj or tagged_list[x][0]=="," or tagged_list[x][0]==";" or tagged_list[x][0]=="."):
			if(x>ind and x<i-1):
				if((tagged_list[x-1][2]== 1 or tagged_list[x-1][2]==2)):
					y=x+1
					while(y<len(tagged_list)-1 and tagged_list[y][1].find("NN")==-1 and tagged_list[y][1].find("VB")==-1):
						y=y+1
					if(tagged_list[y][2]==1 or tagged_list[y][2]==2):
						if(len(lis)==0):
							lis.append(x-1)
						lis.append(y)
	for l in range(len(lis)):
		n.append([tagged_list[x][0] for x in range(ind,i) if(x == lis[l] or x>lis[len(lis)-1]) or (l==0 and x<lis[0]) or (l>0 and x>lis[l-1]) and x<=lis[l]])
	if(len(lis)==0):
		n.append([tagged_list[x][0] for x in range(ind,i)])
lis=[]
print(tagged_list)
print()
print(n)
