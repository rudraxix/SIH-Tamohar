# TAMOHAR 

## OVERVIEW 

__TAMOHAR__ is a software solution designed to analyze and enhance low-light images of **PSR (Permanently Shadowed Regions) of the Lunar Craters** captured and extracted from the data of the OHRC (Obriter Hight Resolution Camera) sensor onboard Chandrayaan-2 satellite.

It aims to provide insights into the Moon's shadowed regions and assist in understanding the geographical composition of them which can be utilised for calculating landing location for rovers, discovering ice deposits or other prospective results on the Lunar surface by using a deep-learning neural network.

This neural network uses a Retinex-net architecture and decomposes the images into their illuminating and reflectance components and processes them seperately to enhance the images.
The key advantages of utilising this style of architecture are 
    - it allows for better noise reduction in these poorly lit images
    - it provides efficient and better-looking results
Hence, allowing for further research into these images and onto the lunar surface and craters.

## DATASETS 

- ### Lunar Reconnaissance Orbiter Camera (LROC) 
 The dataset includes high-resolution images of lunar surfaces which are critical for detecting hidden features such as craters, water/ice deposits, and potential landing sites.

- ### Orbital High Resolution Camera(OHRC)
 The High resolution data provided by the OHRC sensor is utilised for the training and testing of the model using the feature extraction for cropping out poorly lit regions of the Lunar surface specifically craters

- ### more datasets

##  To be continued...

