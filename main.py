import urllib.request

link = "https://en.wikipedia.org/wiki/Special:Random"
file = urllib.request.urlopen(link)
myFile = str(file.read())
print(myFile)

linkStartLocation = myFile.find('<a href="')
print(linkStartLocation)
linkEndLocation = myFile.find('"', linkStartLocation + 9)
print(linkEndLocation)
print(myFile[linkStartLocation:linkEndLocation + 1])

foundLink = myFile[linkStartLocation + 9:linkEndLocation]
src = "https://en.wikipedia.org"
print(src + foundLink)
