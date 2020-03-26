from googlesearch import search
import os, ssl
if (not os.environ.get('PYTHONHTTPSVERIFY', '') and getattr(ssl, '_create_unverified_context', None)):
    ssl._create_default_https_context = ssl._create_unverified_context


print("\n\n     ##     ## ########          ##     ##        ###        ##    ## ")
print("     ###   ### ##     ##         ##     ##       ## ##       ##   ##  ")
print("     #### #### ##     ##         ##     ##      ##   ##      ##  ##   ")
print("     ## ### ## ########  ####### #########     ##     ##     #####    ")
print("     ##     ## ##   ##           ##     ##     #########     ##  ##   ")
print("     ##     ## ##    ##          ##     ## ### ##     ## ### ##   ##  ")
print("     ##     ## ##     ##         ##     ## ### ##     ## ### ##    ## ")
print("                                                                      ")
print("\n                             Hassan Cypher                            ")
print("                           PAKISTAN ZINDABAD\n                          ")
print("                          Google URL Extractor                          ")                     
print("                                                                      ")

search_item = input("Enter Dork : ")
pages = int(input("Links : "))

found = []

while (True):
    for j in search(search_item,tld="com", num=pages, stop=pages, pause=2):
        if j not in found:
            found.append(j+'\n')
        print(j)
    ch = input("X for exit and R for repeat\n").lower()
    if ch == 'x':
        break
print("\nDo you also want to write this to a file? Type 'yes' or 'no'")
con = input()
if con == "yes":
    with open('search.txt', 'w') as w:
        w.writelines(found)
        print("\nProcess Done, please check search.txt file.\n")
else:
    print("\nProcess Done\n")
print("\nMade By CYPHER")
print("Thank You")




