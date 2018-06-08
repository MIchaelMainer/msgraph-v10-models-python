# -*- coding: utf-8 -*- 
'''
# Copyright (c) Microsoft Corporation.  All Rights Reserved.  Licensed under the MIT License.  See License in the project root for license information.
# 
#  This file was generated and any changes will be overwritten.
'''

from __future__ import unicode_literals
from ..model.imported_device_identity_type import ImportedDeviceIdentityType
from ..model.enrollment_state import EnrollmentState
from ..model.platform import Platform
from datetime import datetime
from ..one_drive_object_base import OneDriveObjectBase


class ImportedDeviceIdentity(OneDriveObjectBase):

    def __init__(self, prop_dict={}):
        self._prop_dict = prop_dict

    @property
    def imported_device_identifier(self):
        """
        Gets and sets the importedDeviceIdentifier
        
        Returns:
            str:
                The importedDeviceIdentifier
        """
        if "importedDeviceIdentifier" in self._prop_dict:
            return self._prop_dict["importedDeviceIdentifier"]
        else:
            return None

    @imported_device_identifier.setter
    def imported_device_identifier(self, val):
        self._prop_dict["importedDeviceIdentifier"] = val

    @property
    def imported_device_identity_type(self):
        """
        Gets and sets the importedDeviceIdentityType
        
        Returns: 
            :class:`ImportedDeviceIdentityType<onedrivesdk.model.imported_device_identity_type.ImportedDeviceIdentityType>`:
                The importedDeviceIdentityType
        """
        if "importedDeviceIdentityType" in self._prop_dict:
            if isinstance(self._prop_dict["importedDeviceIdentityType"], OneDriveObjectBase):
                return self._prop_dict["importedDeviceIdentityType"]
            else :
                self._prop_dict["importedDeviceIdentityType"] = ImportedDeviceIdentityType(self._prop_dict["importedDeviceIdentityType"])
                return self._prop_dict["importedDeviceIdentityType"]

        return None

    @imported_device_identity_type.setter
    def imported_device_identity_type(self, val):
        self._prop_dict["importedDeviceIdentityType"] = val

    @property
    def last_modified_date_time(self):
        """
        Gets and sets the lastModifiedDateTime
        
        Returns:
            datetime:
                The lastModifiedDateTime
        """
        if "lastModifiedDateTime" in self._prop_dict:
            return datetime.strptime(self._prop_dict["lastModifiedDateTime"].replace("Z", ""), "%Y-%m-%dT%H:%M:%S.%f")
        else:
            return None

    @last_modified_date_time.setter
    def last_modified_date_time(self, val):
        self._prop_dict["lastModifiedDateTime"] = val.isoformat()+"Z"

    @property
    def created_date_time(self):
        """
        Gets and sets the createdDateTime
        
        Returns:
            datetime:
                The createdDateTime
        """
        if "createdDateTime" in self._prop_dict:
            return datetime.strptime(self._prop_dict["createdDateTime"].replace("Z", ""), "%Y-%m-%dT%H:%M:%S.%f")
        else:
            return None

    @created_date_time.setter
    def created_date_time(self, val):
        self._prop_dict["createdDateTime"] = val.isoformat()+"Z"

    @property
    def last_contacted_date_time(self):
        """
        Gets and sets the lastContactedDateTime
        
        Returns:
            datetime:
                The lastContactedDateTime
        """
        if "lastContactedDateTime" in self._prop_dict:
            return datetime.strptime(self._prop_dict["lastContactedDateTime"].replace("Z", ""), "%Y-%m-%dT%H:%M:%S.%f")
        else:
            return None

    @last_contacted_date_time.setter
    def last_contacted_date_time(self, val):
        self._prop_dict["lastContactedDateTime"] = val.isoformat()+"Z"

    @property
    def description(self):
        """
        Gets and sets the description
        
        Returns:
            str:
                The description
        """
        if "description" in self._prop_dict:
            return self._prop_dict["description"]
        else:
            return None

    @description.setter
    def description(self, val):
        self._prop_dict["description"] = val

    @property
    def enrollment_state(self):
        """
        Gets and sets the enrollmentState
        
        Returns: 
            :class:`EnrollmentState<onedrivesdk.model.enrollment_state.EnrollmentState>`:
                The enrollmentState
        """
        if "enrollmentState" in self._prop_dict:
            if isinstance(self._prop_dict["enrollmentState"], OneDriveObjectBase):
                return self._prop_dict["enrollmentState"]
            else :
                self._prop_dict["enrollmentState"] = EnrollmentState(self._prop_dict["enrollmentState"])
                return self._prop_dict["enrollmentState"]

        return None

    @enrollment_state.setter
    def enrollment_state(self, val):
        self._prop_dict["enrollmentState"] = val

    @property
    def platform(self):
        """
        Gets and sets the platform
        
        Returns: 
            :class:`Platform<onedrivesdk.model.platform.Platform>`:
                The platform
        """
        if "platform" in self._prop_dict:
            if isinstance(self._prop_dict["platform"], OneDriveObjectBase):
                return self._prop_dict["platform"]
            else :
                self._prop_dict["platform"] = Platform(self._prop_dict["platform"])
                return self._prop_dict["platform"]

        return None

    @platform.setter
    def platform(self, val):
        self._prop_dict["platform"] = val

