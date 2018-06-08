# -*- coding: utf-8 -*- 
'''
# Copyright (c) Microsoft Corporation.  All Rights Reserved.  Licensed under the MIT License.  See License in the project root for license information.
# 
#  This file was generated and any changes will be overwritten.
'''

from __future__ import unicode_literals
from ..one_drive_object_base import OneDriveObjectBase


class PersonOrGroupColumn(OneDriveObjectBase):

    def __init__(self, prop_dict={}):
        self._prop_dict = prop_dict

    @property
    def allow_multiple_selection(self):
        """Gets and sets the allowMultipleSelection
        
        Returns: 
            bool:
                The allowMultipleSelection
        """
        if "allowMultipleSelection" in self._prop_dict:
            return self._prop_dict["allowMultipleSelection"]
        else:
            return None

    @allow_multiple_selection.setter
    def allow_multiple_selection(self, val):
        self._prop_dict["allowMultipleSelection"] = val

    @property
    def choose_from_type(self):
        """Gets and sets the chooseFromType
        
        Returns: 
            str:
                The chooseFromType
        """
        if "chooseFromType" in self._prop_dict:
            return self._prop_dict["chooseFromType"]
        else:
            return None

    @choose_from_type.setter
    def choose_from_type(self, val):
        self._prop_dict["chooseFromType"] = val

    @property
    def display_as(self):
        """Gets and sets the displayAs
        
        Returns: 
            str:
                The displayAs
        """
        if "displayAs" in self._prop_dict:
            return self._prop_dict["displayAs"]
        else:
            return None

    @display_as.setter
    def display_as(self, val):
        self._prop_dict["displayAs"] = val

