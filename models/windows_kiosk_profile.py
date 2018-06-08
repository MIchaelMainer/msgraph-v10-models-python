# -*- coding: utf-8 -*- 
'''
# Copyright (c) Microsoft Corporation.  All Rights Reserved.  Licensed under the MIT License.  See License in the project root for license information.
# 
#  This file was generated and any changes will be overwritten.
'''

from __future__ import unicode_literals
from ..model.windows_kiosk_app_configuration import WindowsKioskAppConfiguration
from ..model.windows_kiosk_user import WindowsKioskUser
from ..one_drive_object_base import OneDriveObjectBase


class WindowsKioskProfile(OneDriveObjectBase):

    def __init__(self, prop_dict={}):
        self._prop_dict = prop_dict

    @property
    def profile_id(self):
        """Gets and sets the profileId
        
        Returns: 
            str:
                The profileId
        """
        if "profileId" in self._prop_dict:
            return self._prop_dict["profileId"]
        else:
            return None

    @profile_id.setter
    def profile_id(self, val):
        self._prop_dict["profileId"] = val

    @property
    def profile_name(self):
        """Gets and sets the profileName
        
        Returns: 
            str:
                The profileName
        """
        if "profileName" in self._prop_dict:
            return self._prop_dict["profileName"]
        else:
            return None

    @profile_name.setter
    def profile_name(self, val):
        self._prop_dict["profileName"] = val

    @property
    def app_configuration(self):
        """
        Gets and sets the appConfiguration
        
        Returns: 
            :class:`WindowsKioskAppConfiguration<onedrivesdk.model.windows_kiosk_app_configuration.WindowsKioskAppConfiguration>`:
                The appConfiguration
        """
        if "appConfiguration" in self._prop_dict:
            if isinstance(self._prop_dict["appConfiguration"], OneDriveObjectBase):
                return self._prop_dict["appConfiguration"]
            else :
                self._prop_dict["appConfiguration"] = WindowsKioskAppConfiguration(self._prop_dict["appConfiguration"])
                return self._prop_dict["appConfiguration"]

        return None

    @app_configuration.setter
    def app_configuration(self, val):
        self._prop_dict["appConfiguration"] = val
    @property
    def user_accounts_configuration(self):
        """
        Gets and sets the userAccountsConfiguration
        
        Returns: 
            :class:`WindowsKioskUser<onedrivesdk.model.windows_kiosk_user.WindowsKioskUser>`:
                The userAccountsConfiguration
        """
        if "userAccountsConfiguration" in self._prop_dict:
            if isinstance(self._prop_dict["userAccountsConfiguration"], OneDriveObjectBase):
                return self._prop_dict["userAccountsConfiguration"]
            else :
                self._prop_dict["userAccountsConfiguration"] = WindowsKioskUser(self._prop_dict["userAccountsConfiguration"])
                return self._prop_dict["userAccountsConfiguration"]

        return None

    @user_accounts_configuration.setter
    def user_accounts_configuration(self, val):
        self._prop_dict["userAccountsConfiguration"] = val
