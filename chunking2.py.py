from nltk.corpus import stopwords

# You will have to download the set of stop words the first time
import nltk
#nltk.download('stopwords')
from nltk.stem import PorterStemmer 
from nltk.tokenize import word_tokenize 
ps = PorterStemmer() 
sent="These stories concern the origin and the nature of the world, the lives and activities of deities, heroes, and the origins and significance of the ancient Greeks' own cult and ritual practices and mythological creatures"
#sent="producers produce items and food and their by-products and they can sleep"
#sent= "Boys go to eat and beautiful girls come to play"
#sent="women eat meat and some food for fun and boys go to dance on the sofa and beautifully sing while some cute girls go to eat inside"
#sent="surface water gets heated up and evaporates into water vapour and forms clouds and they come back as rain" #DOESNT WORK
#sent="ram keeps his bag on the shelf and book in the kitchen"
#sent="boys and girls like playing while children sing"
#sent="Dasarath had four sons and they are Ram, Lakshman, Bharat and Shatrugun"
#sent="Monsoon failed which led to severe water crisis" #doesnt work
#sent="We couldn't get tickets to Bangalore so we had to book in Thatkal"
#sent="Rama missed the bus but he was on time"
#sent="SVC maam was a good teacher and a good person but ate slowly"
#sent="Ram goes to play and eats fast"
#sent="i have prepared tea and samosa and kept it in the kitchen"
#sent="i buy bread and butter"
#sent="i like playing and reading" #doesnt work
#sent="Ram and sita play with their bat and ball and sing songs and some small kids and annoying children go to eat and dance"
sent="Kids and children like to play and they like to eat"
#sent="The ball is rolling and the award was given to Obama and the pen was given to me and my friend and was played with by me"
#sent="Plants take in so much of oxygen and carbondioxide and die. Trees give us shade but they are short sometimes"
#sent="The book was writing a boy and a letter was given to a girl and rewritten"
sent="Ram and Sita go to eat food,he comes to buy milk"
words = word_tokenize(sent) 
arr=[]
   
for w in words: 
    arr.append(w) 
li=[word for word in arr]
#print(li)
stop_words = set(stopwords.words('english'))
conj = set(('and', 'or' ,'but','while','so','because'))
operators=set(('were','is','are','was','which','since','not','for','to','of'))
#retain_operators=set(('so','because','since'))
stop = stop_words - operators - conj
#li=[word for word in arr if word not in stop] #WE ARE NOT USING STOP WORDS BEFORE CHUNKING
#print(li)



import spacy
nlp = spacy.load('en_core_web_sm')
#sent = "These stories concern the origin and the nature of the world, the lives and activities of deities, heroes, and mythological creatures, and the origins and significance of the ancient Greeks' own cult and ritual practices"


#doc = nlp('Ram and sita play with their bat and ball and sing beautifully and some small kids and pretty children go out to eat food and dance well')
doc=nlp(sent)
l=[1,2,3]
tagged_list=[[]]
i=0
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
i=0
subj=""
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
				n.append([tagged_list[x][0] for x in range(ind,i) ])
				ind =i+1
			elif(j+1<len(tagged_list)-1):
				if((tagged_list[j+1][1]!="CC" and (tagged_list[j+1][1].find("VB")!=-1or tagged_list[j+1][1].find("NN")!=-1 or tagged_list[j+1][1].find("RB")!=-1))):
					n.append([tagged_list[x][0] for x in range(ind,i)])
					ind=i
					print(1,tagged_list[i][0],i)
		elif(j<len(tagged_list)-1 and tagged_list[j][1].find("VB")!=-1):
			if(i+1<len(tagged_list)-1 and tagged_list[i+1][1]!="PRP"):
				tagged_list[i][0]=subj
			n.append([tagged_list[x][0] for x in range(ind,i) ] )
			ind=i;
			print(2,tagged_list[i][0],i)
	#print(subj)
	if(tagged_list[i][1]=="PRP"):
		tagged_list[i][0]=subj
		print("Pronoun ",tagged_list[i][0])
	i=i+1
n.append([tagged_list[x][0] for x in range(ind,i)])
print(n)


