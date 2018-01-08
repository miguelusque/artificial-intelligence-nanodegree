# Students Admission Prediction

This repository contains the 'studnets admission prediction' project of the Udacity's [Artificial Intelligence Nanodegree](https://www.udacity.com/course/artificial-intelligence-nanodegree--nd889).

## Project Overview
In this project it will be built a Multilayer Perceptron (MLP) that can predict student admissions to graduate school at UCLA based on three pieces of data:
GRE Scores (Test)
GPA Scores (Grades)
Class rank (1-4)



### Instructions

1. Clone the repository and navigate to the downloaded folder.

	```
		git clone https://github.com/udacity/aind2-dl.git
		cd aind2-dl
	```

2. Obtain the necessary Python packages, and switch Keras backend to Tensorflow.

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

3. Enjoy!


source activate aind-dl

. start.sh

KERAS_BACKEND=tensorflow jupyter notebook Student_Admissions.ipynb

In case of issues switching between Thensorflow and Theano backends, please have a look to:
https://www.nodalpoint.com/switch-keras-backend/
