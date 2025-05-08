from django.core.management.base import BaseCommand
from octofit_tracker.models import User, Team, Activity, Leaderboard, Workout
from django.contrib.auth.hashers import make_password

class Command(BaseCommand):
    help = 'Populate the database with test data for OctoFit Tracker'

    def handle(self, *args, **kwargs):
        # Clear existing data
        User.objects.all().delete()
        Team.objects.all().delete()
        Activity.objects.all().delete()
        Leaderboard.objects.all().delete()
        Workout.objects.all().delete()

        # Create test users
        alex = User.objects.create(
            username="alex.smith",
            email="alex.smith@mergington.edu",
            password=make_password("password123")
        )

        emily = User.objects.create(
            username="emily.johnson",
            email="emily.johnson@mergington.edu",
            password=make_password("password123")
        )

        michael = User.objects.create(
            username="michael.brown",
            email="michael.brown@mergington.edu",
            password=make_password("password123")
        )

        # Create test teams
        speed_demons = Team.objects.create(
            name="Speed Demons"
        )
        speed_demons.members.add(alex, emily)

        power_squad = Team.objects.create(
            name="Power Squad"
        )
        power_squad.members.add(michael)

        # Create test activities
        Activity.objects.create(
            user=alex,
            activity_type="Running",
            duration=30  # 30 minutes
        )

        Activity.objects.create(
            user=emily,
            activity_type="Walking",
            duration=45  # 45 minutes
        )

        Activity.objects.create(
            user=michael,
            activity_type="Strength Training",
            duration=60  # 60 minutes
        )

        # Create test leaderboard entries
        Leaderboard.objects.create(
            user=michael,
            score=250,
            period="weekly"
        )

        Leaderboard.objects.create(
            user=alex,
            score=180,
            period="weekly"
        )

        Leaderboard.objects.create(
            user=emily,
            score=150,
            period="weekly"
        )

        # Create test workouts
        Workout.objects.create(
            name="Morning Run",
            description="5K morning run at moderate pace",
            duration=30,
            difficulty="medium",
            activity_type="Running"
        )

        Workout.objects.create(
            name="Strength Training",
            description="Full body workout with bodyweight exercises",
            duration=45,
            difficulty="hard",
            activity_type="Strength Training"
        )

        self.stdout.write(self.style.SUCCESS('Successfully populated the database'))
