import json
import numpy as np
import pickle

__locations = None
__data_columns = None
__model = None

# Functia de incarcare a pretului
def get_property_price(address, rooms, sqmt, level, level_max, baths):

    try:
        loc_index = __data_columns.index(address.lower())
    except:
        loc_index = 5

    x = np.zeros(len(__data_columns))
    x[0] = rooms
    x[1] = sqmt
    x[2] = level
    x[3] = level_max
    x[4] = baths

    # Indentificăm adresa zonei noastre si o facem egala cu 1 
    if loc_index>=0:
        x[loc_index] = 1

    #Rotunjim rezultatul inainte de al trimite
    return round(__model.predict([x])[0],2)

# Functia de incarcare a modelului salvat
def load_saved_model():

    global  __data_columns
    global __locations

    # Extragem coloanele de date pentru a compara valoarea primita cu ele
    with open("./pickled_model/columns.json", "r") as f:
        __data_columns = json.load(f)['data_columns']
        __locations = __data_columns[5:]  

    global __model
    if __model is None:
        with open('./pickled_model/ml_model.pickle', 'rb') as f:
            __model = pickle.load(f)
    print("Loading saved model")

def get_location_names():
    return __locations

def get_data_columns():
    return __data_columns

if __name__ == '__main__':

	load_saved_model()
	
	print(get_property_price('Balta alba', 2, 60, 1, 4, 1))
	print(get_property_price('Balta neagra', 2, 60, 1, 4, 1))

