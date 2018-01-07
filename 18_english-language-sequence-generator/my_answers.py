import numpy as np

from keras.models import Sequential
from keras.layers import Dense
from keras.layers import LSTM
import keras
import string
from keras.layers import Activation

# TODO: fill out the function below that transforms the input series 
# and window-size into a set of input/output pairs for use with our RNN model
def window_transform_series(series, window_size):
    # Ensure it works when window_size > series.size or series.size == 0
    if window_size > series.size:
        window_size = abs(series.size - 1)

    # Containers for input/output pairs
    X = []
    y = []

    for i in range(0, series.size - window_size):
        X.append(series[i:i + window_size])
        y.append(series[i + window_size])
      
    # Reshape each 
    X = np.asarray(X)
    X.shape = (np.shape(X)[0:2])
    y = np.asarray(y)
    y.shape = (len(y),1)

    return X,y


# TODO: build an RNN to perform regression on our time series input/output data
def build_part1_RNN(window_size):
    # Create the two requested layers. 1 LSTM and 1 dense layer with tanh activation
    layer1 = LSTM(5, input_shape = (window_size, 1))
    layer2 = Dense(1, activation = 'tanh')
    
    # Create a sequential model. Add the two layers previously created
    rnn = Sequential()
    rnn.add(layer1)
    rnn.add(layer2)
    
    # Return it
    return rnn


### TODO: return the text input with only ascii lowercase and the punctuation given below included.
def cleaned_text(text):
    punctuation = ['!', ',', '.', ':', ';', '?'] 
    
    # Create a set of valid characters, including the ' '.
    valid_characters = list(string.ascii_lowercase) + punctuation + [' ']
    
    # Return only valid characters.
    text = ''.join([c for c in text if c in valid_characters])

    return text

### TODO: fill out the function below that transforms the input text and window-size into a set of input/output pairs for use with our RNN model
def window_transform_text(text, window_size, step_size):
    # containers for input/output pairs
    inputs = []
    outputs = []

    for i in range(0, len(text) - window_size, step_size):
        inputs.append(text[i:(i + window_size)])
        outputs.append(text[i + window_size])
        
    return inputs, outputs

# TODO build the required RNN model: 
# a single LSTM hidden layer with softmax activation, categorical_crossentropy loss 
def build_part2_RNN(window_size, num_chars):
    # Create the three requested layers. 1 LSTM, 1 dense layer and 1 softmax activation layer
    layer1 = LSTM(200, input_shape = (window_size, num_chars))
    layer2 = Dense(num_chars)
    
    # Please notice that layer3 could be avoided by passing 'activation = 'softmax' to layer2
    layer3 = Activation('softmax') 
    
    
    
    # Create a sequential model. Add the two layers previously created
    rnn = Sequential()
    rnn.add(layer1)
    rnn.add(layer2)
    rnn.add(layer3)
    
    # Return it
    return rnn
