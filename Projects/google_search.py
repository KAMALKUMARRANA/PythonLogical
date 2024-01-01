from googlesearch import search
query=input("Enter your quary: ")
for url in search(query):
    print(url)