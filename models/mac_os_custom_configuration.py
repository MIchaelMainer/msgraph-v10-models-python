# -*- coding: utf-8 -*- 
'''
# Copyright (c) Microsoft Corporation.  All Rights Reserved.  Licensed under the MIT License.  See License in the project root for license information.
# 
#  This file was generated and any changes will be overwritten.
'''

from __future__ import unicode_literals
from ..one_drive_object_base import OneDriveObjectBase


class MacOSCustomConfiguration(OneDriveObjectBase):

    def __init__(self, prop_dict={}):
        self._prop_dict = prop_dict

    @property
    def payload_name(self):
        """
        Gets and sets the payloadName
        
        Returns:
            str:
                The payloadName
        """
        if "payloadName" in self._prop_dict:
            return self._prop_dict["payloadName"]
        else:
            return None

    @payload_name.setter
    def payload_name(self, val):
        self._prop_dict["payloadName"] = val

    @property
    def payload_file_name(self):
        """
        Gets and sets the payloadFileName
        
        Returns:
            str:
                The payloadFileName
        """
        if "payloadFileName" in self._prop_dict:
            return self._prop_dict["payloadFileName"]
        else:
            return None

    @payload_file_name.setter
    def payload_file_name(self, val):
        self._prop_dict["payloadFileName"] = val

