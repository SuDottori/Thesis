import snscrape.modules.twitter as sntwitter
import pandas as pd
from tqdm.auto import tqdm
from time import sleep
from datetime import date
from datetime import timedelta
import os
import glob

def CheckLeap(Year):  
    if((Year % 400 == 0) or  
     (Year % 100 != 0) and  
     (Year % 4 == 0)):   
        return 366
    else:  
        return 365
    
def GrabTweets(month,year,num_tweets_per_day,query):

    # Calculate Total Tweets Per Month to Collect
    if month in [1, 3, 5, 7, 8, 10, 12]:
        days_in_month = 31
        total_tweets = days_in_month * num_tweets_per_day

    elif month in [4, 6, 9, 11]:
        days_in_month = 30
        total_tweets = days_in_month * num_tweets_per_day

    elif month == 2:
        if CheckLeap(year) == 365:
            days_in_month = 28
            total_tweets = days_in_month * num_tweets_per_day
        else:
            days_in_month = 29
            total_tweets = days_in_month * num_tweets_per_day

    # Creating List to Append Tweet Data to
    tweets_list = []
    pbar = tqdm(total=total_tweets)

    # Create Date Object
    until = date(year, month, 2).isoformat()
    last_day = (date.fromisoformat(until)+timedelta(days=days_in_month)).isoformat()

    # Counter
    counter = 0

    # Using TwitterSearchScraper to Scrape Data on Tesla Model 3 in X Month in 2021 & Append Tweets to List
    while counter != total_tweets:
        for j in range(1):
            for i,tweet in enumerate(sntwitter.TwitterSearchScraper('{} until:{} lang:en -filter:links -filter:replies'.format(query,until)).get_items()):
                if i >= num_tweets_per_day:
                    until = (date.fromisoformat(until)+timedelta(days=1)).isoformat()
                    break
                tweets_list.append([tweet.id, tweet.date, tweet.user.username, tweet.content])
                sleep(0.01)
                counter += 1
                pbar.update(1)

    pbar.close()

    # Creating a DataFrame from the Tweets List Above
    DF = pd.DataFrame(tweets_list, columns=['Id','Date', 'User', 'Text'])
    
    # Change Directory
    os.chdir('DIRECTORY')

    # Write to CSV
    DF.to_csv('{}-Tweets-{}-{}-{}.csv'.format(query,month,year,total_tweets), encoding='utf-8', index=False)
    
    # Print Done
    print(pbar,"\n")
    print("Done!")

query = "('Quarantine' OR 'Covid' OR 'Covid19' OR 'Surgical Mask' OR 'Coronavirus' OR 'Virus' OR 'Pandemic' OR 'Vaccine' OR 'Face Mask')"

num_tweets_per_day = 1500
for i in range(1,13):
    GrabTweets(i,2022,num_tweets_per_day,query) 
for i in range(1,13):
    GrabTweets(i,2021,num_tweets_per_day,query)


files = os.path.join("DIRECTORY", "*.csv")
files = glob.glob(files)
df1 = pd.concat(map(pd.read_csv, files), ignore_index=True)
df1= pd.DataFrame(df1).T
df1.to_csv('Dataset_covid', index = False, encoding='utf-8')

os.chdir('DIRECTORY')
csv_files = os.path.join("DIRECTORY", "*.csv")
csv_files = glob.glob(csv_files)
 
df_csv_append = pd.DataFrame()
 
import pandas as pd
 
df_csv_concat = pd.concat([pd.read_csv(file) for file in csv_files ], ignore_index=True)

df_csv_concat.to_csv('Dataset.csv', index = False, encoding='utf-8')
