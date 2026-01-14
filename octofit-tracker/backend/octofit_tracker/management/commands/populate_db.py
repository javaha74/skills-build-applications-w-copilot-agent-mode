from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model
from djongo import models

from octofit_tracker import models as app_models

class Command(BaseCommand):
    help = 'Populate the octofit_db database with test data'

    def handle(self, *args, **options):
        User = get_user_model()
        # Delete all data safely for Djongo
        for model in [app_models.Activity, app_models.Workout, app_models.Leaderboard, User, app_models.Team]:
            for obj in model.objects.all():
                if getattr(obj, 'id', None):
                    obj.delete()

        # Create Teams
        marvel = app_models.Team.objects.create(name='Marvel')
        dc = app_models.Team.objects.create(name='DC')

        # Create Users
        users = [
            User.objects.create_user(username='ironman', email='ironman@marvel.com', password='password', team=marvel),
            User.objects.create_user(username='captainamerica', email='cap@marvel.com', password='password', team=marvel),
            User.objects.create_user(username='batman', email='batman@dc.com', password='password', team=dc),
            User.objects.create_user(username='superman', email='superman@dc.com', password='password', team=dc),
        ]

        # Create Activities
        activities = [
            app_models.Activity.objects.create(user=users[0], type='run', duration=30, distance=5),
            app_models.Activity.objects.create(user=users[1], type='cycle', duration=60, distance=20),
            app_models.Activity.objects.create(user=users[2], type='swim', duration=45, distance=2),
            app_models.Activity.objects.create(user=users[3], type='run', duration=50, distance=10),
        ]

        # Create Workouts
        workouts = [
            app_models.Workout.objects.create(name='Hero HIIT', description='High intensity workout for heroes'),
            app_models.Workout.objects.create(name='Power Lift', description='Strength training for super strength'),
        ]

        # Create Leaderboard
        app_models.Leaderboard.objects.create(team=marvel, points=100)
        app_models.Leaderboard.objects.create(team=dc, points=90)

        self.stdout.write(self.style.SUCCESS('octofit_db database populated with test data.'))
