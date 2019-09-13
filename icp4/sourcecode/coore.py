import pandas as pd
df= pd.read_csv('train.csv')
df['Sex']=df['Sex'].replace( {'female': 1, 'male': 0} )
print(df['Survived'].corr(df['Sex']))