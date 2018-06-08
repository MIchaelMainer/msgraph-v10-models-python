# -*- coding: utf-8 -*- 
'''
# Copyright (c) Microsoft Corporation.  All Rights Reserved.  Licensed under the MIT License.  See License in the project root for license information.
# 
#  This file was generated and any changes will be overwritten.
'''

from __future__ import unicode_literals
from ..one_drive_object_base import OneDriveObjectBase


class OmaSettingBase64(OneDriveObjectBase):

    def __init__(self, prop_dict={}):
        self._prop_dict = prop_dict

    @property
    def file_name(self):
        """Gets and sets the fileName
        
        Returns: 
            str:
                The fileName
        """
        if "fileName" in self._prop_dict:
            return self._prop_dict["fileName"]
        else:
            return None

    @file_name.setter
    def file_name(self, val):
        self._prop_dict["fileName"] = val

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

