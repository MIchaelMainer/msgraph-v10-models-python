# -*- coding: utf-8 -*- 
'''
# Copyright (c) Microsoft Corporation.  All Rights Reserved.  Licensed under the MIT License.  See License in the project root for license information.
# 
#  This file was generated and any changes will be overwritten.
'''

from __future__ import unicode_literals
from ..model.status import Status
from ..model.user_activity import UserActivity
from datetime import datetime
from ..one_drive_object_base import OneDriveObjectBase


class ActivityHistoryItem(OneDriveObjectBase):

    def __init__(self, prop_dict={}):
        self._prop_dict = prop_dict

    @property
    def status(self):
        """
        Gets and sets the status
        
        Returns: 
            :class:`Status<onedrivesdk.model.status.Status>`:
                The status
        """
        if "status" in self._prop_dict:
            if isinstance(self._prop_dict["status"], OneDriveObjectBase):
                return self._prop_dict["status"]
            else :
                self._prop_dict["status"] = Status(self._prop_dict["status"])
                return self._prop_dict["status"]

        return None

    @status.setter
    def status(self, val):
        self._prop_dict["status"] = val

    @property
    def active_duration_seconds(self):
        """
        Gets and sets the activeDurationSeconds
        
        Returns:
            int:
                The activeDurationSeconds
        """
        if "activeDurationSeconds" in self._prop_dict:
            return self._prop_dict["activeDurationSeconds"]
        else:
            return None

    @active_duration_seconds.setter
    def active_duration_seconds(self, val):
        self._prop_dict["activeDurationSeconds"] = val

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
    def last_active_date_time(self):
        """
        Gets and sets the lastActiveDateTime
        
        Returns:
            datetime:
                The lastActiveDateTime
        """
        if "lastActiveDateTime" in self._prop_dict:
            return datetime.strptime(self._prop_dict["lastActiveDateTime"].replace("Z", ""), "%Y-%m-%dT%H:%M:%S.%f")
        else:
            return None

    @last_active_date_time.setter
    def last_active_date_time(self, val):
        self._prop_dict["lastActiveDateTime"] = val.isoformat()+"Z"

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
    def started_date_time(self):
        """
        Gets and sets the startedDateTime
        
        Returns:
            datetime:
                The startedDateTime
        """
        if "startedDateTime" in self._prop_dict:
            return datetime.strptime(self._prop_dict["startedDateTime"].replace("Z", ""), "%Y-%m-%dT%H:%M:%S.%f")
        else:
            return None

    @started_date_time.setter
    def started_date_time(self, val):
        self._prop_dict["startedDateTime"] = val.isoformat()+"Z"

    @property
    def user_timezone(self):
        """
        Gets and sets the userTimezone
        
        Returns:
            str:
                The userTimezone
        """
        if "userTimezone" in self._prop_dict:
            return self._prop_dict["userTimezone"]
        else:
            return None

    @user_timezone.setter
    def user_timezone(self, val):
        self._prop_dict["userTimezone"] = val

    @property
    def activity(self):
        """
        Gets and sets the activity
        
        Returns: 
            :class:`UserActivity<onedrivesdk.model.user_activity.UserActivity>`:
                The activity
        """
        if "activity" in self._prop_dict:
            if isinstance(self._prop_dict["activity"], OneDriveObjectBase):
                return self._prop_dict["activity"]
            else :
                self._prop_dict["activity"] = UserActivity(self._prop_dict["activity"])
                return self._prop_dict["activity"]

        return None

    @activity.setter
    def activity(self, val):
        self._prop_dict["activity"] = val

