#modulo para regular expressions
import re

## Exemplo 1 ##
#Queremos pegar o valor 12345 da seguinte linha de log:
#July 31 07:51:48 mycomputer bad_process[12345]: ERROR Performing package upgrade"
log = "July 31 07:51:48 mycomputer bad_process[12345]: ERROR Performing package upgrade"
regex = r"\[(\d+)\]"

result = re.search(regex, log)
print("_________________________")
print("Exemplo 1 - re.search")
print(result[1])

## Exemplo 2 ##
## Procura no texto uma palavra que segue um certo padrão. ".", nesse caso, é substrituido por qualquer caractere.
## comando re.findall é siminar ao grep do linux
print("_________________________")
print("Exemplo 2 - re.findall")
text = "alo? Qual o seu ano de nascimento?"
result = re.findall("a.o", text)
print(result)

## Exemplo 3 ##
print("_________________________")
print("Exemplo 3 - re.search")

result = re.search(r"aza", "plaza")
print("result1: {}".format(result))

result = re.search(r"aza", "bazaar")
print("result2: {}".format(result))

result = re.search(r"aza", "maze")
print("result3: {}".format(result))

result = re.search(r"^x", "xennon")
print("result4: {}".format(result))

result = re.search(r"p.ng", "penguin")
print("result5: {}".format(result))

result = re.search(r"p.ng", "pingpong")
print("result6: {}".format(result))

result = re.search(r"p.ng", "Pangaea", re.IGNORECASE)
print("result7: {}".format(result))

result = re.search(r"[Pp]ython", "Python")
print("result8: {}".format(result))

result = re.search(r"[a-z]way", "The end of the highway")
print("result9: {}".format(result))

result = re.search(r"[a-w]way", "We will find a way")
print("result10: {}".format(result))

result = re.search(r"cloud[a-zA-Z-0-9]", "cloudy")
print("result11: {}".format(result))

result = re.search(r"cloud[a-zA-Z-0-9]", "cloud9")
print("result12: {}".format(result))

result = re.search(r"[^a-zA-Z]", "asgd1oiasdgas")
print("result13: {}".format(result))

result = re.search(r"cat|dog", "I like cats")
print("result14: {}".format(result))

result = re.findall(r"cat|dog", "I like cats and I like dogs")
print("result15: {}".format(result))

## Exemplo 4 ###
print("_________________________")
print("Exemplo 4 - re.search")
def check_aei (text):
  result = re.search(r"a.e.i", text)
  return result != None

print(check_aei("academia")) # True
print(check_aei("aerial")) # False
print(check_aei("paramedic")) # True

## Exemplo 5 ##
## uma função que retorna true se existe qualquer pontuação na string (De exclamação a ponto na tabela ascii)
print("_________________________")
print("Exemplo 5 - re.search")
def check_punctuation (text):
  result = re.search(r"[!-.]", text)
  return result != None

print(check_punctuation("This is a sentence that ends with a period.")) # True
print(check_punctuation("This is a sentence fragment without a period")) # False
print(check_punctuation("Aren't regular expressions awesome?")) # True
print(check_punctuation("Wow! We're really picking up some steam now!")) # True
print(check_punctuation("End of the line")) # False


## Exemplo 6 ##
## Uma função que retorna true se a palavra tiver pelo menos dois "a"
print("_________________________")
print("Exemplo 6 - re.search")

def repeating_letter_a(text):
  result = re.search(r"[aA].*[aA]", text)
  return result != None

print(repeating_letter_a("banana")) # True
print(repeating_letter_a("pineapple")) # False
print(repeating_letter_a("Animal Kingdom")) # True
print(repeating_letter_a("A is for apple")) # True

## Exemplo 7 ##
## backslash - \    usar caracteres especiais, como o "."
print("_________________________")
print("Exemplo 7 - re.search com backslash")
print(re.search(r".com", "website.com"))

## Exemplo 8 ##
## Achar palavras que começam com A e terminam com a
print("_________________________")
print("Exemplo 8 ")
print(re.search(r"^A.*a$", "Argentina"))    #O sinal ^ indica que a string tem que começar com A e $ indica que deve terminar com a
print(re.search(r"^A.*a$", "Azerbeijan"))

## Exemplo 9 ##
## Verificar se uma string é um nome válido de variavel (não pode começar com numeros nem ter espaços)
print("_________________________")
print("Exemplo 9 ")

pattern = r"^[a-zA-Z_][a-zA-Z0-9_]*$"
print(re.search(pattern, "_this_is_a_valid_variable_name"))
print(re.search(pattern, "1_this_is_a_not valid variable_name"))
print(re.search(pattern, "123quatro"))

## Exemplo 10 ##
print("_________________________")
print("Exemplo 10 ")



## Exemplo 11 ##
print("_________________________")
print("Exemplo 11 ")


