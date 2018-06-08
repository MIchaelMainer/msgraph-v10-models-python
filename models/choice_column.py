# -*- coding: utf-8 -*- 
'''
# Copyright (c) Microsoft Corporation.  All Rights Reserved.  Licensed under the MIT License.  See License in the project root for license information.
# 
#  This file was generated and any changes will be overwritten.
'''

from __future__ import unicode_literals
from ..one_drive_object_base import OneDriveObjectBase


class ChoiceColumn(OneDriveObjectBase):

    def __init__(self, prop_dict={}):
        self._prop_dict = prop_dict

    @property
    def allow_text_entry(self):
        """Gets and sets the allowTextEntry
        
        Returns: 
            bool:
                The allowTextEntry
        """
        if "allowTextEntry" in self._prop_dict:
            return self._prop_dict["allowTextEntry"]
        else:
            return None

    @allow_text_entry.setter
    def allow_text_entry(self, val):
        self._prop_dict["allowTextEntry"] = val

    @property
    def choices(self):
        """Gets and sets the choices
        
        Returns: 
            str:
                The choices
        """
        if "choices" in self._prop_dict:
            return self._prop_dict["choices"]
        else:
            return None

    @choices.setter
    def choices(self, val):
        self._prop_dict["choices"] = val

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

