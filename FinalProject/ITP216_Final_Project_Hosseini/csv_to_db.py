import sqlite3 as sl
import pandas as pd

conn = sl.connect('insurance.db')
curs = conn.cursor()

curs.execute('DROP TABLE IF EXISTS insurance')
curs.execute('CREATE TABLE IF NOT EXISTS insurance (AGE INTEGER, STATE TEXT, TOBACCO TEXT, RATE REAL)')
conn.commit()

df = pd.read_csv('csv/Rate_PUF.csv', usecols=['Age', 'StateCode', 'Tobacco', 'IndividualRate'])
df = df[df['IndividualRate'].notnull()]
print('First couple df results:')
print(df.head(5))

df.to_sql(name='insurance', con=conn, if_exists='replace', index=False)
print('\nFirst 3 db results:')
query = 'SELECT * FROM insurance'
results = curs.execute(query).fetchmany(3)
for result in results:
    print(result)

