# -*- coding: utf-8 -*- 
'''
# Copyright (c) Microsoft Corporation.  All Rights Reserved.  Licensed under the MIT License.  See License in the project root for license information.
# 
#  This file was generated and any changes will be overwritten.
'''

from __future__ import unicode_literals
from ..model.device_management_exchange_access_rule_type import DeviceManagementExchangeAccessRuleType
from ..one_drive_object_base import OneDriveObjectBase


class DeviceManagementExchangeDeviceClass(OneDriveObjectBase):

    def __init__(self, prop_dict={}):
        self._prop_dict = prop_dict

    @property
    def name(self):
        """Gets and sets the name
        
        Returns: 
            str:
                The name
        """
        if "name" in self._prop_dict:
            return self._prop_dict["name"]
        else:
            return None

    @name.setter
    def name(self, val):
        self._prop_dict["name"] = val

    @property
    def type(self):
        """
        Gets and sets the type
        
        Returns: 
            :class:`DeviceManagementExchangeAccessRuleType<onedrivesdk.model.device_management_exchange_access_rule_type.DeviceManagementExchangeAccessRuleType>`:
                The type
        """
        if "type" in self._prop_dict:
            if isinstance(self._prop_dict["type"], OneDriveObjectBase):
                return self._prop_dict["type"]
            else :
                self._prop_dict["type"] = DeviceManagementExchangeAccessRuleType(self._prop_dict["type"])
                return self._prop_dict["type"]

        return None

    @type.setter
    def type(self, val):
        self._prop_dict["type"] = val
