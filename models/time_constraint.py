# -*- coding: utf-8 -*- 
'''
# Copyright (c) Microsoft Corporation.  All Rights Reserved.  Licensed under the MIT License.  See License in the project root for license information.
# 
#  This file was generated and any changes will be overwritten.
'''

from __future__ import unicode_literals
from ..model.activity_domain import ActivityDomain
from ..model.time_slot import TimeSlot
from ..one_drive_object_base import OneDriveObjectBase


class TimeConstraint(OneDriveObjectBase):

    def __init__(self, prop_dict={}):
        self._prop_dict = prop_dict

    @property
    def activity_domain(self):
        """
        Gets and sets the activityDomain
        
        Returns: 
            :class:`ActivityDomain<onedrivesdk.model.activity_domain.ActivityDomain>`:
                The activityDomain
        """
        if "activityDomain" in self._prop_dict:
            if isinstance(self._prop_dict["activityDomain"], OneDriveObjectBase):
                return self._prop_dict["activityDomain"]
            else :
                self._prop_dict["activityDomain"] = ActivityDomain(self._prop_dict["activityDomain"])
                return self._prop_dict["activityDomain"]

        return None

    @activity_domain.setter
    def activity_domain(self, val):
        self._prop_dict["activityDomain"] = val
    @property
    def timeslots(self):
        """
        Gets and sets the timeslots
        
        Returns: 
            :class:`TimeSlot<onedrivesdk.model.time_slot.TimeSlot>`:
                The timeslots
        """
        if "timeslots" in self._prop_dict:
            if isinstance(self._prop_dict["timeslots"], OneDriveObjectBase):
                return self._prop_dict["timeslots"]
            else :
                self._prop_dict["timeslots"] = TimeSlot(self._prop_dict["timeslots"])
                return self._prop_dict["timeslots"]

        return None

    @timeslots.setter
    def timeslots(self, val):
        self._prop_dict["timeslots"] = val
