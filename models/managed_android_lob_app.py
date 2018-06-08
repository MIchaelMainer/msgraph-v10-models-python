# -*- coding: utf-8 -*- 
'''
# Copyright (c) Microsoft Corporation.  All Rights Reserved.  Licensed under the MIT License.  See License in the project root for license information.
# 
#  This file was generated and any changes will be overwritten.
'''

from __future__ import unicode_literals
from ..model.android_minimum_operating_system import AndroidMinimumOperatingSystem
from ..one_drive_object_base import OneDriveObjectBase


class ManagedAndroidLobApp(OneDriveObjectBase):

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
    def identity_name(self):
        """
        Gets and sets the identityName
        
        Returns:
            str:
                The identityName
        """
        if "identityName" in self._prop_dict:
            return self._prop_dict["identityName"]
        else:
            return None

    @identity_name.setter
    def identity_name(self, val):
        self._prop_dict["identityName"] = val

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

    @property
    def version_name(self):
        """
        Gets and sets the versionName
        
        Returns:
            str:
                The versionName
        """
        if "versionName" in self._prop_dict:
            return self._prop_dict["versionName"]
        else:
            return None

    @version_name.setter
    def version_name(self, val):
        self._prop_dict["versionName"] = val

    @property
    def version_code(self):
        """
        Gets and sets the versionCode
        
        Returns:
            str:
                The versionCode
        """
        if "versionCode" in self._prop_dict:
            return self._prop_dict["versionCode"]
        else:
            return None

    @version_code.setter
    def version_code(self, val):
        self._prop_dict["versionCode"] = val

    @property
    def identity_version(self):
        """
        Gets and sets the identityVersion
        
        Returns:
            str:
                The identityVersion
        """
        if "identityVersion" in self._prop_dict:
            return self._prop_dict["identityVersion"]
        else:
            return None

    @identity_version.setter
    def identity_version(self, val):
        self._prop_dict["identityVersion"] = val

