from django.core.management.base import BaseCommand

from django.contrib.auth.models import User
from octofit_tracker.models import Team, Profile, Activity, Workout, Leaderboard

class Command(BaseCommand):
    help = 'Populate the octofit_db database with test data'

    def handle(self, *args, **options):
        # Delete existing data

        Activity.objects.all().delete()
        Workout.objects.all().delete()
        Leaderboard.objects.all().delete()
        Profile.objects.all().delete()
        Team.objects.all().delete()
        User.objects.all().delete()

        # Create teams
        marvel = Team.objects.create(name='Team Marvel')
        dc = Team.objects.create(name='Team DC')

        # Create users

        ironman = User.objects.create_user(username='ironman', email='ironman@marvel.com', password='password', first_name='Tony', last_name='Stark')
        batman = User.objects.create_user(username='batman', email='batman@dc.com', password='password', first_name='Bruce', last_name='Wayne')
        Profile.objects.create(user=ironman, team=marvel)
        Profile.objects.create(user=batman, team=dc)

        # Create activities
        Activity.objects.create(user=ironman, type='run', duration=30, distance=5)
        Activity.objects.create(user=batman, type='cycle', duration=60, distance=20)

        # Create workouts
        Workout.objects.create(user=ironman, name='Chest Day', description='Bench press and pushups')
        Workout.objects.create(user=batman, name='Leg Day', description='Squats and lunges')

        # Create leaderboard
        Leaderboard.objects.create(user=ironman, points=100)
        Leaderboard.objects.create(user=batman, points=120)

        self.stdout.write(self.style.SUCCESS('Database populated with test data.'))
