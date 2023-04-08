import joblib
import os
import pandas as pd
import copy

from .models import Location

MODEL_NAME = os.path.dirname(os.path.realpath(__file__)) + '/model/model.joblib'

ORDER = ['longitude', 'latitude', 'housing_median_age', 'total_rooms',
       'total_bedrooms', 'population', 'households', 'median_income',
       'ocean_proximity_<1H OCEAN', 'ocean_proximity_INLAND',
       'ocean_proximity_ISLAND', 'ocean_proximity_NEAR BAY',
       'ocean_proximity_NEAR OCEAN']

class Handler:
    def __init__(self, data):
        self.data = self._preprocess(copy.copy(data))
    
    def _preprocess(self, data):
        data['ocean_proximity'] = data['ocean_proximity'].name
        data = pd.DataFrame(data, index=[0])
        locations = self._get_location_names()
        for dummy in locations:
            if dummy not in data.columns:
                data[dummy] = 0
        return data[ORDER]
    
    def _get_location_names(self):
        return Location.objects.values_list('name', flat=True)

    def predict(self) -> float:
        model = joblib.load(MODEL_NAME)
        Y = model.predict(self.data)
        return Y[0]