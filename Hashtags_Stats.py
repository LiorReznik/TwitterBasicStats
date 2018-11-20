# -*- coding: utf-8 -*-
"""
@author: Lior Reznik
"""
import json
import pandas as pd
class hashtags_stats:
    
    
    def __init__(self,tweets):
        self.__tweets=tweets
        self.__json_phrase
        self.__to_pandas
      

    @property
    def __json_phrase(self):
            """phrasing the json list into list of dics"""
            self.__hashtags=[]
            self.__tweets_list = []            
            # Iterateing through each tweet
            for tweet in self.__tweets:
                tweet_obj = json.loads(tweet)#making dict out of the tweet json object
                #flatting the hashtags  child for future easy access from the dataframe
                if 'entities' in tweet_obj.keys() and len(tweet_obj['entities']['hashtags'])>0:
                    tweet_obj['hashtags']=[]
                    for hashtag in tweet_obj['entities']['hashtags']:
                        tweet_obj['hashtags'].append(hashtag['text'])
                        self.__hashtags.append(hashtag['text'])
                #flatting the retweeted dict child for future easy access from the dataframe 
                if 'retweeted_status' in tweet_obj:
                    # Storeing the retweet text in 'retweeted_status-text'
                    tweet_obj['RT_text'] = tweet_obj['retweeted_status']['text']
                    # Storeing the retweeted count in 'Rt_count'
                    tweet_obj['RT_count']=tweet_obj['retweeted_status']['retweet_count']

                self.__tweets_list.append(tweet_obj)
            self.__tweets=self.__tweets_list

            
    @property        
    def __to_pandas(self):
         """Method to transform the tweets from dicts into dataframes"""
         self.__tweets = pd.DataFrame(self.__tweets_list,columns=['hashtags', 'retweeted','retweet_count','id','text','RT_count','RT_text'])#building the dataframe
         #seperating the attr hastags that contains list of hastags into new rows
         df_hashtags = self.__tweets.hashtags.apply(pd.Series).stack().rename('hashtags').reset_index()#seperating the hastags into rows,all the othe columns are copied 
         self.__tweets=pd.merge(df_hashtags,self.__tweets,left_on='level_0',right_index=True, suffixes=(['','_old']))[self.__tweets.columns]
         self.__tweets['hashtags']=self.__tweets['hashtags'].str.lower()#making all the hashtags low_case ,we do it as a prepresion to counting tweets per hashtag
         self.__tweets=self.__tweets.drop_duplicates(subset='id', keep="last")#removing the duplicated id rows so we dont count twice the same counter
         self.__tweets=self.__tweets.drop_duplicates(subset=['hashtags','RT_text'], keep='last')#removing the duplicated hastags and rt_text rows
        
    
    @property
    def hashtags_freq(self):
        """Function that finds the freq of the hashtags in the dataset"""
        print pd.Series.value_counts(self.__tweets['hashtags'])#printing the freq of hashtags  in descending  order
       
        
    @property
    def retweets_per_hashtags(self):
        """function that finds the amount of retweets for the hastags in the dataset"""
        print
        print
        print self.__tweets.groupby('hashtags')['RT_count'].sum().sort_values(ascending=False)#printing the retweets count per hashtag in descending  order
        

        
