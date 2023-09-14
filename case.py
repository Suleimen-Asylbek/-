import pandas as pd
import matplotlib.pyplot as plt
df = pd.read_csv('Space_Corrected.csv')
df.info()
kazakhstan_loc = 0
kazakhstan_miss = 0
usa_loc = 0
usa_miss = 0
def status_apply(row):
    global kazakhstan_loc, kazakhstan_miss, usa_loc, usa_miss
    if row['Status Mission'].find('Success') != -1:
        kazakhstan_miss += 1
    if row['Location'].find('Kazakhstan') != -1:
        kazakhstan_loc += 1
    if row['Location'].find('USA') != -1:
        usa_loc += 1
    if row['Status Mission'].find('Success') != -1:
        usa_miss += 1

df.apply(status_apply, axis = 1)
print('В Казахстане больше успешных миссий чем у Америки')
print('Успешных миссий Казахстана:', kazakhstan_miss-kazakhstan_loc)
print('Успешных миссий Америки:',usa_miss-usa_loc)
d = pd.Series(data = [(kazakhstan_miss-kazakhstan_loc),(usa_miss-usa_loc)],index = ['Kazakhstan','USA'])
d.plot(kind = 'barh', figsize = (8, 5))
plt.show()

