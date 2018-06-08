# -*- coding: utf-8 -*- 
'''
# Copyright (c) Microsoft Corporation.  All Rights Reserved.  Licensed under the MIT License.  See License in the project root for license information.
# 
#  This file was generated and any changes will be overwritten.
'''

from __future__ import unicode_literals
from ..model.device_management_exchange_device_class import DeviceManagementExchangeDeviceClass
from ..model.device_management_exchange_access_level import DeviceManagementExchangeAccessLevel
from ..one_drive_object_base import OneDriveObjectBase


class DeviceManagementExchangeAccessRule(OneDriveObjectBase):

    def __init__(self, prop_dict={}):
        self._prop_dict = prop_dict

    @property
    def device_class(self):
        """
        Gets and sets the deviceClass
        
        Returns: 
            :class:`DeviceManagementExchangeDeviceClass<onedrivesdk.model.device_management_exchange_device_class.DeviceManagementExchangeDeviceClass>`:
                The deviceClass
        """
        if "deviceClass" in self._prop_dict:
            if isinstance(self._prop_dict["deviceClass"], OneDriveObjectBase):
                return self._prop_dict["deviceClass"]
            else :
                self._prop_dict["deviceClass"] = DeviceManagementExchangeDeviceClass(self._prop_dict["deviceClass"])
                return self._prop_dict["deviceClass"]

        return None

    @device_class.setter
    def device_class(self, val):
        self._prop_dict["deviceClass"] = val
    @property
    def access_level(self):
        """
        Gets and sets the accessLevel
        
        Returns: 
            :class:`DeviceManagementExchangeAccessLevel<onedrivesdk.model.device_management_exchange_access_level.DeviceManagementExchangeAccessLevel>`:
                The accessLevel
        """
        if "accessLevel" in self._prop_dict:
            if isinstance(self._prop_dict["accessLevel"], OneDriveObjectBase):
                return self._prop_dict["accessLevel"]
            else :
                self._prop_dict["accessLevel"] = DeviceManagementExchangeAccessLevel(self._prop_dict["accessLevel"])
                return self._prop_dict["accessLevel"]

        return None

    @access_level.setter
    def access_level(self, val):
        self._prop_dict["accessLevel"] = val
