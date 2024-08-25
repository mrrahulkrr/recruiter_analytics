import pandas as pd
from sklearn.ensemble import RandomForestRegressor, RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder

class PredictiveAnalytics:
    def __init__(self):
        self.time_to_hire_model = RandomForestRegressor()
        self.candidate_success_model = RandomForestClassifier()
        self.le_role = LabelEncoder()
        self.le_location = LabelEncoder()
        self.le_education = LabelEncoder()

    def preprocess_data(self, data):
        data['role_type'] = self.le_role.fit_transform(data['role_type'])
        data['location'] = self.le_location.fit_transform(data['location'])
        data['education'] = self.le_education.fit_transform(data['education'])
        return data

    def train_models(self, data):
        data = self.preprocess_data(data)
        
        X_time = data[['role_type', 'location', 'experience']]
        y_time = data['time_to_hire']
        self.time_to_hire_model.fit(X_time, y_time)

        X_success = data[['education', 'experience', 'time_to_hire']]
        y_success = data['success']
        self.candidate_success_model.fit(X_success, y_success)

    def predict_time_to_hire(self, features):
        features['role_type'] = self.le_role.transform([features['role_type']])[0]
        features['location'] = self.le_location.transform([features['location']])[0]
        X = pd.DataFrame([features])
        return self.time_to_hire_model.predict(X)[0]

    def predict_candidate_success(self, features):
        features['education'] = self.le_education.transform([features['education']])[0]
        X = pd.DataFrame([features])
        return self.candidate_success_model.predict_proba(X)[0][1]