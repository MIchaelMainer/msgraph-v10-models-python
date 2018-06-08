# -*- coding: utf-8 -*- 
'''
# Copyright (c) Microsoft Corporation.  All Rights Reserved.  Licensed under the MIT License.  See License in the project root for license information.
# 
#  This file was generated and any changes will be overwritten.
'''

from __future__ import unicode_literals
from ..one_drive_object_base import OneDriveObjectBase


class ConfigurationManagerClientEnabledFeatures(OneDriveObjectBase):

    def __init__(self, prop_dict={}):
        self._prop_dict = prop_dict

    @property
    def inventory(self):
        """Gets and sets the inventory
        
        Returns: 
            bool:
                The inventory
        """
        if "inventory" in self._prop_dict:
            return self._prop_dict["inventory"]
        else:
            return None

    @inventory.setter
    def inventory(self, val):
        self._prop_dict["inventory"] = val

    @property
    def modern_apps(self):
        """Gets and sets the modernApps
        
        Returns: 
            bool:
                The modernApps
        """
        if "modernApps" in self._prop_dict:
            return self._prop_dict["modernApps"]
        else:
            return None

    @modern_apps.setter
    def modern_apps(self, val):
        self._prop_dict["modernApps"] = val

    @property
    def resource_access(self):
        """Gets and sets the resourceAccess
        
        Returns: 
            bool:
                The resourceAccess
        """
        if "resourceAccess" in self._prop_dict:
            return self._prop_dict["resourceAccess"]
        else:
            return None

    @resource_access.setter
    def resource_access(self, val):
        self._prop_dict["resourceAccess"] = val

    @property
    def device_configuration(self):
        """Gets and sets the deviceConfiguration
        
        Returns: 
            bool:
                The deviceConfiguration
        """
        if "deviceConfiguration" in self._prop_dict:
            return self._prop_dict["deviceConfiguration"]
        else:
            return None

    @device_configuration.setter
    def device_configuration(self, val):
        self._prop_dict["deviceConfiguration"] = val

    @property
    def compliance_policy(self):
        """Gets and sets the compliancePolicy
        
        Returns: 
            bool:
                The compliancePolicy
        """
        if "compliancePolicy" in self._prop_dict:
            return self._prop_dict["compliancePolicy"]
        else:
            return None

    @compliance_policy.setter
    def compliance_policy(self, val):
        self._prop_dict["compliancePolicy"] = val

    @property
    def windows_update_for_business(self):
        """Gets and sets the windowsUpdateForBusiness
        
        Returns: 
            bool:
                The windowsUpdateForBusiness
        """
        if "windowsUpdateForBusiness" in self._prop_dict:
            return self._prop_dict["windowsUpdateForBusiness"]
        else:
            return None

    @windows_update_for_business.setter
    def windows_update_for_business(self, val):
        self._prop_dict["windowsUpdateForBusiness"] = val

