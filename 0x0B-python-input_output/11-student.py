#!/usr/bin/python3

"""
A class
"""


class Student:
    """
    A student class that json serializes itself
    """

    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """
        Serializes to json
        """
        class_dict = self.__dict__
        self_dict = dict()

        if type(attrs) is list:
            for attr in attrs:
                if type(attr) is not str:
                    return class_dict

                if attr in class_dict:
                    self_dict[attr] = class_dict[attr]

            return self_dict

        return class_dict

    def reload_from_json(self, json):
        for i in json:
            if i in self.__dict__.keys():
                self.__dict__[i] = json[i]
