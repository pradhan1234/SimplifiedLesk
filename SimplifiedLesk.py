# CS 6320
# NLP Homework 4
# Implemention of Simplified Lesk algorithm for Word Sense Disambiguation



# imports

import nltk
nltk.download('wordnet')
nltk.download('stopwords')
nltk.download('punkt')

from nltk.corpus import wordnet as wn
from nltk.corpus import stopwords 
from nltk.tokenize import word_tokenize 




# important variables and functions

stop_words = set(stopwords.words('english')) 

# function to remove function words (stop words)
def filterText(s):
    tokens = word_tokenize(s) 
    return [word for word in tokens if not word in stop_words]

# function to generate signature
def getSignature(sense):
    
    wordSet = set(filterText(sense.definition()))
    
    for example in sense.examples():
        wordSet = wordSet.union(set(filterText(example)))
    
    return wordSet

# function to compute overlap
def computeOverlap(signature, context):
    return len(context.intersection(signature))


# SIMPLIFIED LESK

def getBestSense(word, sentence):
    
    senses = wn.synsets(word)
    
    bestSense = senses[0]
    maxOverlap = 0
    context = set(filterText(sentence))
    
    for sense in senses:
        
        signature = getSignature(sense)
        overlap = computeOverlap(signature, context)

        print(sense,"\nDefinition: ", sense.definition(), "\nOverlap: ", overlap,"\n")

    
        if overlap > maxOverlap:
            maxOverlap = overlap
            bestSense = sense
    
    return bestSense, maxOverlap


sentence = "The bank can guarantee deposits will eventually cover future tuition costs because it invests in adjustable-rate mortgage securities."
word = "bank"

bestSense, maxOverlap = getBestSense(word, sentence)

print("\n\nBest Sense by Simplified Lesk:\n")
print("Sentence:", sentence)
print("\nword:", word)

print(bestSense)
print("\nMax Overlap:", maxOverlap)
print("\nDefinition:", bestSense.definition())
examples = bestSense.examples()

for i in range(len(examples)):
	print("Example ", i+1, ": ", examples[i])
