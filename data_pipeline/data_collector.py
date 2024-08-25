import pandas as pd
import sqlite3
from datetime import datetime, timedelta
import random

def generate_sample_data(num_records=1000):
    role_types = ['Software Engineer', 'Data Scientist', 'Product Manager', 'Designer', 'Marketing Specialist']
    locations = ['New York', 'San Francisco', 'London', 'Berlin', 'Tokyo']
    education_levels = ['Bachelor', 'Master', 'PhD']

    data = []
    start_date = datetime.now() - timedelta(days=365)

    for _ in range(num_records):
        role_type = random.choice(role_types)
        location = random.choice(locations)
        experience = random.randint(0, 15)
        education = random.choice(education_levels)
        skills = ', '.join(random.sample(['Python', 'Java', 'SQL', 'JavaScript', 'React', 'Machine Learning'], k=random.randint(2, 4)))
        time_to_hire = random.randint(10, 90)
        success = random.choice([True, False])
        date = start_date + timedelta(days=random.randint(0, 365))

        data.append({
            'role_type': role_type,
            'location': location,
            'experience': experience,
            'education': education,
            'skills': skills,
            'time_to_hire': time_to_hire,
            'success': success,
            'date': date.strftime('%Y-%m-%d %H:%M:%S')
        })

    return pd.DataFrame(data)

def insert_data_to_db(data, db_path):
    conn = sqlite3.connect(db_path)
    data.to_sql('recruitment_data', conn, if_exists='append', index=False)
    conn.close()

if __name__ == '__main__':
    db_path = '../backend/app.db'  # Adjust this path if necessary
    sample_data = generate_sample_data()
    insert_data_to_db(sample_data, db_path)
    print(f"Inserted {len(sample_data)} records into the database.")