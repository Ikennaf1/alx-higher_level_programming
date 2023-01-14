#!/usr/bin/python3

"""
A Python Class
"""

import json
from os import path


class Base:
    """
    A python base class

    Attr:
        __nb_objects: `int`
        id: `int`
    """

    __nb_objects = 0
    id = 0

    def __init__(self, id=None):
        """
        The constructor

        Args:
            id: `int`
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return '[]'

        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """
        Saves json representation to file
        """
        filename = cls.__name__ + '.json'

        with open(filename, mode='w', encoding='utf-8') as f:
            if list_objs is None:
                return f.write(cls.to_json_string(None))

            json_attrs = []

            for elem in list_objs:
                json_attrs.append(elem.to_dictionary())

            return f.write(cls.to_json_string(json_attrs))

    @staticmethod
    def from_json_string(json_string):
        """
        From static string
        """
        if json_string is None or len(json_string) == 0:
            return []

        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """
        Creates
        """
        if cls.__name__ == 'Square':
            new_class = cls(3)

        if cls.__name__ == 'Rectangle':
            new_class = cls(3, 3)

        new_class.update(**dictionary)
        return new_class

    @classmethod
    def load_from_file(cls):
        """
        Loads from file
        """
        filename = cls.__name__ + '.json'

        if path.exists(filename) is False:
            return []

        with open(filename, mode='r', encoding='utf-8') as f:
            objs = cls.from_json_string(f.read())
            instances = []

            for elem in objs:
                instances.append(cls.create(**elem))

            return instances
