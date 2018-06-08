# -*- coding: utf-8 -*- 
'''
# Copyright (c) Microsoft Corporation.  All Rights Reserved.  Licensed under the MIT License.  See License in the project root for license information.
# 
#  This file was generated and any changes will be overwritten.
'''

from __future__ import unicode_literals
from ..one_drive_object_base import OneDriveObjectBase


class AppRole(OneDriveObjectBase):

    def __init__(self, prop_dict={}):
        self._prop_dict = prop_dict

    @property
    def allowed_member_types(self):
        """Gets and sets the allowedMemberTypes
        
        Returns: 
            str:
                The allowedMemberTypes
        """
        if "allowedMemberTypes" in self._prop_dict:
            return self._prop_dict["allowedMemberTypes"]
        else:
            return None

    @allowed_member_types.setter
    def allowed_member_types(self, val):
        self._prop_dict["allowedMemberTypes"] = val

    @property
    def description(self):
        """Gets and sets the description
        
        Returns: 
            str:
                The description
        """
        if "description" in self._prop_dict:
            return self._prop_dict["description"]
        else:
            return None

    @description.setter
    def description(self, val):
        self._prop_dict["description"] = val

    @property
    def display_name(self):
        """Gets and sets the displayName
        
        Returns: 
            str:
                The displayName
        """
        if "displayName" in self._prop_dict:
            return self._prop_dict["displayName"]
        else:
            return None

    @display_name.setter
    def display_name(self, val):
        self._prop_dict["displayName"] = val

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
    def is_enabled(self):
        """Gets and sets the isEnabled
        
        Returns: 
            bool:
                The isEnabled
        """
        if "isEnabled" in self._prop_dict:
            return self._prop_dict["isEnabled"]
        else:
            return None

    @is_enabled.setter
    def is_enabled(self, val):
        self._prop_dict["isEnabled"] = val

    @property
    def origin(self):
        """Gets and sets the origin
        
        Returns: 
            str:
                The origin
        """
        if "origin" in self._prop_dict:
            return self._prop_dict["origin"]
        else:
            return None

    @origin.setter
    def origin(self, val):
        self._prop_dict["origin"] = val

    @property
    def value(self):
        """Gets and sets the value
        
        Returns: 
            str:
                The value
        """
        if "value" in self._prop_dict:
            return self._prop_dict["value"]
        else:
            return None

    @value.setter
    def value(self, val):
        self._prop_dict["value"] = val

