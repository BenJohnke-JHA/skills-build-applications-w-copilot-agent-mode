from django.test import TestCase
from django.contrib.auth.models import User
from .models import Team, Profile, Activity, Workout, Leaderboard

class ModelTests(TestCase):
    def setUp(self):
        self.team = Team.objects.create(name='Test Team')
        self.user = User.objects.create_user(username='testuser', email='test@example.com', password='testpass')
        self.profile = Profile.objects.create(user=self.user, team=self.team)
        self.activity = Activity.objects.create(user=self.user, type='run', duration=10, distance=2.5)
        self.workout = Workout.objects.create(user=self.user, name='Test Workout', description='Test Desc')
        self.leaderboard = Leaderboard.objects.create(user=self.user, points=50)

    def test_team(self):
        self.assertEqual(self.team.name, 'Test Team')

    def test_profile(self):
        self.assertEqual(self.profile.team, self.team)

    def test_activity(self):
        self.assertEqual(self.activity.type, 'run')

    def test_workout(self):
        self.assertEqual(self.workout.name, 'Test Workout')

    def test_leaderboard(self):
        self.assertEqual(self.leaderboard.points, 50)
