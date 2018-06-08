# -*- coding: utf-8 -*- 
'''
# Copyright (c) Microsoft Corporation.  All Rights Reserved.  Licensed under the MIT License.  See License in the project root for license information.
# 
#  This file was generated and any changes will be overwritten.
'''

from __future__ import unicode_literals
from ..one_drive_object_base import OneDriveObjectBase


class SizeRange(OneDriveObjectBase):

    def __init__(self, prop_dict={}):
        self._prop_dict = prop_dict

    @property
    def minimum_size(self):
        """Gets and sets the minimumSize
        
        Returns: 
            int:
                The minimumSize
        """
        if "minimumSize" in self._prop_dict:
            return self._prop_dict["minimumSize"]
        else:
            return None

    @minimum_size.setter
    def minimum_size(self, val):
        self._prop_dict["minimumSize"] = val

    @property
    def maximum_size(self):
        """Gets and sets the maximumSize
        
        Returns: 
            int:
                The maximumSize
        """
        if "maximumSize" in self._prop_dict:
            return self._prop_dict["maximumSize"]
        else:
            return None

    @maximum_size.setter
    def maximum_size(self, val):
        self._prop_dict["maximumSize"] = val

