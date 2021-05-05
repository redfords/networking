import pandas as pd

csv_path = 'file1.csv'
df = pd.read_csv(csv_path) #df is short for data frame
df.head() #examine the first five rows

xlsx_path = 'file1.xlsx'
df = pd.read_excel(xlsx_path)
df.head()

""" A data frame is comprised rows and colums. We can create a data frame out of a dictionary."""

songs = {'Album':['Thriller', 'Back in Black', 'The Dark Side of the Moon', 'The Bodyguard',
'Bat Out of Hell'],
'Released':[1982, 1980, 1973, 1992, 1977],
'Length':['00:42:19', '00:42:11', '00:42:49', '00:57:44', '00:46:33']}

songs_frame = pd.DataFrame(songs)

x = df[['Length']] #create a new df of one column

df['Released'].unique() #select unique values
df['Released']>=1980 #returns a column of true or false
df1 = df[df['Released']>=1980] #return all rows

df1.to_csv('new_songs.csv')
