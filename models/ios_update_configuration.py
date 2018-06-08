# -*- coding: utf-8 -*- 
'''
# Copyright (c) Microsoft Corporation.  All Rights Reserved.  Licensed under the MIT License.  See License in the project root for license information.
# 
#  This file was generated and any changes will be overwritten.
'''

from __future__ import unicode_literals
from ..model.time_of_day import TimeOfDay
from ..model.day_of_week import DayOfWeek
from ..one_drive_object_base import OneDriveObjectBase


class IosUpdateConfiguration(OneDriveObjectBase):

    def __init__(self, prop_dict={}):
        self._prop_dict = prop_dict

    @property
    def is_enabled(self):
        """
        Gets and sets the isEnabled
        
        Returns:
            bool:
                The isEnabled
        """
        if "isEnabled" in self._prop_dict:
            return self._prop_dict["isEnabled"]
        else:
            return None

    @is_enabled.setter
    def is_enabled(self, val):
        self._prop_dict["isEnabled"] = val

    @property
    def active_hours_start(self):
        """
        Gets and sets the activeHoursStart
        
        Returns: 
            :class:`TimeOfDay<onedrivesdk.model.time_of_day.TimeOfDay>`:
                The activeHoursStart
        """
        if "activeHoursStart" in self._prop_dict:
            if isinstance(self._prop_dict["activeHoursStart"], OneDriveObjectBase):
                return self._prop_dict["activeHoursStart"]
            else :
                self._prop_dict["activeHoursStart"] = TimeOfDay(self._prop_dict["activeHoursStart"])
                return self._prop_dict["activeHoursStart"]

        return None

    @active_hours_start.setter
    def active_hours_start(self, val):
        self._prop_dict["activeHoursStart"] = val

    @property
    def active_hours_end(self):
        """
        Gets and sets the activeHoursEnd
        
        Returns: 
            :class:`TimeOfDay<onedrivesdk.model.time_of_day.TimeOfDay>`:
                The activeHoursEnd
        """
        if "activeHoursEnd" in self._prop_dict:
            if isinstance(self._prop_dict["activeHoursEnd"], OneDriveObjectBase):
                return self._prop_dict["activeHoursEnd"]
            else :
                self._prop_dict["activeHoursEnd"] = TimeOfDay(self._prop_dict["activeHoursEnd"])
                return self._prop_dict["activeHoursEnd"]

        return None

    @active_hours_end.setter
    def active_hours_end(self, val):
        self._prop_dict["activeHoursEnd"] = val

    @property
    def scheduled_install_days(self):
        """Gets and sets the scheduledInstallDays
        
        Returns: 
            :class:`ScheduledInstallDaysCollectionPage<onedrivesdk.request.scheduled_install_days_collection.ScheduledInstallDaysCollectionPage>`:
                The scheduledInstallDays
        """
        if "scheduledInstallDays" in self._prop_dict:
            return ScheduledInstallDaysCollectionPage(self._prop_dict["scheduledInstallDays"])
        else:
            return None

    @property
    def utc_time_offset_in_minutes(self):
        """
        Gets and sets the utcTimeOffsetInMinutes
        
        Returns:
            int:
                The utcTimeOffsetInMinutes
        """
        if "utcTimeOffsetInMinutes" in self._prop_dict:
            return self._prop_dict["utcTimeOffsetInMinutes"]
        else:
            return None

    @utc_time_offset_in_minutes.setter
    def utc_time_offset_in_minutes(self, val):
        self._prop_dict["utcTimeOffsetInMinutes"] = val

