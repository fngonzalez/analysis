import pandas as pd
import openpyxl as op

workbook= op.load_workbook("C:/Users/Rodolfo/Documents/FNG/Autodidactismo/Finanzas/DB/DB.xlsx")
excel_sheet= workbook.active
###Obtengo títulos
titles=next(excel_sheet.values)[0:]

###Creo el dataframe
dirty_qcom_dataframe= pd.DataFrame(excel_sheet.values, columns=titles)

###Agarro los datos que me interesan
relevant_columns=['Date', 'Close/Last', 'Variation%', 'Volume', 'Open', 'High', 'Low']
qcom_dataframe= dirty_qcom_dataframe[relevant_columns]

###Ya puedo borrar la primera fila porque ya tengo los títulos
qcom_dataframe=qcom_dataframe.drop(qcom_dataframe.index[0])

###Busco los valores maximos y minimos
max_value_stock= qcom_dataframe['High'].min(axis=0)
max_close_last_52_days=qcom_dataframe['High'].tail(21).min(axis=0)
max_close_last_52_days=qcom_dataframe['Close/Last'].tail(21).min(axis=0)
min_value_stock=qcom_dataframe['Low'].min(axis=0)
min_close_last_52_days=qcom_dataframe['Low'].tail(52).min(axis=0)
min_close_last_52_days=qcom_dataframe['Low'].tail(52).min(axis=0)

###Busco los promedios de los dias que me interesan
prom_close_last_52_days=qcom_dataframe['Close/Last'].tail(52).mean()
prom_close_last_21_days=qcom_dataframe['Close/Last'].tail(21).mean()
prom_close_days=qcom_dataframe['Close/Last'].mean()
prom_close_last_52_days=qcom_dataframe['Volume'].tail(52).mean()
prom_close_last_21_days=qcom_dataframe['Volume'].tail(21).mean()
prom_close_days=qcom_dataframe['Volume'].mean()

###Busco la desviacion estandar de los dias que me interesan