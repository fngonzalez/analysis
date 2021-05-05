import pandas as pd
import openpyxl as op

workbook= op.load_workbook("C:/Users/Rodolfo/Documents/FNG/Autodidactismo/Finanzas/DB/DB.xlsx")
excel_sheet= workbook.active

###Obtengo títulos
titles=next(excel_sheet.values)[0:]

###Creo el dataframe
qcom_dataframe= pd.DataFrame(excel_sheet.values, columns=titles)

###Agarro los datos que me interesan
relevant_columns=['Date', 'Close/Last', 'Variation%', 'Volume', 'Open', 'High', 'Low']
qcom_fixed= qcom_dataframe[relevant_columns]

###Ya puedo borrar la primera fila porque ya tengo los títulos
qcom_fixed=qcom_fixed.drop(qcom_fixed.index[0])
print(qcom_fixed.describe())
