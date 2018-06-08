# -*- coding: utf-8 -*- 
'''
# Copyright (c) Microsoft Corporation.  All Rights Reserved.  Licensed under the MIT License.  See License in the project root for license information.
# 
#  This file was generated and any changes will be overwritten.
'''

from __future__ import unicode_literals
from ..model.windows_user_type import WindowsUserType
from ..model.windows_device_usage_type import WindowsDeviceUsageType
from ..one_drive_object_base import OneDriveObjectBase


class OutOfBoxExperienceSettings(OneDriveObjectBase):

    def __init__(self, prop_dict={}):
        self._prop_dict = prop_dict

    @property
    def hide_privacy_settings(self):
        """Gets and sets the hidePrivacySettings
        
        Returns: 
            bool:
                The hidePrivacySettings
        """
        if "hidePrivacySettings" in self._prop_dict:
            return self._prop_dict["hidePrivacySettings"]
        else:
            return None

    @hide_privacy_settings.setter
    def hide_privacy_settings(self, val):
        self._prop_dict["hidePrivacySettings"] = val

    @property
    def hide_eula(self):
        """Gets and sets the hideEULA
        
        Returns: 
            bool:
                The hideEULA
        """
        if "hideEULA" in self._prop_dict:
            return self._prop_dict["hideEULA"]
        else:
            return None

    @hide_eula.setter
    def hide_eula(self, val):
        self._prop_dict["hideEULA"] = val

    @property
    def user_type(self):
        """
        Gets and sets the userType
        
        Returns: 
            :class:`WindowsUserType<onedrivesdk.model.windows_user_type.WindowsUserType>`:
                The userType
        """
        if "userType" in self._prop_dict:
            if isinstance(self._prop_dict["userType"], OneDriveObjectBase):
                return self._prop_dict["userType"]
            else :
                self._prop_dict["userType"] = WindowsUserType(self._prop_dict["userType"])
                return self._prop_dict["userType"]

        return None

    @user_type.setter
    def user_type(self, val):
        self._prop_dict["userType"] = val
    @property
    def device_usage_type(self):
        """
        Gets and sets the deviceUsageType
        
        Returns: 
            :class:`WindowsDeviceUsageType<onedrivesdk.model.windows_device_usage_type.WindowsDeviceUsageType>`:
                The deviceUsageType
        """
        if "deviceUsageType" in self._prop_dict:
            if isinstance(self._prop_dict["deviceUsageType"], OneDriveObjectBase):
                return self._prop_dict["deviceUsageType"]
            else :
                self._prop_dict["deviceUsageType"] = WindowsDeviceUsageType(self._prop_dict["deviceUsageType"])
                return self._prop_dict["deviceUsageType"]

        return None

    @device_usage_type.setter
    def device_usage_type(self, val):
        self._prop_dict["deviceUsageType"] = val
    @property
    def skip_keyboard_selection_page(self):
        """Gets and sets the skipKeyboardSelectionPage
        
        Returns: 
            bool:
                The skipKeyboardSelectionPage
        """
        if "skipKeyboardSelectionPage" in self._prop_dict:
            return self._prop_dict["skipKeyboardSelectionPage"]
        else:
            return None

    @skip_keyboard_selection_page.setter
    def skip_keyboard_selection_page(self, val):
        self._prop_dict["skipKeyboardSelectionPage"] = val

