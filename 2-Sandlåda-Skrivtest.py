#coding: utf-8
import random 
import time 
from difflib import SequenceMatcher

def starttimer():
    start_time = time.time()
    return start_time

def endtimer(start_time):
    end_time = time.time()
    
    total_time = int(end_time - start_time)   
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
    Sentence = str(randomsentence())
    print(Sentence)
    Original_sentence = str(Sentence)
    start_time = starttimer()
    answer = answer_sentence()
    endtime = endtimer(start_time)
    ratio = SequenceMatcher(None, Original_sentence, answer).ratio()
    
    print("-"*50)
    print("Accuracy:", int(ratio*100),"%")
    print("Time:", endtime,"seconds")
    total_words = len(Sentence.split())
    wpmtime = 60 // endtime
    wpm = wpmtime*total_words
    speed = print("Wpm:",wpm)  
    youranswer = print("Du skrev:",answer)
    correctsentence = print("Rätt svar:",Original_sentence)
    print("-"*50) 
    
    
def randomsentence():
    with open("Citat.txt","r") as file: 
        allText = file.read()
        words = list(map(str, allText.split(".")))
        
        Sentence = (random.choice(words))
        return Sentence
       
       
def comparison():
    last10 = []
    time = timer()
    Sentence = writing()
    print("Time:",time,"seconds")    
    total_words = len(Sentence.split())
    wpmtime = 60 // time
    wpm = wpmtime*total_words
    print("Wpm:",wpm)        
    last10.append(wpm)
    
def answer_sentence():
    written_sentence = input("Tryck Enter när du är klar:")
    return written_sentence
    
test = writing()
print(test)
