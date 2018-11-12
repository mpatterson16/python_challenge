# -*- coding: utf-8 -*-
"""
Created on Fri Nov  9 21:37:58 2018

@author: Maegan Patterson

This program finds IP addresses in a text file, finds GeoIP information about
them, and allows the user to filter the information by country, city, or 
timezone.
"""

import json
import flask
import parseips
import geoiplookups

#text file containing ip addresses
ips = open('list_of_ips.txt', 'r')

#find ip addresses in text file
ip_list = parseips.parse_ip_addresses(ips)
#convert into dict of addresses and info
ip_dict = geoiplookups.geo_ip(ip_list)

application = flask.Flask(__name__)

#display all ip addresses and info
@application.route('/ipaddresses')
def display_all_addresses():
    return json.dumps(ip_dict)

#display info about specific ip address
@application.route('/ipaddresses/<address>')
def display_address(address):
    return json.dumps(ip_dict[address])

#display ip addresses that meet a certain criteria
@application.route('/ipaddresses/<query_type>/<query>')
def display_query(query_type, query):
    ip_list = []
    for key, val in ip_dict.items():
        if query_type == 'city' or query_type == 'country' or query_type == 'timezone':
            if query_type in val:
                if query.lower() in val[query_type].lower():
                    ip_list.append(key)
    return json.dumps(ip_list)

if __name__ == '__main__':
    application.run()
