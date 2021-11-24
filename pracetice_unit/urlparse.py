import urllib.parse

result = urllib.parse.urlparse("https://www.python.org:80/guido/python.html;philosophy?overall=3#n10")
print(type(result), result, sep='\n')