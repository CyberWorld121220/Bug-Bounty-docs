import urllib.parse as urlparse
url = "http://www.example.com?type=a"
trigger = ["viraj","tanisha","divya"]

parsed = urlparse.urlparse(url)
querys = parsed.query.split("&")
result = []
for pairs in trigger:
    new_query = "&".join([ "{}{}".format(query, pairs) for query in querys])
    parsed = parsed._replace(query=new_query)
    result.append(urlparse.urlunparse(parsed))
print(result[0])
print(result[1])
print(result[2])
