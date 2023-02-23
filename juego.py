import random
import string

from db_palabras import palabras
from diagrama_vidas import vidas_diccionario_visual


def obtner_palabra_válida(lista_palabras):
  #Seleccionar una palabra al azar
  palabra_elegida=random.choice(lista_palabras)
  
  while '-' in palabra_elegida or ' ' in palabra_elegida :
    palabra_elegida=random.choice(lista_palabras)
  
  return palabra_elegida.upper()

def ahorcado():
  print("           __   __   __        __   __  ")
  print(" /\  |__| /  \ |__) /  `  /\  |  \ /  \ ")
  print("/~~\ |  | \__/ |  \ \__, /~~\ |__/ \__/ ")
  print("                                        ")

  palabra = obtner_palabra_válida(palabras)

  letras_por_adivinar = set(palabra)
  letras_adivinadas = set()
  abecedario = set(string.ascii_uppercase)

  vidas = 7

  while len(letras_por_adivinar) > 0 and vidas >0 :
    if len(letras_adivinadas)==0:
      print(f"Vidas restantes: {vidas}")
    else:
      print(f"Vidas restantes: {vidas} y usaste las letras: {' '.join(letras_adivinadas)}")

    #mostrar estado de la palabra 
    #list comprehension
    palabra_lista = [letra if letra in letras_adivinadas else "-" for letra in palabra]

    # palabra_lista2=[]
    # for letra in palabra:
    #   if letra in letras_adivinadas :
    #     palabra_lista2.append(letra)
    #   else:
    #     palabra_lista2.append('-')
    
    #Mostrar estado de la horca
    print(vidas_diccionario_visual[vidas])

    #Mostrar estado de la palabra
    print(f"Palabra: {' '.join(palabra_lista)}")

    letra_ingresada = input("Elige una letra: ").upper()

    #si la letra ingresada esta en el abecedario pero no el conjunto de letras elegidas, se añade al conjunto de letras elegidas
    if letra_ingresada in abecedario - letras_adivinadas :
      letras_adivinadas.add(letra_ingresada)

      #si la letra esta en la palabras quita la letras del conjunto de letras por adivinar
      if letra_ingresada in letras_por_adivinar:
        letras_por_adivinar.remove(letra_ingresada)
        print('')
      #si la letra no esta en la palabras quita una vida al usuario
      else:
        vidas-=1
        print(f'\n La letra {letra_ingresada} no está en la palabra.')

    #si la letra ingresada esta en el abecedario y en el conjunto de letras elegidas
    elif letra_ingresada in letras_adivinadas:
      print(f'\n Ya elegiste la letra {letra_ingresada}, escoge una letra nueva.')
    else:
      print("\n La letra ingresada no es válida.")
  
  if vidas == 0 :
    print("===============================")
    print("|          ¡Perdiste!          |")
    print("===============================")
    print(vidas_diccionario_visual[vidas])
    print(f'Ya no te quedan vidas. La palabra era {palabra}')
  else:
    print("===============================")
    print("|      ¡Ganaste el juego!      |")
    print("===============================")

ahorcado()