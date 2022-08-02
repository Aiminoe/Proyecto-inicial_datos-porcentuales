


from ast import While
import csv
from tkinter import W

#funcion_1 la idea es realizar una funcion que logre filtrar el ingreso por comando, haciendo coincidir en el diccionario
#las dos opciones seleccionadas por el usuario y hacer una sumatoria de un tercer valor
#Me falta completar la funcio para validar los datos que ingreso el usuario

def archivo_csv():
    with open ("origen_y_destinos_visitados.csv") as csvfile:
            data = list(csv.DictReader(csvfile))
    return data

    
def origen_1():
        print('''Seleccione un pais de residencia: 
            Brasil
            Chile
            Bolivia
            Uruguay
            Paraguay
            Europa
            Resto del mundo
            EE.UU y Canada
            Resto América
            Para Finalizar indique FIN''')
        residencia = input()
        return residencia
   

def destino_1():
        print(''' Selecione la provincia de destino
            Buenos Aires
            Caba
            Cordoba
            Catamarca
            Chaco
            Chubut
            Corrientes
            Entre Rios
            Formosa
            Jujuy
            La Pampa
            Formosa
            La Rioja
            Mendoza
            Misiones
            Neuquen
            Rio Negro
            Salta
            San Juan
            San Luis
            Santa Cruz
            Santa Fe
            Santiago del Estero
            Tierra del Fuego
            Tucuman
            ''')
        destino = input()
        return destino





def filtro_residencia(residencia):
        
    data = archivo_csv()
    
    try:    
        for i in range(len(data)):
            diccionario = data[i]
            for k,v in diccionario.items():
                if k == ("pais_de_residencia") and v == residencia: 
                    lista_residencia = []
                    lista_residencia.append(diccionario)

    except:
            pass
    return lista_residencia



def filtro_destino(destino, residencia):
    lista= filtro_residencia(residencia)
    lista_destino = []
    try:    
        for i in range(len(lista)):
            filtro_2 = lista[i]
        for k,v in filtro_2.items():
            if k == ("provincia_de_destino") and v == destino: 
                lista_destino.append(filtro_2)
    except:
            pass
    return lista_destino



def funcion_sumatoria(destino):
    lista = filtro_destino(destino)
    sumatoria = 0
    try:    
        for i in range(len(lista)):
            diccionario = lista[i]
        for k,v in diccionario.items():
            if k == "turistas_no_residentes":  
                sumatoria += int(v)
    except:
        pass
    return sumatoria
                                 
#funcion_2 la idea de esta funcion es sumar todos los residentes elegido por el usuario para poder hacer la cuenta
#y poder calcular el promedio con el numero que retorna la funcion_1

def promedio_origen():
    data = archivo_csv()
    promedio_suma = 0
    destino = destino_1()
    try:    
        for i in range(len(data)):
            diccionario = data[i]
            for k,v in diccionario.items():
                if v == destino:
                    for k,v in diccionario.items():
                        if k == "turistas_no_residentes":  
                            promedio_suma += int(v)        
    except:
            pass                  
            return promedio_suma

    #funcion promedio la idea es realizar en esta funcion el calculo matematico que me arroje el promedio de turistas elejido
    #elejido por el usuario que visito la provincia elejida por el usuario

def promedio(destino, residencia):
        numero_1 = int(funcion_sumatoria(destino))
        numero_2 = int(promedio_origen())
        promedio = int(numero_1 * 100) / int(numero_2)
        
        print("{}% es el promedio de turistas que visito la provincia de {}, cuyo pais de origen es {} ".format(promedio,destino, residencia)) 




if __name__ == '__main__':
    print("Bienvenido")
        
    origen_1()

    destino_1()

    filtro_residencia()

    filtro_destino()

    funcion_sumatoria()

    promedio()
            
            