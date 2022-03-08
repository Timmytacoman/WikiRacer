import urllib.request
import webbrowser
from threading import Thread

links = []

badExtensions = [".JPG", ".svg", ".jpg", ".png", ".ogg", ".webm", ".oga", "JPEG"]

boringSites = ["https", "/wiki/Wikipedia:", "/wiki/Help:", "/wiki/Special:", "/wiki/File:"]


def getLinks(start, ident, index=0):
    print(f"ID = {ident}")
    print(f"STARTING TO OPEN: {start} at index: {index}")
    # webbrowser.open(start, new=2)
    file = urllib.request.urlopen(start)
    myFile = str(file.read())
    # print(myFile)

    # base case occurs when no more links are found
    linkStartLocation = myFile.find('<a href="', index)
    if linkStartLocation == -1:
        print("No more links found")
        return

    # print(linkStartLocation)
    linkEndLocation = myFile.find('"', linkStartLocation + 9)
    # print(linkEndLocation)
    foundLink = myFile[linkStartLocation + 9:linkEndLocation]
    # print(foundLink)
    newLink = "https://en.wikipedia.org" + foundLink
    # print(newLink)

    isValidLink = True

    # check valid type
    for i in badExtensions:
        if newLink.endswith(i):
            # print(f"Not adding link: {newLink}")
            newLink = start
            # print(f"Changing newLink to: {newLink}")
            isValidLink = False
            break

    # check valid link (no hashtag movers or editors)
    if ('#' in newLink) or ('&' in newLink):
        # print(f"Not adding link: {newLink} because of # or &")
        newLink = start
        # print(f"Changing newLink to: {newLink} to not enter # or &")
        isValidLink = False

    # remove boring websites
    for i in boringSites:
        if i in newLink[3:]:
            # print(f"Not adding link: {newLink} because of boring {i}")
            newLink = start
            # print(f"Changing newLink to: {newLink} to not boring {i}")
            isValidLink = False

    # if valid link (not image and not a hastag mover or editor)
    if isValidLink:

        # avoid looping between two sites, we only do this if it is not an image
        if newLink in links:
            # print(f"Not adding previously visited link: {newLink}")
            newLink = start
            # print(f"Changing newLink to: {newLink} to avoid loop")
            # print(f"index={linkEndLocation}")

        else:
            linkEndLocation = 0

    if newLink not in links:
        links.append(newLink + "ID===" + str(ident))

    print(f"Num visited: {len(links)}")
    print(links)
    print("-=-=-=-=-=-=-=")

    links1 = []
    links2 = []
    for i in links:
        if i.endswith("ID===1"):
            links1.append(i[:-6])
        else:
            links2.append(i[:-6])

    print("links1: ")
    print(links1)

    print("links2: ")
    print(links2)

    for i in links1:
        if i in links2:
            print("MATCH!!!")
            exit()

    getLinks(newLink, ident, linkEndLocation)


# start = "https://en.wikipedia.org/wiki/Special:Random"
start = "https://en.wikipedia.org/wiki/Hartebeest"
end = "https://en.wikipedia.org/wiki/Kongoni_(operating_system)"
# start = "file:///C:/Users/timot/OneDrive/Desktop/WikiRacer/Test.html"

startThread = Thread(target=getLinks, args=(start, 1))
endThread = Thread(target=getLinks, args=(end, 2))

startThread.start()
endThread.start()

startThread.join()
endThread.join()
