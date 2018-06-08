# -*- coding: utf-8 -*- 
'''
# Copyright (c) Microsoft Corporation.  All Rights Reserved.  Licensed under the MIT License.  See License in the project root for license information.
# 
#  This file was generated and any changes will be overwritten.
'''

from __future__ import unicode_literals
from ..model.date import Date
from ..model.time_of_day import TimeOfDay
from ..one_drive_object_base import OneDriveObjectBase


class TimeStamp(OneDriveObjectBase):

    def __init__(self, prop_dict={}):
        self._prop_dict = prop_dict

    @property
    def date(self):
        """
        Gets and sets the date
        
        Returns: 
            :class:`Date<onedrivesdk.model.date.Date>`:
                The date
        """
        if "date" in self._prop_dict:
            if isinstance(self._prop_dict["date"], OneDriveObjectBase):
                return self._prop_dict["date"]
            else :
                self._prop_dict["date"] = Date(self._prop_dict["date"])
                return self._prop_dict["date"]

        return None

    @date.setter
    def date(self, val):
        self._prop_dict["date"] = val
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
    def time_zone(self):
        """Gets and sets the timeZone
        
        Returns: 
            str:
                The timeZone
        """
        if "timeZone" in self._prop_dict:
            return self._prop_dict["timeZone"]
        else:
            return None

    @time_zone.setter
    def time_zone(self, val):
        self._prop_dict["timeZone"] = val

