# -*- coding: utf-8 -*- 
'''
# Copyright (c) Microsoft Corporation.  All Rights Reserved.  Licensed under the MIT License.  See License in the project root for license information.
# 
#  This file was generated and any changes will be overwritten.
'''

from __future__ import unicode_literals
from ..model.duration import Duration
from ..one_drive_object_base import OneDriveObjectBase


class BookingSchedulingPolicy(OneDriveObjectBase):

    def __init__(self, prop_dict={}):
        self._prop_dict = prop_dict

    @property
    def time_slot_interval(self):
        """
        Gets and sets the timeSlotInterval
        
        Returns: 
            :class:`Duration<onedrivesdk.model.duration.Duration>`:
                The timeSlotInterval
        """
        if "timeSlotInterval" in self._prop_dict:
            if isinstance(self._prop_dict["timeSlotInterval"], OneDriveObjectBase):
                return self._prop_dict["timeSlotInterval"]
            else :
                self._prop_dict["timeSlotInterval"] = Duration(self._prop_dict["timeSlotInterval"])
                return self._prop_dict["timeSlotInterval"]

        return None

    @time_slot_interval.setter
    def time_slot_interval(self, val):
        self._prop_dict["timeSlotInterval"] = val
    @property
    def minimum_lead_time(self):
        """
        Gets and sets the minimumLeadTime
        
        Returns: 
            :class:`Duration<onedrivesdk.model.duration.Duration>`:
                The minimumLeadTime
        """
        if "minimumLeadTime" in self._prop_dict:
            if isinstance(self._prop_dict["minimumLeadTime"], OneDriveObjectBase):
                return self._prop_dict["minimumLeadTime"]
            else :
                self._prop_dict["minimumLeadTime"] = Duration(self._prop_dict["minimumLeadTime"])
                return self._prop_dict["minimumLeadTime"]

        return None

    @minimum_lead_time.setter
    def minimum_lead_time(self, val):
        self._prop_dict["minimumLeadTime"] = val
    @property
    def maximum_advance(self):
        """
        Gets and sets the maximumAdvance
        
        Returns: 
            :class:`Duration<onedrivesdk.model.duration.Duration>`:
                The maximumAdvance
        """
        if "maximumAdvance" in self._prop_dict:
            if isinstance(self._prop_dict["maximumAdvance"], OneDriveObjectBase):
                return self._prop_dict["maximumAdvance"]
            else :
                self._prop_dict["maximumAdvance"] = Duration(self._prop_dict["maximumAdvance"])
                return self._prop_dict["maximumAdvance"]

        return None

    @maximum_advance.setter
    def maximum_advance(self, val):
        self._prop_dict["maximumAdvance"] = val
    @property
    def send_confirmations_to_owner(self):
        """Gets and sets the sendConfirmationsToOwner
        
        Returns: 
            bool:
                The sendConfirmationsToOwner
        """
        if "sendConfirmationsToOwner" in self._prop_dict:
            return self._prop_dict["sendConfirmationsToOwner"]
        else:
            return None

    @send_confirmations_to_owner.setter
    def send_confirmations_to_owner(self, val):
        self._prop_dict["sendConfirmationsToOwner"] = val

    @property
    def allow_staff_selection(self):
        """Gets and sets the allowStaffSelection
        
        Returns: 
            bool:
                The allowStaffSelection
        """
        if "allowStaffSelection" in self._prop_dict:
            return self._prop_dict["allowStaffSelection"]
        else:
            return None

    @allow_staff_selection.setter
    def allow_staff_selection(self, val):
        self._prop_dict["allowStaffSelection"] = val

