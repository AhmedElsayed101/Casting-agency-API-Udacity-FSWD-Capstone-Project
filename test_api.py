import os
import unittest
import json
from flask_sqlalchemy import SQLAlchemy

from api.init import app
from database.models import Actor, Movie, db
from api.basicRoutes import *
from api.apiRoutes import *
from api.errorHandelers import *

assistant_token = os.getenv('ASSISTANT_TOKEN')
director_token = os.getenv('DIRECTOR_TOKEN')
producer_token = os.getenv('PRODUCER_TOKEN')


def set_auth_header(role):
    if role == 'assistant':
        return {'Authorization': f'Bearer {assistant_token}'}
    elif role == 'director':
        return {'Authorization': f'Bearer {director_token}'}
    elif role == 'producer':
        return {'Authorization': f'Bearer {producer_token}'}


class AgencyTestCase(unittest.TestCase):

    def setUp(self):
        """Define test variables and initialize app."""
        self.app = app
        self.client = self.app.test_client
        self.database_name = "capstone_test"
        self.database = f"postgresql://mohsen:123456@localhost/"
        self.database_path = self.database + self.database_name
        # setup_db(self.app, self.database_path)

        # binds the app to the current context

        with self.app.app_context():
            self.app.config["SQLALCHEMY_DATABASE_URI"] = self.database_path
            self.app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
            self.db = db
            self.db.app = self.app
            # self.db.init_app(self.app)
            # create all tables
            self.db.drop_all()
            self.db.create_all()

        with self.app.app_context():
            for i in range(10):
                new_actor = Actor(
                    name='ahmed',
                    age=30,
                    gender='male'
                )
                new_movie = Movie(
                    title='new movie',
                    start_time='2015-5-6'
                )
                new_actor.insert()
                new_movie.insert()

    new_actor = {
        "name": "eample",
        "age": 123,
        "gender": "male"
    }
    bad_new_actor = {
        "name": "eample",
        "age": 123,
    }
    new_movie = {
        "title": "eample",
        "start_time": "2015-5-5"
    }
    bad_new_movie = {
        "title": "eample",
    }

    def tearDown(self):
        """Executed after reach test"""
        pass

    def test_get_movies(self):
        res = self.client().get(
            '/api/movies',
            headers=set_auth_header('assistant'))
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertTrue(len(data['movies']))

    def test_get_one_movie(self):
        res = self.client().get(
            '/api/movies/1',
            headers=set_auth_header('assistant'))
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertTrue(data['movie'])

    def test_404_get_one_movie(self):
        res = self.client().get(
            '/api/movies/1000',
            headers=set_auth_header('assistant'))
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 404)
        self.assertEqual(data['success'], False)
    ####################

    def test_create_new_movie(self):
        res = self.client().post(
            '/api/movies',
            headers=set_auth_header('producer'),
            json=self.new_movie)
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)

    def test_400_create_new_movie(self):
        res = self.client().post('/api/movies',
                                 headers=set_auth_header('producer'),
                                 json=self.bad_new_movie)
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 400)
        self.assertEqual(data['success'], False)
    ######################

    def test_delete_movie(self):
        res = self.client().delete('api/movies/10',
                                   headers=set_auth_header('producer'))
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertEqual(data['deleted'], 10)

    def test_404_delete_movie(self):
        res = self.client().delete('api/movies/1000',
                                   headers=set_auth_header('producer'))
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 404)
        self.assertEqual(data['success'], False)
    #######################

    def test_edit_new_movie(self):
        res = self.client().patch('/api/movies/5',
                                  headers=set_auth_header('producer'),
                                  json=self.new_movie)
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)

    def test_404_edit_new_movie(self):
        res = self.client().patch('/api/movies/1000',
                                  headers=set_auth_header('producer'),
                                  json=self.bad_new_movie)
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 404)
        self.assertEqual(data['success'], False)

    #########################################

    def test_get_actors(self):
        res = self.client().get('/api/actors',
                                headers=set_auth_header('assistant'))
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertTrue(len(data['actors']))

    def test_get_one_actor(self):
        res = self.client().get('/api/actors/1',
                                headers=set_auth_header('assistant'))
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertTrue(data['actor'])

    def test_404_get_one_actor(self):
        res = self.client().get('/api/actors/1000',
                                headers=set_auth_header('assistant'))
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 404)
        self.assertEqual(data['success'], False)
    ####################

    def test_create_new_actor(self):
        res = self.client().post('/api/actors',
                                 headers=set_auth_header('producer'),
                                 json=self.new_actor)
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)

    def test_400_create_new_actor(self):
        res = self.client().post('/api/actors',
                                 headers=set_auth_header('producer'),
                                 json=self.bad_new_actor)
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 400)
        self.assertEqual(data['success'], False)
    ######################

    def test_delete_actor(self):
        res = self.client().delete('api/actors/10',
                                   headers=set_auth_header('producer'))
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertEqual(data['deleted'], 10)

    def test_404_delete_actor(self):
        res = self.client().delete('api/actors/1000',
                                   headers=set_auth_header('producer'))
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 404)
        self.assertEqual(data['success'], False)
    #######################

    def test_edit_new_actor(self):
        res = self.client().patch('/api/actors/5',
                                  headers=set_auth_header('producer'),
                                  json=self.new_actor)
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)

    def test_404_edit_new_actor(self):
        res = self.client().patch('/api/actors/1000',
                                  headers=set_auth_header('producer'),
                                  json=self.bad_new_actor)
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 404)
        self.assertEqual(data['success'], False)

    ##################################

    def test_assistant_pass(self):
        res = self.client().get('/api/movies',
                                headers=set_auth_header('assistant'))
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertTrue(len(data['movies']))

    def test_assistant_fail(self):
        res = self.client().post('/api/movies',
                                 headers=set_auth_header('assistant'),
                                 json=self.bad_new_movie)
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 401)
        self.assertEqual(data['success'], False)
    ######################

    def test_director_pass(self):
        res = self.client().get('/api/movies',
                                headers=set_auth_header('director'))
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertTrue(len(data['movies']))

    def test_director_fail(self):
        res = self.client().post('/api/movies',
                                 headers=set_auth_header('director'),
                                 json=self.bad_new_movie)
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 401)
        self.assertEqual(data['success'], False)
    #####################

    def test_producer_pass(self):
        res = self.client().post('/api/movies',
                                 headers=set_auth_header('producer'),
                                 json=self.bad_new_movie)
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 400)
        self.assertEqual(data['success'], False)

    # def test_producer_fail(self):
    #     pass


if __name__ == "__main__":
    unittest.main()
