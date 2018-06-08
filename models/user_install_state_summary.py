# -*- coding: utf-8 -*- 
'''
# Copyright (c) Microsoft Corporation.  All Rights Reserved.  Licensed under the MIT License.  See License in the project root for license information.
# 
#  This file was generated and any changes will be overwritten.
'''

from __future__ import unicode_literals
from ..model.device_install_state import DeviceInstallState
from ..one_drive_object_base import OneDriveObjectBase


class UserInstallStateSummary(OneDriveObjectBase):

    def __init__(self, prop_dict={}):
        self._prop_dict = prop_dict

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
    def installed_device_count(self):
        """
        Gets and sets the installedDeviceCount
        
        Returns:
            int:
                The installedDeviceCount
        """
        if "installedDeviceCount" in self._prop_dict:
            return self._prop_dict["installedDeviceCount"]
        else:
            return None

    @installed_device_count.setter
    def installed_device_count(self, val):
        self._prop_dict["installedDeviceCount"] = val

    @property
    def failed_device_count(self):
        """
        Gets and sets the failedDeviceCount
        
        Returns:
            int:
                The failedDeviceCount
        """
        if "failedDeviceCount" in self._prop_dict:
            return self._prop_dict["failedDeviceCount"]
        else:
            return None

    @failed_device_count.setter
    def failed_device_count(self, val):
        self._prop_dict["failedDeviceCount"] = val

    @property
    def not_installed_device_count(self):
        """
        Gets and sets the notInstalledDeviceCount
        
        Returns:
            int:
                The notInstalledDeviceCount
        """
        if "notInstalledDeviceCount" in self._prop_dict:
            return self._prop_dict["notInstalledDeviceCount"]
        else:
            return None

    @not_installed_device_count.setter
    def not_installed_device_count(self, val):
        self._prop_dict["notInstalledDeviceCount"] = val

    @property
    def device_states(self):
        """Gets and sets the deviceStates
        
        Returns: 
            :class:`DeviceStatesCollectionPage<onedrivesdk.request.device_states_collection.DeviceStatesCollectionPage>`:
                The deviceStates
        """
        if "deviceStates" in self._prop_dict:
            return DeviceStatesCollectionPage(self._prop_dict["deviceStates"])
        else:
            return None

