import pandas as pd
df = pd.read_csv("data/pandas/airbnb.csv")
df.head()

print ("Modulo 4 \nCaso1:")
a=df[(df['reviews']>10) & (df['overall_satisfaction']>4)]
b=a.sort_values('overall_satisfaction',ascending=False)
print (b.head(3))
print ("Modulo 4 \nCaso2:")
a=df[(df.room_id==97503)]
print ("Casa de Roberto")
print (a)
b=df[(df.room_id==90387)]
print ("Casa de clara\n")
print(b)
print ("Modulo 4 \nCaso3:")
a=df[(df.room_type=="Shared room")&(df.price<=50)]
df = a.sort_values(["overall_satisfaction","price"], ascending = (False, True))
print (df.head(10))