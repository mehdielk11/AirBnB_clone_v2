#!/usr/bin/env python3
'''
    Test module for db_storage module
'''

import models
import os
import unittest
from models.engine.db_storage import DBStorage
from unittest.mock import patch


class testDBStorage(unittest.TestCase):
    '''
        unittest class for testing DBStorage module
    '''

    def setUp(self):
        '''
            Sets up the environment for testing DBStorage
        '''
        os.environ['HBNB_TYPE_STORAGE'] = 'db'
        os.environ['HBNB_MYSQL_USER'] = 'hbnb_test'
        os.environ['HBNB_MYSQL_PWD'] = 'hbnb_test_pwd'
        os.environ['HBNB_MYSQL_HOST'] = 'localhost'
        os.environ['HBNB_MYSQL_DB'] = 'hbnb_test_db'
        self.storage = DBStorage()
        self.my_model = models.BaseModel()
        self.storage.reload()

    def test_DBStorage_type_storage_environ(self):
        '''
            Test if environment is updating
        '''
        self.assertEqual(os.getenv('HBNB_TYPE_STORAGE'), 'db')

    def test_DBStorage_all_method(self):
        '''
            Test all method
        '''
        new_dict = self.storage.all()
        self.assertTrue(type(new_dict) == type(dict()))

    def test_DBStorage_new_method(self):
        '''
            Test new method
        '''
        new_state = models.State()
        self.storage.new(new_state)
        self.assertTrue(new_state in self.storage._DBStorage__session)

    def test_DBStorage_reload_method(self):
        '''
            Test reload method
        '''
        test = self.storage._DBStorage__engine.execute("show databases;")
        test = [x for x in test]
        new = False
        for x in test:
            if os.getenv('HBNB_MYSQL_DB') in x[0]:
                new = True
        self.assertTrue(new,)

    def test_DBStorage_delete_method(self):
        '''
            Test delete method
        '''

    def test_DBStorage_delete_parent_deletes_children(self):
        '''
            Test if deleting a parent deletes the children as well
        '''

    def test_DBStorage_save_method(self):
        '''
            Test save method
        '''

    def test_DBStorage_in_correct_DB(self):
        '''
            Test if going to correct database
        '''

    def test_DBStorage_drop_all(self):
        '''
            Test if HBNB_ENV == test drop all tables
        '''
