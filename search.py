from googlesearch import search

url = input("Search google - ")

for dat in search(url):
    print(dat)
    