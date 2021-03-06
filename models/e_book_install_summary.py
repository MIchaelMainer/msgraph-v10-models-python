# -*- coding: utf-8 -*- 
'''
# Copyright (c) Microsoft Corporation.  All Rights Reserved.  Licensed under the MIT License.  See License in the project root for license information.
# 
#  This file was generated and any changes will be overwritten.
'''

from __future__ import unicode_literals
from ..one_drive_object_base import OneDriveObjectBase


class EBookInstallSummary(OneDriveObjectBase):

    def __init__(self, prop_dict={}):
        self._prop_dict = prop_dict

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
    def installed_user_count(self):
        """
        Gets and sets the installedUserCount
        
        Returns:
            int:
                The installedUserCount
        """
        if "installedUserCount" in self._prop_dict:
            return self._prop_dict["installedUserCount"]
        else:
            return None

    @installed_user_count.setter
    def installed_user_count(self, val):
        self._prop_dict["installedUserCount"] = val

    @property
    def failed_user_count(self):
        """
        Gets and sets the failedUserCount
        
        Returns:
            int:
                The failedUserCount
        """
        if "failedUserCount" in self._prop_dict:
            return self._prop_dict["failedUserCount"]
        else:
            return None

    @failed_user_count.setter
    def failed_user_count(self, val):
        self._prop_dict["failedUserCount"] = val

    @property
    def not_installed_user_count(self):
        """
        Gets and sets the notInstalledUserCount
        
        Returns:
            int:
                The notInstalledUserCount
        """
        if "notInstalledUserCount" in self._prop_dict:
            return self._prop_dict["notInstalledUserCount"]
        else:
            return None

    @not_installed_user_count.setter
    def not_installed_user_count(self, val):
        self._prop_dict["notInstalledUserCount"] = val

