# -*- coding: utf-8 -*- 
'''
# Copyright (c) Microsoft Corporation.  All Rights Reserved.  Licensed under the MIT License.  See License in the project root for license information.
# 
#  This file was generated and any changes will be overwritten.
'''

from __future__ import unicode_literals
from ..model.key_value import KeyValue
from ..one_drive_object_base import OneDriveObjectBase


class AddIn(OneDriveObjectBase):

    def __init__(self, prop_dict={}):
        self._prop_dict = prop_dict

    @property
    def id(self):
        """Gets and sets the id
        
        Returns: 
            UUID:
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
    def type(self):
        """Gets and sets the type
        
        Returns: 
            str:
                The type
        """
        if "type" in self._prop_dict:
            return self._prop_dict["type"]
        else:
            return None

    @type.setter
    def type(self, val):
        self._prop_dict["type"] = val

    @property
    def properties(self):
        """
        Gets and sets the properties
        
        Returns: 
            :class:`KeyValue<onedrivesdk.model.key_value.KeyValue>`:
                The properties
        """
        if "properties" in self._prop_dict:
            if isinstance(self._prop_dict["properties"], OneDriveObjectBase):
                return self._prop_dict["properties"]
            else :
                self._prop_dict["properties"] = KeyValue(self._prop_dict["properties"])
                return self._prop_dict["properties"]

        return None

    @properties.setter
    def properties(self, val):
        self._prop_dict["properties"] = val
