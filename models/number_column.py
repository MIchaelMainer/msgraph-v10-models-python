# -*- coding: utf-8 -*- 
'''
# Copyright (c) Microsoft Corporation.  All Rights Reserved.  Licensed under the MIT License.  See License in the project root for license information.
# 
#  This file was generated and any changes will be overwritten.
'''

from __future__ import unicode_literals
from ..one_drive_object_base import OneDriveObjectBase


class NumberColumn(OneDriveObjectBase):

    def __init__(self, prop_dict={}):
        self._prop_dict = prop_dict

    @property
    def decimal_places(self):
        """Gets and sets the decimalPlaces
        
        Returns: 
            str:
                The decimalPlaces
        """
        if "decimalPlaces" in self._prop_dict:
            return self._prop_dict["decimalPlaces"]
        else:
            return None

    @decimal_places.setter
    def decimal_places(self, val):
        self._prop_dict["decimalPlaces"] = val

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
    def maximum(self):
        """Gets and sets the maximum
        
        Returns: 
            float:
                The maximum
        """
        if "maximum" in self._prop_dict:
            return self._prop_dict["maximum"]
        else:
            return None

    @maximum.setter
    def maximum(self, val):
        self._prop_dict["maximum"] = val

    @property
    def minimum(self):
        """Gets and sets the minimum
        
        Returns: 
            float:
                The minimum
        """
        if "minimum" in self._prop_dict:
            return self._prop_dict["minimum"]
        else:
            return None

    @minimum.setter
    def minimum(self, val):
        self._prop_dict["minimum"] = val

