# -*- coding: utf-8 -*- 
'''
# Copyright (c) Microsoft Corporation.  All Rights Reserved.  Licensed under the MIT License.  See License in the project root for license information.
# 
#  This file was generated and any changes will be overwritten.
'''

from __future__ import unicode_literals
from ..one_drive_object_base import OneDriveObjectBase


class DeviceExchangeAccessStateSummary(OneDriveObjectBase):

    def __init__(self, prop_dict={}):
        self._prop_dict = prop_dict

    @property
    def allowed_device_count(self):
        """Gets and sets the allowedDeviceCount
        
        Returns: 
            int:
                The allowedDeviceCount
        """
        if "allowedDeviceCount" in self._prop_dict:
            return self._prop_dict["allowedDeviceCount"]
        else:
            return None

    @allowed_device_count.setter
    def allowed_device_count(self, val):
        self._prop_dict["allowedDeviceCount"] = val

    @property
    def blocked_device_count(self):
        """Gets and sets the blockedDeviceCount
        
        Returns: 
            int:
                The blockedDeviceCount
        """
        if "blockedDeviceCount" in self._prop_dict:
            return self._prop_dict["blockedDeviceCount"]
        else:
            return None

    @blocked_device_count.setter
    def blocked_device_count(self, val):
        self._prop_dict["blockedDeviceCount"] = val

    @property
    def quarantined_device_count(self):
        """Gets and sets the quarantinedDeviceCount
        
        Returns: 
            int:
                The quarantinedDeviceCount
        """
        if "quarantinedDeviceCount" in self._prop_dict:
            return self._prop_dict["quarantinedDeviceCount"]
        else:
            return None

    @quarantined_device_count.setter
    def quarantined_device_count(self, val):
        self._prop_dict["quarantinedDeviceCount"] = val

    @property
    def unknown_device_count(self):
        """Gets and sets the unknownDeviceCount
        
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

    @property
    def unavailable_device_count(self):
        """Gets and sets the unavailableDeviceCount
        
        Returns: 
            int:
                The unavailableDeviceCount
        """
        if "unavailableDeviceCount" in self._prop_dict:
            return self._prop_dict["unavailableDeviceCount"]
        else:
            return None

    @unavailable_device_count.setter
    def unavailable_device_count(self, val):
        self._prop_dict["unavailableDeviceCount"] = val

