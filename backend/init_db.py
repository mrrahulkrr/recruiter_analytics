from app import create_app, db
from app.models import RecruitmentData
from app.predictive_analytics import PredictiveAnalytics
import pandas as pd

app = create_app()

def init_db():
    with app.app_context():
        # Create tables
        db.create_all()

        # Check if data exists
        if RecruitmentData.query.first() is None:
            print("No data found. Please run the data_collector.py script to populate the database.")
            return

        # Train models
        data = RecruitmentData.query.all()
        df = pd.DataFrame([d.to_dict() for d in data])
        
        pa = PredictiveAnalytics()
        pa.train_models(df)
        
        print("Database initialized and models trained successfully.")

if __name__ == '__main__':
    init_db()