import pandas as pd

#Leo el CSV y lo convierto en DataFrame
qcom_csv = pd.read_csv('../db/qcom.csv')
qcom_df = pd.DataFrame(qcom_csv)

#Le saco caracteres que no me interesan
qcom_df = qcom_df.replace({'\$': ''}, regex=True)

#convierto los valores del df a tipos correspondientes
qcom_df = qcom_df.apply(pd.to_numeric, errors='ignore')
qcom_df.Date = pd.to_datetime(qcom_df.Date)


#Simplifico la manera de buscar minimos
def find_min_value(days, column, df):
    min_value = 0
    if days == 0:
        min_value = df[f'{column}'].min(axis=0)
    else:
        min_value = df[f'{column}'].head(days).min(axis=0)
    return min_value


#Simplifico la manera de buscar maximos
def find_max_value(days, column, df):
    max_value = 0
    if days == 0:
        max_value = df[f'{column}'].max(axis=0)
    else:
        max_value = df[f'{column}'].head(days).max(axis=0)
    return max_value


#Simplifico la manera de buscar la media
def find_mean_value(days, column, df):
    mean_value = 0
    if days == 0:
        mean_value = df[f'{column}'].mean()
    else:
        mean_value = df[f'{column}'].head(days).mean()
    return round(mean_value, 2)


#busco los valores que me interesan para ciertos periodos
minimal_year = find_min_value(0, 'Low', qcom_df)
minimal_21 = find_min_value(21, 'Low', qcom_df)
minimal_52 = find_min_value(52, 'Low', qcom_df)

maximal_year = find_max_value(0, 'High', qcom_df)
maximal_21 = find_max_value(21, 'High', qcom_df)
maximal_52 = find_max_value(52, 'High', qcom_df)

mean_y_close = find_mean_value(0, 'Close/Last', qcom_df)
mean_21_close = find_mean_value(21, 'Close/Last', qcom_df)
mean_52_close = find_mean_value(52, 'Close/Last', qcom_df)

mean_y_vol = find_mean_value(0, 'Volume', qcom_df)
mean_21_vol = find_mean_value(21, 'Volume', qcom_df)
mean_52_vol = find_mean_value(52, 'Volume', qcom_df)

#los imprimo
print(qcom_df)
print(
    f"""El PRECIO PROMEDIO historico del utlimo año de la accion es de {mean_y_close},
con el PRECIO PROMEDIO de los ultimos 52 dias en un valor de {mean_52_close}, y con
valor PRECIO PROMEDIO de los ultimos 21 dias de {mean_21_close}""")
print()
print()
print(
    f"""El VOLUMEN PROMEDIO de la accion en el ultimo año es de {mean_y_vol}, y
con un VOLUMEN PROMEDIO de los ultimos 52 dias en {mean_52_vol}, y con un VOLUMEN
PROMEDIO en los ultimos 21 dias de {mean_21_vol}""")
print()
print()
print(
    f"""El MAXIMO que alcanzo la accion en el ultimo año fue {maximal_year}, y
el MAXIMO de los ultimos 52 dias es {maximal_52}, con un MAXIMO de {maximal_21}
en los ultimos 21 dias""")
print()
print()
print(f"""El MINIMO alcanzado por la accion en el año fue {minimal_year}, y
con un MINIMO de los ultimos 52 dias en {minimal_52}, y en las ultimos 21 dias
el MINIMO se mantuvo en {minimal_21}""")
print()
print()

