# http://www.apple.com/itunes/affiliates/resources/documentation/itunes-store-web-service-search-api.html
import webbrowser # This module can control the browser

baseURL = "https://itunes.apple.com/search?"
searchKeys = [
    ["term", "Red Light Tiesto"],
    ["country", "US"],
    ["media", "music"],
    ["limit", "50"],
    ["lang", "en_us"],
    ["explicit", "yes"]
]

finalURL = baseURL
for i in range(0, len(searchKeys)): # len() returns length of a variable
    # print "Term: %d" % (i)
    currentKey = searchKeys[i]
    criteria = str(currentKey[1]) #Make sure it's a string
    criteria = criteria.replace(" ", "%20") # %20 represents a space
    appendStr = currentKey[0] + "=" + criteria # Build url
    # print(appendStr)
    if i < (len(searchKeys) - 1):
        appendStr += "&"
    finalURL += appendStr

print("Final URL: " + finalURL)
webbrowser.open(finalURL)
