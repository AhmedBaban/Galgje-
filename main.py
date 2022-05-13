#data
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

for i in range(len(word)):
  blanks.append('_')

blanks = '_' * len(word)

for i in range(len(word)): 
  if word[i] in goed:
    blanks = blanks[:i] + word[i] + blanks[i+1:]
  
#code voor input
while True:
  print(blanks)
  answer = input()
  controle = word.find(answer)

  if answer in goed:
    print ("je hebt deze letter al gegokt, probeer het opnieuw")

  elif answer in fout:
   print("je hebt deze letter al gegokt, probeer het opnieuw")

  elif len(answer) != 1:
    print("er is maar 1 letter mogelijk te gokken")
    break #tijdelijke functie
    
  elif controle == -1:
    fout.append(answer)
    print(fout)
    print(str(answer) + " zat niet in het woord. Je foute letters zijn " + str(fout))
    pogingen -= 1
    
  elif controle != -1:
    goed.append(answer)
    print(str(answer) + " zat in het woord. Je goede letters zijn " + str(goed)) #verander dit wanneer de letter in de letterinwoord werkt
  
  if pogingen == 0:
    print("je hebt verloren hahaha") #verander dit nog ff
    break
  print("je hebt nog " + str(pogingen) + " pogingen over")


