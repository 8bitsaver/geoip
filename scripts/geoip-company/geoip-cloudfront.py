#!/usr/bin/env python3

###
# https://docs.aws.amazon.com/general/latest/gr/aws-ip-ranges.html
# https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/LocationsOfEdgeServers.html
# `pip install httpx[http2]` at first
# Difference between global and regional IP addresses in AWS CloudFront?
# https://stackoverflow.com/questions/69697280/difference-between-global-and-regional-ip-addresses-in-aws-cloudfront
###


import json
from ipaddress import ip_network

import httpx

url = 'https://d7uri8nf7uskq.cloudfront.net/tools/list-cloudfront-ips'
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'}
with httpx.Client(headers=headers, http2=True) as client:
    res = client.get(url)
    ips = res.json()
    arr = ips['CLOUDFRONT_GLOBAL_IP_LIST'] + ips['CLOUDFRONT_REGIONAL_EDGE_IP_LIST']
    ipv4_arr = []
    ipv6_arr = []

    for e in arr:
        if ':' in e:
            ipv6_arr.append(e)
        else:
            ipv4_arr.append(e)

    sorted_ipv4_arr = sorted(ipv4_arr, key=lambda x: ip_network(x))
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
    with open('geoip-cloudfront.json', 'w') as outfile:
        outfile.write(rule_set_json)
    print('write geoip-cloudfront.json')
