# -*- coding: utf-8 -*-
"""
@author: Lior Reznik
"""
import Tweet_Stream
from tweepy import OAuthHandler
from tweepy import API
from tweepy import Stream
import time
from Hashtags_Stats import hashtags_stats
from urllib3.exceptions import ProtocolError

class controller:
    
    
    def set_credentials(self,consumer_key,consumer_secret,access_key,access_secret):
         """
            function to set the api credentials
            the function builds a dict of the keys that neccesry to connect to the api and setup the api
            
            params: 
                consumer_key
                consumer_secret
                access_key
                access_secret
         
         """
         self.__keys={'consumer_key':consumer_key,'consumer_secret':consumer_secret,'access_key':access_key,'access_secret':access_secret}
         self._setup_api
         
         
    @property    
    def _setup_api(self):
        """
        function to setup the api
        the function setups the api by making authentication with the given consumer and access keys, afterwrds instantiates the slistenr object(the stream)
        
        """
        # Consumer key authentication
        self.__auth = OAuthHandler(consumer_key=self.__keys['consumer_key'], consumer_secret=self.__keys['consumer_secret'])
        # Access key authentication
        self.__auth.set_access_token(key=self.__keys['access_key'], secret=self.__keys['access_secret'])
        # Set up the API with the authentication handler
        api = API(auth_handler=self.__auth)
        # Instantiation of  the SListener object 
        self.__listen = Tweet_Stream.SListener(api=api)
  
    
    def start_stream(self,timer):
         """
         function that starts the input stream for a given amount of time
           
           params:
               timer-the desired time to get the tweets
         """
         #Instantiation of the Stream object
         stream = Stream(auth=self.__auth, listener=self.__listen)
         #starting the stream in another thread
         stream.sample(async=True)
         #timer
         time.sleep(timer) #sending the current thread to sleep for a given amount of time
         stream.disconnect() #disconnecting the stream 

    @property    
    def to_pandas(self):
        """funtcion to phrase the json tweets into dataframe"""
        self.__statistic_maker=hashtags_stats(tweets=self.__listen.return_data)#sending the tweets to the hastags_stats ctor
    
    
    @property
    def stats(self):
        """function to make statistics on the tweets dataframe"""
        print "tweets per hashtag/freq of hashtags"
        print
        self.__statistic_maker.hashtags_freq#printing the freq of the hastags in the dataset //tweets per hashtag
        print
        print "retweets per hashtag"
        print
        self.__statistic_maker.retweets_per_hashtags