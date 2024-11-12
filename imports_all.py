import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import datetime
from datetime import timedelta
import time
import pickle

print('ALL DEPENDECIES IMPORTS DONE !!')

from breeze_cred import cred_dct

api_key_ = cred_dct['breeze']['api_key'] 
api_secret_ = cred_dct['breeze']['api_secret']   

from breeze_connect import BreezeConnect
breeze = BreezeConnect(api_key=api_key_)

import urllib
print("https://api.icicidirect.com/apiuser/login?api_key="+urllib.parse.quote_plus(api_key_))

# Generate Session
breeze.generate_session(api_secret= 'api_secret',
                        session_token="45551397")   # AUTOMATE THIS 

print('BREEZE API CONNECTED !!')
