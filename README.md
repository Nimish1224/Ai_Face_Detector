# <em> AI Face Detection Algorithm </em>
## Working Principle
<ul><li><b> A facial recognition system identifies or verifies a person’s identity by analyzing their face. The raw input for the camera is the person’s face recorded in real-time. The AI-enabled face recognition system captures the person’s image from the recorded video, analyzes it and compares it with images stored in its database.
Facial recognition combined with a biometric fingerprint is useful for access control and prohibition of entry for unintended persons.</b></ul></li>
## Requirements
The first step is to install OpenCV. Run the following command line in your terminal :

<img src="https://github.com/Nimish1224/Ai_Face_Detector/blob/master/readme-src/cv.PNG">

## Imports and models path

We’ll create a new Jupyter notebook / python file and start off with :

<img src="https://github.com/Nimish1224/Ai_Face_Detector/blob/master/readme-src/import.PNG">

<ul> I. Cascade Classifiers
We’ll explore Cascade Classifiers at first.

1. Theory
Cascade classifier, or namely cascade of boosted classifiers working with haar-like features, is a special case of ensemble learning, called boosting. It typically relies on Adaboost classifiers (and other models such as Real Adaboost, Gentle Adaboost or Logitboost).

Cascade classifiers are trained on a few hundred sample images of image that contain the object we want to detect, and other images that do not contain those images.

How can we detect if a face is there or not ? There is an algorithm, called Viola–Jones object detection framework, that includes all the steps required for live face detection :

Haar Feature Selection, features derived from Haar wavelets
Create integral image
Adaboost Training
Cascading Classifiers
The original paper was published in 2001.

