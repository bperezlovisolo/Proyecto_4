import pandas as pd

def informe(x):
    print("Información del DataFrame:")
    print(x.info())
    print("Descripción estadística:")
    print(x.describe())
    print("Valores nulos:")
    print(x.isnull().sum())
    print("Tipos de datos:")
    print(x.dtypes)
    
    print("Primeras 5 filas:")
    print(x.head())
    print("Últimas 5 filas:")
    print(x.tail())
    print("Forma del DataFrame:")
    print(x.shape)
    print("columnas")
    print(x.columns)
    print("numericos")
    print(x.select_dtypes(include=["number"]).columns)

def datos(x):
    print("datos nulos")
    print(x.isnull().sum())
    print("datos totales")
    print(x.count())   
    print("porcentaje de nulos")
    print(x.isnull().sum() / x.shape[0]*100)
    print("datos duplicados")
    print(x.duplicated().sum())
    print(x.duplicated().any())


def limpiar_nulos(x):
    df = x.copy()
    df = x.dropna()
    return df


def drop_columns (df, columns):
    df.drop(columns, axis=1, inplace=True)


def clean_demo_data(df):
    #Renombramos columnas
    df = df.rename(columns={
        'clnt_tenure_yr': 'tenure_year',
        'clnt_tenure_mnth': 'tenure_month', 
        'clnt_age': 'age', 
        'gendr': 'gender', 
        'num_accts': 'num_accounts'})
    
    #Convertimos y redondeamos
    cols_to_int = ['num_accounts', 'calls_6_mnth', 'logons_6_mnth', 'tenure_year', 'tenure_month', 'age']
    for col in cols_to_int:
        df[col] = df[col].round(0).astype('Int64')
    
    #Limpiamos género
    df['gender'] = (df['gender'].astype("string").str.strip().str.upper().replace("X", "U").fillna("U"))

    return df


def categorize_columns(df):
    #Creamos categoría edad
    age_bins = [0, 18, 35, 60, df["age"].max()]
    age_labels = ['Under 18', 'Young Adult', 'Adult', 'Senior']
    df['age_category'] = pd.cut(df['age'], bins=age_bins, labels=age_labels, include_lowest=True)

    #Creamos categoría antigüedad
    tenure_bins = [0, 5, 10, 20, df["tenure_year"].max()]
    tenure_labels = ['New', 'Intermediate', 'Long Term', 'Veteran']
    df['tenure_category'] = pd.cut(df['tenure_year'], bins=tenure_bins, labels=tenure_labels, include_lowest=True)

    return df