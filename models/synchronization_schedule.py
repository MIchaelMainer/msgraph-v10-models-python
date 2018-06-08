# -*- coding: utf-8 -*- 
'''
# Copyright (c) Microsoft Corporation.  All Rights Reserved.  Licensed under the MIT License.  See License in the project root for license information.
# 
#  This file was generated and any changes will be overwritten.
'''

from __future__ import unicode_literals
from ..model.duration import Duration
from ..model.synchronization_schedule_state import SynchronizationScheduleState
from datetime import datetime
from ..one_drive_object_base import OneDriveObjectBase


class SynchronizationSchedule(OneDriveObjectBase):

    def __init__(self, prop_dict={}):
        self._prop_dict = prop_dict

    @property
    def expiration(self):
        """Gets and sets the expiration
        
        Returns: 
            datetime:
                The expiration
        """
        if "expiration" in self._prop_dict:
            return datetime.strptime(self._prop_dict["expiration"].replace("Z", ""), "%Y-%m-%dT%H:%M:%S.%f")
        else:
            return None

    @expiration.setter
    def expiration(self, val):
        self._prop_dict["expiration"] = val.isoformat()+"Z"

    @property
    def interval(self):
        """
        Gets and sets the interval
        
        Returns: 
            :class:`Duration<onedrivesdk.model.duration.Duration>`:
                The interval
        """
        if "interval" in self._prop_dict:
            if isinstance(self._prop_dict["interval"], OneDriveObjectBase):
                return self._prop_dict["interval"]
            else :
                self._prop_dict["interval"] = Duration(self._prop_dict["interval"])
                return self._prop_dict["interval"]

        return None

    @interval.setter
    def interval(self, val):
        self._prop_dict["interval"] = val
    @property
    def state(self):
        """
        Gets and sets the state
        
        Returns: 
            :class:`SynchronizationScheduleState<onedrivesdk.model.synchronization_schedule_state.SynchronizationScheduleState>`:
                The state
        """
        if "state" in self._prop_dict:
            if isinstance(self._prop_dict["state"], OneDriveObjectBase):
                return self._prop_dict["state"]
            else :
                self._prop_dict["state"] = SynchronizationScheduleState(self._prop_dict["state"])
                return self._prop_dict["state"]

        return None

    @state.setter
    def state(self, val):
        self._prop_dict["state"] = val
