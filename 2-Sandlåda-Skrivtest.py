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
    begin = input("Tryck 1 för att börja, Tryck 2 för instruktioner, Tryck 3 för att byta kategori:")
    choose = "Citat"
    if begin == "1":
        startgame(choose)
    if begin == "2":
        print("Spelet går ut på att du ska skriva meningen som kommer upp så snabbt som möjligt.")
        print("Efter du skrivit meningen kommer du få resultat i form av ord per minut och träffsäkerhet")
        begin = input("För att komma till menyn igen tryck 1 följt av Enter:")
        if begin == "1":
            startgame(choose)
    if begin == "3":
        choose = choosefiles()
        startgame(choose)
        
    
    
def choosefiles():
    choose = input("Välj vilket tema du vill skriva på. Skriv Quotes eller Böcker för att välja:")
    choose = choose.capitalize()
    if choose != "böcker" or choose != "Böcker":
        choose = input("Något blev fel, var snäll och skriv igen")
    return choose
    
def randomsentence(choose):
    with open(str(choose) + ".txt","r") as file: 
        allText = file.read()
        words = list(map(str, allText.split(".")))
        
        sentence = (random.choice(words))

    return sentence
       
       
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
    
    
def startgame(choose):
    print("Då kör vi!")
    time.sleep(1)
    print("3")
    time.sleep(1)
    print("2")
    time.sleep(1)
    print("1")
    time.sleep(1)
    Sentence = str(randomsentence(choose))
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
test = writing()
print(test)
