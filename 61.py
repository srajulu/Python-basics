import pandas as pd
df=pd.read_csv("E:\matches.csv")

#list of cities where match conducted using unique()
print("Unique cities where matches were conducted")
print(df.city.unique())

#list of teams played the match using unique()
print("List of all teams played for T20")
print(df.team1.unique())

#total number of matches in 2010,2015,2017
a1=(df.season == 2015).sum()
a2=(df.season == 2010).sum()
a3=(df.season == 2017).sum()
print("Total matches in 2010,2015 and 2017: ",a1+a2+a3)

#matches held in bangalore
b=(df.city == 'Bangalore').sum()
print("Total matches in Bangalore: ",b)

#Count of match in APRIL-2017
m=df[ (df['date'].str.endswith('-04-17') )]
print(m['date'].count())

#number of matches tie
c=(df.result == 'tie').sum()
print("Number of times the result was TIE: ",c)

#number of matches in which SK Raina was player of match
print("Number of times SK Raina was player of the match: ",(df.player_of_match == 'SK Raina').sum())

#Count of Toss won by each team
print(df['toss_winner'].value_counts() )

#number of matches in which Yuvi was player of match
print("Number of times Yuvi was player of the match: ",(df.player_of_match == 'Yuvraj Singh').sum())

#team that won maximum matches in 2014
m=df[ (df['season']==2014 )]
print(m['winner'].value_counts().index[0] )
print(m['winner'].value_counts().values[0] )
