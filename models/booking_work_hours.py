# -*- coding: utf-8 -*- 
'''
# Copyright (c) Microsoft Corporation.  All Rights Reserved.  Licensed under the MIT License.  See License in the project root for license information.
# 
#  This file was generated and any changes will be overwritten.
'''

from __future__ import unicode_literals
from ..model.day_of_week import DayOfWeek
from ..model.booking_work_time_slot import BookingWorkTimeSlot
from ..one_drive_object_base import OneDriveObjectBase


class BookingWorkHours(OneDriveObjectBase):

    def __init__(self, prop_dict={}):
        self._prop_dict = prop_dict

    @property
    def day(self):
        """
        Gets and sets the day
        
        Returns: 
            :class:`DayOfWeek<onedrivesdk.model.day_of_week.DayOfWeek>`:
                The day
        """
        if "day" in self._prop_dict:
            if isinstance(self._prop_dict["day"], OneDriveObjectBase):
                return self._prop_dict["day"]
            else :
                self._prop_dict["day"] = DayOfWeek(self._prop_dict["day"])
                return self._prop_dict["day"]

        return None

    @day.setter
    def day(self, val):
        self._prop_dict["day"] = val
    @property
    def time_slots(self):
        """
        Gets and sets the timeSlots
        
        Returns: 
            :class:`BookingWorkTimeSlot<onedrivesdk.model.booking_work_time_slot.BookingWorkTimeSlot>`:
                The timeSlots
        """
        if "timeSlots" in self._prop_dict:
            if isinstance(self._prop_dict["timeSlots"], OneDriveObjectBase):
                return self._prop_dict["timeSlots"]
            else :
                self._prop_dict["timeSlots"] = BookingWorkTimeSlot(self._prop_dict["timeSlots"])
                return self._prop_dict["timeSlots"]

        return None

    @time_slots.setter
    def time_slots(self, val):
        self._prop_dict["timeSlots"] = val
