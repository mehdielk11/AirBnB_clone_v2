#!/usr/bin/python3
'''
    Testing the file_storage module.
'''

import os
import time
import json
import unittest
from models.base_model import BaseModel
from models.state import State
from models.engine.file_storage import FileStorage
import models


class testFileStorage(unittest.TestCase):
    '''
        Testing the FileStorage class
    '''

    def setUp(self):
        '''
            Initializing classes
        '''
        os.environ['HBNB_TYPE_STORAGE'] = 'file'
        self.storage = FileStorage()
        self.my_model = BaseModel()

    def tearDown(self):
        '''
            Cleaning up.
        '''

        try:
            os.remove("file.json")
        except FileNotFoundError:
            pass

    def test_FileStorage_all_return_type(self):
        '''
            Tests the data type of the return value of the all method.
        '''
        storage_all = self.storage.all()
        self.assertIsInstance(storage_all, dict)

    def test_FileStorage_all_class_specific(self):
        '''
            Test all method with a class specified
        '''
        new_city = models.City()
        new_state = models.State()
        state_key = str(new_state.__class__.__name__) + "." + str(new_state.id)
        city_key = str(new_city.__class__.__name__) + "." + str(new_city.id)
        self.storage.new(new_city)
        self.storage.new(new_state)
        tmp = self.storage.all(models.City)
        state = tmp.get(state_key, None)
        city = tmp.get(city_key, None)
        self.assertTrue(city is not None, msg="\n{}\n{}".format(tmp, city))
        self.assertTrue(state is None)

    def test_FileStorage_new_method(self):
        '''
            Tests that the new method sets the right key and value pair
            in the FileStorage.__object attribute
        '''
        self.storage.new(self.my_model)
        key = str(self.my_model.__class__.__name__) + "." + self.my_model.id
        self.assertTrue(key in self.storage._FileStorage__objects)

    def test_FileStorage_objects_value_type(self):
        '''
            Tests that the type of value contained in the FileStorage.__object
            is of type obj.__class__.__name__
        '''
        self.storage.new(self.my_model)
        key = str(self.my_model.__class__.__name__) + "." + self.my_model.id
        val = self.storage._FileStorage__objects[key]
        self.assertIsInstance(self.my_model, type(val))

    def test_FileStorage_save_file_exists(self):
        '''
            Tests that a file gets created with the name file.json
        '''
        self.storage.save()
        self.assertTrue(os.path.isfile("file.json"))

    def test_FileStorage_save_file_read(self):
        '''
            Testing the contents of the files inside the file.json
        '''
        self.storage.save()
        self.storage.new(self.my_model)

        with open("file.json", encoding="UTF8") as fd:
            content = json.load(fd)

        self.assertTrue(type(content) is dict)

    def test_FileStorage_the_type_file_content(self):
        '''
            testing the type of the contents inside the file.
        '''
        self.storage.save()
        self.storage.new(self.my_model)

        with open("file.json", encoding="UTF8") as fd:
            content = fd.read()

        self.assertIsInstance(content, str)

    def test_FileStorage_reaload_without_file(self):
        '''
            Tests that nothing happens when file.json does not exists
            and reload is called
        '''

        try:
            self.storage.reload()
            self.assertTrue(True)
        except:
            self.assertTrue(False)

    def test_FileStorage_delete(self):
        '''
            Tests delete function works
        '''
        new_state = State()
        key = str(new_state.__class__.__name__ + "." + new_state.id)
        self.storage.new(new_state)
        self.assertTrue(key in self.storage._FileStorage__objects, msg="Object wasn't saved to storage")
        self.storage.save()
        self.storage.delete(new_state)
        self.storage.save()
        self.assertTrue(key not in self.storage._FileStorage__objects, msg="Object wasn't deleted from storage")

    def test_FileStorage_delete_not_in(self):
        '''
            Tests delete works for key not in storage
        '''
        new_state = State()
        key = str(new_state.__class__.__name__ + "." + new_state.id)
        self.storage.delete(new_state)
        self.assertTrue(key not in self.storage._FileStorage__objects)

    def test_FileStorage_delete_None(self):
        '''
            Tests delete function works for None - no change to __objects
        '''
        old_storage = self.storage._FileStorage__objects
        self.storage.delete(None)
        self.assertTrue(old_storage == self.storage._FileStorage__objects)
