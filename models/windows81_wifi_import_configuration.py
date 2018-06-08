# -*- coding: utf-8 -*- 
'''
# Copyright (c) Microsoft Corporation.  All Rights Reserved.  Licensed under the MIT License.  See License in the project root for license information.
# 
#  This file was generated and any changes will be overwritten.
'''

from __future__ import unicode_literals
from ..one_drive_object_base import OneDriveObjectBase


class Windows81WifiImportConfiguration(OneDriveObjectBase):

    def __init__(self, prop_dict={}):
        self._prop_dict = prop_dict

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

    @property
    def profile_name(self):
        """
        Gets and sets the profileName
        
        Returns:
            str:
                The profileName
        """
        if "profileName" in self._prop_dict:
            return self._prop_dict["profileName"]
        else:
            return None

    @profile_name.setter
    def profile_name(self, val):
        self._prop_dict["profileName"] = val

