# -*- coding: utf-8 -*- 
'''
# Copyright (c) Microsoft Corporation.  All Rights Reserved.  Licensed under the MIT License.  See License in the project root for license information.
# 
#  This file was generated and any changes will be overwritten.
'''

from __future__ import unicode_literals
from ..one_drive_object_base import OneDriveObjectBase


class DeviceManagementScriptRunSummary(OneDriveObjectBase):

    def __init__(self, prop_dict={}):
        self._prop_dict = prop_dict

    @property
    def success_device_count(self):
        """
        Gets and sets the successDeviceCount
        
        Returns:
            int:
                The successDeviceCount
        """
        if "successDeviceCount" in self._prop_dict:
            return self._prop_dict["successDeviceCount"]
        else:
            return None

    @success_device_count.setter
    def success_device_count(self, val):
        self._prop_dict["successDeviceCount"] = val

    @property
    def error_device_count(self):
        """
        Gets and sets the errorDeviceCount
        
        Returns:
            int:
                The errorDeviceCount
        """
        if "errorDeviceCount" in self._prop_dict:
            return self._prop_dict["errorDeviceCount"]
        else:
            return None

    @error_device_count.setter
    def error_device_count(self, val):
        self._prop_dict["errorDeviceCount"] = val

    @property
    def success_user_count(self):
        """
        Gets and sets the successUserCount
        
        Returns:
            int:
                The successUserCount
        """
        if "successUserCount" in self._prop_dict:
            return self._prop_dict["successUserCount"]
        else:
            return None

    @success_user_count.setter
    def success_user_count(self, val):
        self._prop_dict["successUserCount"] = val

    @property
    def error_user_count(self):
        """
        Gets and sets the errorUserCount
        
        Returns:
            int:
                The errorUserCount
        """
        if "errorUserCount" in self._prop_dict:
            return self._prop_dict["errorUserCount"]
        else:
            return None

    @error_user_count.setter
    def error_user_count(self, val):
        self._prop_dict["errorUserCount"] = val

