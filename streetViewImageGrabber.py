#https://www.google.com/maps/@3.1481281,101.713907,3a,28.1y,22.31h,98.63t/data=!3m6!1e1!3m4!1sj0mhuERB8MvasM8R_VUqsg!2e0!7i13312!8i6656


import urllib.request
APIkey = "AIzaSyDIJ9XX2ZvRKCJcFRrl-lRanEtFUow4piM"
downloadDirectory = "/home/redrange0/Desktop/street/"


locationList = [[3.098594, 101.6794974],
                [3.1301633, 101.6705928],
                [3.15288105006454,101.694120398408],
                [3.15572532981701,101.738853808438],
                [3.2104929,101.6711727],
                [3.16827540004374,101.70724061157],
                [3.1053007,101.67799545],
                [3.12749104525972,101.670485781298],
                [3.12850659999064,101.730704749984],
                [3.16951785143926,101.694380098328]
                ]


for cordinates in locationList:
    llong = cordinates[0]
    llat = cordinates[1]

    for i in range(48):
        pitch = 0
        if(i > 24):#position camera up after full 360 degree spin
            pitch = 15

        urlString = "https://maps.googleapis.com/maps/api/streetview?size=1920x1080&location=" + str(llong) + ',' + str(llat) + "&fov=20&heading=" + str(i*15) + "&pitch=" + str(pitch) + "&key=" + APIkey
        print("saving: " + urlString)
        imageName = urlString.replace('https://maps.googleapis.com/maps/api/streetview?size=1920x1080&location=', '')
        #imageName = "image" + str(i + 1)
        try:
            urllib.request.urlretrieve(urlString, downloadDirectory + imageName + ".jpg")
        except:
            print("Error with cord " + str(cordinates))
