# -*- coding: utf-8 -*- 
'''
# Copyright (c) Microsoft Corporation.  All Rights Reserved.  Licensed under the MIT License.  See License in the project root for license information.
# 
#  This file was generated and any changes will be overwritten.
'''

from __future__ import unicode_literals
from ..one_drive_object_base import OneDriveObjectBase


class DeviceKey(OneDriveObjectBase):

    def __init__(self, prop_dict={}):
        self._prop_dict = prop_dict

    @property
    def key_type(self):
        """Gets and sets the keyType
        
        Returns: 
            str:
                The keyType
        """
        if "keyType" in self._prop_dict:
            return self._prop_dict["keyType"]
        else:
            return None

    @key_type.setter
    def key_type(self, val):
        self._prop_dict["keyType"] = val

    @property
    def device_id(self):
        """Gets and sets the deviceId
        
        Returns: 
            UUID:
                The deviceId
        """
        if "deviceId" in self._prop_dict:
            return self._prop_dict["deviceId"]
        else:
            return None

    @device_id.setter
    def device_id(self, val):
        self._prop_dict["deviceId"] = val

