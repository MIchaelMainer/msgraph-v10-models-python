# -*- coding: utf-8 -*- 
'''
# Copyright (c) Microsoft Corporation.  All Rights Reserved.  Licensed under the MIT License.  See License in the project root for license information.
# 
#  This file was generated and any changes will be overwritten.
'''

from __future__ import unicode_literals
from ..one_drive_object_base import OneDriveObjectBase


class WindowsManagementAppHealthSummary(OneDriveObjectBase):

    def __init__(self, prop_dict={}):
        self._prop_dict = prop_dict

    @property
    def healthy_device_count(self):
        """
        Gets and sets the healthyDeviceCount
        
        Returns:
            int:
                The healthyDeviceCount
        """
        if "healthyDeviceCount" in self._prop_dict:
            return self._prop_dict["healthyDeviceCount"]
        else:
            return None

    @healthy_device_count.setter
    def healthy_device_count(self, val):
        self._prop_dict["healthyDeviceCount"] = val

    @property
    def unhealthy_device_count(self):
        """
        Gets and sets the unhealthyDeviceCount
        
        Returns:
            int:
                The unhealthyDeviceCount
        """
        if "unhealthyDeviceCount" in self._prop_dict:
            return self._prop_dict["unhealthyDeviceCount"]
        else:
            return None

    @unhealthy_device_count.setter
    def unhealthy_device_count(self, val):
        self._prop_dict["unhealthyDeviceCount"] = val

    @property
    def unknown_device_count(self):
        """
        Gets and sets the unknownDeviceCount
        
        Returns:
            int:
                The unknownDeviceCount
        """
        if "unknownDeviceCount" in self._prop_dict:
            return self._prop_dict["unknownDeviceCount"]
        else:
            return None

    @unknown_device_count.setter
    def unknown_device_count(self, val):
        self._prop_dict["unknownDeviceCount"] = val

