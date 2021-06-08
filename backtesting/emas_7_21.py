import pandas as pd

# Leo el CSV y lo convierto en DataFrame
spy_csv = pd.read_csv("~/Trading/db/SPY.csv")
spy_df = pd.DataFrame(spy_csv.tail(1000)).round(2)
spy_df = spy_df.reset_index()
del spy_df["index"]


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


def buy_or_sell(list_of_mean, df):
    df["status"] = ""
    df["result"] = ""
    q_day = 1
    for day in range(1, len(df)):
        # #si la mediana no tiene valores, entonces que no calcule nada
        if df.loc[day, list_of_mean[0]] == 0.00 or df.loc[day, list_of_mean[1]] == 0.00:
            df.loc[day, "status"] = ""

        # # si la mediana mas chica tiene un valor mas alto que la mas grande o igual, entonces que compre
        elif df.loc[day, list_of_mean[0]] >= df.loc[day, list_of_mean[1]]:
            df.loc[day, "status"] = "long"
            df.loc[day, "result"] = 0
            # #si el dia de ayer estabamos cortos
            if df.loc[day - 1, "status"] == "short":
                df.loc[day, "status"] = "c_short"
                yest_result = df.loc[day - 1, "result"]
                today_change = df.loc[day, "diff"]
                df.loc[day, "t_result"] = yest_result + -today_change
                df.loc[day, "result"] = yest_result + -today_change
                
                # le sumo el dia de hoy, y despues lo reinicio
                df.loc[day, "q_days"] = q_day + 1
                q_day = 1

            # si el dia de ayer estabamos largos
            elif df.loc[day - 1, "status"] == "long":
                # le sumamos el resultado al resultado
                yest_result = df.loc[day - 1, "result"]
                today_change = df.loc[day, "diff"]
                df.loc[day, "result"] = yest_result + today_change
                
                # le sumo el dia
                q_day = q_day + 1

        # en cualquier otro caso, sera que la mediana mas chica es mas pequenna
        else:
            df.loc[day, "status"] = "short"
            df.loc[day, "result"] = 0

            # si el dia de ayer estabamos largos
            if df.loc[day - 1, "status"] == "long":
                df.loc[day, "status"] = "c_long"
                yest_result = df.loc[day - 1, "result"]
                today_change = df.loc[day, "diff"]
                df.loc[day, "t_result"] = yest_result + today_change
                df.loc[day, "result"] = yest_result + today_change
                
                # le sumo el dia de hoy, y despues lo reinicio
                df.loc[day, "q_days"] = q_day + 1
                q_day = 1

            # si el dia de ayer estabamos cortos
            elif df.loc[day - 1, "status"] == "short":
                # le sumamos el resultado de ayer al resultado de hoy
                yest_result = df.loc[day - 1, "result"]
                today_change = df.loc[day, "diff"]
                df.loc[day, "result"] = yest_result + -today_change
                
                # le sumo el dia
                q_day = q_day + 1


# calcula la variacion de los valores
def calc_diff(df):
    # en el dia cero no vamos a tener comparacion
    df.loc[0, "diff"] = 0
    for day in range(1, len(df)):
        # agarra el valor del dia de hoy
        today_close = df.loc[day, "Close"]

        # agarra el valor del dia de ayer
        yest_close = df.loc[day - 1, "Close"]

        # calcula la diferencia
        diff = today_close - yest_close

        # se mete la variable en la columna correspondiente
        df.loc[day, "diff"] = diff.round(2)


def send_to_excel(df, path, sheetname):
    writer = pd.ExcelWriter(path)
    df.to_excel(
        writer,
        sheetname,
    )
    writer.save()


def run():
    list_of_mean = []
    list_of_mean.append(create_mean_in_df(7, spy_df))
    list_of_mean.append(create_mean_in_df(21, spy_df))
    calc_diff(spy_df)
    buy_or_sell(list_of_mean, spy_df)
    path = "~/Documentos/Analisis-spy.xlsx"
    sheetname = "analisis-medias"
    send_to_excel(spy_df, path, sheetname)


if __name__ == "__main__":
    run()
