from django.core.management.base import BaseCommand
from pymongo import MongoClient
from django.contrib.auth.hashers import make_password

class Command(BaseCommand):
    help = 'Populate the database with test data'

    def handle(self, *args, **kwargs):
        client = MongoClient('localhost', 27017)
        db = client['octofit_db']

        # Clear existing data
        db.users.delete_many({})
        db.teams.delete_many({})
        db.activities.delete_many({})
        db.leaderboard.delete_many({})
        db.workouts.delete_many({})

        # Insert test data
        db.users.insert_many([
            {"username": "alex.smith", "email": "alex.smith@mergington.edu", "password": make_password("password123")},
            {"username": "emily.johnson", "email": "emily.johnson@mergington.edu", "password": make_password("password123")},
            {"username": "michael.brown", "email": "michael.brown@mergington.edu", "password": make_password("password123")},
        ])

        db.teams.insert_many([
            {"name": "Speed Demons", "members": ["alex.smith", "emily.johnson"]},
            {"name": "Power Squad", "members": ["michael.brown"]},
        ])

        db.activities.insert_many([
            {"user": "alex.smith", "activity_type": "Running", "duration": 30},
            {"user": "emily.johnson", "activity_type": "Walking", "duration": 45},
            {"user": "michael.brown", "activity_type": "Strength Training", "duration": 60},
        ])

        db.leaderboard.insert_many([
            {"user": "michael.brown", "score": 250},
            {"user": "alex.smith", "score": 180},
            {"user": "emily.johnson", "score": 150},
        ])

        db.workouts.insert_many([
            {"name": "Morning Run", "description": "5K morning run at moderate pace", "duration": 30, "difficulty": "medium", "activity_type": "Running"},
            {"name": "Strength Training", "description": "Full body workout with bodyweight exercises", "duration": 45, "difficulty": "hard", "activity_type": "Strength Training"},
        ])

        self.stdout.write(self.style.SUCCESS('Successfully populated the database with test data'))
