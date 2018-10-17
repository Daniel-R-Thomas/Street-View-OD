# Google Street View Machine Learning Intelligence

## Intent

The intent behind this project is to be able to download all available street view images of a given city then perform object recognition for pre trained objects. Detected objects will have their GPS coordinates saved to be mapped out.

![Image of Recognized Camera](https://raw.githubusercontent.com/Daniel-R-Thomas/Street-View-OD/master/exa.png)
Detected security camera on collected Street View image

Project can be listed into three subcategories below. These issues all had to be solved independently and combined together.

### Project Structure

* Object recognition

* Street View image collection

* Mapping given area

### Object Recognition

Object recognition software used: Google tensorflow in a docker environment https://github.com/sofwerx/tensorflow-object-detection-docker. Collect the majority of the images via google streetview as this will be the same environment the image recognition will be performing in. Once collected, these images needs to be annotated per object. Afterwards, the CPU/GPU training can begin. It’s recommended to use a slower, more accurate model for this phase as nothing needs to be done in real time. After the training is finished, the model should be collected. The street view images can now be run through the object detection.


### Street View image collection

Street View images will be collected from google street views API via url request in the following format: https://www.google.com/maps/@3.1481281,101.713907,3a,28.1y,22.31h,98.63t/data=!3m6!1e1!3m4!1sj0mhuERB8MvasM8R_VUqsg!2e0!7i13312!8i6656
Mass amounts of relevant coordinates will need to be collected in a give area in order to make this useful. Traversing google maps is very time intensive to program. Another way of getting effective coordinates is by using this opensource tool that makes use of OpenStreetMaps: https://extract.bbbike.org/. This will give a mass export of coordinates and other data of a given area. Parse through this data to extract only the coordinates. The next problem is if the coordinates parsed are within the city or not. Use the attached code to reverse geo locate the coordinates into addresses. If the addresses do not return the city you want, throw them away. This will then give a large list of good coordinates that can be pumped into the API to mass download pictures of the entire city. 

### Mapping given area

After the object model is training and the street view images are downloaded in mass quantities, the time to run object recognition on the street view images can begin. Every time and object is detected, the image name should be logged in any data format along with the object type. Each image name will have the coordinates and direction of the detected object. Compiling all this data together can then be uploaded to any mapping tool to begin analysing.

### Project contributions

* Daniel R. Thomas - daniel.r.thomas.drt@gmail.com
* Ronald Davindra Bactawar - ronbactawar@gmail.com
* Christina Ling - christina.m.ling@gmail.com

### Presentation

https://docs.google.com/presentation/d/12L9wRIfx4t7goYt1r5_rZdbqoIJEMxBmE8FkHz6T9Eg/edit#slide=id.g44e1f9511a_0_169
