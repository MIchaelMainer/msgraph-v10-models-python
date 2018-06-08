# -*- coding: utf-8 -*- 
'''
# Copyright (c) Microsoft Corporation.  All Rights Reserved.  Licensed under the MIT License.  See License in the project root for license information.
# 
#  This file was generated and any changes will be overwritten.
'''

from __future__ import unicode_literals
from ..model.device_configuration import DeviceConfiguration
from ..one_drive_object_base import OneDriveObjectBase


class DeviceConfigurationGroupAssignment(OneDriveObjectBase):

    def __init__(self, prop_dict={}):
        self._prop_dict = prop_dict

    @property
    def target_group_id(self):
        """
        Gets and sets the targetGroupId
        
        Returns:
            str:
                The targetGroupId
        """
        if "targetGroupId" in self._prop_dict:
            return self._prop_dict["targetGroupId"]
        else:
            return None

    @target_group_id.setter
    def target_group_id(self, val):
        self._prop_dict["targetGroupId"] = val

    @property
    def exclude_group(self):
        """
        Gets and sets the excludeGroup
        
        Returns:
            bool:
                The excludeGroup
        """
        if "excludeGroup" in self._prop_dict:
            return self._prop_dict["excludeGroup"]
        else:
            return None

    @exclude_group.setter
    def exclude_group(self, val):
        self._prop_dict["excludeGroup"] = val

    @property
    def device_configuration(self):
        """
        Gets and sets the deviceConfiguration
        
        Returns: 
            :class:`DeviceConfiguration<onedrivesdk.model.device_configuration.DeviceConfiguration>`:
                The deviceConfiguration
        """
        if "deviceConfiguration" in self._prop_dict:
            if isinstance(self._prop_dict["deviceConfiguration"], OneDriveObjectBase):
                return self._prop_dict["deviceConfiguration"]
            else :
                self._prop_dict["deviceConfiguration"] = DeviceConfiguration(self._prop_dict["deviceConfiguration"])
                return self._prop_dict["deviceConfiguration"]

        return None

    @device_configuration.setter
    def device_configuration(self, val):
        self._prop_dict["deviceConfiguration"] = val

