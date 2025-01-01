from django.test import SimpleTestCase
from django.urls import reverse, resolve
from crud.views import create_view, update_view, detail_view, retrieve_view, home, delete_view

class TestUrls(SimpleTestCase):
    
    def test_create_url_is_resolved(self):
        url = reverse("create-view")
        #print(resolve(url))
        self.assertEqual(resolve(url).func, create_view)

   
    def test_update_url_is_resolved(self):  
        url = reverse("update-view", args=[1])
        self.assertEqual(resolve(url).func, update_view)

    def test_retrieve_url_is_resolved(self):  
        url = reverse("retrieve-view")
        self.assertEqual(resolve(url).func, retrieve_view) 

    def test_detail_url_is_resolved(self):  
        url = reverse("detail-view", args=[1])
        self.assertEqual(resolve(url).func, detail_view) 

    def test_delete_url_is_resolved(self):  
        url = reverse("delete-view", args=[1])
        self.assertEqual(resolve(url).func, delete_view) 
    

    def test_home_url_is_resolved(self):  
        url = reverse("home")
        self.assertEqual(resolve(url).func, home) 

                           