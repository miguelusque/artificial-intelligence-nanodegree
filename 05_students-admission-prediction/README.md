# Students Admission Prediction

This repository contains the 'students admission prediction' project of the Udacity's [Artificial Intelligence Nanodegree](https://www.udacity.com/course/artificial-intelligence-nanodegree--nd889).

![Students Admission Prediction](cover.jpg)

## Project Overview
In this project it will be built a Multilayer Perceptron (MLP) that can predict student admissions to graduate school at UCLA based on three pieces of data:

 - GRE Scores (Test)
 - GPA Scores (Grades)
 - Class rank (1-4)

The dataset originally came from [here](http://www.ats.ucla.edu/).

## Install

 1. Obtain the necessary Python packages, and switch Keras backend to Tensorflow.

	For __Mac/OSX__:
	```
		conda env create -f requirements/aind-dl-mac.yml
		source activate aind-dl
		KERAS_BACKEND=tensorflow python -c "from keras import backend"
	```

	For __Windows__:
	```
		conda env create -f requirements/aind-dl-windows.yml
		activate aind-dl
		set KERAS_BACKEND=tensorflow
		python -c "from keras import backend"
	```

	For __Linux__:
	```
		conda env create -f requirements/aind-dl-linux.yml
		source activate aind-dl
		KERAS_BACKEND=tensorflow python -c "from keras import backend"
	```

 2. Run jupyter notebook
 	```
		source activate aind-dl
		. start.sh
	```

 3. Enjoy!
