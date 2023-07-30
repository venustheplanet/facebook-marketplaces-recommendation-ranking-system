import pandas as pd
# Remove all null values in any column
# Convert the prices into a numerical format, remove pound sign, and the comma 

def get_data_from_csv(csv_file):
    data = pd.read_csv(csv_file)
    # print(data)
    # print(data.info())
    # print(data.head())
    return data

def remove_null_val(df):
    df.dropna(inplace=True)
    return df

def convert_price_to_num(df):
    df['price'] = df['price'].str.replace('£', '').str.replace(',','')
    df['price'] = pd.to_numeric(df['price'])
    return df
    
if __name__ == "__main__":
    df = get_data_from_csv('Products.csv')
    df = remove_null_val(df)
    df = convert_price_to_num(df)
    print(df.info())
    print(df['price'])