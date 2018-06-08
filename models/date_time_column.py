# -*- coding: utf-8 -*- 
'''
# Copyright (c) Microsoft Corporation.  All Rights Reserved.  Licensed under the MIT License.  See License in the project root for license information.
# 
#  This file was generated and any changes will be overwritten.
'''

from __future__ import unicode_literals
from ..one_drive_object_base import OneDriveObjectBase


class DateTimeColumn(OneDriveObjectBase):

    def __init__(self, prop_dict={}):
        self._prop_dict = prop_dict

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

    @property
    def format(self):
        """Gets and sets the format
        
        Returns: 
            str:
                The format
        """
        if "format" in self._prop_dict:
            return self._prop_dict["format"]
        else:
            return None

    @format.setter
    def format(self, val):
        self._prop_dict["format"] = val

