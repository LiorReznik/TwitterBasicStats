# -*- coding: utf-8 -*-
"""
@author: Lior Reznik
"""
from tweepy.streaming import StreamListener

class SListener(StreamListener):
    
    
    def __init__(self,api):
        self.api=api
        self.__tweets=[]
    
    
    def on_data(self, data):
       """function that handels the data that we are getting from the stream"""
       self.__tweets.append(data)#sppending the data tweet into the list of tweets
       return True
   
    
    @property 
    def return_data(self):
        """function to return the list of tweets"""
        return  self.__tweets

