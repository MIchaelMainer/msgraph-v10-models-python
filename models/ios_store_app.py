# -*- coding: utf-8 -*- 
'''
# Copyright (c) Microsoft Corporation.  All Rights Reserved.  Licensed under the MIT License.  See License in the project root for license information.
# 
#  This file was generated and any changes will be overwritten.
'''

from __future__ import unicode_literals
from ..model.ios_device_type import IosDeviceType
from ..model.ios_minimum_operating_system import IosMinimumOperatingSystem
from ..one_drive_object_base import OneDriveObjectBase


class IosStoreApp(OneDriveObjectBase):

    def __init__(self, prop_dict={}):
        self._prop_dict = prop_dict

    @property
    def bundle_id(self):
        """
        Gets and sets the bundleId
        
        Returns:
            str:
                The bundleId
        """
        if "bundleId" in self._prop_dict:
            return self._prop_dict["bundleId"]
        else:
            return None

    @bundle_id.setter
    def bundle_id(self, val):
        self._prop_dict["bundleId"] = val

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
    def applicable_device_type(self):
        """
        Gets and sets the applicableDeviceType
        
        Returns: 
            :class:`IosDeviceType<onedrivesdk.model.ios_device_type.IosDeviceType>`:
                The applicableDeviceType
        """
        if "applicableDeviceType" in self._prop_dict:
            if isinstance(self._prop_dict["applicableDeviceType"], OneDriveObjectBase):
                return self._prop_dict["applicableDeviceType"]
            else :
                self._prop_dict["applicableDeviceType"] = IosDeviceType(self._prop_dict["applicableDeviceType"])
                return self._prop_dict["applicableDeviceType"]

        return None

    @applicable_device_type.setter
    def applicable_device_type(self, val):
        self._prop_dict["applicableDeviceType"] = val

    @property
    def minimum_supported_operating_system(self):
        """
        Gets and sets the minimumSupportedOperatingSystem
        
        Returns: 
            :class:`IosMinimumOperatingSystem<onedrivesdk.model.ios_minimum_operating_system.IosMinimumOperatingSystem>`:
                The minimumSupportedOperatingSystem
        """
        if "minimumSupportedOperatingSystem" in self._prop_dict:
            if isinstance(self._prop_dict["minimumSupportedOperatingSystem"], OneDriveObjectBase):
                return self._prop_dict["minimumSupportedOperatingSystem"]
            else :
                self._prop_dict["minimumSupportedOperatingSystem"] = IosMinimumOperatingSystem(self._prop_dict["minimumSupportedOperatingSystem"])
                return self._prop_dict["minimumSupportedOperatingSystem"]

        return None

    @minimum_supported_operating_system.setter
    def minimum_supported_operating_system(self, val):
        self._prop_dict["minimumSupportedOperatingSystem"] = val

