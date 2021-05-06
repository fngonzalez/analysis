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

#busco los valores maximos y minimos
max_value_stock= qcom_dataframe['High'].min(axis=0)
min_value_stock=qcom_dataframe['Low'].min(axis=0)

