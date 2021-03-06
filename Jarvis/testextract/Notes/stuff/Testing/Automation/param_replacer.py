#!/usr/bin/python3
import argparse
import urllib.parse as urlparse
parser = argparse.ArgumentParser()
#parser.add_argument("-t","--target",help="Target name...")
parser.add_argument("-l","--path",help="Target File Path...")
args = parser.parse_args()
#target = args.target
path = args.path
def url_reflect_check(url):
    trigger = ["viraj","<viraj>",'<"viraj">']

    parsed = urlparse.urlparse(url)
    querys = parsed.query.split("&")
    #print(querys)
    manipulated_querys = list()
    for query in querys:
       print(query)
       if "=" in query:
          index = query.index('=')
          Q = query[0:index+1]
          manipulated_querys.append(Q)
       else:
          print("quey has no parameter")
    #print(manipulated_querys)
    result = []
    for pairs in trigger:
        new_query = "&".join([ "{}{}".format(query, pairs) for query in manipulated_querys])
        #print(querys)
        #print(pairs)
        #print(new_query)
        parsed = parsed._replace(query=new_query)
        result.append(urlparse.urlunparse(parsed))
    return result[0]
urls = list()
with open(path, "r") as f:
    lines = f.readlines()
for line in lines:
        if '=' in str(line):
           #print(line.strip("\n"))
           x = url_reflect_check(line.strip("\n"))
           urls.append(x)
        else:
           print("URL has no parameter")
urls = list(dict.fromkeys(urls))
#print(urls)
file = open(path[0:-4]+"_reflect.txt", "w")
for url in urls:
    file.write(url+"\n")
file.close()
