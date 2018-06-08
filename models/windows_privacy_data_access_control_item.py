# -*- coding: utf-8 -*- 
'''
# Copyright (c) Microsoft Corporation.  All Rights Reserved.  Licensed under the MIT License.  See License in the project root for license information.
# 
#  This file was generated and any changes will be overwritten.
'''

from __future__ import unicode_literals
from ..model.windows_privacy_data_access_level import WindowsPrivacyDataAccessLevel
from ..model.windows_privacy_data_category import WindowsPrivacyDataCategory
from ..one_drive_object_base import OneDriveObjectBase


class WindowsPrivacyDataAccessControlItem(OneDriveObjectBase):

    def __init__(self, prop_dict={}):
        self._prop_dict = prop_dict

    @property
    def access_level(self):
        """
        Gets and sets the accessLevel
        
        Returns: 
            :class:`WindowsPrivacyDataAccessLevel<onedrivesdk.model.windows_privacy_data_access_level.WindowsPrivacyDataAccessLevel>`:
                The accessLevel
        """
        if "accessLevel" in self._prop_dict:
            if isinstance(self._prop_dict["accessLevel"], OneDriveObjectBase):
                return self._prop_dict["accessLevel"]
            else :
                self._prop_dict["accessLevel"] = WindowsPrivacyDataAccessLevel(self._prop_dict["accessLevel"])
                return self._prop_dict["accessLevel"]

        return None

    @access_level.setter
    def access_level(self, val):
        self._prop_dict["accessLevel"] = val

    @property
    def data_category(self):
        """
        Gets and sets the dataCategory
        
        Returns: 
            :class:`WindowsPrivacyDataCategory<onedrivesdk.model.windows_privacy_data_category.WindowsPrivacyDataCategory>`:
                The dataCategory
        """
        if "dataCategory" in self._prop_dict:
            if isinstance(self._prop_dict["dataCategory"], OneDriveObjectBase):
                return self._prop_dict["dataCategory"]
            else :
                self._prop_dict["dataCategory"] = WindowsPrivacyDataCategory(self._prop_dict["dataCategory"])
                return self._prop_dict["dataCategory"]

        return None

    @data_category.setter
    def data_category(self, val):
        self._prop_dict["dataCategory"] = val

    @property
    def app_package_family_name(self):
        """
        Gets and sets the appPackageFamilyName
        
        Returns:
            str:
                The appPackageFamilyName
        """
        if "appPackageFamilyName" in self._prop_dict:
            return self._prop_dict["appPackageFamilyName"]
        else:
            return None

    @app_package_family_name.setter
    def app_package_family_name(self, val):
        self._prop_dict["appPackageFamilyName"] = val

    @property
    def app_display_name(self):
        """
        Gets and sets the appDisplayName
        
        Returns:
            str:
                The appDisplayName
        """
        if "appDisplayName" in self._prop_dict:
            return self._prop_dict["appDisplayName"]
        else:
            return None

    @app_display_name.setter
    def app_display_name(self, val):
        self._prop_dict["appDisplayName"] = val

