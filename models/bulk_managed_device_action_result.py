# -*- coding: utf-8 -*- 
'''
# Copyright (c) Microsoft Corporation.  All Rights Reserved.  Licensed under the MIT License.  See License in the project root for license information.
# 
#  This file was generated and any changes will be overwritten.
'''

from __future__ import unicode_literals
from ..one_drive_object_base import OneDriveObjectBase


class BulkManagedDeviceActionResult(OneDriveObjectBase):

    def __init__(self, prop_dict={}):
        self._prop_dict = prop_dict

    @property
    def successful_device_ids(self):
        """Gets and sets the successfulDeviceIds
        
        Returns: 
            str:
                The successfulDeviceIds
        """
        if "successfulDeviceIds" in self._prop_dict:
            return self._prop_dict["successfulDeviceIds"]
        else:
            return None

    @successful_device_ids.setter
    def successful_device_ids(self, val):
        self._prop_dict["successfulDeviceIds"] = val

    @property
    def failed_device_ids(self):
        """Gets and sets the failedDeviceIds
        
        Returns: 
            str:
                The failedDeviceIds
        """
        if "failedDeviceIds" in self._prop_dict:
            return self._prop_dict["failedDeviceIds"]
        else:
            return None

    @failed_device_ids.setter
    def failed_device_ids(self, val):
        self._prop_dict["failedDeviceIds"] = val

    @property
    def not_found_device_ids(self):
        """Gets and sets the notFoundDeviceIds
        
        Returns: 
            str:
                The notFoundDeviceIds
        """
        if "notFoundDeviceIds" in self._prop_dict:
            return self._prop_dict["notFoundDeviceIds"]
        else:
            return None

    @not_found_device_ids.setter
    def not_found_device_ids(self, val):
        self._prop_dict["notFoundDeviceIds"] = val

    @property
    def not_supported_device_ids(self):
        """Gets and sets the notSupportedDeviceIds
        
        Returns: 
            str:
                The notSupportedDeviceIds
        """
        if "notSupportedDeviceIds" in self._prop_dict:
            return self._prop_dict["notSupportedDeviceIds"]
        else:
            return None

    @not_supported_device_ids.setter
    def not_supported_device_ids(self, val):
        self._prop_dict["notSupportedDeviceIds"] = val

