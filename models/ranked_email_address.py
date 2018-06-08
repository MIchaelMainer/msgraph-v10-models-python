# -*- coding: utf-8 -*- 
'''
# Copyright (c) Microsoft Corporation.  All Rights Reserved.  Licensed under the MIT License.  See License in the project root for license information.
# 
#  This file was generated and any changes will be overwritten.
'''

from __future__ import unicode_literals
from ..one_drive_object_base import OneDriveObjectBase


class RankedEmailAddress(OneDriveObjectBase):

    def __init__(self, prop_dict={}):
        self._prop_dict = prop_dict

    @property
    def address(self):
        """Gets and sets the address
        
        Returns: 
            str:
                The address
        """
        if "address" in self._prop_dict:
            return self._prop_dict["address"]
        else:
            return None

    @address.setter
    def address(self, val):
        self._prop_dict["address"] = val

    @property
    def rank(self):
        """Gets and sets the rank
        
        Returns: 
            float:
                The rank
        """
        if "rank" in self._prop_dict:
            return self._prop_dict["rank"]
        else:
            return None

    @rank.setter
    def rank(self, val):
        self._prop_dict["rank"] = val

