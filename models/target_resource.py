# -*- coding: utf-8 -*- 
'''
# Copyright (c) Microsoft Corporation.  All Rights Reserved.  Licensed under the MIT License.  See License in the project root for license information.
# 
#  This file was generated and any changes will be overwritten.
'''

from __future__ import unicode_literals
from ..model.modified_property import ModifiedProperty
from ..one_drive_object_base import OneDriveObjectBase


class TargetResource(OneDriveObjectBase):

    def __init__(self, prop_dict={}):
        self._prop_dict = prop_dict

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
    def modified_properties(self):
        """
        Gets and sets the modifiedProperties
        
        Returns: 
            :class:`ModifiedProperty<onedrivesdk.model.modified_property.ModifiedProperty>`:
                The modifiedProperties
        """
        if "modifiedProperties" in self._prop_dict:
            if isinstance(self._prop_dict["modifiedProperties"], OneDriveObjectBase):
                return self._prop_dict["modifiedProperties"]
            else :
                self._prop_dict["modifiedProperties"] = ModifiedProperty(self._prop_dict["modifiedProperties"])
                return self._prop_dict["modifiedProperties"]

        return None

    @modified_properties.setter
    def modified_properties(self, val):
        self._prop_dict["modifiedProperties"] = val
