# -*- coding: utf-8 -*- 
'''
# Copyright (c) Microsoft Corporation.  All Rights Reserved.  Licensed under the MIT License.  See License in the project root for license information.
# 
#  This file was generated and any changes will be overwritten.
'''

from __future__ import unicode_literals
from ..model.managed_device import ManagedDevice
from ..one_drive_object_base import OneDriveObjectBase


class DetectedApp(OneDriveObjectBase):

    def __init__(self, prop_dict={}):
        self._prop_dict = prop_dict

    @property
    def display_name(self):
        """
        Gets and sets the displayName
        
        Returns:
            str:
                The displayName
        """
        if "displayName" in self._prop_dict:
            return self._prop_dict["displayName"]
        else:
            return None

    @display_name.setter
    def display_name(self, val):
        self._prop_dict["displayName"] = val

    @property
    def version(self):
        """
        Gets and sets the version
        
        Returns:
            str:
                The version
        """
        if "version" in self._prop_dict:
            return self._prop_dict["version"]
        else:
            return None

    @version.setter
    def version(self, val):
        self._prop_dict["version"] = val

    @property
    def size_in_byte(self):
        """
        Gets and sets the sizeInByte
        
        Returns:
            int:
                The sizeInByte
        """
        if "sizeInByte" in self._prop_dict:
            return self._prop_dict["sizeInByte"]
        else:
            return None

    @size_in_byte.setter
    def size_in_byte(self, val):
        self._prop_dict["sizeInByte"] = val

    @property
    def device_count(self):
        """
        Gets and sets the deviceCount
        
        Returns:
            int:
                The deviceCount
        """
        if "deviceCount" in self._prop_dict:
            return self._prop_dict["deviceCount"]
        else:
            return None

    @device_count.setter
    def device_count(self, val):
        self._prop_dict["deviceCount"] = val

    @property
    def managed_devices(self):
        """Gets and sets the managedDevices
        
        Returns: 
            :class:`ManagedDevicesCollectionPage<onedrivesdk.request.managed_devices_collection.ManagedDevicesCollectionPage>`:
                The managedDevices
        """
        if "managedDevices" in self._prop_dict:
            return ManagedDevicesCollectionPage(self._prop_dict["managedDevices"])
        else:
            return None

