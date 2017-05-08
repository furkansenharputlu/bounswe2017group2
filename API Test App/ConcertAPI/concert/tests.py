# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from concert.models import Concert
from rest_framework.test import APITestCase
from rest_framework import status
from time import sleep
import json


class TestsForConcerts(APITestCase):
    #Populating Database
    def setUp(self):
        Concert.objects.create(artist="Duman", location="BogaziciUniTasoda", date="2017-05-20")
        sleep(1)
        Concert.objects.create(artist="Bulent Ortacgil", location ="BogaziciUniTasoda", date="2017-05-21")
        sleep(1)
                
    #Testcase 1:
    def test_update_concert(self):

        url = '/concert/1/'
        data = {'artist': 'Sebnem Ferah', 'date':'2017-06-20', 'location':'BogaziciUniTasoda'}
        response = self.client.put(url, data, format='json')
        self.assertEqual(json.loads(response.content), {'id': 1, 'artist': 'Sebnem Ferah', 'date':'2017-06-20', 'location':'BogaziciUniTasoda', 'minprice': 0, 'maxprice': 0})

    #Testcase 2:
    def test_get_all_concerts(self):
        url = '/concert/'
        response = self.client.get(url)
        self.assertEqual(json.loads(response.content), [{'id': 1, 'artist': 'Duman', 'location': 'BogaziciUniTasoda', 'date': '2017-05-20', 'minprice': 0, 'maxprice': 0},{'id': 2, 'artist': 'Bulent Ortacgil', 'location': 'BogaziciUniTasoda', 'date': '2017-05-21', 'minprice': 0, 'maxprice': 0}])
    
    #Testcase 3:
    def test_get_concert_via_id(self):
        url = '/concert/1/'
        response = self.client.get(url)
        self.assertEqual(json.loads(response.content), {'id': 1, 'artist': 'Duman', 'location': 'BogaziciUniTasoda', 'date': '2017-05-20', 'minprice': 0, 'maxprice': 0})
 
class TestsForUsers(APITestCase):
    #Populating Database
    def setUp(self):
        User.objects.create(name="Elif Guler", email="elif@gmail.com", password="12345", age="20")
        sleep(1)
        User.objects.create(name="Haluk Alper Karaevli", email="haluk@gmail.com", password="12345", age="22")
        sleep(1)
    
    #Testcase User 1:    
    def test_create_user(self):
        url = '/user/'
        data = {'name': 'Sezen Aksu', 'email':'saksu@gmail.com', 'password':'minikkus', 'age': 52}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(json.loads(response.content), {'id': 3, 'name': 'Sezen Aksu', 'email':'saksu@gmail.com', 'password':'minikkus', 'age':'52'})

if __name__ == '__main__':
    unittest.main()
