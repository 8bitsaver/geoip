## geoip

Overlap the Chinese IP list published by  `china_ip_list`, `chunzhen CN` and `APNIC CN` into the official `MaxMind` GeoLite2 database.

It's suitable for using in network offloading tools and compatible with MaxMind DB client! It is more friendly to Chinese IP matching and distribution.

Automatically pull new MaxMind, china_ip_list, Chunzhen CN and APNIC database every day, and release a new Release version.

### Download Link

- Both Release and Daily switch to build with the golang version of the mmdb writer
- The full version is based on loading the official `GeoLite2-Country.mmdb`, overwriting `china_ip_list`, `chunzhen CN` and `APNIC CN`, not built from scratch

| File | release (Daily) | CDN (Daily) |
| ------ | ------ | ------ |
| Country.mmdb | [link](https://raw.githubusercontent.com/8bitsaver/geoip/release/Country.mmdb) | [link](https://cdn.jsdelivr.net/gh/8bitsaver/geoip@release/Country.mmdb) |
| geoip.db | [link](https://raw.githubusercontent.com/8bitsaver/geoip/release/geoip.db) | [link](https://cdn.jsdelivr.net/gh/8bitsaver/geoip@release/geoip.db) |

### Introduction

Is not very friendly to Chinese IP matching. So there are many problems in actual using the `GeoLite2-Country` of [MaxMind](https://www.maxmind.com/en/home) in network tapping tools (such as Clash).

This project, on the basis of the MaxMind database, added `china_ip_list`, `chunzhen CN` and `APNIC CN`, making it more friendly to Chinese IP matching.

Because the mmdb is built, the latter overrides the former, and the order of inserting the ip list is as follows:

1. [APNIC CN](https://ftp.apnic.net/stats/apnic/delegated-apnic-latest)
2. [chunzhen CN](https://raw.githubusercontent .com/metowolf/iplist/master/data/country/CN.txt)
3. [china_ip_list](https://raw.githubusercontent.com/17mon/china_ip_list/master/china_ip_list.txt)

### How to use

Download the generated `Country.mmdb` from [Release](https://github.com/8bitsaver/geoip/releases).

The usage is the same as the official API of MaxMind, please refer to [Guide Document](https://maxmind.github.io/MaxMind-DB/).

### Using in OpenClash

Download `Country.mmdb`, then replace `/etc/openclash/Country.mmdb`, and finally restart clash.

You can edit the `update url` in update script and enable auto update.

### MaxMind GeoIP Format

The official said little about the content of their own database.
It's the format that I found out  with debugging the source code. And then generated the database.

Examples of all fields are listed below for reference.

header

``` json
{
    "database_type": "GeoLite2-Country",
    "binary_format_major_version": 2,
    "build_epoch": 1589304057,
    "ip_version": 6,
    "languages": [
        "de",
        "en",
        "es",
        "fr",
        "ja",
        "pt-BR",
        "ru",
        "zh-CN"
    ],
    "description": {
        "en": "GeoLite2 Country database"
    },
    "record_size": 24,
    "node_count": 616946,
    "binary_format_minor_version": 0
}
```

network-field

``` json
{
    "continent": {
        "code": "AS",
        "names": {
            "de": "Asien",
            "ru": "Азия",
            "pt-BR": "Ásia",
            "ja": "アジア",
            "en": "Asia",
            "fr": "Asie",
            "zh-CN": "亚洲",
            "es": "Asia"
        },
        "geoname_id": 6255147
    },
    "country": {
        "names": {
            "de": "China",
            "ru": "Китай",
            "pt-BR": "China",
            "ja": "中国",
            "en": "China",
            "fr": "Chine",
            "zh-CN": "中国",
            "es": "China"
        },
        "iso_code": "CN",
        "geoname_id": 1814991,
        "is_in_european_union": false,
    },
    "registered_country": {
        "names": {
            "de": "China",
            "ru": "Китай",
            "pt-BR": "China",
            "ja": "中国",
            "en": "China",
            "fr": "Chine",
            "zh-CN": "中国",
            "es": "China"
        },
        "iso_code": "CN",
        "geoname_id": 1814991
    },
    "represented_country": {
        "names": {
            "de": "China",
            "ru": "Китай",
            "pt-BR": "China",
            "ja": "中国",
            "en": "China",
            "fr": "Chine",
            "zh-CN": "中国",
            "es": "China"
        },
        "iso_code": "CN",
        "geoname_id": 1814991
    },
    "traits": {
        "is_anonymous_proxy": true,
        "is_satellite_provider": true
    }
}
```

### References

- [Example of using mmdb writer for Golang version](https://github.com/JMVoid/ipip2mmdb)
- https://github.com/alecthw/mmdb_china_ip_list

