# -*- coding: utf-8 -*- 
'''
# Copyright (c) Microsoft Corporation.  All Rights Reserved.  Licensed under the MIT License.  See License in the project root for license information.
# 
#  This file was generated and any changes will be overwritten.
'''

from __future__ import unicode_literals
from ..one_drive_object_base import OneDriveObjectBase


class DefaultColumnValue(OneDriveObjectBase):

    def __init__(self, prop_dict={}):
        self._prop_dict = prop_dict

    @property
    def formula(self):
        """Gets and sets the formula
        
        Returns: 
            str:
                The formula
        """
        if "formula" in self._prop_dict:
            return self._prop_dict["formula"]
        else:
            return None

    @formula.setter
    def formula(self, val):
        self._prop_dict["formula"] = val

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

