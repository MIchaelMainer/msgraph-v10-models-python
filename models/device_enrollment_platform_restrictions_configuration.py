# -*- coding: utf-8 -*- 
'''
# Copyright (c) Microsoft Corporation.  All Rights Reserved.  Licensed under the MIT License.  See License in the project root for license information.
# 
#  This file was generated and any changes will be overwritten.
'''

from __future__ import unicode_literals
from ..model.device_enrollment_platform_restriction import DeviceEnrollmentPlatformRestriction
from ..one_drive_object_base import OneDriveObjectBase


class DeviceEnrollmentPlatformRestrictionsConfiguration(OneDriveObjectBase):

    def __init__(self, prop_dict={}):
        self._prop_dict = prop_dict

    @property
    def ios_restriction(self):
        """
        Gets and sets the iosRestriction
        
        Returns: 
            :class:`DeviceEnrollmentPlatformRestriction<onedrivesdk.model.device_enrollment_platform_restriction.DeviceEnrollmentPlatformRestriction>`:
                The iosRestriction
        """
        if "iosRestriction" in self._prop_dict:
            if isinstance(self._prop_dict["iosRestriction"], OneDriveObjectBase):
                return self._prop_dict["iosRestriction"]
            else :
                self._prop_dict["iosRestriction"] = DeviceEnrollmentPlatformRestriction(self._prop_dict["iosRestriction"])
                return self._prop_dict["iosRestriction"]

        return None

    @ios_restriction.setter
    def ios_restriction(self, val):
        self._prop_dict["iosRestriction"] = val

    @property
    def windows_restriction(self):
        """
        Gets and sets the windowsRestriction
        
        Returns: 
            :class:`DeviceEnrollmentPlatformRestriction<onedrivesdk.model.device_enrollment_platform_restriction.DeviceEnrollmentPlatformRestriction>`:
                The windowsRestriction
        """
        if "windowsRestriction" in self._prop_dict:
            if isinstance(self._prop_dict["windowsRestriction"], OneDriveObjectBase):
                return self._prop_dict["windowsRestriction"]
            else :
                self._prop_dict["windowsRestriction"] = DeviceEnrollmentPlatformRestriction(self._prop_dict["windowsRestriction"])
                return self._prop_dict["windowsRestriction"]

        return None

    @windows_restriction.setter
    def windows_restriction(self, val):
        self._prop_dict["windowsRestriction"] = val

    @property
    def windows_mobile_restriction(self):
        """
        Gets and sets the windowsMobileRestriction
        
        Returns: 
            :class:`DeviceEnrollmentPlatformRestriction<onedrivesdk.model.device_enrollment_platform_restriction.DeviceEnrollmentPlatformRestriction>`:
                The windowsMobileRestriction
        """
        if "windowsMobileRestriction" in self._prop_dict:
            if isinstance(self._prop_dict["windowsMobileRestriction"], OneDriveObjectBase):
                return self._prop_dict["windowsMobileRestriction"]
            else :
                self._prop_dict["windowsMobileRestriction"] = DeviceEnrollmentPlatformRestriction(self._prop_dict["windowsMobileRestriction"])
                return self._prop_dict["windowsMobileRestriction"]

        return None

    @windows_mobile_restriction.setter
    def windows_mobile_restriction(self, val):
        self._prop_dict["windowsMobileRestriction"] = val

    @property
    def android_restriction(self):
        """
        Gets and sets the androidRestriction
        
        Returns: 
            :class:`DeviceEnrollmentPlatformRestriction<onedrivesdk.model.device_enrollment_platform_restriction.DeviceEnrollmentPlatformRestriction>`:
                The androidRestriction
        """
        if "androidRestriction" in self._prop_dict:
            if isinstance(self._prop_dict["androidRestriction"], OneDriveObjectBase):
                return self._prop_dict["androidRestriction"]
            else :
                self._prop_dict["androidRestriction"] = DeviceEnrollmentPlatformRestriction(self._prop_dict["androidRestriction"])
                return self._prop_dict["androidRestriction"]

        return None

    @android_restriction.setter
    def android_restriction(self, val):
        self._prop_dict["androidRestriction"] = val

    @property
    def android_for_work_restriction(self):
        """
        Gets and sets the androidForWorkRestriction
        
        Returns: 
            :class:`DeviceEnrollmentPlatformRestriction<onedrivesdk.model.device_enrollment_platform_restriction.DeviceEnrollmentPlatformRestriction>`:
                The androidForWorkRestriction
        """
        if "androidForWorkRestriction" in self._prop_dict:
            if isinstance(self._prop_dict["androidForWorkRestriction"], OneDriveObjectBase):
                return self._prop_dict["androidForWorkRestriction"]
            else :
                self._prop_dict["androidForWorkRestriction"] = DeviceEnrollmentPlatformRestriction(self._prop_dict["androidForWorkRestriction"])
                return self._prop_dict["androidForWorkRestriction"]

        return None

    @android_for_work_restriction.setter
    def android_for_work_restriction(self, val):
        self._prop_dict["androidForWorkRestriction"] = val

    @property
    def mac_restriction(self):
        """
        Gets and sets the macRestriction
        
        Returns: 
            :class:`DeviceEnrollmentPlatformRestriction<onedrivesdk.model.device_enrollment_platform_restriction.DeviceEnrollmentPlatformRestriction>`:
                The macRestriction
        """
        if "macRestriction" in self._prop_dict:
            if isinstance(self._prop_dict["macRestriction"], OneDriveObjectBase):
                return self._prop_dict["macRestriction"]
            else :
                self._prop_dict["macRestriction"] = DeviceEnrollmentPlatformRestriction(self._prop_dict["macRestriction"])
                return self._prop_dict["macRestriction"]

        return None

    @mac_restriction.setter
    def mac_restriction(self, val):
        self._prop_dict["macRestriction"] = val

    @property
    def mac_os_restriction(self):
        """
        Gets and sets the macOSRestriction
        
        Returns: 
            :class:`DeviceEnrollmentPlatformRestriction<onedrivesdk.model.device_enrollment_platform_restriction.DeviceEnrollmentPlatformRestriction>`:
                The macOSRestriction
        """
        if "macOSRestriction" in self._prop_dict:
            if isinstance(self._prop_dict["macOSRestriction"], OneDriveObjectBase):
                return self._prop_dict["macOSRestriction"]
            else :
                self._prop_dict["macOSRestriction"] = DeviceEnrollmentPlatformRestriction(self._prop_dict["macOSRestriction"])
                return self._prop_dict["macOSRestriction"]

        return None

    @mac_os_restriction.setter
    def mac_os_restriction(self, val):
        self._prop_dict["macOSRestriction"] = val

