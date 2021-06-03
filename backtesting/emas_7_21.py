import pandas as pd

# Leo el CSV y lo convierto en DataFrame
spy_csv = pd.read_csv("~/Trading/db/SPY.csv")
spy_df = pd.DataFrame(spy_csv)


def calcular_media(df, media):
    # tomo el df y agarro los closes
    spy_red = spy_df["Close"].round(2)
    spy_red = spy_red.reset_index()
    del spy_red["index"]
    spy_red["mean"] = 0
    q_period = len(df)

    for period in range(0, q_period - 1):
        # a partir de que linea quiero escribir la media
        row = media + period - 1

        # si la linea cabe dentro de los periodos electos
        if row < q_period:

            # calculo la media para los valores que quiero
            mean_value = spy_red.loc[period:row, "Close"].mean().round(2)

            # asigno el valor a la columna
            spy_red.loc[row, "mean"] = mean_value
    return spy_red[["mean"]]


# conseguir los valores en una nueva funcion, devolver su nombre
def create_mean_in_df(mean, df):
    df[f"mean_{mean}"] = calcular_media(df, mean)
    return f"mean_{mean}"

#quiero que me genere una nueva columna en la que me diga cuando estar largo o corto
def buy_or_sell(list_of_mean, df):
    
    for day in range(len(df)):
        
        #si la mediana no tiene valores, entonces que no calcule nada
        if df.loc[day, list_of_mean[0]] == 0.00 or df.loc[day, list_of_mean[1]] == 0.00:
            pass
        
        #si la mediana mas chica tiene un valor mas alto que la mas grande o igual, entonces que compre
        elif df.loc[day, list_of_mean[0]] >= df.loc[day, list_of_mean[1]]:
            df.loc[day, "status"] = "long"
        
        #en cualquier otro caso, sera que la mediana mas chica es mas pequenna
        else:
            df.loc[day, "status"] = "short"

def run():
    list_of_mean = []
    list_of_mean.append(create_mean_in_df(10, spy_df))
    list_of_mean.append(create_mean_in_df(50, spy_df))
    buy_or_sell(list_of_mean, spy_df)


if __name__ == "__main__":
    run()
