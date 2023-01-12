import shelve, pyperclip, sys, pprint

tag = sys.argv

clipboard = shelve.open("clipboard.txt")
db = dict(clipboard.items())


if tag[1].lower() == "list":
    for key, value in db.items():
        print("Tag:",key, 4 * " ", "Valor armazenado:", value)

elif tag[1].lower() == "copy":
    copia = db.get(tag[2])
    pyperclip.copy(copia)
    print("Copiei", copia,"para a sua área de transferência!")

elif tag[1].lower() == "del":
    key = tag[2]
    print("Apagando: ", clipboard.get(key))
    del clipboard[key]

else:
    key = tag[1]
    clipboard[key] = pyperclip.paste()

clipboard.close()
