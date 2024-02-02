#!/usr/bin/env python3

###
# https://api.github.com/meta
# `pip install httpx[http2]` at first
###


import json
from ipaddress import ip_network

import httpx

url = 'https://api.github.com/meta'
# https://www.whatismybrowser.com/guides/the-latest-user-agent/chrome
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36'}
with httpx.Client(headers=headers, http2=True) as client:
    res = client.get(url)
    ips = res.json()

    ipv4_set = set()
    ipv6_set = set()
    
    hooks_iplist = ips.get('hooks', [])
    web_iplist = ips.get('web', [])
    api_iplist = ips.get('api', [])
    git_iplist = ips.get('git', [])
    github_enterprise_importer_iplist = ips.get('github_enterprise_importer', [])
    packages_iplist = ips.get('packages', [])
    pages_iplist = ips.get('pages', [])
    importer_iplist = ips.get('importer', [])
    actions_iplist = ips.get('actions', [])
    dependabot_iplist = ips.get('dependabot', [])
    
    for eles in [hooks_iplist, web_iplist, api_iplist, git_iplist,
              github_enterprise_importer_iplist, packages_iplist,
              pages_iplist, importer_iplist, actions_iplist,
              dependabot_iplist]:
        for e in eles:
            if ':' in e:
                ipv6_set.add(e)
            else:
                ipv4_set.add(e)
    
    sorted_ipv4_arr = sorted(list(ipv4_set), key=lambda x: ip_network(x))
    sorted_ipv6_arr = sorted(list(ipv6_set), key=lambda x: ip_network(x))

    rule_set = {
        'version': 1,
        'rules': [
            {
                'ip_cidr': sorted_ipv4_arr + sorted_ipv6_arr
            }
        ]
    }

    rule_set_json = json.dumps(rule_set, indent=2)
    with open('geoip-github.json', 'w') as outfile:
        outfile.write(rule_set_json)
    print('write geoip-github.json')
