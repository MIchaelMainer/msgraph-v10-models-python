# -*- coding: utf-8 -*- 
'''
# Copyright (c) Microsoft Corporation.  All Rights Reserved.  Licensed under the MIT License.  See License in the project root for license information.
# 
#  This file was generated and any changes will be overwritten.
'''

from __future__ import unicode_literals
from ..model.mobile_app_provisioning_config_group_assignment import MobileAppProvisioningConfigGroupAssignment
from ..model.ios_lob_app_provisioning_configuration_assignment import IosLobAppProvisioningConfigurationAssignment
from ..model.managed_device_mobile_app_configuration_device_status import ManagedDeviceMobileAppConfigurationDeviceStatus
from ..model.managed_device_mobile_app_configuration_user_status import ManagedDeviceMobileAppConfigurationUserStatus
from datetime import datetime
from ..one_drive_object_base import OneDriveObjectBase


class IosLobAppProvisioningConfiguration(OneDriveObjectBase):

    def __init__(self, prop_dict={}):
        self._prop_dict = prop_dict

    @property
    def expiration_date_time(self):
        """
        Gets and sets the expirationDateTime
        
        Returns:
            datetime:
                The expirationDateTime
        """
        if "expirationDateTime" in self._prop_dict:
            return datetime.strptime(self._prop_dict["expirationDateTime"].replace("Z", ""), "%Y-%m-%dT%H:%M:%S.%f")
        else:
            return None

    @expiration_date_time.setter
    def expiration_date_time(self, val):
        self._prop_dict["expirationDateTime"] = val.isoformat()+"Z"

    @property
    def payload_file_name(self):
        """
        Gets and sets the payloadFileName
        
        Returns:
            str:
                The payloadFileName
        """
        if "payloadFileName" in self._prop_dict:
            return self._prop_dict["payloadFileName"]
        else:
            return None

    @payload_file_name.setter
    def payload_file_name(self, val):
        self._prop_dict["payloadFileName"] = val

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
    def version(self):
        """
        Gets and sets the version
        
        Returns:
            int:
                The version
        """
        if "version" in self._prop_dict:
            return self._prop_dict["version"]
        else:
            return None

    @version.setter
    def version(self, val):
        self._prop_dict["version"] = val

    @property
    def group_assignments(self):
        """Gets and sets the groupAssignments
        
        Returns: 
            :class:`GroupAssignmentsCollectionPage<onedrivesdk.request.group_assignments_collection.GroupAssignmentsCollectionPage>`:
                The groupAssignments
        """
        if "groupAssignments" in self._prop_dict:
            return GroupAssignmentsCollectionPage(self._prop_dict["groupAssignments"])
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

    @property
    def device_statuses(self):
        """Gets and sets the deviceStatuses
        
        Returns: 
            :class:`DeviceStatusesCollectionPage<onedrivesdk.request.device_statuses_collection.DeviceStatusesCollectionPage>`:
                The deviceStatuses
        """
        if "deviceStatuses" in self._prop_dict:
            return DeviceStatusesCollectionPage(self._prop_dict["deviceStatuses"])
        else:
            return None

    @property
    def user_statuses(self):
        """Gets and sets the userStatuses
        
        Returns: 
            :class:`UserStatusesCollectionPage<onedrivesdk.request.user_statuses_collection.UserStatusesCollectionPage>`:
                The userStatuses
        """
        if "userStatuses" in self._prop_dict:
            return UserStatusesCollectionPage(self._prop_dict["userStatuses"])
        else:
            return None

