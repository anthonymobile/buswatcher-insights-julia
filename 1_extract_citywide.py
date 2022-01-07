import pandas as pd
df = pd.read_csv('data/nyc_buses_with_passenger_counts_20210401_20210630.csv')
df.to_parquet(f'data/citywide_test_python.parquet')
