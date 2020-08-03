# <em> AI Face Detection Algorithm </em>
## Working Principle
<b> A facial recognition system identifies or verifies a person’s identity by analyzing their face. The raw input for the camera is the person’s face recorded in real-time. The AI-enabled face recognition system captures the person’s image from the recorded video, analyzes it and compares it with images stored in its database.
Facial recognition combined with a biometric fingerprint is useful for access control and prohibition of entry for unintended persons.</b>
## Requirements
The first step is to install OpenCV. Run the following command line in your terminal :

<img src="https://github.com/Nimish1224/Ai_Face_Detector/blob/master/readme-src/cv.PNG">

## Imports and models path

We’ll create a new Jupyter notebook / python file and start off with :

<img src="https://github.com/Nimish1224/Ai_Face_Detector/blob/master/readme-src/import.PNG">

## I. Cascade Classifiers
   Let's explore Cascade Classifiers.
   
   <b>Theory :-</b>
     Cascade classifier, or namely cascade of boosted classifiers working with haar-like features, is a special case of ensemble learning, called boosting. It typically              relies on   Adaboost classifiers (and other models such as Real Adaboost, Gentle Adaboost or Logitboost).
     Cascade classifiers are trained on a few hundred sample images of image that contain the object we want to detect, and other images that do not contain those images.

   How can we detect if a face is there or not ? There is an algorithm, called Viola–Jones object detection framework, that includes all the steps required for live face          detection :

  <ul><li>Haar Feature Selection, features derived from Haar wavelets</li>
  <li>Create integral image</li>
  <li>Adaboost Training</li>
  <li>Cascading Classifiers</li></ul>
  
The original [paper](https://www.cs.cmu.edu/~efros/courses/LBMV07/Papers/viola-cvpr-01.pdf) was published in 2001.

<b> Haar Feature Selection</b>

There are some common features that we find on most common human faces :

<ul><li>a dark eye region compared to upper-cheeks</li>
<li>a bright nose bridge region compared to the eyes</li>
<li>some specific location of eyes, mouth, nose.</li></ul>
The characteristics are called Haar Features. The feature extraction process will look like this :

