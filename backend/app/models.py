from app import db
from datetime import datetime

class RecruitmentData(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    role_type = db.Column(db.String(50), nullable=False)
    location = db.Column(db.String(50), nullable=False)
    experience = db.Column(db.Integer, nullable=False)
    education = db.Column(db.String(50), nullable=False)
    skills = db.Column(db.String(200), nullable=False)
    time_to_hire = db.Column(db.Integer, nullable=False)
    success = db.Column(db.Boolean, nullable=False)
    date = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)

    def to_dict(self):
        return {
            'id': self.id,
            'role_type': self.role_type,
            'location': self.location,
            'experience': self.experience,
            'education': self.education,
            'skills': self.skills,
            'time_to_hire': self.time_to_hire,
            'success': self.success,
            'date': self.date.isoformat()
        }