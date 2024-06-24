macaco = 'africano mongo tongo'
babuino = '  manga suculenta  '
songs = ["Yesterday", "Hello", "Believer"]
items = ["book", "pen", "pencil"]
#a função len fala a quantidade caracteres da string
print(len(macaco))
#a função .count vai falar quantos caracteres 'o' existem na string
print(macaco.count('o', 0, 14))
#a função .find vai falar em que parte da string 'cano' vai aparecer
print(macaco.find('cano'))
# a função 'in' vai falar se a string 'tongo' aparece na variavel 'macaco' se ela aparecer true se não false
print('tongo'in macaco)
print(macaco)
#a função .replace troca a string 'africano' pela string 'garoto'
print(macaco.replace('africano', 'garoto'))
#a função .upper() deixa a string da variavel 'macaco' em maiúscula
print(macaco.upper())
#é o oposto da .upper
print(macaco.lower())
#a função .capitalize deixa toda string em minusculo mais a primeira letra em maiúculo
print(macaco.capitalize())
#a função .title todas as palavras com a primeira letra maiuscula
print(macaco.title())
#a função .strip vai fazer com os espaços vazios do começo e do final da string sejam removidos
print(babuino.strip())
#a função .rstrip vai remover os espaços vazios só da direita
print(babuino.rstrip())
#A função append() adiciona um novo item ao final de uma lista. 
songs.append("Imagine")
print(songs)
#A função insert() permite que você adicione um elemento a uma lista, em uma posição específica.
items.insert(2,"marker")
print(items)
print(items[2])
#A função pop() remove um elemento de uma lista.
items.pop(1)
print(items)
print(items[1])
#a função .split transforma a string em uma lista
print(babuino.split())