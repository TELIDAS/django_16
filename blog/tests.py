from django.test import TestCase
from datetime import date
from . import models


class TestModel(TestCase):
    """Case to test models from blog app"""

    def test_create_model_post_success(self):
        payload = {
            "title": "Test Title",
            "description": "Test description",
            "created_date": date.today(),
            "updated_date": date.today(),
            "rating": 5,
        }
        post = models.Post.objects.create(**payload)
        self.assertEqual(post.title, payload['title'])
        self.assertEqual(post.description, payload['description'])
        self.assertEqual(post.rating, payload['rating'])
        self.assertEqual(post.created_date, payload['created_date'])
        self.assertEqual(post.updated_date, payload['updated_date'])

    def test_create_model_post_fail(self):
        payload = {
            "title": 'New Title',
            "description": "description",
            "created_date": date.today(),
            "updated_date": date.today(),
            "rating": "five",
        }
        with self.assertRaises(ValueError):
            post = models.Post.objects.create(**payload)

    def test_update_model_post(self):
        payload = {
            "title": "Test Title",
            "description": "description",
            "created_date": date.today(),
            "updated_date": date.today(),
            "rating": 5,

        }
        new_title = "New title"
        post = models.Post.objects.create(**payload)
        post.title = new_title
        post.save()
        post.refresh_from_db()
        self.assertEqual(post.title, new_title)

    def test_delete_model_post(self):
        payload = {
            "title": "Test Title",
            "description": "description",
            "created_date": date.today(),
            "updated_date": date.today(),
            "rating": 5,

        }
        post = models.Post.objects.create(**payload)
        pk = post.pk
        post.delete()
        with self.assertRaises(models.Post.DoesNotExist):
            models.Post.objects.get(pk=pk)
