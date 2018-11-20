# -*- coding: utf-8 -*-
"""
@author: Lior Reznik
"""

import Controller

#the code will be excecuted only if the file is not imported/if the file is the main module
if __name__ == "__main__":
    
    cont=Controller.controller()#building controller instance
    cont.set_credentials(consumer_key='ENTER YOUR API KEY',consumer_secret="ENTER YOUR API SECRET",access_key="ENTER YOUR ACCESS TOKEN",access_secret="ENTER YOUR ACCESS TOKEN SECRET")#seting the credentials
    cont.start_stream(timer="SET TIME")#starting the stream for a given amount of time
    cont.to_pandas#converting the tweets into pandas dataframe
    cont.stats#doing some statistics on the hashtags