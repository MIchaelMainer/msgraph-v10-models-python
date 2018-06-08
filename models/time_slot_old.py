# -*- coding: utf-8 -*- 
'''
# Copyright (c) Microsoft Corporation.  All Rights Reserved.  Licensed under the MIT License.  See License in the project root for license information.
# 
#  This file was generated and any changes will be overwritten.
'''

from __future__ import unicode_literals
from ..model.time_stamp import TimeStamp
from ..one_drive_object_base import OneDriveObjectBase


class TimeSlotOLD(OneDriveObjectBase):

    def __init__(self, prop_dict={}):
        self._prop_dict = prop_dict

    @property
    def start(self):
        """
        Gets and sets the start
        
        Returns: 
            :class:`TimeStamp<onedrivesdk.model.time_stamp.TimeStamp>`:
                The start
        """
        if "start" in self._prop_dict:
            if isinstance(self._prop_dict["start"], OneDriveObjectBase):
                return self._prop_dict["start"]
            else :
                self._prop_dict["start"] = TimeStamp(self._prop_dict["start"])
                return self._prop_dict["start"]

        return None

    @start.setter
    def start(self, val):
        self._prop_dict["start"] = val
    @property
    def end(self):
        """
        Gets and sets the end
        
        Returns: 
            :class:`TimeStamp<onedrivesdk.model.time_stamp.TimeStamp>`:
                The end
        """
        if "end" in self._prop_dict:
            if isinstance(self._prop_dict["end"], OneDriveObjectBase):
                return self._prop_dict["end"]
            else :
                self._prop_dict["end"] = TimeStamp(self._prop_dict["end"])
                return self._prop_dict["end"]

        return None

    @end.setter
    def end(self, val):
        self._prop_dict["end"] = val
