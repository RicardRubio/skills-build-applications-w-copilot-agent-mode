from django.core.management.base import BaseCommand
from pymongo import MongoClient

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
            {"name": "Alice", "email": "alice@example.com", "age": 16},
            {"name": "Bob", "email": "bob@example.com", "age": 17},
        ])

        db.teams.insert_many([
            {"name": "Team A", "members": ["Alice", "Bob"]},
        ])

        db.activities.insert_many([
            {"user": "Alice", "activity": "Running", "duration": 30},
            {"user": "Bob", "activity": "Cycling", "duration": 45},
        ])

        # Ensure '_id' is not included to avoid duplicate key errors
        db.leaderboard.insert_many([
            {"user": "Alice", "points": 100},
            {"user": "Bob", "points": 80},
        ])

        db.workouts.insert_many([
            {"name": "Morning Run", "duration": 30, "calories_burned": 300},
            {"name": "Evening Cycle", "duration": 45, "calories_burned": 450},
        ])

        self.stdout.write(self.style.SUCCESS('Successfully populated the database with test data'))
