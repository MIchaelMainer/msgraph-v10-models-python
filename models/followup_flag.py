# -*- coding: utf-8 -*- 
'''
# Copyright (c) Microsoft Corporation.  All Rights Reserved.  Licensed under the MIT License.  See License in the project root for license information.
# 
#  This file was generated and any changes will be overwritten.
'''

from __future__ import unicode_literals
from ..model.date_time_time_zone import DateTimeTimeZone
from ..model.followup_flag_status import FollowupFlagStatus
from ..one_drive_object_base import OneDriveObjectBase


class FollowupFlag(OneDriveObjectBase):

    def __init__(self, prop_dict={}):
        self._prop_dict = prop_dict

    @property
    def completed_date_time(self):
        """
        Gets and sets the completedDateTime
        
        Returns: 
            :class:`DateTimeTimeZone<onedrivesdk.model.date_time_time_zone.DateTimeTimeZone>`:
                The completedDateTime
        """
        if "completedDateTime" in self._prop_dict:
            if isinstance(self._prop_dict["completedDateTime"], OneDriveObjectBase):
                return self._prop_dict["completedDateTime"]
            else :
                self._prop_dict["completedDateTime"] = DateTimeTimeZone(self._prop_dict["completedDateTime"])
                return self._prop_dict["completedDateTime"]

        return None

    @completed_date_time.setter
    def completed_date_time(self, val):
        self._prop_dict["completedDateTime"] = val
    @property
    def due_date_time(self):
        """
        Gets and sets the dueDateTime
        
        Returns: 
            :class:`DateTimeTimeZone<onedrivesdk.model.date_time_time_zone.DateTimeTimeZone>`:
                The dueDateTime
        """
        if "dueDateTime" in self._prop_dict:
            if isinstance(self._prop_dict["dueDateTime"], OneDriveObjectBase):
                return self._prop_dict["dueDateTime"]
            else :
                self._prop_dict["dueDateTime"] = DateTimeTimeZone(self._prop_dict["dueDateTime"])
                return self._prop_dict["dueDateTime"]

        return None

    @due_date_time.setter
    def due_date_time(self, val):
        self._prop_dict["dueDateTime"] = val
    @property
    def start_date_time(self):
        """
        Gets and sets the startDateTime
        
        Returns: 
            :class:`DateTimeTimeZone<onedrivesdk.model.date_time_time_zone.DateTimeTimeZone>`:
                The startDateTime
        """
        if "startDateTime" in self._prop_dict:
            if isinstance(self._prop_dict["startDateTime"], OneDriveObjectBase):
                return self._prop_dict["startDateTime"]
            else :
                self._prop_dict["startDateTime"] = DateTimeTimeZone(self._prop_dict["startDateTime"])
                return self._prop_dict["startDateTime"]

        return None

    @start_date_time.setter
    def start_date_time(self, val):
        self._prop_dict["startDateTime"] = val
    @property
    def flag_status(self):
        """
        Gets and sets the flagStatus
        
        Returns: 
            :class:`FollowupFlagStatus<onedrivesdk.model.followup_flag_status.FollowupFlagStatus>`:
                The flagStatus
        """
        if "flagStatus" in self._prop_dict:
            if isinstance(self._prop_dict["flagStatus"], OneDriveObjectBase):
                return self._prop_dict["flagStatus"]
            else :
                self._prop_dict["flagStatus"] = FollowupFlagStatus(self._prop_dict["flagStatus"])
                return self._prop_dict["flagStatus"]

        return None

    @flag_status.setter
    def flag_status(self, val):
        self._prop_dict["flagStatus"] = val
