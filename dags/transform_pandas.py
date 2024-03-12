import pandas as pd
import json

def transform(ti):
    """ Transforms the dataset 
    1) API data is saved as a JSON file. 
    2) This function reads it and converts it to a pandas dataframe.
    3) Then the pandas df is saved as a CSV file.
    """
    # read JSON
    json_path = ti.xcom_pull(task_ids='coinmarketcap_fetch_data')
    with open(json_path) as f:
        data = json.load(f)
    
    # convert it to pandas dataframe
    df = pd.DataFrame(data["data"])

    #df_usd = pd.DataFrame(id = df["id"], pd.)# take out nested dict
    #print(f"Total number of rows {len(data)}")
    #print(df)

    # write to CSV
    csv_path = f'{json_path[:-5]}.csv'
    df.to_csv(csv_path, index=False)

    return csv_path