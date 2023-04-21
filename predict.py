from keras.models import load_model
from keras.models import Sequential
from keras.layers import Conv2D, MaxPooling2D
from keras.layers import Activation, Dropout, Flatten, Dense
import pandas as pd
#from keras.preprocessing.image import img_to_array, load_img
from keras.utils import img_to_array, load_img
import numpy as np

# -----------------------------------------------------------------------------
# Dimensions of images
# -----------------------------------------------------------------------------
img_width, img_height = 250, 250
input_shape = (img_width, img_height, 3)

# -----------------------------------------------------------------------------
# Load model
# -----------------------------------------------------------------------------
test_model = load_model('model.h5')

# -----------------------------------------------------------------------------
# Image data path
# -----------------------------------------------------------------------------
basedir = "data/test/"

# -----------------------------------------------------------------------------
# Prediction
# -----------------------------------------------------------------------------
i=0

def predict(basedir, i, model):
    
    path = basedir+str(i)+'.png'
    
    img = load_img(path,False,target_size=(img_width,img_height))
        
    x = img_to_array(img)
    x = np.expand_dims(x, axis=0)
        
    #preds = model.predict_classes(x)
    preds = np.argmax(model.predict(x), axis=1)
    #preds = (model.predict(x)>0.5).astype("int32")
   # probs = model.predict_proba(x)
    probs = model.predict(x)
    #probs = np.argmax(model.predict(x), axis=1)
        
    if preds==0: print('COVID-19')
    if preds==1: print('Normal')
    if preds==2: print('Pneumonia')

    print ('')
    print ('Probability: ', probs*100)
    
    return preds, probs
 
# ***********************************************

# MAIN
the_save = []
for i in range (0,1389): # Images to be tested

    print('Test Sample: ', i)

    (preds,probs)=predict(basedir, i, test_model) # prediction
    
    the_save.append(preds)

    print(' ')

df = pd.DataFrame(the_save)
df.to_csv('classification report.csv', index=True)
