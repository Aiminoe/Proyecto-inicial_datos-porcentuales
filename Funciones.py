


import csv

#funcion para abrir archivo csv

def archivo_csv():
    with open ("origen_y_destinos_visitados.csv") as csvfile:
            data = list(csv.DictReader(csvfile))
    return data

#funcion para extender la lista de paises de origen y dar entrada a la seleccion del usuario
    
def origen_1():
        paises = {"1": "Brasil" , "2": "Chile", "3": "Bolivia" , "4": "Uruguay", "5": "Paraguay", "6": "Europa", "7": "Resto del mundo", "8": "EE.UU y Canada", "9": "Resto America", "10": "FIN"}   
        print('''Ingrese el numero del pais de residencia que desea selecionar, o el numero para finalizar: 
            1)Brasil
            2)Chile
            3)Bolivia
            4)Uruguay
            5)Paraguay
            6)Europa
            7)Resto del mundo
            8)EE.UU y Canada
            9)Resto America
            10)FIN''')
        opcion_1 = input("Ingrese una opcion: ")
        print()
        residencia = paises.get(opcion_1, '')
        return residencia

#funcion para extender la lista de provincias de destino y dar entrada ala seleccion del usuario   

def destino_1():
    provincias = {"1": "Buenos Aires", "2": "Caba", "3": "Cordoba", "4": "Catamarca", "5": "Chaco", "6": "Chubut", "7": "Corrientes", "8": "Entre Rios", "9": "Formosa", "10": "Jujuy", "11": "La Pampa", "12": "Formosa", "13": "La Rioja", "14": "Mendoza", "15": "Misiones", "16": "Neuquen", "17": "Rio Negro", "18": "Salta", "19": "San Juan", "20": "San Luis", "21": "Santa Cruz", "22": "Santa Fe", "23": "Santiago del Estero", "24": "Tierra del Fuego", "25": "Tucuman"}
    print(''' Selecione el numero de la provincia de destino
            1)Buenos Aires
            2)Caba
            3)Cordoba
            4)Catamarca
            5)Chaco
            6)Chubut
            7)Corrientes
            8)Entre Rios
            9)Formosa
            10)Jujuy
            11)La Pampa
            12)Formosa
            13)La Rioja
            14)Mendoza
            15)Misiones
            16)Neuquen
            17)Rio Negro
            18)Salta
            19)San Juan
            20)San Luis
            21)Santa Cruz
            22)Santa Fe
            23)Santiago del Estero
            24)Tierra del Fuego
            25)Tucuman
            ''')
    opcion_2 = input("Ingrese una opcion: ")
    destino = provincias.get(opcion_2,'') 
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
        
        print('''{}% es el promedio de turistas,cuyo pais de origen es {}, visitaron la proviancia de {} 
        desde el comienzo del año 2022 hasta el mes de Mayo \n'''.format(round(promedio,2), residencia,destino)) 



if __name__ == '__main__':
    print("Bienvenido")
    
    opcion_1 = ''
    opcion_2 = ''
    
    while opcion_1 != '10':

        lugar_origen = origen_1()
        

        if opcion_1.isdigit():

            if opcion_1 != '10':

                provincia_destino = destino_1()
                

                if opcion_2.isdigit():
                    

                    filtro_residencia(lugar_origen)

                    filtro_destino((provincia_destino),(lugar_origen))

                    funcion_sumatoria((provincia_destino),(lugar_origen))

                    promedio_origen(lugar_origen)

                    promedio((provincia_destino),(lugar_origen))
                else:
                    print("La opcion ingresada no es valida, ingrese una correcta")
                    provincia_destino = destino_1(opcion_2)          
            else:
                break
        else:
            print("La opcion ingresada no es valida, ingrese la opcion nuevamente")
            

                      

    print('Fin del programa.\n')    
    
            
            