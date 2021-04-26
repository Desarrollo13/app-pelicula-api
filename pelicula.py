import jinja2
import requests
import json

def programa_pelicula():

    ruta= jinja2.Environment(loader= jinja2.FileSystemLoader("C:/xampp/htdocs/python/pelicula/"))
    plantilla=ruta.get_template("plantilla_pelicula.html")
    pelicula=input("Elige una pelicula: ")

    # hacemos una peticion
    peticion = requests.get(f"http://www.omdbapi.com/?t={pelicula.lower()}&apikey=886aec54 ")

    contenidojson=json.loads(peticion.text)
    nombre=contenidojson["Title"]
    genero=contenidojson["Genre"]
    sipnosis=contenidojson["Plot"]
    director=contenidojson["Director"]
    protagonistas=contenidojson["Actors"]
    poster=contenidojson["Poster"]


    # Vamos a crear un diccionario de datos
    datos_pelicula={
        "Nombre":nombre,
        "Genero":genero,
        "Sipnosis":sipnosis,
        "Director":director,
        "Protagonistas":protagonistas,
        "Poster":poster
    }
    # vamos a crear una variable que va contener el html el render va sobreescibrir en el html los datos_pelicula
    html=plantilla.render(datos_pelicula)
    file=open(f"{nombre}.html","w")
    file.write(html)
    file.close()
    continuar()
def continuar():
    intentar=input("Quieres buscar otra pelicula? (si o no): ")
    if intentar.lower()=="si":
        print("")
        programa_pelicula()    
    elif intentar.lower()=="no":
        print("Hasta lugo")    
        return False
    else:
        continuar()
        
programa_pelicula()        
        