# -*- coding: utf-8 -*- 
'''
# Copyright (c) Microsoft Corporation.  All Rights Reserved.  Licensed under the MIT License.  See License in the project root for license information.
# 
#  This file was generated and any changes will be overwritten.
'''

from __future__ import unicode_literals
from ..model.device_management_exchange_access_level import DeviceManagementExchangeAccessLevel
from ..model.device_management_exchange_access_rule import DeviceManagementExchangeAccessRule
from ..model.device_management_exchange_device_class import DeviceManagementExchangeDeviceClass
from ..model.on_premises_conditional_access_settings import OnPremisesConditionalAccessSettings
from ..one_drive_object_base import OneDriveObjectBase


class DeviceManagementExchangeOnPremisesPolicy(OneDriveObjectBase):

    def __init__(self, prop_dict={}):
        self._prop_dict = prop_dict

    @property
    def default_access_level(self):
        """
        Gets and sets the defaultAccessLevel
        
        Returns: 
            :class:`DeviceManagementExchangeAccessLevel<onedrivesdk.model.device_management_exchange_access_level.DeviceManagementExchangeAccessLevel>`:
                The defaultAccessLevel
        """
        if "defaultAccessLevel" in self._prop_dict:
            if isinstance(self._prop_dict["defaultAccessLevel"], OneDriveObjectBase):
                return self._prop_dict["defaultAccessLevel"]
            else :
                self._prop_dict["defaultAccessLevel"] = DeviceManagementExchangeAccessLevel(self._prop_dict["defaultAccessLevel"])
                return self._prop_dict["defaultAccessLevel"]

        return None

    @default_access_level.setter
    def default_access_level(self, val):
        self._prop_dict["defaultAccessLevel"] = val

    @property
    def access_rules(self):
        """Gets and sets the accessRules
        
        Returns: 
            :class:`AccessRulesCollectionPage<onedrivesdk.request.access_rules_collection.AccessRulesCollectionPage>`:
                The accessRules
        """
        if "accessRules" in self._prop_dict:
            return AccessRulesCollectionPage(self._prop_dict["accessRules"])
        else:
            return None

    @property
    def known_device_classes(self):
        """Gets and sets the knownDeviceClasses
        
        Returns: 
            :class:`KnownDeviceClassesCollectionPage<onedrivesdk.request.known_device_classes_collection.KnownDeviceClassesCollectionPage>`:
                The knownDeviceClasses
        """
        if "knownDeviceClasses" in self._prop_dict:
            return KnownDeviceClassesCollectionPage(self._prop_dict["knownDeviceClasses"])
        else:
            return None

    @property
    def conditional_access_settings(self):
        """
        Gets and sets the conditionalAccessSettings
        
        Returns: 
            :class:`OnPremisesConditionalAccessSettings<onedrivesdk.model.on_premises_conditional_access_settings.OnPremisesConditionalAccessSettings>`:
                The conditionalAccessSettings
        """
        if "conditionalAccessSettings" in self._prop_dict:
            if isinstance(self._prop_dict["conditionalAccessSettings"], OneDriveObjectBase):
                return self._prop_dict["conditionalAccessSettings"]
            else :
                self._prop_dict["conditionalAccessSettings"] = OnPremisesConditionalAccessSettings(self._prop_dict["conditionalAccessSettings"])
                return self._prop_dict["conditionalAccessSettings"]

        return None

    @conditional_access_settings.setter
    def conditional_access_settings(self, val):
        self._prop_dict["conditionalAccessSettings"] = val

