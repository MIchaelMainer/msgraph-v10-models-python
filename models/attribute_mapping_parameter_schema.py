# -*- coding: utf-8 -*- 
'''
# Copyright (c) Microsoft Corporation.  All Rights Reserved.  Licensed under the MIT License.  See License in the project root for license information.
# 
#  This file was generated and any changes will be overwritten.
'''

from __future__ import unicode_literals
from ..model.attribute_type import AttributeType
from ..one_drive_object_base import OneDriveObjectBase


class AttributeMappingParameterSchema(OneDriveObjectBase):

    def __init__(self, prop_dict={}):
        self._prop_dict = prop_dict

    @property
    def allow_multiple_occurrences(self):
        """Gets and sets the allowMultipleOccurrences
        
        Returns: 
            bool:
                The allowMultipleOccurrences
        """
        if "allowMultipleOccurrences" in self._prop_dict:
            return self._prop_dict["allowMultipleOccurrences"]
        else:
            return None

    @allow_multiple_occurrences.setter
    def allow_multiple_occurrences(self, val):
        self._prop_dict["allowMultipleOccurrences"] = val

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
    def required(self):
        """Gets and sets the required
        
        Returns: 
            bool:
                The required
        """
        if "required" in self._prop_dict:
            return self._prop_dict["required"]
        else:
            return None

    @required.setter
    def required(self, val):
        self._prop_dict["required"] = val

    @property
    def type(self):
        """
        Gets and sets the type
        
        Returns: 
            :class:`AttributeType<onedrivesdk.model.attribute_type.AttributeType>`:
                The type
        """
        if "type" in self._prop_dict:
            if isinstance(self._prop_dict["type"], OneDriveObjectBase):
                return self._prop_dict["type"]
            else :
                self._prop_dict["type"] = AttributeType(self._prop_dict["type"])
                return self._prop_dict["type"]

        return None

    @type.setter
    def type(self, val):
        self._prop_dict["type"] = val
