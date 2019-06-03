{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "metadata": {},
   "outputs": [
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "[nltk_data] Downloading package stopwords to\n",
      "[nltk_data]     C:\\Users\\HAI\\AppData\\Roaming\\nltk_data...\n",
      "[nltk_data]   Package stopwords is already up-to-date!\n"
     ]
    },
    {
     "data": {
      "text/plain": [
       "True"
      ]
     },
     "execution_count": 1,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "from nltk.corpus import stopwords\n",
    "\n",
    "# You will have to download the set of stop words the first time\n",
    "import nltk\n",
    "nltk.download('stopwords')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "metadata": {},
   "outputs": [],
   "source": [
    "from nltk.stem import PorterStemmer \n",
    "from nltk.tokenize import word_tokenize \n",
    "ps = PorterStemmer() "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 812,
   "metadata": {},
   "outputs": [],
   "source": [
    "sent=\"These stories concern the origin and the nature of the world, the lives and activities of deities, heroes, and the origins and significance of the ancient Greeks' own cult and ritual practices and mythological creatures\"\n",
    "sent=\"producers produce items and food and their by-products and it can sleep\"\n",
    "sent= \"Boys go to eat and beautiful girls come to play\"\n",
    "sent=\"women eat meat and some food for fun and boys go to dance on the sofa and beautifully sing while some cute girls go to eat inside\"\n",
    "sent=\"surface water gets heated up and evaporates into vapour and forms clouds and they come back as rain\"\n",
    "sent=\"boys and girls go out to play while children love to sing\" #doesnt work\n",
    "sent=\"Dasarath had four sons and they are Ram, Lakshman, Bharat and Shatrugun\"\n",
    "sent=\"Monsoon failed which led to severe water crisis\" #doesnt work\n",
    "sent=\"We couldn't get tickets to Bangalore so we had to book in Thatkal\"\n",
    "sent=\"Rama missed the bus but he was on time\"\n",
    "sent=\"SVC maam was a good teacher and a good person\"\n",
    "#sent=\"Ram goes to play and he eats fast\"\n",
    "#sent=\"i have prepared tea and samosa and kept it in the kitchen\"\n",
    "#sent=\"i buy bread and butter\"\n",
    "sent=\"i like playing and reading\"\n",
    "words = word_tokenize(sent) \n",
    "arr=[]\n",
    "   \n",
    "for w in words: \n",
    "    arr.append(w) "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 813,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "['i', 'like', 'playing', 'and', 'reading']"
      ]
     },
     "execution_count": 813,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "li=[word for word in arr]\n",
    "li"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 814,
   "metadata": {},
   "outputs": [],
   "source": [
    "stop_words = set(stopwords.words('english'))\n",
    "conj = set(('and', 'or' ,'but','while','so','because'))\n",
    "operators=set(('were','is','are','was','which','since','not','for','to','of'))\n",
    "#retain_operators=set(('so','because','since'))\n",
    "stop = stop_words - operators - conj\n",
    "li=[word for word in arr if word not in stop]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 815,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "{'i', 'me', 'my', 'myself', 'we'}"
      ]
     },
     "execution_count": 815,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": 817,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "['like', 'playing', 'and', 'reading']"
      ]
     },
     "execution_count": 817,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "li"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 818,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "[('like', 'IN'), ('playing', 'VBG'), ('and', 'CC'), ('reading', 'VBG')]"
      ]
     },
     "execution_count": 818,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "tagged = nltk.pos_tag(li) \n",
    "tagged"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 819,
   "metadata": {},
   "outputs": [],
   "source": [
    "n=\"\"\n",
    "import numpy as np\n",
    "tagged_list=[list(item) for item in tagged]\n",
    "#tagged_list[5][1]='VBZ'\n",
    "#tagged_list[7][1]='VBZ'"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 824,
   "metadata": {},
   "outputs": [],
   "source": [
    "# n=[[]]\n",
    "# ind=0\n",
    "# for i in range(0,len(tagged_list)):\n",
    "#     if(i+2<len(tagged_list) and tagged_list[i][1]==\"CC\" and tagged_list[i+1][1].find(\"NN\")!=-1 and tagged_list[i+2][1].find(\"VB\")!=-1): #producers produce items and consumers consume\n",
    "#         print(1,tagged_list[i][0],i)\n",
    "#         n.append([tagged_list[x][0] for x in range(ind,i) ] )\n",
    "#         ind=i;\n",
    "#     elif(i+3<len(tagged_list) and tagged_list[i][1]==\"CC\" and tagged_list[i+1][1].find(\"NN\")==-1 and tagged_list[i+2][1].find(\"NN\")!=-1  and tagged_list[i+3][1].find(\"VB\")!=-1): #producers produce items and some consumers consume\n",
    "#         print(2, tagged_list[i][0],i)\n",
    "#         n.append([tagged_list[x][0] for x in range(ind,i) ] )\n",
    "#         ind=i;\n",
    "#     elif(i+1<len(tagged_list) and tagged_list[i][1]==\"CC\" and tagged_list[i+1][1].find(\"VB\")!=-1): #producers produce items and food and their by-products and it can sleep\n",
    "#         print(3,tagged_list[i][0],i)\n",
    "#         n.append([tagged_list[x][0] for x in range(ind,i) ] )\n",
    "#         ind=i;\n",
    "# n.append([tagged_list[x][0] for x in range(ind,i+1)])\n",
    "    "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 825,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "[[], ['like', 'playing'], ['and', 'reading']]"
      ]
     },
     "execution_count": 825,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 826,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "2 and 2\n"
     ]
    }
   ],
   "source": [
    "n=[[]]\n",
    "ind=0\n",
    "i=1\n",
    "while(i<len(tagged_list)):\n",
    "    if(tagged_list[i][1]==\"CC\"  or tagged_list[i][0] in conj):\n",
    "        j=i+1\n",
    "        while(j<len(tagged_list) and tagged_list[j][1].find(\"NN\")==-1 and tagged_list[j][1].find(\"VB\")==-1): \n",
    "            #producers produce items and some consumers consume\n",
    "            j=j+1\n",
    "        if(j<len(tagged_list)and tagged_list[j][1].find(\"NN\")!=-1):\n",
    "            if(j+1<len(tagged_list) and (tagged_list[j+1][1]!=\"CC\" and (tagged_list[j+1][1].find(\"VB\")!=-1or tagged_list[j+1][1].find(\"NN\")!=-1 or tagged_list[j+1][1].find(\"RB\")!=-1))):\n",
    "                n.append([tagged_list[x][0] for x in range(ind,i) ] )\n",
    "                ind=i;\n",
    "                print(1,tagged_list[i][0],i)\n",
    "            # or tagged_list[j+1][1].find(\"NN\")!=-1 or tagged_list[j+1][1].find(\"RB\")!=-1\n",
    "        elif(j<len(tagged_list)and tagged_list[j][1].find(\"VB\")!=-1):\n",
    "            n.append([tagged_list[x][0] for x in range(ind,i) ] )\n",
    "            ind=i;\n",
    "            print(2,tagged_list[i][0],i)\n",
    "    i=i+1\n",
    "n.append([tagged_list[x][0] for x in range(ind,i)])"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": 827,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "[[], ['like', 'playing'], ['and', 'reading']]"
      ]
     },
     "execution_count": 827,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.7.1"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 2
}
