#!/usr/bin/env python3

import random

subjectSing=["angel",
"crown",
"earth",
"lion",
"fire",
"demon",
"death",
"goat",
"horse",
"locust",
"mankind",
"mouth",
"plague",
"river",
"scorpion",
"serpent",
"star",
"sun",
"tree",
"trumpet",
"smell",
"you"]

subjectPlur=["angels",
"crowns",
"fires",
"demons",
"deaths",
"goats",
"horses",
"lions",
"locusts",
"mankind",
"mouths",
"plagues",
"rivers",
"scorpions",
"serpents",
"stars",
"suns",
"trees",
"trumpets",
"smells",
"they",
"you"]

verbSing=["feels",
"hears",
"sees",
"smells",
"releases",
"rushes",
"rises"
"strikes"]

verbPlur=["feel",
"hear",
"kill",
"see",
"smell",
"release",
"rush",
"rise",
"strike",]

verbCond=["can feel",
"can hear",
"can release",
"can see",
"can smell",
"can rush",
"can rise",
"can strike",
"will feel",
"will hear",
"will kill",
"will release",
"will see",
"will smell",
"will rush",
"will rise",
"will strike"]

adjective=["blue",
"golden",
"red",
"rising",
"rushing",
"sunny"]

objectSing=["angel",
"crown",
"earth",
"lion",
"fire",
"demon",
"death",
"goat",
"horse",
"locust",
"mouth",
"plague",
"river",
"scorpion",
"serpent",
"star",
"sun",
"tree",
"trumpet",
"smell",
]

objectPlur=["angels",
"crowns",
"fires",
"demons",
"deaths",
"goats",
"horses",
"lions",
"locusts",
"mouths",
"plagues",
"rivers",
"scorpions",
"serpents",
"stars",
"suns",
"trees",
"trumpets",
"smells",
"they"
]

articleSing=["the"]

articlePlur=["the"]

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
["Av", "Sp", "Vc", "Aj"]]

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
        
    theProphesy = str(theSentence) + spacer + theProphesy #uncomment to see expanded string for debugging
    return(theProphesy)

for i in range(10):
    print(constructProphesy())







