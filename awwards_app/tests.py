# Create your tests here.
from django.test import TestCase
from .models import Rate,Profile,Project
from django.contrib.auth.models import User


class RateTest(TestCase):
    def setUp(self):
        self.user = User.objects.create(id=1, username='NgetichNIck')
        self.project = Project.objects.create(id=1, title='Moringa Project', description='Moringa Project description',posted_on='2021,6,19',project_image='https://cloudinary url', repo_link='http://github.com',live_link='http://heroku.com',user=self.user,technologies_used='Python')
        self.rating = Rate.objects.create(id=1, design_wise=5, usability_wise=8, content_wise=6, user=self.user, project=self.project)

    def test_instance(self):
        self.assertTrue(isinstance(self.rating, Rate))

    def test_save_rating(self):
        self.rating.save_rating()
        rating = Rate.objects.all()
        self.assertTrue(len(rating) > 0)

    def test_get_ratings(self, id):
        self.rating.save()
        rating = Rate.get_ratings(post_id=id)
        self.assertTrue(len(rating) == 1)

class TestProfile(TestCase):
    def setUp(self):
        self.user = User(id=1, username='NgetichNick', password='Moringa')
        self.user.save()

    def test_instance(self):
        self.assertTrue(isinstance(self.user, User))

    def test_save_user(self):
        self.user.save()

    def test_delete_user(self):
        self.user.delete()

