import pandas as pd
from spello.model import SpellCorrectionModel  
from spello.model import SpellCorrectionModel
from nltk.tokenize import TreebankWordTokenizer
import re

#Defining Model
sp = SpellCorrectionModel(language='en')

#Reading keywords from CSV file
df = pd.read_csv('/home/bikes/Desktop/test/backend/proxy/keywords.csv')

#Creating list of keywords
mec_list = df['bruh'].tolist()

tokenizer  = TreebankWordTokenizer()

#Removing unwanted strings from keywords
list_words = [re.sub('^\W|\s'," ",w).lower().strip() for w in mec_list if len(w) > 2]
#print(list_words)
#Train 
lista=[]
sp.train(list_words)

#while(1):
 #  keyword = input('Enter any keysdsdword.. ')
  # wordl=keyword.split('_')
   #print(wordl)
   #trocar os elementos da lista world pela correcao dos mesmos
  # for i in wordl:
        #print(i)
  #      corrected_keyword=sp.spell_correct(i)
        #print(corrected_keyword)
  #      a=corrected_keyword['spell_corrected_text']
  #      lista +=[a]
  # word="_".join(str(x) for x in lista)
   
  

def testsyntax(word):
    wordl=word.split('_')
    lista=[]
    for i in wordl:
        corrected_keyword=sp.spell_correct(i)
        a=corrected_keyword['spell_corrected_text']
        lista +=[a]
    word="_".join(str(x) for x in lista)
    return word