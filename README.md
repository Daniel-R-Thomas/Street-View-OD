# Google Street View Machine Learning Intelligence

## Introduction

This a log of my development of the Google Street View Machine Learning Intelligence project during my internship at SOFWERX. [SOFWERX](http://www.sofwerx.org) is an organization devoted to open-sourcing solutions to challenges faced by warfighters every day. The intent behind this project is to be able to quickly and automatically search for trained objects in an entire city via Google Street View. For example, being able to map out a large portion of an areas security cameras or power grid via poles and transformers is very useful.

![Image of Recognized Camera](https://raw.githubusercontent.com/Daniel-R-Thomas/weekly-activity-report/master/datascience/Daniel/cam2.png)
<p align="center">Detected security camera on collected Street View image</p>

### Objectives

* Automated collection of every Google Street View image in a given city

* Performing object recognition on collected images for a specific object(s) and recording location

* Analyzing and mapping collected data

### Current Capabilities

* Given a list of coordinates, imageGrabber.py will download the nearest Street View images.

* TensorFlow is currently setup to properly train and recognize given objects/images. Dome cameras are being detected Successfully

### Pending Implementations

* Method of downloading all Street View images in given area. Either via brute forcing coordinates or DFS/BFS traversal of the streets

* Logging objects location once recognized in TensorFlow

* Loading and displaying data pinpoints onto map

* Objects to be collected: Domecams, longcams, transformers, power polls

* Pending...

### Dependencies

* SOFWERX [TensorFlow Object Detection Docker](https://github.com/sofwerx/tensorflow-object-detection-docker) file

* Python 2 and 3

* Pending...

### How To Run

* Pending...

### Change Log

* Pending...
