# -*- coding: utf-8 -*- 
'''
# Copyright (c) Microsoft Corporation.  All Rights Reserved.  Licensed under the MIT License.  See License in the project root for license information.
# 
#  This file was generated and any changes will be overwritten.
'''

from __future__ import unicode_literals
from ..one_drive_object_base import OneDriveObjectBase


class NumberRange(OneDriveObjectBase):

    def __init__(self, prop_dict={}):
        self._prop_dict = prop_dict

    @property
    def lower_number(self):
        """Gets and sets the lowerNumber
        
        Returns: 
            int:
                The lowerNumber
        """
        if "lowerNumber" in self._prop_dict:
            return self._prop_dict["lowerNumber"]
        else:
            return None

    @lower_number.setter
    def lower_number(self, val):
        self._prop_dict["lowerNumber"] = val

    @property
    def upper_number(self):
        """Gets and sets the upperNumber
        
        Returns: 
            int:
                The upperNumber
        """
        if "upperNumber" in self._prop_dict:
            return self._prop_dict["upperNumber"]
        else:
            return None

    @upper_number.setter
    def upper_number(self, val):
        self._prop_dict["upperNumber"] = val

