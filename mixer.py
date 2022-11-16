#!/usr/bin/env python3

import random

subjectSing=[
"angel",
"goat",
"horse",
"locust",
"mouth",
"scorpion",
"serpent",
"star",
"sun",
"trumpet",
"smell"
]

subjectPlur=[
"angels",
"goats",
"horses",
"locusts",
"mouths",
"scorpions",
"serpents",
"stars",
"suns",
"trumpets",
"smells",
"they"
]

verbSing=[
"feels",
"hears",
"sees",
"smells",
"rushes",
"rises"
]

verbPlur=[
"feel",
"hear",
"see",
"smell",
"rush",
"rise"
]

verbCond=[
"can feel",
"can hear",
"can see",
"can smell",
"can rush",
"can rise"
]

adjective=[
"golden",
"rising",
"rushing",
"sunny"
]

objectSing=[
"angel",
"goat",
"horse",
"locust",
"mouth",
"scorpion",
"serpent",
"star",
"sun",
"trumpet",
"smell"
]

objectPlur=[
"angels",
"goats",
"horses",
"locusts",
"mouths",
"scorpions",
"serpents",
"stars",
"suns",
"trumpets",
"smells"
]

articleSing=["the"]

articlePlur=["the","some"]

adverb=["now","soon"]

sentences=[
["Sp", "Vc", "As", "Os"],       
["Sp", "Vp", "Ap", "Aj", "Op"],
["Sp", "Vc", "As", "Op", "Aj"],
["Sp", "Vc", "As", "Op", "Vs", "Av"],
["Sp", "Vp", "Op"],
["Sp", "Av", "Vc"],
["Sp", "Vp", "Aj", "Op"],
["Sp", "Vp", "Op", "An", "Op"],
["Sp", "Vp", "Op"],
["Sp", "Vc", "Op"],
["Sp", "Vp", "Ap", "Op", "Vp"],
["Sp", "Sp", "Vc"],
["Sp", "Sp", "An", "Sp", "Al", "Vp"],
["Sp", "Vp", "As", "Aj", "Op"],
["Sp", "Vc", "As", "Os", "Aj"],
["Sp", "Vc", "As", "Op", "Aj"],
["Sp", "Vp", "Aj"],
["As", "Ss", "Ap", "Sp", "Vp", "Aj"],
["As", "Ss", "Vc"],
["Av", "Sp", "Vc"],
["Av", "As", "Ss", "Av", "As", "Ss"],
["Av", "Sp", "Vc", "Aj"]
]

def Ss():
    #get singular subject
    word=pickWord(subjectSing)
    return(word)

def Sp():
    #get plural subject
    word=pickWord(subjectPlur)
    return(word)

def Vs():
    #get singular verb
    word=pickWord(verbSing)
    return(word)

def Vp():
    #get plural verb
    word=pickWord(verbPlur)
    return(word)

def Vc():
    #get conditional verb
    word=pickWord(verbCond)
    return(word)

def Aj():
    #get adjective
    word=pickWord(adjective)
    return(word)

def Os():
    #get singular object
    word=pickWord(objectSing)
    return(word)

def Op():
    #get plural object
    word=pickWord(objectPlur)
    return(word)

def As():
    #get singular article
    word=pickWord(articleSing)
    return(word)

def Ap():
    #get plural article
    word=pickWord(articlePlur)
    return(word)

def Av():
    #get adverb
    word=pickWord(adverb)
    return(word)

def Al():
    return("all")

def An():
    return("and")

def pickWord(wordList):
    #get a random word from whichever word list is sent in (e.g. subjectSing)
    return(random.choice(wordList))

def pickSentence():
    #get a sentence from the list of sentence prototypes
    theSentence = random.choice(sentences)
    return(theSentence)

def getWord(functionString): 
    #use the string notation of the sentence prototype as a named function call
    return(globals()[functionString]())

def constructProphesy():
    #the oracle speaks!
    theSentence=pickSentence()
    
    spacer = ''
    tabs= 7 - len(theSentence)
    for item in range(tabs):
        spacer = spacer + '      '

    theProphesy = ''
    for thisWord in theSentence:
        theProphesy = theProphesy + getWord(thisWord) + " "
        
    #theProphesy = str(theSentence) + spacer + theProphesy #uncomment to see expanded string for debugging
    return(theProphesy)

for i in range(10):
    print(constructProphesy())




# %%



