# -*- coding: utf-8 -*- 
'''
# Copyright (c) Microsoft Corporation.  All Rights Reserved.  Licensed under the MIT License.  See License in the project root for license information.
# 
#  This file was generated and any changes will be overwritten.
'''

from __future__ import unicode_literals
from ..one_drive_object_base import OneDriveObjectBase


class UnsupportedDeviceConfigurationDetail(OneDriveObjectBase):

    def __init__(self, prop_dict={}):
        self._prop_dict = prop_dict

    @property
    def message(self):
        """Gets and sets the message
        
        Returns: 
            str:
                The message
        """
        if "message" in self._prop_dict:
            return self._prop_dict["message"]
        else:
            return None

    @message.setter
    def message(self, val):
        self._prop_dict["message"] = val

    @property
    def property_name(self):
        """Gets and sets the propertyName
        
        Returns: 
            str:
                The propertyName
        """
        if "propertyName" in self._prop_dict:
            return self._prop_dict["propertyName"]
        else:
            return None

    @property_name.setter
    def property_name(self, val):
        self._prop_dict["propertyName"] = val

