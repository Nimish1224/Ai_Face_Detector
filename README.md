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

### Haar Feature Selection

There are some common features that we find on most common human faces :
<ul><li>a dark eye region compared to upper-cheeks</li>
<li>a bright nose bridge region compared to the eyes</li>
<li>some specific location of eyes, mouth, nose.</li></ul>
The characteristics are called Haar Features. The feature extraction process will look like this :

<img src="https://github.com/Nimish1224/Ai_Face_Detector/blob/master/readme-src/haar.jpg">


n this example, the first feature measures the difference in intensity between the region of the eyes and a region across the upper cheeks. The feature value is simply computed by summing the pixels in the black area and subtracting the pixels in the white area.

Then, we apply this rectangle as a convolutional kernel, over our whole image. In order to be exhaustive, we should apply all possible dimensions and positions of each kernel. A simple 24*24 images would typically result in over 160’000 features, each made of a sum/subtraction of pixels values. It would computationally be impossible for live face detection. So, how do we speed up this process ?

<ul><li>once the good region has been identified by a rectangle, it is useless to run the window over a completely different region of the image. This can be achieved by Adaboost.</li>
<li>compute the rectangle features using the integral image principle, which is way faster. We’ll cover this in the next section.</li></ul>

<img src="https://github.com/Nimish1224/Ai_Face_Detector/blob/master/readme-src/haar_selection.jpg">

There are several types of rectangles that can be applied for Haar Features extraction. According to the original paper :

<ul><li>the two-rectangle feature is the difference between the sum of the pixels within two rectangular regions, used mainly for detecting edges (a,b)</li>
<li>the three-rectangle feature computes the sum within two outside rectangles subtracted from the sum in a center rectangle, used mainly for detecting lines (c,d)</li>
<li>the four-rectangle feature computes the difference between diagonal pairs of rectangle (e)</li></ul>

<img src="https://github.com/Nimish1224/Ai_Face_Detector/blob/master/readme-src/haar_rectangles.jpg">


Now that the features have been selected, we apply them on the set of training images using Adaboost classification, that combines a set of weak classifiers to create an accurate ensemble model. With 200 features (instead of 160’000 initially), an accuracy of 95% is acheived. The authors of the paper have selected 6’000 features.

<h2> Crafted 💖 with 🐍 Python 🐍</h2>


