# -*- coding: utf-8 -*- 
'''
# Copyright (c) Microsoft Corporation.  All Rights Reserved.  Licensed under the MIT License.  See License in the project root for license information.
# 
#  This file was generated and any changes will be overwritten.
'''

from __future__ import unicode_literals
from ..one_drive_object_base import OneDriveObjectBase


class FilterOperand(OneDriveObjectBase):

    def __init__(self, prop_dict={}):
        self._prop_dict = prop_dict

    @property
    def values(self):
        """Gets and sets the values
        
        Returns: 
            str:
                The values
        """
        if "values" in self._prop_dict:
            return self._prop_dict["values"]
        else:
            return None

    @values.setter
    def values(self, val):
        self._prop_dict["values"] = val

