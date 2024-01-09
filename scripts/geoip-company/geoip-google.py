#!/usr/bin/env python3

###
# https://support.google.com/a/answer/10026322?hl=en
# `pip install httpx[http2]` at first
###


import json
from ipaddress import ip_network

import httpx

url = 'https://www.gstatic.com/ipranges/goog.json'
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'}
with httpx.Client(headers=headers, http2=True) as client:
    res = client.get(url)
    ips = res.json()['prefixes']

    ipv4_arr = []
    ipv6_arr = []
    for e in ips:
        if 'ipv4Prefix' in e:
            ipv4_arr.append(e['ipv4Prefix'])
        if 'ipv6Prefix' in e:
            ipv6_arr.append(e['ipv6Prefix'])

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
    with open('geoip-google.json', 'w') as outfile:
        outfile.write(rule_set_json)
    print('write geoip-google.json')
