from django.contrib.auth import get_user_model
from django.http import response
from django.test import TestCase
from django.urls import reverse

from .models import Post


# Create your tests here.
class BlogTests(TestCase):
    def setUp(self):
        self.user = get_user_model().objects.create_user(
            username = 'testuser',
            email = 'test@gmail.com',
            password = 'secret'
        )
        self.post = Post.objects.create(
            title="This is test title", 
            author=self.user, 
            ebody="THis is body"
            )
    
    def test_string_representation(self):
        post = Post(title="A sample title")
        self.assertEqual(str(post), post.title)
    
    def test_post_content(self):
        self.assertEqual(f"{self.post.title}", "This is test title")
        self.assertEqual(f"{self.post.author}", "testuser")
        self.assertEqual(f"{self.post.ebody}", "THis is body")
    
    def test_post_list_view(self):
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'home.html')
        self.assertContains(response, "THis is body")
    
    def test_post_detail_view(self):
        response = self.client.get('/post/1/')
        not_response = self.client.get('/post/10000/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(not_response.status_code, 404)
        self.assertTemplateUsed(response, 'post_details.html')
        self.assertContains(response, "This is test title")
    
