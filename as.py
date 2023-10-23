from keras.models import load_model

import pickle

model = pickle.load(open('project_model.pkl','rb'))

print(model.predict([[5.4,3.0,4.5,1.5]])[0])
