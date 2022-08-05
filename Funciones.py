


from ast import While
import csv
from tkinter import W

#funcion para abrir archivo csv

def archivo_csv():
    with open ("origen_y_destinos_visitados.csv") as csvfile:
            data = list(csv.DictReader(csvfile))
    return data

#funcion para extender la lista de paises de origen y dar entrada a la seleccion del usuario
    
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
        print()
        return residencia

#funcion para extender la lista de provincias de destino y dar entrada ala seleccion del usuario   

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
        print()
        return destino




#funcion para filtrar datos sobre el pais de residencia de turista seleccionado por el usuario, creando una lista

def filtro_residencia(residencia):    
    data = archivo_csv()
    lista_residencia = []
    try:    
        for i in range(len(data)):
            diccionario = data[i]
            for k,v in diccionario.items():
                if k == ("pais_de_residencia") and v == residencia:     
                   lista_residencia.append(diccionario)

    except:
            pass
    return lista_residencia


#funcion para filtrar datos sobre la provincia de recidencia visitada, seleccionada por el usuario. Se utiliza
#la lista anteriormente creada en la funcion filtro_residencia

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


#funcion que realiza una sumatoria de la cantidad de turistas (de origen seleccionado por el usuario), que visito
#la provincia argentina (seleccionada por el usuario)

def funcion_sumatoria(destino,residencia):
    lista = filtro_destino(destino,residencia)
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
                                 
#esta funcion suma todos los residentes elegido por el usuario para poder hacer la operacion
#y poder calcular el promedio con el numero que retorna la funcion_sumatoria

def promedio_origen(residencia):
    lista = filtro_residencia(residencia)
    promedio_suma = 0
    try:    
        for i in range(len(lista)):
            diccionario = lista[i]
            for k,v in diccionario.items():
                if v == residencia:
                    for k,v in diccionario.items():
                        if k == "turistas_no_residentes":  
                            promedio_suma += int(v)        
    except:
            pass                  
    return promedio_suma

    #funcion promedio realiza el calculo matematico resultando del promedio de turistas
    #elejido por el usuario que visito la provincia elejida por el usuario

def promedio(destino, residencia):
        numero_1 = int(funcion_sumatoria(destino,residencia))
        numero_2 = int(promedio_origen(residencia))
        promedio = int(numero_1 * 100) / int(numero_2)
        
        print('''{}% es el promedio de turistas,cuyo pais de origen es {}, que visitaron la proviancia de {} 
        desde el comienzo del año 2022 hasta el mes de Mayo \n'''.format(round(promedio,2), residencia,destino)) 



if __name__ == '__main__':
    print("Bienvenido")
    
    lugar_origen = ''
    
    while lugar_origen.upper() != 'FIN':

        lugar_origen = origen_1()

        if lugar_origen.upper() != 'FIN':
           
            provincia_destino = destino_1()

            filtro_residencia((lugar_origen))

            filtro_destino((provincia_destino),(lugar_origen))

            funcion_sumatoria((provincia_destino),(lugar_origen))

            promedio_origen(lugar_origen)

            promedio((provincia_destino),(lugar_origen))
                      

            print('Fin del programa.\n')    
    
            
            