""" Example of prediction from CLI """
import sys
import gzip
import pickle
import warnings

warnings.filterwarnings("ignore")

CLASSES = {
    0: "negative",
    4: "positive"
}


def load_model(model_filename):
    """ Load model from file """
    # print("loading the model...")
    try:
        with gzip.open(model_filename, 'rb') as fmodel:
            model = pickle.load(fmodel,encoding='latin1')
    except Exception as ex:
        raise IOError("Couldn't load  model: %r" % ex)

    return model

def predict(model, text):
    """ Predict class given model and input (text) """
    # print("Extracting features...")
    x_vector = model.vectorizer.transform([text])
    y_predicted = model.predict_proba(x_vector)#model.predict_proba(x_vector)
    return y_predicted[:,1][0]#CLASSES.get(y_predicted[0])

# def main(argv):
def main(text):
    """ Predict the sentiment of the given text """
    # text = argv[1]
    model_filename = "data/model.dat.gz"
    model = load_model(model_filename)
    return predict(model, text)