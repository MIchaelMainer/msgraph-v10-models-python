# -*- coding: utf-8 -*- 
'''
# Copyright (c) Microsoft Corporation.  All Rights Reserved.  Licensed under the MIT License.  See License in the project root for license information.
# 
#  This file was generated and any changes will be overwritten.
'''

from __future__ import unicode_literals
from ..model.managed_device_mobile_app_configuration_assignment import ManagedDeviceMobileAppConfigurationAssignment
from ..model.managed_device_mobile_app_configuration_device_status import ManagedDeviceMobileAppConfigurationDeviceStatus
from ..model.managed_device_mobile_app_configuration_user_status import ManagedDeviceMobileAppConfigurationUserStatus
from ..model.managed_device_mobile_app_configuration_device_summary import ManagedDeviceMobileAppConfigurationDeviceSummary
from ..model.managed_device_mobile_app_configuration_user_summary import ManagedDeviceMobileAppConfigurationUserSummary
from datetime import datetime
from ..one_drive_object_base import OneDriveObjectBase


class ManagedDeviceMobileAppConfiguration(OneDriveObjectBase):

    def __init__(self, prop_dict={}):
        self._prop_dict = prop_dict

    @property
    def targeted_mobile_apps(self):
        """
        Gets and sets the targetedMobileApps
        
        Returns:
            str:
                The targetedMobileApps
        """
        if "targetedMobileApps" in self._prop_dict:
            return self._prop_dict["targetedMobileApps"]
        else:
            return None

    @targeted_mobile_apps.setter
    def targeted_mobile_apps(self, val):
        self._prop_dict["targetedMobileApps"] = val

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

    @property
    def device_status_summary(self):
        """
        Gets and sets the deviceStatusSummary
        
        Returns: 
            :class:`ManagedDeviceMobileAppConfigurationDeviceSummary<onedrivesdk.model.managed_device_mobile_app_configuration_device_summary.ManagedDeviceMobileAppConfigurationDeviceSummary>`:
                The deviceStatusSummary
        """
        if "deviceStatusSummary" in self._prop_dict:
            if isinstance(self._prop_dict["deviceStatusSummary"], OneDriveObjectBase):
                return self._prop_dict["deviceStatusSummary"]
            else :
                self._prop_dict["deviceStatusSummary"] = ManagedDeviceMobileAppConfigurationDeviceSummary(self._prop_dict["deviceStatusSummary"])
                return self._prop_dict["deviceStatusSummary"]

        return None

    @device_status_summary.setter
    def device_status_summary(self, val):
        self._prop_dict["deviceStatusSummary"] = val

    @property
    def user_status_summary(self):
        """
        Gets and sets the userStatusSummary
        
        Returns: 
            :class:`ManagedDeviceMobileAppConfigurationUserSummary<onedrivesdk.model.managed_device_mobile_app_configuration_user_summary.ManagedDeviceMobileAppConfigurationUserSummary>`:
                The userStatusSummary
        """
        if "userStatusSummary" in self._prop_dict:
            if isinstance(self._prop_dict["userStatusSummary"], OneDriveObjectBase):
                return self._prop_dict["userStatusSummary"]
            else :
                self._prop_dict["userStatusSummary"] = ManagedDeviceMobileAppConfigurationUserSummary(self._prop_dict["userStatusSummary"])
                return self._prop_dict["userStatusSummary"]

        return None

    @user_status_summary.setter
    def user_status_summary(self, val):
        self._prop_dict["userStatusSummary"] = val

