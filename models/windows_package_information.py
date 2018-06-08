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


class WindowsPackageInformation(OneDriveObjectBase):

    def __init__(self, prop_dict={}):
        self._prop_dict = prop_dict

    @property
    def applicable_architecture(self):
        """
        Gets and sets the applicableArchitecture
        
        Returns: 
            :class:`WindowsArchitecture<onedrivesdk.model.windows_architecture.WindowsArchitecture>`:
                The applicableArchitecture
        """
        if "applicableArchitecture" in self._prop_dict:
            if isinstance(self._prop_dict["applicableArchitecture"], OneDriveObjectBase):
                return self._prop_dict["applicableArchitecture"]
            else :
                self._prop_dict["applicableArchitecture"] = WindowsArchitecture(self._prop_dict["applicableArchitecture"])
                return self._prop_dict["applicableArchitecture"]

        return None

    @applicable_architecture.setter
    def applicable_architecture(self, val):
        self._prop_dict["applicableArchitecture"] = val
    @property
    def display_name(self):
        """Gets and sets the displayName
        
        Returns: 
            str:
                The displayName
        """
        if "displayName" in self._prop_dict:
            return self._prop_dict["displayName"]
        else:
            return None

    @display_name.setter
    def display_name(self, val):
        self._prop_dict["displayName"] = val

    @property
    def identity_name(self):
        """Gets and sets the identityName
        
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
    def identity_publisher(self):
        """Gets and sets the identityPublisher
        
        Returns: 
            str:
                The identityPublisher
        """
        if "identityPublisher" in self._prop_dict:
            return self._prop_dict["identityPublisher"]
        else:
            return None

    @identity_publisher.setter
    def identity_publisher(self, val):
        self._prop_dict["identityPublisher"] = val

    @property
    def identity_resource_identifier(self):
        """Gets and sets the identityResourceIdentifier
        
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
    def identity_version(self):
        """Gets and sets the identityVersion
        
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
