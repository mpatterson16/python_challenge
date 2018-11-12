# -*- coding: utf-8 -*-
"""
Created on Sun Nov 11 21:10:01 2018

@author: Maegan Patterson

This module contains a function to find GeoIP information about a list of IP
addresses.
"""

import requests
import time
import json

def geo_ip(ip_list):
    ip_dict = {}
    for ip in ip_list:
        geo = requests.get('http://ip-api.com/json/' + ip)
        #sleep necessary because too many in a time frame gets your IP
        #address banned
        time.sleep(.4)
        ip_dict[ip] = json.loads(geo.text)
    return ip_dict