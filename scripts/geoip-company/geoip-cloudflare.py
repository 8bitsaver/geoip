#!/usr/bin/env python3

###
# https://www.cloudflare.com/ips/
# `pip install httpx[http2]` at first
###


import json
from ipaddress import ip_network

import httpx

ipv4_url = 'https://www.cloudflare.com/ips-v4'
ipv6_url = 'https://www.cloudflare.com/ips-v6'
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'}
with httpx.Client(headers=headers, http2=True) as client:
    ipv4_res = client.get(ipv4_url)
    ipv4_arr = ipv4_res.content.decode().split()
    sorted_ipv4_arr = sorted(ipv4_arr, key=lambda x: ip_network(x))

    ipv6_res = client.get(ipv6_url)
    ipv6_arr = ipv6_res.content.decode().split()
    sorted_ipv6_arr = sorted(ipv6_arr, key=lambda x: ip_network(x))

    rule_set = {
        'version': 1,
        'rules': [
            {
                'ip_cidr': sorted_ipv4_arr + sorted_ipv6_arr
            }
        ]
    }

    rule_set_json = json.dumps(rule_set, indent=2)
    with open('geoip-cloudflare.json', 'w') as outfile:
        outfile.write(rule_set_json)
    print('write geoip-cloudflare.json')
