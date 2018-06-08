# -*- coding: utf-8 -*- 
'''
# Copyright (c) Microsoft Corporation.  All Rights Reserved.  Licensed under the MIT License.  See License in the project root for license information.
# 
#  This file was generated and any changes will be overwritten.
'''

from __future__ import unicode_literals
from ..one_drive_object_base import OneDriveObjectBase


class DeviceEnrollmentPlatformRestriction(OneDriveObjectBase):

    def __init__(self, prop_dict={}):
        self._prop_dict = prop_dict

    @property
    def platform_blocked(self):
        """Gets and sets the platformBlocked
        
        Returns: 
            bool:
                The platformBlocked
        """
        if "platformBlocked" in self._prop_dict:
            return self._prop_dict["platformBlocked"]
        else:
            return None

    @platform_blocked.setter
    def platform_blocked(self, val):
        self._prop_dict["platformBlocked"] = val

    @property
    def personal_device_enrollment_blocked(self):
        """Gets and sets the personalDeviceEnrollmentBlocked
        
        Returns: 
            bool:
                The personalDeviceEnrollmentBlocked
        """
        if "personalDeviceEnrollmentBlocked" in self._prop_dict:
            return self._prop_dict["personalDeviceEnrollmentBlocked"]
        else:
            return None

    @personal_device_enrollment_blocked.setter
    def personal_device_enrollment_blocked(self, val):
        self._prop_dict["personalDeviceEnrollmentBlocked"] = val

    @property
    def os_minimum_version(self):
        """Gets and sets the osMinimumVersion
        
        Returns: 
            str:
                The osMinimumVersion
        """
        if "osMinimumVersion" in self._prop_dict:
            return self._prop_dict["osMinimumVersion"]
        else:
            return None

    @os_minimum_version.setter
    def os_minimum_version(self, val):
        self._prop_dict["osMinimumVersion"] = val

    @property
    def os_maximum_version(self):
        """Gets and sets the osMaximumVersion
        
        Returns: 
            str:
                The osMaximumVersion
        """
        if "osMaximumVersion" in self._prop_dict:
            return self._prop_dict["osMaximumVersion"]
        else:
            return None

    @os_maximum_version.setter
    def os_maximum_version(self, val):
        self._prop_dict["osMaximumVersion"] = val

