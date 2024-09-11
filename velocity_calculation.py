import pandas as pd


extension = '_0004PR'

# Load the data
data = pd.read_csv(f'tracking_data{extension}.csv')


# Initialize the velocity columns
data['XVel'] = 0
data['YVel'] = 0

for i in range (5, len(data['TimeStamp']) - 5):
#for i in range(1,20):
    if data.iloc[i+5]['PersonId'] == data.iloc[i-5]['PersonId']:
        data.at[i, 'XVel'] = round((data.iloc[i + 5]['x-Position'] - data.iloc[i - 5]['x-Position']) / 0.4, 2)
        data.at[i, 'YVel'] = round((data.iloc[i + 5]['y-Position'] - data.iloc[i - 5]['y-Position']) / 0.4, 2)



# Save the DataFrame as a CSV file

data.to_csv(f"tracking_data_with_velocity{extension}.csv", index=False)








