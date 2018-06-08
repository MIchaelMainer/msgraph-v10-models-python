# -*- coding: utf-8 -*- 
'''
# Copyright (c) Microsoft Corporation.  All Rights Reserved.  Licensed under the MIT License.  See License in the project root for license information.
# 
#  This file was generated and any changes will be overwritten.
'''

from __future__ import unicode_literals
from ..model.time_of_day import TimeOfDay
from ..one_drive_object_base import OneDriveObjectBase


class WindowsUpdateActiveHoursInstall(OneDriveObjectBase):

    def __init__(self, prop_dict={}):
        self._prop_dict = prop_dict

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
