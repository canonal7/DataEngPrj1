import logging
import pickle

from keras.models import load_model


class IrisPredictor:
    def __init__(self, model_file):
        self.model = pickle.load(open(model_file, 'rb'))

    def predict_single_record(self, df):
        y_pred = self.model.predict(df)
        logging.info("Prediction Output : %s", y_pred[0])
        status = (y_pred[0])
        return status
