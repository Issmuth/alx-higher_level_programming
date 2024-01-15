#!/usr/bin/python3
"""Module of the base class definition."""
import json


class Base:
    """Base class definition."""

    __nb_objects = 0

    def __init__(self, id=None):
        """Class constructor.

        Args:
            id: ...
        """
        if id is None:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
        else:
            self.id = id

    @staticmethod
    def to_json_string(list_dictionaries):
        """returns json string representation of
           a list of dictionaries.

        Args:
            list_dictionaries: list of dictionaries
        Returns:
            json string form of the dictionaries
        """
        if (list_dictionaries is None or
                len(list_dictionaries) == 0):
            return "[]"

        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """Writes JSON string representation of
        a list of object instances.

        Args:
            list_objs: list of objects
            cls: ...
        """
        list_dictionaries = []
        for objs in list_objs:
            list_dictionaries.append(objs.to_dictionary())

        class_name = cls.__name__ + ".json"
        with open(class_name, 'w', encoding="utf-8") as f:
            f.write(cls.to_json_string(list_dictionaries))

    @staticmethod
    def from_json_string(json_string):
        """Returns the list form of a JSON string.

        Args:
            json_string: JSON string

        Returns: list form of the json_string
        """
        if json_string is None or json_string == "[]":
            return []

        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """Returns an instance with all the
        attributes aleady set using the dictionary.

        Args:
            dictionary: a dictionary form of an instance

        Returns: an instance based on the dictionary
        """
        if dictionary and dictionary != {}:
            if cls.__name__ == "Square":
                dummy = cls(1)
            else:
                dummy = cls(1, 1)

            dummy.update(**dictionary)
            return dummy

    @classmethod
    def load_from_file(cls):
        """Returns a list of instance read from
           a JSON string file.

        Returns: list of instances
        """
        filename = cls.__name__ + ".json"
        try:
            with open(filename, 'r', encoding="utf-8") as f:
                json_string = f.read()

            dic_list = cls.from_json_string(json_string)
            instance_list = []
            for dic in dic_list:
                instance_list.append(cls.create(**dic))

            return instance_list
        except FileNotFoundError:
            return []
