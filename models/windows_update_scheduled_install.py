# -*- coding: utf-8 -*- 
'''
# Copyright (c) Microsoft Corporation.  All Rights Reserved.  Licensed under the MIT License.  See License in the project root for license information.
# 
#  This file was generated and any changes will be overwritten.
'''

from __future__ import unicode_literals
from ..model.weekly_schedule import WeeklySchedule
from ..model.time_of_day import TimeOfDay
from ..one_drive_object_base import OneDriveObjectBase


class WindowsUpdateScheduledInstall(OneDriveObjectBase):

    def __init__(self, prop_dict={}):
        self._prop_dict = prop_dict

    @property
    def scheduled_install_day(self):
        """
        Gets and sets the scheduledInstallDay
        
        Returns: 
            :class:`WeeklySchedule<onedrivesdk.model.weekly_schedule.WeeklySchedule>`:
                The scheduledInstallDay
        """
        if "scheduledInstallDay" in self._prop_dict:
            if isinstance(self._prop_dict["scheduledInstallDay"], OneDriveObjectBase):
                return self._prop_dict["scheduledInstallDay"]
            else :
                self._prop_dict["scheduledInstallDay"] = WeeklySchedule(self._prop_dict["scheduledInstallDay"])
                return self._prop_dict["scheduledInstallDay"]

        return None

    @scheduled_install_day.setter
    def scheduled_install_day(self, val):
        self._prop_dict["scheduledInstallDay"] = val
    @property
    def scheduled_install_time(self):
        """
        Gets and sets the scheduledInstallTime
        
        Returns: 
            :class:`TimeOfDay<onedrivesdk.model.time_of_day.TimeOfDay>`:
                The scheduledInstallTime
        """
        if "scheduledInstallTime" in self._prop_dict:
            if isinstance(self._prop_dict["scheduledInstallTime"], OneDriveObjectBase):
                return self._prop_dict["scheduledInstallTime"]
            else :
                self._prop_dict["scheduledInstallTime"] = TimeOfDay(self._prop_dict["scheduledInstallTime"])
                return self._prop_dict["scheduledInstallTime"]

        return None

    @scheduled_install_time.setter
    def scheduled_install_time(self, val):
        self._prop_dict["scheduledInstallTime"] = val
