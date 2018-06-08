# -*- coding: utf-8 -*- 
'''
# Copyright (c) Microsoft Corporation.  All Rights Reserved.  Licensed under the MIT License.  See License in the project root for license information.
# 
#  This file was generated and any changes will be overwritten.
'''

from __future__ import unicode_literals
from ..model.device_enrollment_type import DeviceEnrollmentType
from ..model.device_enrollment_failure_reason import DeviceEnrollmentFailureReason
from ..one_drive_object_base import OneDriveObjectBase


class EnrollmentTroubleshootingEvent(OneDriveObjectBase):

    def __init__(self, prop_dict={}):
        self._prop_dict = prop_dict

    @property
    def managed_device_identifier(self):
        """
        Gets and sets the managedDeviceIdentifier
        
        Returns:
            str:
                The managedDeviceIdentifier
        """
        if "managedDeviceIdentifier" in self._prop_dict:
            return self._prop_dict["managedDeviceIdentifier"]
        else:
            return None

    @managed_device_identifier.setter
    def managed_device_identifier(self, val):
        self._prop_dict["managedDeviceIdentifier"] = val

    @property
    def operating_system(self):
        """
        Gets and sets the operatingSystem
        
        Returns:
            str:
                The operatingSystem
        """
        if "operatingSystem" in self._prop_dict:
            return self._prop_dict["operatingSystem"]
        else:
            return None

    @operating_system.setter
    def operating_system(self, val):
        self._prop_dict["operatingSystem"] = val

    @property
    def os_version(self):
        """
        Gets and sets the osVersion
        
        Returns:
            str:
                The osVersion
        """
        if "osVersion" in self._prop_dict:
            return self._prop_dict["osVersion"]
        else:
            return None

    @os_version.setter
    def os_version(self, val):
        self._prop_dict["osVersion"] = val

    @property
    def user_id(self):
        """
        Gets and sets the userId
        
        Returns:
            str:
                The userId
        """
        if "userId" in self._prop_dict:
            return self._prop_dict["userId"]
        else:
            return None

    @user_id.setter
    def user_id(self, val):
        self._prop_dict["userId"] = val

    @property
    def device_id(self):
        """
        Gets and sets the deviceId
        
        Returns:
            str:
                The deviceId
        """
        if "deviceId" in self._prop_dict:
            return self._prop_dict["deviceId"]
        else:
            return None

    @device_id.setter
    def device_id(self, val):
        self._prop_dict["deviceId"] = val

    @property
    def enrollment_type(self):
        """
        Gets and sets the enrollmentType
        
        Returns: 
            :class:`DeviceEnrollmentType<onedrivesdk.model.device_enrollment_type.DeviceEnrollmentType>`:
                The enrollmentType
        """
        if "enrollmentType" in self._prop_dict:
            if isinstance(self._prop_dict["enrollmentType"], OneDriveObjectBase):
                return self._prop_dict["enrollmentType"]
            else :
                self._prop_dict["enrollmentType"] = DeviceEnrollmentType(self._prop_dict["enrollmentType"])
                return self._prop_dict["enrollmentType"]

        return None

    @enrollment_type.setter
    def enrollment_type(self, val):
        self._prop_dict["enrollmentType"] = val

    @property
    def failure_category(self):
        """
        Gets and sets the failureCategory
        
        Returns: 
            :class:`DeviceEnrollmentFailureReason<onedrivesdk.model.device_enrollment_failure_reason.DeviceEnrollmentFailureReason>`:
                The failureCategory
        """
        if "failureCategory" in self._prop_dict:
            if isinstance(self._prop_dict["failureCategory"], OneDriveObjectBase):
                return self._prop_dict["failureCategory"]
            else :
                self._prop_dict["failureCategory"] = DeviceEnrollmentFailureReason(self._prop_dict["failureCategory"])
                return self._prop_dict["failureCategory"]

        return None

    @failure_category.setter
    def failure_category(self, val):
        self._prop_dict["failureCategory"] = val

    @property
    def failure_reason(self):
        """
        Gets and sets the failureReason
        
        Returns:
            str:
                The failureReason
        """
        if "failureReason" in self._prop_dict:
            return self._prop_dict["failureReason"]
        else:
            return None

    @failure_reason.setter
    def failure_reason(self, val):
        self._prop_dict["failureReason"] = val

