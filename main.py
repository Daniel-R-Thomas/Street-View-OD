#need api key
#Kuala Lumpur for testing
#https://www.google.com/maps/@3.1481281,101.713907,3a,28.1y,22.31h,98.63t/data=!3m6!1e1!3m4!1sj0mhuERB8MvasM8R_VUqsg!2e0!7i13312!8i6656


import urllib.request

APIkey = ""
downloadDirectory = "/home/redrange0/Desktop/street/"


locationList = [[3.1522421, 101.7178791]]
                #[3.1495211, 01.7229022]]


for cordinates in locationList:
    llong = cordinates[0]
    llat = cordinates[1]

    for i in range(48):
        pitch = 0
        if(i > 24):#position camera up after full 360 degree spin
            pitch = 15

        urlString = "https://maps.googleapis.com/maps/api/streetview?size=1920x1080&location=" + str(llong) + ',' + str(llat) + "&fov=20&heading=" + str(i*15) + "&pitch=" + str(pitch) + "&key=" + APIkey
        print("saving: " + urlString)
        #imageName = urlString.replace('https://maps.googleapis.com/maps/api/streetview?size=1920x1080&location=', '')
        imageName = "image" + str(i + 1)
        urllib.request.urlretrieve(urlString, downloadDirectory + imageName + ".jpg")
