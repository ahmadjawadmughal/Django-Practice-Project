from django.urls import reverse, resolve
from crud.views import create_view, update_view, detail_view, retrieve_view, home, delete_view
from django.test import TestCase, Client
from crud.models import Person

class TestViews(TestCase):

    def setUp(self):
        
        self.client = Client()
        self.create_url = reverse("create-view")
        self.update_url = reverse("update-view", args=[1])
        self.delete_url = reverse("delete-view", args=[1])
        self.detail_url = reverse("detail-view", args=[1])
        self.retrieve_url = reverse("retrieve-view")
        self.home_url = reverse("home")


        Person.objects.create(
            name = "MR. Nobody",
            age = "10",
            country = "NO WHERE",
            email = "nothing@mail.com"
        )

    def test_create_view_POST(self):

        response = self.client.post(self.create_url) #test code
        self.assertEqual(response.status_code, 302) #302 because of redirect()
        # self.assertTemplateUsed(response, "crud/forms.html")


    def test_update_view_POST(self):

        response = self.client.post(self.update_url) #test code
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "forms.html")    


    def test_delete_view_POST(self):

        response = self.client.post(self.delete_url) #test code
        self.assertEqual(response.status_code, 302) #302 because of redirect()
        # self.assertTemplateUsed(response, "delete_confirmation.html")    

    
    def test_detail_view_GET(self):

        response = self.client.get(self.detail_url) #test code
        self.assertEqual(response.status_code, 200) 
        self.assertTemplateUsed(response, "detail.html")    

      
    def test_retrieve_view_GET(self):

        response = self.client.get(self.retrieve_url) #test code
        self.assertEqual(response.status_code, 200) 
        self.assertTemplateUsed(response, "retrieve.html")                

    
    def test_home_view_GET(self):

        response = self.client.get(self.home_url) #test code
        self.assertEqual(response.status_code, 200) 
        self.assertTemplateUsed(response, "home.html")        
        