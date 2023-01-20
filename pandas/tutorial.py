import numpy as np
import pandas as pd

dict1 = {
    "names":['Zeeshan','John','Jane'],
    "marks":[95,75,72],
    "city":['Srinagar',"Jammu","New Delhi"],
}

df = pd.DataFrame(dict1)


# df.describe()
# df.to_csv('Details.csv',index=False)
df.to_json('dict.json')

# df = pd.read_csv("Details.csv")

# data = df['marks']

data = pd.DataFrame(np.random.rand(200,5),index=np.arange(200))

# transpose a matrix
# data = data.T

# data = data.sort_index(axis=0, ascending = False)

# data = data.dtypes


data.columns = list('ABCDE')
# data.loc[0,0] = 232323
# data = data.drop(0,axis=1)

# print(data.loc[[1,2],['A','B']])
# print(data.loc[:,['A','B']])

# newData = data.loc[(data['A'] < .3) & (data['C'] > 0.1)]

# data.to_json('File.json')

print(data.head())
# print(newData.head())