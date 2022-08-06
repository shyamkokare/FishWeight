import config
import pickle 
import json
import numpy as np

class FishWeight():

    def __init__(self,Length1,Length2,Length3,Height,Width,Species):

        self.Length1 = Length1
        self.Length2 = Length2
        self.Length3 = Length3
        self.Height = Height
        self.Width = Width
        self.Species = 'Species_' + Species

    def load_model(self):

        with open(config.MODEL_FILE_PATH,'rb') as f:
            self.reg_model = pickle.load(f)

        with open(config.JSON_FILE_PATH,'r') as f:
            self.project_data = json.load(f)

    def get_fish_weight(self):

        self.load_model()

        species_index = self.project_data['columns'].index(self.Species)

        array = np.zeros(len(self.project_data['columns']))

        array[0] = self.Length1
        array[1] = self.Length2
        array[2] = self.Length3
        array[3] = self.Height
        array[4] = self.Width
        array[species_index] = 1

        weight = self.reg_model.predict([array])

        return weight