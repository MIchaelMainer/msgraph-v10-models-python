# -*- coding: utf-8 -*- 
'''
# Copyright (c) Microsoft Corporation.  All Rights Reserved.  Licensed under the MIT License.  See License in the project root for license information.
# 
#  This file was generated and any changes will be overwritten.
'''

from __future__ import unicode_literals
from ..model.windows_minimum_operating_system import WindowsMinimumOperatingSystem
from ..one_drive_object_base import OneDriveObjectBase


class WindowsPhoneXAP(OneDriveObjectBase):

    def __init__(self, prop_dict={}):
        self._prop_dict = prop_dict

    @property
    def minimum_supported_operating_system(self):
        """
        Gets and sets the minimumSupportedOperatingSystem
        
        Returns: 
            :class:`WindowsMinimumOperatingSystem<onedrivesdk.model.windows_minimum_operating_system.WindowsMinimumOperatingSystem>`:
                The minimumSupportedOperatingSystem
        """
        if "minimumSupportedOperatingSystem" in self._prop_dict:
            if isinstance(self._prop_dict["minimumSupportedOperatingSystem"], OneDriveObjectBase):
                return self._prop_dict["minimumSupportedOperatingSystem"]
            else :
                self._prop_dict["minimumSupportedOperatingSystem"] = WindowsMinimumOperatingSystem(self._prop_dict["minimumSupportedOperatingSystem"])
                return self._prop_dict["minimumSupportedOperatingSystem"]

        return None

    @minimum_supported_operating_system.setter
    def minimum_supported_operating_system(self, val):
        self._prop_dict["minimumSupportedOperatingSystem"] = val

    @property
    def product_identifier(self):
        """
        Gets and sets the productIdentifier
        
        Returns:
            str:
                The productIdentifier
        """
        if "productIdentifier" in self._prop_dict:
            return self._prop_dict["productIdentifier"]
        else:
            return None

    @product_identifier.setter
    def product_identifier(self, val):
        self._prop_dict["productIdentifier"] = val

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

