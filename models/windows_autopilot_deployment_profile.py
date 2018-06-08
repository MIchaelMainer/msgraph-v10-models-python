# -*- coding: utf-8 -*- 
'''
# Copyright (c) Microsoft Corporation.  All Rights Reserved.  Licensed under the MIT License.  See License in the project root for license information.
# 
#  This file was generated and any changes will be overwritten.
'''

from __future__ import unicode_literals
from ..model.out_of_box_experience_settings import OutOfBoxExperienceSettings
from ..model.windows_enrollment_status_screen_settings import WindowsEnrollmentStatusScreenSettings
from ..model.windows_autopilot_device_identity import WindowsAutopilotDeviceIdentity
from ..model.windows_autopilot_deployment_profile_assignment import WindowsAutopilotDeploymentProfileAssignment
from datetime import datetime
from ..one_drive_object_base import OneDriveObjectBase


class WindowsAutopilotDeploymentProfile(OneDriveObjectBase):

    def __init__(self, prop_dict={}):
        self._prop_dict = prop_dict

    @property
    def display_name(self):
        """
        Gets and sets the displayName
        
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
    def language(self):
        """
        Gets and sets the language
        
        Returns:
            str:
                The language
        """
        if "language" in self._prop_dict:
            return self._prop_dict["language"]
        else:
            return None

    @language.setter
    def language(self, val):
        self._prop_dict["language"] = val

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
    def out_of_box_experience_settings(self):
        """
        Gets and sets the outOfBoxExperienceSettings
        
        Returns: 
            :class:`OutOfBoxExperienceSettings<onedrivesdk.model.out_of_box_experience_settings.OutOfBoxExperienceSettings>`:
                The outOfBoxExperienceSettings
        """
        if "outOfBoxExperienceSettings" in self._prop_dict:
            if isinstance(self._prop_dict["outOfBoxExperienceSettings"], OneDriveObjectBase):
                return self._prop_dict["outOfBoxExperienceSettings"]
            else :
                self._prop_dict["outOfBoxExperienceSettings"] = OutOfBoxExperienceSettings(self._prop_dict["outOfBoxExperienceSettings"])
                return self._prop_dict["outOfBoxExperienceSettings"]

        return None

    @out_of_box_experience_settings.setter
    def out_of_box_experience_settings(self, val):
        self._prop_dict["outOfBoxExperienceSettings"] = val

    @property
    def enrollment_status_screen_settings(self):
        """
        Gets and sets the enrollmentStatusScreenSettings
        
        Returns: 
            :class:`WindowsEnrollmentStatusScreenSettings<onedrivesdk.model.windows_enrollment_status_screen_settings.WindowsEnrollmentStatusScreenSettings>`:
                The enrollmentStatusScreenSettings
        """
        if "enrollmentStatusScreenSettings" in self._prop_dict:
            if isinstance(self._prop_dict["enrollmentStatusScreenSettings"], OneDriveObjectBase):
                return self._prop_dict["enrollmentStatusScreenSettings"]
            else :
                self._prop_dict["enrollmentStatusScreenSettings"] = WindowsEnrollmentStatusScreenSettings(self._prop_dict["enrollmentStatusScreenSettings"])
                return self._prop_dict["enrollmentStatusScreenSettings"]

        return None

    @enrollment_status_screen_settings.setter
    def enrollment_status_screen_settings(self, val):
        self._prop_dict["enrollmentStatusScreenSettings"] = val

    @property
    def assigned_devices(self):
        """Gets and sets the assignedDevices
        
        Returns: 
            :class:`AssignedDevicesCollectionPage<onedrivesdk.request.assigned_devices_collection.AssignedDevicesCollectionPage>`:
                The assignedDevices
        """
        if "assignedDevices" in self._prop_dict:
            return AssignedDevicesCollectionPage(self._prop_dict["assignedDevices"])
        else:
            return None

    @property
    def assignments(self):
        """Gets and sets the assignments
        
        Returns: 
            :class:`AssignmentsCollectionPage<onedrivesdk.request.assignments_collection.AssignmentsCollectionPage>`:
                The assignments
        """
        if "assignments" in self._prop_dict:
            return AssignmentsCollectionPage(self._prop_dict["assignments"])
        else:
            return None

