import enum


def df_to_mongo():
    import pandas as pd
    df = pd.read_csv("test-data.csv", header=3)
    df = df.drop(columns=["Unnamed: 0"])
    df.dropna()
    data = [df.iloc[i].to_dict() for i in range(len(df))]

    return data

def string_to_month(input_month):
    months = ["january", "febuary", "march", 
                "april", "may", "june",
                "july", "august", "september",
                "october", "november", "december"]
    
    for month in months:
        if input_month.lower() in month:
            return months.index(month) + 1

    return 

def month_to_string(month):
    months = ["January", "Febuary", "March", 
                "April", "May", "June",
                "July", "August", "September",
                "October", "November", "December"]

    return months[month - 1]

def body_formatter(data):
    body = ""

    for idx, val in enumerate(data):
        body += f"{str(idx + 1)}.  {val}"

    return body