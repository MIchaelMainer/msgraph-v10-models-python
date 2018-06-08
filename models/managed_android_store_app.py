# -*- coding: utf-8 -*- 
'''
# Copyright (c) Microsoft Corporation.  All Rights Reserved.  Licensed under the MIT License.  See License in the project root for license information.
# 
#  This file was generated and any changes will be overwritten.
'''

from __future__ import unicode_literals
from ..model.android_minimum_operating_system import AndroidMinimumOperatingSystem
from ..one_drive_object_base import OneDriveObjectBase


class ManagedAndroidStoreApp(OneDriveObjectBase):

    def __init__(self, prop_dict={}):
        self._prop_dict = prop_dict

    @property
    def package_id(self):
        """
        Gets and sets the packageId
        
        Returns:
            str:
                The packageId
        """
        if "packageId" in self._prop_dict:
            return self._prop_dict["packageId"]
        else:
            return None

    @package_id.setter
    def package_id(self, val):
        self._prop_dict["packageId"] = val

    @property
    def app_store_url(self):
        """
        Gets and sets the appStoreUrl
        
        Returns:
            str:
                The appStoreUrl
        """
        if "appStoreUrl" in self._prop_dict:
            return self._prop_dict["appStoreUrl"]
        else:
            return None

    @app_store_url.setter
    def app_store_url(self, val):
        self._prop_dict["appStoreUrl"] = val

    @property
    def minimum_supported_operating_system(self):
        """
        Gets and sets the minimumSupportedOperatingSystem
        
        Returns: 
            :class:`AndroidMinimumOperatingSystem<onedrivesdk.model.android_minimum_operating_system.AndroidMinimumOperatingSystem>`:
                The minimumSupportedOperatingSystem
        """
        if "minimumSupportedOperatingSystem" in self._prop_dict:
            if isinstance(self._prop_dict["minimumSupportedOperatingSystem"], OneDriveObjectBase):
                return self._prop_dict["minimumSupportedOperatingSystem"]
            else :
                self._prop_dict["minimumSupportedOperatingSystem"] = AndroidMinimumOperatingSystem(self._prop_dict["minimumSupportedOperatingSystem"])
                return self._prop_dict["minimumSupportedOperatingSystem"]

        return None

    @minimum_supported_operating_system.setter
    def minimum_supported_operating_system(self, val):
        self._prop_dict["minimumSupportedOperatingSystem"] = val

