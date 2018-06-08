# -*- coding: utf-8 -*- 
'''
# Copyright (c) Microsoft Corporation.  All Rights Reserved.  Licensed under the MIT License.  See License in the project root for license information.
# 
#  This file was generated and any changes will be overwritten.
'''

from __future__ import unicode_literals
from ..model.mobile_app import MobileApp
from ..model.mobile_app_install_status import MobileAppInstallStatus
from ..one_drive_object_base import OneDriveObjectBase


class UserAppInstallStatus(OneDriveObjectBase):

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
    def user_principal_name(self):
        """
        Gets and sets the userPrincipalName
        
        Returns:
            str:
                The userPrincipalName
        """
        if "userPrincipalName" in self._prop_dict:
            return self._prop_dict["userPrincipalName"]
        else:
            return None

    @user_principal_name.setter
    def user_principal_name(self, val):
        self._prop_dict["userPrincipalName"] = val

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
    def app(self):
        """
        Gets and sets the app
        
        Returns: 
            :class:`MobileApp<onedrivesdk.model.mobile_app.MobileApp>`:
                The app
        """
        if "app" in self._prop_dict:
            if isinstance(self._prop_dict["app"], OneDriveObjectBase):
                return self._prop_dict["app"]
            else :
                self._prop_dict["app"] = MobileApp(self._prop_dict["app"])
                return self._prop_dict["app"]

        return None

    @app.setter
    def app(self, val):
        self._prop_dict["app"] = val

    @property
    def device_statuses(self):
        """Gets and sets the deviceStatuses
        
        Returns: 
            :class:`DeviceStatusesCollectionPage<onedrivesdk.request.device_statuses_collection.DeviceStatusesCollectionPage>`:
                The deviceStatuses
        """
        if "deviceStatuses" in self._prop_dict:
            return DeviceStatusesCollectionPage(self._prop_dict["deviceStatuses"])
        else:
            return None

