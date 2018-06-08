# -*- coding: utf-8 -*- 
'''
# Copyright (c) Microsoft Corporation.  All Rights Reserved.  Licensed under the MIT License.  See License in the project root for license information.
# 
#  This file was generated and any changes will be overwritten.
'''

from __future__ import unicode_literals
from ..model.object_definition import ObjectDefinition
from ..one_drive_object_base import OneDriveObjectBase


class DirectoryDefinition(OneDriveObjectBase):

    def __init__(self, prop_dict={}):
        self._prop_dict = prop_dict

    @property
    def id(self):
        """Gets and sets the id
        
        Returns: 
            str:
                The id
        """
        if "id" in self._prop_dict:
            return self._prop_dict["id"]
        else:
            return None

    @id.setter
    def id(self, val):
        self._prop_dict["id"] = val

    @property
    def name(self):
        """Gets and sets the name
        
        Returns: 
            str:
                The name
        """
        if "name" in self._prop_dict:
            return self._prop_dict["name"]
        else:
            return None

    @name.setter
    def name(self, val):
        self._prop_dict["name"] = val

    @property
    def objects(self):
        """
        Gets and sets the objects
        
        Returns: 
            :class:`ObjectDefinition<onedrivesdk.model.object_definition.ObjectDefinition>`:
                The objects
        """
        if "objects" in self._prop_dict:
            if isinstance(self._prop_dict["objects"], OneDriveObjectBase):
                return self._prop_dict["objects"]
            else :
                self._prop_dict["objects"] = ObjectDefinition(self._prop_dict["objects"])
                return self._prop_dict["objects"]

        return None

    @objects.setter
    def objects(self, val):
        self._prop_dict["objects"] = val
