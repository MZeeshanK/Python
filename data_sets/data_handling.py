import pandas as pd

data_set = pd.read_csv('employees.csv')


def fillInNull(series, data):
  data_set[series] = data_set[series].fillna(data)
  

fillInNull('First Name','Unknown')
fillInNull('Gender','Male')
fillInNull('Team','Unknown')
fillInNull('Senior Management',False)

defaultSalary = data_set['Salary'].describe()['50%']
fillInNull('Salary',defaultSalary)

data_set['Start Date'] = pd.to_datetime(data_set['Start Date'])

time = data_set['Last Login Time']

data = data_set[['Gender',"Team"]]

gender = pd.get_dummies(data['Gender'])

gender = pd.get_dummies(data['Gender'],drop_first=True)

print(gender)
# print(data_set)







  



