# -*- coding: utf-8 -*- 
'''
# Copyright (c) Microsoft Corporation.  All Rights Reserved.  Licensed under the MIT License.  See License in the project root for license information.
# 
#  This file was generated and any changes will be overwritten.
'''

from __future__ import unicode_literals
from ..one_drive_object_base import OneDriveObjectBase


class IosDeviceType(OneDriveObjectBase):

    def __init__(self, prop_dict={}):
        self._prop_dict = prop_dict

    @property
    def i_pad(self):
        """Gets and sets the iPad
        
        Returns: 
            bool:
                The iPad
        """
        if "iPad" in self._prop_dict:
            return self._prop_dict["iPad"]
        else:
            return None

    @i_pad.setter
    def i_pad(self, val):
        self._prop_dict["iPad"] = val

    @property
    def i_phone_and_i_pod(self):
        """Gets and sets the iPhoneAndIPod
        
        Returns: 
            bool:
                The iPhoneAndIPod
        """
        if "iPhoneAndIPod" in self._prop_dict:
            return self._prop_dict["iPhoneAndIPod"]
        else:
            return None

    @i_phone_and_i_pod.setter
    def i_phone_and_i_pod(self, val):
        self._prop_dict["iPhoneAndIPod"] = val

