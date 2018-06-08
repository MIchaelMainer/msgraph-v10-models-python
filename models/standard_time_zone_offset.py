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


class StandardTimeZoneOffset(OneDriveObjectBase):

    def __init__(self, prop_dict={}):
        self._prop_dict = prop_dict

    @property
    def time(self):
        """
        Gets and sets the time
        
        Returns: 
            :class:`TimeOfDay<onedrivesdk.model.time_of_day.TimeOfDay>`:
                The time
        """
        if "time" in self._prop_dict:
            if isinstance(self._prop_dict["time"], OneDriveObjectBase):
                return self._prop_dict["time"]
            else :
                self._prop_dict["time"] = TimeOfDay(self._prop_dict["time"])
                return self._prop_dict["time"]

        return None

    @time.setter
    def time(self, val):
        self._prop_dict["time"] = val
    @property
    def day_occurrence(self):
        """Gets and sets the dayOccurrence
        
        Returns: 
            int:
                The dayOccurrence
        """
        if "dayOccurrence" in self._prop_dict:
            return self._prop_dict["dayOccurrence"]
        else:
            return None

    @day_occurrence.setter
    def day_occurrence(self, val):
        self._prop_dict["dayOccurrence"] = val

    @property
    def day_of_week(self):
        """
        Gets and sets the dayOfWeek
        
        Returns: 
            :class:`DayOfWeek<onedrivesdk.model.day_of_week.DayOfWeek>`:
                The dayOfWeek
        """
        if "dayOfWeek" in self._prop_dict:
            if isinstance(self._prop_dict["dayOfWeek"], OneDriveObjectBase):
                return self._prop_dict["dayOfWeek"]
            else :
                self._prop_dict["dayOfWeek"] = DayOfWeek(self._prop_dict["dayOfWeek"])
                return self._prop_dict["dayOfWeek"]

        return None

    @day_of_week.setter
    def day_of_week(self, val):
        self._prop_dict["dayOfWeek"] = val
    @property
    def month(self):
        """Gets and sets the month
        
        Returns: 
            int:
                The month
        """
        if "month" in self._prop_dict:
            return self._prop_dict["month"]
        else:
            return None

    @month.setter
    def month(self, val):
        self._prop_dict["month"] = val

    @property
    def year(self):
        """Gets and sets the year
        
        Returns: 
            int:
                The year
        """
        if "year" in self._prop_dict:
            return self._prop_dict["year"]
        else:
            return None

    @year.setter
    def year(self, val):
        self._prop_dict["year"] = val

