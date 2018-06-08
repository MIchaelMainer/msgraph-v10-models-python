# -*- coding: utf-8 -*- 
'''
# Copyright (c) Microsoft Corporation.  All Rights Reserved.  Licensed under the MIT License.  See License in the project root for license information.
# 
#  This file was generated and any changes will be overwritten.
'''

from __future__ import unicode_literals
from ..model.policy_platform_type import PolicyPlatformType
from ..model.restricted_apps_state import RestrictedAppsState
from ..model.managed_device_reported_app import ManagedDeviceReportedApp
from ..one_drive_object_base import OneDriveObjectBase


class RestrictedAppsViolation(OneDriveObjectBase):

    def __init__(self, prop_dict={}):
        self._prop_dict = prop_dict

    @property
    def user_id(self):
        """
        Gets and sets the userId
        
        Returns:
            str:
                The userId
        """
        if "userId" in self._prop_dict:
            return self._prop_dict["userId"]
        else:
            return None

    @user_id.setter
    def user_id(self, val):
        self._prop_dict["userId"] = val

    @property
    def user_name(self):
        """
        Gets and sets the userName
        
        Returns:
            str:
                The userName
        """
        if "userName" in self._prop_dict:
            return self._prop_dict["userName"]
        else:
            return None

    @user_name.setter
    def user_name(self, val):
        self._prop_dict["userName"] = val

    @property
    def managed_device_id(self):
        """
        Gets and sets the managedDeviceId
        
        Returns:
            str:
                The managedDeviceId
        """
        if "managedDeviceId" in self._prop_dict:
            return self._prop_dict["managedDeviceId"]
        else:
            return None

    @managed_device_id.setter
    def managed_device_id(self, val):
        self._prop_dict["managedDeviceId"] = val

    @property
    def device_name(self):
        """
        Gets and sets the deviceName
        
        Returns:
            str:
                The deviceName
        """
        if "deviceName" in self._prop_dict:
            return self._prop_dict["deviceName"]
        else:
            return None

    @device_name.setter
    def device_name(self, val):
        self._prop_dict["deviceName"] = val

    @property
    def device_configuration_id(self):
        """
        Gets and sets the deviceConfigurationId
        
        Returns:
            str:
                The deviceConfigurationId
        """
        if "deviceConfigurationId" in self._prop_dict:
            return self._prop_dict["deviceConfigurationId"]
        else:
            return None

    @device_configuration_id.setter
    def device_configuration_id(self, val):
        self._prop_dict["deviceConfigurationId"] = val

    @property
    def device_configuration_name(self):
        """
        Gets and sets the deviceConfigurationName
        
        Returns:
            str:
                The deviceConfigurationName
        """
        if "deviceConfigurationName" in self._prop_dict:
            return self._prop_dict["deviceConfigurationName"]
        else:
            return None

    @device_configuration_name.setter
    def device_configuration_name(self, val):
        self._prop_dict["deviceConfigurationName"] = val

    @property
    def platform_type(self):
        """
        Gets and sets the platformType
        
        Returns: 
            :class:`PolicyPlatformType<onedrivesdk.model.policy_platform_type.PolicyPlatformType>`:
                The platformType
        """
        if "platformType" in self._prop_dict:
            if isinstance(self._prop_dict["platformType"], OneDriveObjectBase):
                return self._prop_dict["platformType"]
            else :
                self._prop_dict["platformType"] = PolicyPlatformType(self._prop_dict["platformType"])
                return self._prop_dict["platformType"]

        return None

    @platform_type.setter
    def platform_type(self, val):
        self._prop_dict["platformType"] = val

    @property
    def restricted_apps_state(self):
        """
        Gets and sets the restrictedAppsState
        
        Returns: 
            :class:`RestrictedAppsState<onedrivesdk.model.restricted_apps_state.RestrictedAppsState>`:
                The restrictedAppsState
        """
        if "restrictedAppsState" in self._prop_dict:
            if isinstance(self._prop_dict["restrictedAppsState"], OneDriveObjectBase):
                return self._prop_dict["restrictedAppsState"]
            else :
                self._prop_dict["restrictedAppsState"] = RestrictedAppsState(self._prop_dict["restrictedAppsState"])
                return self._prop_dict["restrictedAppsState"]

        return None

    @restricted_apps_state.setter
    def restricted_apps_state(self, val):
        self._prop_dict["restrictedAppsState"] = val

    @property
    def restricted_apps(self):
        """Gets and sets the restrictedApps
        
        Returns: 
            :class:`RestrictedAppsCollectionPage<onedrivesdk.request.restricted_apps_collection.RestrictedAppsCollectionPage>`:
                The restrictedApps
        """
        if "restrictedApps" in self._prop_dict:
            return RestrictedAppsCollectionPage(self._prop_dict["restrictedApps"])
        else:
            return None

