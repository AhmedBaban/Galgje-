#data
import os
import random
wordlist = ['informatica', 'informatiekunde', 'spelletje', 'aardigheidje', 'scholier', 'fotografie', 'waardebepaling', 'specialiteit', 'verzekering', 'universiteit', 'heesterperk']
goed = [] 
fout = []
pogingen = 5
blanks = []

#code
print("Hallo, welkom bij galgje")
print("Het doel van het spel is om een woord raden door letters te kiezen die in het woord zitten. Je krijgt te weten hoeveel letters er in het woord zitten. Je hebt vijf beurten, bij elke fout gaat er één beurt van af.")
print("je hebt " + str(pogingen) + " pogingen over")


word = random.choice(wordlist)
resterende_geraden = ""

def printword():
  printword = []
  for l in list(word):
    if l in goed:
      printword.append(l)
    else:
      printword.append('_')
  print(' '.join(printword))
      
def systemclear():
   os.system("clear")



  
#code voor input
while True:
  answer = input()
  controle = word.find(answer)
  

  if answer in goed:
    print ("je hebt deze letter al gegokt, probeer het opnieuw")

  elif answer in fout:
   print("je hebt deze letter al gegokt, probeer het opnieuw")

  elif len(answer) != 1:
    print("er is maar 1 letter mogelijk te gokken")
    
    
  elif controle == -1:
    fout.append(answer)
    print(fout)
    print(str(answer) + " zat niet in het woord. Je foute letters zijn " + str(fout))
    pogingen -= 1
    printword()
    
  elif controle != -1:
    goed.append(answer)
    print(str(answer) + " zat in het woord.") 
    printword()
  
  if pogingen == 0:
    print("Geen pogingen meer, je hebt verloren") 
    break
    
  print("je hebt nog " + str(pogingen) + " pogingen over")

print("wil je nog een keer spelen? y/n")
if input() == "y":
  
else:
  print("bedankt voor het spelen")
