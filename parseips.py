# -*- coding: utf-8 -*-
"""
Created on Sun Nov 11 21:00:26 2018

@author: Maegan Patterson

This module contains a function to find all the IP addresses in a text file and
return them as a list.
"""

import re

def parse_ip_addresses(ips):
    ip_list = []
    text = ips.readlines()
    regex = '([0-9]*\.[0-9]*\.[0-9]*\.[0-9]*)'
    for line in text:
        r = re.search(regex, line)
        while r:
            address = r.group()
            ip_list.append(address)
            line = line.replace(address, ' ')
            r = re.search(regex, line)
    return ip_list