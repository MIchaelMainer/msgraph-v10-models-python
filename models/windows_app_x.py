# -*- coding: utf-8 -*- 
'''
# Copyright (c) Microsoft Corporation.  All Rights Reserved.  Licensed under the MIT License.  See License in the project root for license information.
# 
#  This file was generated and any changes will be overwritten.
'''

from __future__ import unicode_literals
from ..model.windows_architecture import WindowsArchitecture
from ..model.windows_minimum_operating_system import WindowsMinimumOperatingSystem
from ..one_drive_object_base import OneDriveObjectBase


class WindowsAppX(OneDriveObjectBase):

    def __init__(self, prop_dict={}):
        self._prop_dict = prop_dict

    @property
    def applicable_architectures(self):
        """
        Gets and sets the applicableArchitectures
        
        Returns: 
            :class:`WindowsArchitecture<onedrivesdk.model.windows_architecture.WindowsArchitecture>`:
                The applicableArchitectures
        """
        if "applicableArchitectures" in self._prop_dict:
            if isinstance(self._prop_dict["applicableArchitectures"], OneDriveObjectBase):
                return self._prop_dict["applicableArchitectures"]
            else :
                self._prop_dict["applicableArchitectures"] = WindowsArchitecture(self._prop_dict["applicableArchitectures"])
                return self._prop_dict["applicableArchitectures"]

        return None

    @applicable_architectures.setter
    def applicable_architectures(self, val):
        self._prop_dict["applicableArchitectures"] = val

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
    def identity_publisher_hash(self):
        """
        Gets and sets the identityPublisherHash
        
        Returns:
            str:
                The identityPublisherHash
        """
        if "identityPublisherHash" in self._prop_dict:
            return self._prop_dict["identityPublisherHash"]
        else:
            return None

    @identity_publisher_hash.setter
    def identity_publisher_hash(self, val):
        self._prop_dict["identityPublisherHash"] = val

    @property
    def identity_resource_identifier(self):
        """
        Gets and sets the identityResourceIdentifier
        
        Returns:
            str:
                The identityResourceIdentifier
        """
        if "identityResourceIdentifier" in self._prop_dict:
            return self._prop_dict["identityResourceIdentifier"]
        else:
            return None

    @identity_resource_identifier.setter
    def identity_resource_identifier(self, val):
        self._prop_dict["identityResourceIdentifier"] = val

    @property
    def is_bundle(self):
        """
        Gets and sets the isBundle
        
        Returns:
            bool:
                The isBundle
        """
        if "isBundle" in self._prop_dict:
            return self._prop_dict["isBundle"]
        else:
            return None

    @is_bundle.setter
    def is_bundle(self, val):
        self._prop_dict["isBundle"] = val

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

