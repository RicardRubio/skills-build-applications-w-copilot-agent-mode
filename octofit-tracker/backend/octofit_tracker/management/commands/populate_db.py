from django.core.management.base import BaseCommand
from pymongo import MongoClient

class Command(BaseCommand):
    help = 'Populate the database with test data for OctoFit Tracker'

    def handle(self, *args, **kwargs):
        client = MongoClient('localhost', 27017)
        db = client['octofit_db']

        # Clear existing data
        db.users.delete_many({})
        db.teams.delete_many({})
        db.activities.delete_many({})
        db.leaderboard.delete_many({})
        db.workouts.delete_many({})

        # Insert test users (students)
        db.users.insert_many([
            {
                "name": "Alex Smith",
                "email": "alex.smith@mergington.edu",
                "age": 16,
                "grade": "10th",
                "fitness_level": "intermediate"
            },
            {
                "name": "Emily Johnson",
                "email": "emily.johnson@mergington.edu",
                "age": 15,
                "grade": "9th",
                "fitness_level": "beginner"
            },
            {
                "name": "Michael Brown",
                "email": "michael.brown@mergington.edu",
                "age": 17,
                "grade": "11th",
                "fitness_level": "advanced"
            }
        ])

        # Insert test teams
        db.teams.insert_many([
            {
                "name": "Speed Demons",
                "members": ["Alex Smith", "Emily Johnson"],
                "category": "Running",
                "points": 150
            },
            {
                "name": "Power Squad",
                "members": ["Michael Brown"],
                "category": "Strength Training",
                "points": 200
            }
        ])

        # Insert test activities
        db.activities.insert_many([
            {
                "user": "Alex Smith",
                "activity_type": "Running",
                "duration": 30,
                "distance": 5.0,
                "calories_burned": 300,
                "date": "2025-05-07"
            },
            {
                "user": "Emily Johnson",
                "activity_type": "Walking",
                "duration": 45,
                "distance": 3.5,
                "calories_burned": 200,
                "date": "2025-05-07"
            },
            {
                "user": "Michael Brown",
                "activity_type": "Strength Training",
                "duration": 60,
                "exercises": ["Push-ups", "Pull-ups", "Squats"],
                "calories_burned": 400,
                "date": "2025-05-07"
            }
        ])

        # Insert test leaderboard data
        db.leaderboard.insert_many([
            {
                "user": "Michael Brown",
                "points": 250,
                "badges": ["Heavyweight Champion", "Early Bird"],
                "streak": 5
            },
            {
                "user": "Alex Smith",
                "points": 180,
                "badges": ["Speed Runner"],
                "streak": 3
            },
            {
                "user": "Emily Johnson",
                "points": 120,
                "badges": ["Dedicated Beginner"],
                "streak": 2
            }
        ])

        # Insert test workouts (suggested workouts)
        db.workouts.insert_many([
            {
                "name": "Beginner Workout",
                "duration": 30,
                "difficulty": "beginner",
                "exercises": [
                    {"name": "Brisk Walking", "duration": 10},
                    {"name": "Basic Stretches", "duration": 10},
                    {"name": "Simple Squats", "duration": 10}
                ],
                "calories_target": 200
            },
            {
                "name": "Intermediate Cardio",
                "duration": 45,
                "difficulty": "intermediate",
                "exercises": [
                    {"name": "Light Jogging", "duration": 15},
                    {"name": "Core Exercises", "duration": 15},
                    {"name": "High-Intensity Intervals", "duration": 15}
                ],
                "calories_target": 350
            },
            {
                "name": "Advanced Training",
                "duration": 60,
                "difficulty": "advanced",
                "exercises": [
                    {"name": "Intense Running", "duration": 20},
                    {"name": "Weight Training", "duration": 20},
                    {"name": "Endurance Exercises", "duration": 20}
                ],
                "calories_target": 500
            }
        ])

        self.stdout.write(self.style.SUCCESS('Successfully populated the database with test data for OctoFit Tracker'))
