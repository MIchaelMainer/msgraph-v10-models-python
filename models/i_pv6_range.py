# -*- coding: utf-8 -*- 
'''
# Copyright (c) Microsoft Corporation.  All Rights Reserved.  Licensed under the MIT License.  See License in the project root for license information.
# 
#  This file was generated and any changes will be overwritten.
'''

from __future__ import unicode_literals
from ..one_drive_object_base import OneDriveObjectBase


class IPv6Range(OneDriveObjectBase):

    def __init__(self, prop_dict={}):
        self._prop_dict = prop_dict

    @property
    def lower_address(self):
        """Gets and sets the lowerAddress
        
        Returns: 
            str:
                The lowerAddress
        """
        if "lowerAddress" in self._prop_dict:
            return self._prop_dict["lowerAddress"]
        else:
            return None

    @lower_address.setter
    def lower_address(self, val):
        self._prop_dict["lowerAddress"] = val

    @property
    def upper_address(self):
        """Gets and sets the upperAddress
        
        Returns: 
            str:
                The upperAddress
        """
        if "upperAddress" in self._prop_dict:
            return self._prop_dict["upperAddress"]
        else:
            return None

    @upper_address.setter
    def upper_address(self, val):
        self._prop_dict["upperAddress"] = val

