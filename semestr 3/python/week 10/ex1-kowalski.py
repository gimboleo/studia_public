'''
SOURCES

avg_temps.csv is a file provided by Maciej Witkowski on Teams modified a little bit for consistency
covid_data.csv is a file taken from https://www.domo.com/covid19/data-explorer/all/ (Country Summary-Data Grid for Poland)

Sorry for not implementing the data retrieval but it wasn't possible in both cases
(domo.com seems to generate the csv files somewhat dynamically and I wasn't able to recreate the appropriate post request)
I provided both csv files along with this file on SKOS
'''


import pandas as pd
import matplotlib.pyplot as plt


#'Wave' period timestamps
t1 = '2020-10-23'
t2 = '2020-11-23'

#'No Wave' period timestamps
t3 = '2020-05-23'
t4 = '2020-07-23'


covid = pd.read_csv('covid_data.csv', usecols = ['Date', 'New Cases']) #Only taking the columns that are needed for the task
temps = pd.read_csv('avg_temps.csv')
total = covid.merge(temps, on = 'Date') #Merging both DataFrames on the 'Date' column
total['Date'] = pd.to_datetime(total['Date']) #Converting dates into Python's datetime objects

#I decided to plot the data on weekly averages to make the graph less 'jumpy'
#To calculate additional 2 columns containing these weekly averages I use the moving average
#DataFrame.rolling provides a rolling window calculations of given size that we can call mean() on
#In conclusion, for each given date we'll take 7 next values (including the current one) and save them under the given date in the new column
#So in reality, for a given date we'll be using an average value from the whole next week
#It would be better if a given date would be the last one (so we would be considering last 7 days)
#To make it happen, we shift the results backwards accordingly
total['Average Cases'] = total['New Cases'].rolling(window = 7).mean().shift(-6)
total['Average Temperature'] = total['Temperature'].rolling(window = 7).mean().shift(-6)


#Only considering data located between the given timestamps
intvs = (total.loc[(total['Date'] >= t1) & (total['Date'] <= t2)], total.loc[(total['Date'] >= t3) & (total['Date'] <= t4)])


#Creating a separate supblot for every interval
#These subplots will be aligned vertically
fig, axs = plt.subplots(len(intvs))
labels = ('"Wave" period', '"No wave" period')
axxs = []


#I also plotted actual data for each day, not just the averages
#I commented them out, because I thought they make the graph look a little cluttered (but it's still a nice addition)
#They are located in the lines 62 and 71, feel free to uncomment them
for i in range(len(intvs)):
    color = 'tab:red'
    axs[i].set_title(labels[i])
    axs[i].set_xlabel('Date')
    axs[i].set_ylabel('New cases (week average)', color = color)
    axs[i].plot(intvs[i]['Date'], intvs[i]['Average Cases'], color = color)
    #axs[i].scatter(intvs[i]['Date'], intvs[i]['New Cases'], 8, color, 'x')
    axs[i].tick_params(axis = 'y', labelcolor = color)

    axxs.append(axs[i].twinx())  #Create a second Axes that shares the same x-axis with the first one
    #It will be plotted on the same subplot as well

    color = 'tab:blue'
    axxs[i].set_ylabel('Temperature (week average in $^\circ$C)', color = color)  #We already handled the xlabel
    axxs[i].plot(intvs[i]['Date'], intvs[i]['Average Temperature'], color = color)
    #axxs[i].scatter(intvs[i]['Date'], intvs[i]['Temperature'], 8, color)
    axxs[i].tick_params(axis = 'y', labelcolor = color)


fig.tight_layout()  #Without this line the ylabel is slightly clipped
plt.show()


'''
The results seem to confirm the claim made in the task, although less visibly in the 'No wave' phase
I think the fluctuations are more chatoic when overall long-term infection rate is low
'''