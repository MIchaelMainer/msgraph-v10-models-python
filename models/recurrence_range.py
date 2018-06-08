# -*- coding: utf-8 -*- 
'''
# Copyright (c) Microsoft Corporation.  All Rights Reserved.  Licensed under the MIT License.  See License in the project root for license information.
# 
#  This file was generated and any changes will be overwritten.
'''

from __future__ import unicode_literals
from ..model.recurrence_range_type import RecurrenceRangeType
from ..model.date import Date
from ..one_drive_object_base import OneDriveObjectBase


class RecurrenceRange(OneDriveObjectBase):

    def __init__(self, prop_dict={}):
        self._prop_dict = prop_dict

    @property
    def type(self):
        """
        Gets and sets the type
        
        Returns: 
            :class:`RecurrenceRangeType<onedrivesdk.model.recurrence_range_type.RecurrenceRangeType>`:
                The type
        """
        if "type" in self._prop_dict:
            if isinstance(self._prop_dict["type"], OneDriveObjectBase):
                return self._prop_dict["type"]
            else :
                self._prop_dict["type"] = RecurrenceRangeType(self._prop_dict["type"])
                return self._prop_dict["type"]

        return None

    @type.setter
    def type(self, val):
        self._prop_dict["type"] = val
    @property
    def start_date(self):
        """
        Gets and sets the startDate
        
        Returns: 
            :class:`Date<onedrivesdk.model.date.Date>`:
                The startDate
        """
        if "startDate" in self._prop_dict:
            if isinstance(self._prop_dict["startDate"], OneDriveObjectBase):
                return self._prop_dict["startDate"]
            else :
                self._prop_dict["startDate"] = Date(self._prop_dict["startDate"])
                return self._prop_dict["startDate"]

        return None

    @start_date.setter
    def start_date(self, val):
        self._prop_dict["startDate"] = val
    @property
    def end_date(self):
        """
        Gets and sets the endDate
        
        Returns: 
            :class:`Date<onedrivesdk.model.date.Date>`:
                The endDate
        """
        if "endDate" in self._prop_dict:
            if isinstance(self._prop_dict["endDate"], OneDriveObjectBase):
                return self._prop_dict["endDate"]
            else :
                self._prop_dict["endDate"] = Date(self._prop_dict["endDate"])
                return self._prop_dict["endDate"]

        return None

    @end_date.setter
    def end_date(self, val):
        self._prop_dict["endDate"] = val
    @property
    def recurrence_time_zone(self):
        """Gets and sets the recurrenceTimeZone
        
        Returns: 
            str:
                The recurrenceTimeZone
        """
        if "recurrenceTimeZone" in self._prop_dict:
            return self._prop_dict["recurrenceTimeZone"]
        else:
            return None

    @recurrence_time_zone.setter
    def recurrence_time_zone(self, val):
        self._prop_dict["recurrenceTimeZone"] = val

    @property
    def number_of_occurrences(self):
        """Gets and sets the numberOfOccurrences
        
        Returns: 
            int:
                The numberOfOccurrences
        """
        if "numberOfOccurrences" in self._prop_dict:
            return self._prop_dict["numberOfOccurrences"]
        else:
            return None

    @number_of_occurrences.setter
    def number_of_occurrences(self, val):
        self._prop_dict["numberOfOccurrences"] = val

