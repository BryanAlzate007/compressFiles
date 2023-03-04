from zipfile import ZipFile
#comentario#
def descomprimir():
    archivo = "C:\\Users\\USER2021\\GREENFIELD\\*.zip"
    with ZipFile(file = archivo, mode = "r", allowZip64=True) as file:
        archivo = file.open(name = file.namelist()[0], mode = "r")
        print(archivo.read())
        archivo.close()

        navegacion = "C:\\Users\\USER2021\\GREENFIELD"
        print("Descomprimiendo")
        file.extractall(path = navegacion)
        print("archivo descomprimido")
descomprimir()
