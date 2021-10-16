def read():

    names = []
    with open('./nombres_estudiantes.txt', 'r', encoding='utf-8') as f:
        for line in f:
            names.append(line)
            print(names)


def write():

    animes = ["One piece", "Naruto", "Inuyasha",
              "Shaman King", "El detective Conan"]
    with open('./lista_anime.txt', 'w', encoding='utf-8') as f:
        for anime in animes:
            f.write(anime)
            f.write('\n')


def insert_anime_console():

    continuar = 'y'


while continuar == 'y':
with open('./lista_anime.txt', 'a', encoding='utf-8') as f:
nuevo_anime = input('Ingresa el nombre del nuevo anime:')
f.write(nuevo_anime)
f.write('\n')
continuar = input("Desea continuar (y/n): ")
if continuar == 'n':
print('El programa a finalizado correctamente.')


# def run():
# # read()
# write()


if _name_ == '_main_':
    insert_anime_console()
