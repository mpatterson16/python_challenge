# python_challenge

This program finds IPs in a text file, finds GeoIP information about them, and can filter the results.

When running it locally from an IDE (I used Spyder), http://127.0.0.1:5000/ipaddresses displays all of the IP addresses,
http://127.0.0.1:5000/ipaddresses/<address> displays the GeoIP information about that particular address, and
http://127.0.0.1:5000/ipaddresses/<type>/<specific> displays all IP addresses that meet a certain criteria, where 'type'
can be city, country, or timezone, and 'specific' is the particular city, country, or timezone you are looking for.

ipproject.py is the main application that should be run. parseips.py contains a function to find all the IP addresses and
geoiplookups.py finds GeoIP information about those IPs and stores it.

Due to the time restraints on the API at http://ip-api.com/json/ the program takes 50 minutes to gather all the GeoIP
information. RDAP is not implemented because with the time restrictions at https://about.rdap.org/ it would take hours to
gather the information for all 5000 IP addresses.