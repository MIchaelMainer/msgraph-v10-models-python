# -*- coding: utf-8 -*- 
'''
# Copyright (c) Microsoft Corporation.  All Rights Reserved.  Licensed under the MIT License.  See License in the project root for license information.
# 
#  This file was generated and any changes will be overwritten.
'''

from __future__ import unicode_literals
from ..model.phone_type import PhoneType
from ..one_drive_object_base import OneDriveObjectBase


class Phone(OneDriveObjectBase):

    def __init__(self, prop_dict={}):
        self._prop_dict = prop_dict

    @property
    def type(self):
        """
        Gets and sets the type
        
        Returns: 
            :class:`PhoneType<onedrivesdk.model.phone_type.PhoneType>`:
                The type
        """
        if "type" in self._prop_dict:
            if isinstance(self._prop_dict["type"], OneDriveObjectBase):
                return self._prop_dict["type"]
            else :
                self._prop_dict["type"] = PhoneType(self._prop_dict["type"])
                return self._prop_dict["type"]

        return None

    @type.setter
    def type(self, val):
        self._prop_dict["type"] = val
    @property
    def number(self):
        """Gets and sets the number
        
        Returns: 
            str:
                The number
        """
        if "number" in self._prop_dict:
            return self._prop_dict["number"]
        else:
            return None

    @number.setter
    def number(self, val):
        self._prop_dict["number"] = val

