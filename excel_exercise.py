#####Los datos presentados en el codigo son diarios a menos que se explicite lo contrario######

import openpyxl as oppx
excelworkbook = oppx.load_workbook(
    "C:/Users/Rodolfo/Documents/FNG/Autodidactismo/Finanzas/DB/DB.xlsx")
excel_sheet = excelworkbook.active

cantidad_de_dias = excel_sheet.max_row
daily_cl = excel_sheet["B"]
daily_vol = excel_sheet["D"]
daily_max = excel_sheet["F"]
daily_min = excel_sheet["G"]

#limpiamos un array sacando los valores que nos interesan de lo que está 
#adentro del array que está recién salido de la planilla de excel.
def array_cleaner(dirty_array):
    clean_array = []
    counter = 0
    for data in dirty_array:
        if counter > 0:
            clean_array.append(float(data.value))
        counter = counter+1
    return clean_array

#buscamos el valor promedio de cierta cantidad de valores, y de cierto array.
def prom_calculator(array, number_of_lasts_values):
    total_value = 0.0
    
    #si el valor es cero, entonces buscamos el promedio de todos los valores
    if number_of_lasts_values == 0: 
        length_array = len(array)
        for value in array:
            total_value += value
        prom_calculated = round(total_value/length_array, 2)
        return prom_calculated
    
    #cuando el valor está determinado por el usuario, buscamos el promedio
    #del numero los valores dados
    elif number_of_lasts_values > 0:
        until = (number_of_lasts_values*-1)-1
        for value in range(-1, until, -1):
            total_value += array[value]
            prom_calculated = round(total_value/number_of_lasts_values, 2)
        return prom_calculated
    
    #cuando el valor de number_of_lasts_values no es válido
    else: 
        no_specific_value="La cantidad de dias no ha sido especificada adecuadamente.\
        Asegurate de darla en numeros: 0 da toda la historia, y los numeros positivos\
        seran los que daran el monto de sesiones a promediar"
        return no_specific_value

#buscamos los minimos y los maximos de un array, y lo sacamos en otro array que mantiene el 
#minimo y maximo, en el orden que esta expresado en el nombre de la función
def minmax_finder(array, number_of_sessions_required):
    minimal_value = 0.0
    maximal_value = 0.0
    
    if number_of_sessions_required == 0:  #tomamos todos los valores del array
        minimal_value = min(array)
        maximal_value = max(array)
    
    elif number_of_sessions_required > 0:  #tomamos ciertos los valores del array
        array_for_n_sessions = []
        until = -(number_of_sessions_required)-1
        for value in range(-1, until, -1):
            array_for_n_sessions.append(array[value])
        minimal_value = min(array_for_n_sessions)
        maximal_value = max(array_for_n_sessions)
        
    else:    #en el caso que no tenga un valor válido
        no_specific_value_content="La cantidad de dias no ha sido especificada adecuadamente.\
        Asegurate de darla en numeros: 0 da toda la historia, y los numeros positivos\
        seran los que daran el monto de sesiones a promediar"
        no_specific_value=[no_specific_value_content,no_specific_value_content]
        return no_specific_value
    minmax = [minimal_value, maximal_value]
    return minmax


daily_history_price = array_cleaner(daily_cl)
prom_historical_close = prom_calculator(daily_history_price, 0)
prom_52_close = prom_calculator(daily_history_price, 52)
prom_21_close = prom_calculator(daily_history_price, 21)

daily_history_vol = array_cleaner(daily_vol)
prom_historical_vol = prom_calculator(daily_history_vol, 0)
prom_52_vol = prom_calculator(daily_history_vol, 52)
prom_21_vol = prom_calculator(daily_history_vol, -5)

daily_history_high = array_cleaner(daily_max)
minmax_historical_high = minmax_finder(daily_history_high, 0)
minmax_52_high = minmax_finder(daily_history_high, -2)
minmax_21_high = minmax_finder(daily_history_high, 21)

daily_history_low = array_cleaner(daily_min)
minmax_historical_low = minmax_finder(daily_history_low, 0)
minmax_52_low = minmax_finder(daily_history_low, -52)
minmax_21_low = minmax_finder(daily_history_low, -9)






print(f"""El PRECIO PROMEDIO historico de la accion es de {prom_historical_close}, 
con el PRECIO PROMEDIO de los ultimos 52 dias en un valor de {prom_52_close}, y con 
valor PRECIO PROMEDIO de los ultimos 21 dias de {prom_21_close}""")
print()
print()
print(f"""El VOLUMEN PROMEDIO historico de la accion es de {prom_historical_vol}, y
con un VOLUMEN PROMEDIO de los ultimos 52 dias en {prom_52_vol}, y con un VOLUMEN
PROMEDIO en los ultimos 21 dias de {prom_21_vol}""")
print()
print()
print(f"""El MAXIMO que alcanzo la accion en su historia fue {minmax_historical_high[1]}, y
el MAXIMO de los ultimos 52 dias es {minmax_52_high[1]}, con un MAXIMO de {minmax_21_high[1]}
en los ultimos 21 dias""")
print()
print()
print(f"""El MINIMO alcanzado por la accion en su historia fue {minmax_historical_low[0]}, y
con un MINIMO de los ultimos 52 dias en {minmax_52_low[0]}, y en las ultimos 21 dias
el MINIMO se mantuvo en {minmax_21_low[0]}""")
print()
print()
