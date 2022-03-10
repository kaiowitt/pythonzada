from ast import If
from cmath import inf

acelerar  = "acelerar"
voar = "voar"
planar = "planar"
pilotoautomatico = "pilotoautomatico"
pousar = "pousar"

print ("Os comandos devem ser inseridos em ordem crescente como indica o manual | 1° acelerar , 2° voar , 3° planar , 4° levantar voo , 5° pousar "   )

def pergunta() :
    
    (input("comando incorreto, digite novamente  . "))
    
comando1 = (input("digite seu comando.   "))


    
while True : 
    if comando1 != acelerar : pergunta()
    
    else : print ("acelerando")
    break

comando2 = (input("digite o comando 2    ."))

while voar :
    if comando2 != voar : pergunta()
    else : print ("decolando")
    break

comando3 = (input("digite o comando 3    . "))

while planar :
    if comando3 != planar : pergunta()
    else : print ("planando")
    break

comando4 = (input("digite o comando 4   ."))

while pousar :
    if comando3 != pousar : pergunta()
    else : print ("avião pousando em segurança")
    break

print ("você chegou ao seu local de destino")

  






    

         
