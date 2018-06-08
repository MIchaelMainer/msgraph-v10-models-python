# -*- coding: utf-8 -*- 
'''
# Copyright (c) Microsoft Corporation.  All Rights Reserved.  Licensed under the MIT License.  See License in the project root for license information.
# 
#  This file was generated and any changes will be overwritten.
'''

from __future__ import unicode_literals
from ..model.day_of_week import DayOfWeek
from ..model.time_of_day import TimeOfDay
from ..model.time_zone_base import TimeZoneBase
from ..one_drive_object_base import OneDriveObjectBase


class WorkingHours(OneDriveObjectBase):

    def __init__(self, prop_dict={}):
        self._prop_dict = prop_dict

    @property
    def days_of_week(self):
        """
        Gets and sets the daysOfWeek
        
        Returns: 
            :class:`DayOfWeek<onedrivesdk.model.day_of_week.DayOfWeek>`:
                The daysOfWeek
        """
        if "daysOfWeek" in self._prop_dict:
            if isinstance(self._prop_dict["daysOfWeek"], OneDriveObjectBase):
                return self._prop_dict["daysOfWeek"]
            else :
                self._prop_dict["daysOfWeek"] = DayOfWeek(self._prop_dict["daysOfWeek"])
                return self._prop_dict["daysOfWeek"]

        return None

    @days_of_week.setter
    def days_of_week(self, val):
        self._prop_dict["daysOfWeek"] = val
    @property
    def start_time(self):
        """
        Gets and sets the startTime
        
        Returns: 
            :class:`TimeOfDay<onedrivesdk.model.time_of_day.TimeOfDay>`:
                The startTime
        """
        if "startTime" in self._prop_dict:
            if isinstance(self._prop_dict["startTime"], OneDriveObjectBase):
                return self._prop_dict["startTime"]
            else :
                self._prop_dict["startTime"] = TimeOfDay(self._prop_dict["startTime"])
                return self._prop_dict["startTime"]

        return None

    @start_time.setter
    def start_time(self, val):
        self._prop_dict["startTime"] = val
    @property
    def end_time(self):
        """
        Gets and sets the endTime
        
        Returns: 
            :class:`TimeOfDay<onedrivesdk.model.time_of_day.TimeOfDay>`:
                The endTime
        """
        if "endTime" in self._prop_dict:
            if isinstance(self._prop_dict["endTime"], OneDriveObjectBase):
                return self._prop_dict["endTime"]
            else :
                self._prop_dict["endTime"] = TimeOfDay(self._prop_dict["endTime"])
                return self._prop_dict["endTime"]

        return None

    @end_time.setter
    def end_time(self, val):
        self._prop_dict["endTime"] = val
    @property
    def time_zone(self):
        """
        Gets and sets the timeZone
        
        Returns: 
            :class:`TimeZoneBase<onedrivesdk.model.time_zone_base.TimeZoneBase>`:
                The timeZone
        """
        if "timeZone" in self._prop_dict:
            if isinstance(self._prop_dict["timeZone"], OneDriveObjectBase):
                return self._prop_dict["timeZone"]
            else :
                self._prop_dict["timeZone"] = TimeZoneBase(self._prop_dict["timeZone"])
                return self._prop_dict["timeZone"]

        return None

    @time_zone.setter
    def time_zone(self, val):
        self._prop_dict["timeZone"] = val
