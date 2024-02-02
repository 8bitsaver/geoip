#!/usr/bin/env python3

###
# https://developer.fastly.com/reference/api/utils/public-ip-list/
# `pip install httpx[http2]` at first
###


import json
# from ipaddress import ip_network

import httpx

url = 'https://api.fastly.com/public-ip-list'
# https://www.whatismybrowser.com/guides/the-latest-user-agent/chrome
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36'}
with httpx.Client(headers=headers, http2=True) as client:
    res = client.get(url)
    ips = res.json()
    
    ipv4_arr = ips['addresses']
    ipv6_arr = ips['ipv6_addresses']

    # sorted_ipv4_arr = sorted(ipv4_arr, key=lambda x: ip_network(x))
    # sorted_ipv6_arr = sorted(ipv6_arr, key=lambda x: ip_network(x))

    rule_set = {
        'version': 1,
        'rules': [
            {
                'ip_cidr': ipv4_arr + ipv6_arr
            }
        ]
    }

    rule_set_json = json.dumps(rule_set, indent=2)
    with open('geoip-fastly.json', 'w') as outfile:
        outfile.write(rule_set_json)
    print('write geoip-fastly.json')
