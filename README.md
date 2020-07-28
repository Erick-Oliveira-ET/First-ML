# First-ML
## Introduction
  This project is the starting point to my machine learning practical experience. I've been reading and watching videos for a long time now but never put anything in practice because my intension was to use ML in a robot simulation but I thought about it and building a simulation entirely would mine my energy to make the actual ML. Anyways, I have a really good understanding of the theory but not the actual thing.

  For my first project, I'm going to make a ML that gets a list of bucketized data (just a list of 0s and 1s that represents the real data)of 5 elements that represents a single hand (if the finger is up it's 1 an if it's down it's 0). 

  I'm using as inspiration an anime called Naruto. In this anime's world, the ninjas uses the hand positioning, called seal, to manipulate an energy, called chakra. 
This project is the complementation of an another project that I intend to make that consistes in building a glove that identifies the state of the fingers of the user.

  I'm aware that everything in this project could be make using computational vision. The thing is, computational vision is not the most efficient method to use in embedded systems or in microcontrollers and I want to be able to build an robot that uses ML, mainly, to use in the robotic team in my colege that I'm member called TERA (team of study in aplied robotics, literally translate from portuguese. More information in https://www.instagram.com/teraufu/?hl=pt-br.

  I can't wait to make this work.

## Preparing the dataset
  At first I thought it would be better if the ML randonly picked a hand seal in a file for an indefinitely time. But after reading the Tensorflow documentation, it would be better if I had a file with the dataset defined as it uses less processing and I can reuse the same data or increase if I need.
  
  First I need to select the position of each finger in the array: starts at the thumb of the right hand as 0 and increase until the pinky of the left hand as 9. 
  
  ![hand-seal](/Dataset/Hand_Enumaration.png?raw=true)
  
  Because of the limitations of this method, some hand seals are the same when buckerized because the fingers are up or down but the hand is in a different position. It's valid enphasize that there's no middle term, it's just up or down, 1 or 0. I could use the [bucketized_column](https://www.tensorflow.org/api_docs/python/tf/feature_column/bucketized_column) method of TensorFlow and make each seal be a random selection of 0s and 1s in a list but I want to make my dataset by hand and know wich image is wich list. Anyways. Because of the limitations I select 10 [specifics seals](Dataset/img/) and made a [cvs file](Dataset/data_set.csv) with the seal_name,bucket_list and number (number is the corresponding output as bucket_list is the input).
  
  Because my dataset is too small, hte ML will overfit anyways. So I want to make a CSV file with a lot of the same data randomly positioned and test different bach sizes and different layers configurations and plot everything to compare. For that, I'll make a script that randomly pics a item from a list and put on a CSV file a thousand times (literaly).
