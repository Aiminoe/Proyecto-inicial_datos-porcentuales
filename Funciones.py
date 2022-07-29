


from ast import While
import csv

#funcion_1 la idea es realizar una funcion que logre filtrar el ingreso por comando, haciendo coincidir en el diccionario
#las dos opciones seleccionadas por el usuario y hacer una sumatoria de un tercer valor
#Me falta completar la funcio para validar los datos que ingreso el usuario

def funcion_1():
    with open ("origen_y_destinos_visitados.csv") as csvfile:
            data = list(csv.DictReader(csvfile))
   
    sumatoria = 0
    try:    
        for i in range(len(data)):
            diccionario = data[i]
            for k,v in diccionario.items():
                if v == destino:
                    for k,v in diccionario.items():
                        if v == residencia:
                            for k,v in diccionario.items():
                                if k == "turistas_no_residentes":  
                                    sumatoria += int(v)
                        elif residencia == ("FIN"):
                                break
                            #else: 
                                #print("Ingrese nuevamente pais de residencia:")
                                #residencia = input()
                    #else:
                        #print("Ingrese nuevamente provincia de destino")
                        #destino = input()   
    except:
        pass
    return sumatoria

#funcion_2 la idea de esta funcion es sumar todos los residentes elegido por el usuario para poder hacer la cuenta
#y poder calcular el promedio con el numero que retorna la funcion_1

def funcion_2():
    with open ("origen_y_destinos_visitados.csv") as csvfile:
            data = list(csv.DictReader(csvfile))
    promedio_suma = 0
    try:    
        for i in range(len(data)):
            diccionario = data[i]
            for k,v in diccionario.items():
                if v == residencia:
                    for k,v in diccionario.items():
                        if k == "turistas_no_residentes":  
                            promedio_suma += int(v)        
    except:
        pass                  
    return promedio_suma

#funcion promedio la idea es realizar en esta funcion el calculo matematico que me arroje el promedio de turistas elejido
#elejido por el usuario que visito la provincia elejida por el usuario

def promedio():
    numero_1 = int(funcion_1())
    numero_2 = int(funcion_2())
    promedio = int(numero_1 * 100) / int(numero_2)
    
    print("{}% es el promedio de turistas que visito la provincia de {}, cuyo pais de origen es {} ".format(promedio,destino, residencia)) 



if __name__ == '__main__':
    print("Bienvenido")
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
    
    funcion_1()
    
    funcion_2()

    promedio()