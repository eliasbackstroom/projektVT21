#coding: utf-8
import random 
import time 
from difflib import SequenceMatcher

def timer():
    start_time = time.time()
    
    written_sentence = answer_sentence()
    end_time = time.time()
    
    total_time = str(end_time - start_time)
    
    return total_time
    
    
def writing():
    print("Välkommen att Spela!")
    print("Skriv meningen så snabbt du kan")
    input("Tryck Enter när du känner dig redo för att börja:")
    print("Då kör vi!")
    time.sleep(1)
    print("3")
    time.sleep(1)
    print("2")
    time.sleep(1)
    print("1")
    time.sleep(1)
    Sentence = randomsentence()
    print(Sentence)
    answer = timer()
    ratio = SequenceMatcher(None, Sentence, answer).ratio()
    print("Accuracy:", int(ratio*100),"%")
    return Sentence
    
def randomsentence():
    with open("Citat.txt","r") as file: 
        allText = file.read()
        words = list(map(str, allText.split(".")))
        
        print(random.choice(words))
       
       
def comparison():
    time = timer()
    Sentence = writing()
    print("Time:",time,"seconds")    
    total_words = len(Sentence.split())
    wpmtime = 60 // time
    wpm = wpmtime*total_words
    print("Wpm:",wpm)        
    
def answer_sentence():
    written_sentence = input("Tryck Enter när du är klar:")
    return written_sentence
    
test = writing()
print(test)
