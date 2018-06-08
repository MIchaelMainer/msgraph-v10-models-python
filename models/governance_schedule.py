# -*- coding: utf-8 -*- 
'''
# Copyright (c) Microsoft Corporation.  All Rights Reserved.  Licensed under the MIT License.  See License in the project root for license information.
# 
#  This file was generated and any changes will be overwritten.
'''

from __future__ import unicode_literals
from ..model.duration import Duration
from datetime import datetime
from ..one_drive_object_base import OneDriveObjectBase


class GovernanceSchedule(OneDriveObjectBase):

    def __init__(self, prop_dict={}):
        self._prop_dict = prop_dict

    @property
    def type(self):
        """Gets and sets the type
        
        Returns: 
            str:
                The type
        """
        if "type" in self._prop_dict:
            return self._prop_dict["type"]
        else:
            return None

    @type.setter
    def type(self, val):
        self._prop_dict["type"] = val

    @property
    def start_date_time(self):
        """Gets and sets the startDateTime
        
        Returns: 
            datetime:
                The startDateTime
        """
        if "startDateTime" in self._prop_dict:
            return datetime.strptime(self._prop_dict["startDateTime"].replace("Z", ""), "%Y-%m-%dT%H:%M:%S.%f")
        else:
            return None

    @start_date_time.setter
    def start_date_time(self, val):
        self._prop_dict["startDateTime"] = val.isoformat()+"Z"

    @property
    def end_date_time(self):
        """Gets and sets the endDateTime
        
        Returns: 
            datetime:
                The endDateTime
        """
        if "endDateTime" in self._prop_dict:
            return datetime.strptime(self._prop_dict["endDateTime"].replace("Z", ""), "%Y-%m-%dT%H:%M:%S.%f")
        else:
            return None

    @end_date_time.setter
    def end_date_time(self, val):
        self._prop_dict["endDateTime"] = val.isoformat()+"Z"

    @property
    def duration(self):
        """
        Gets and sets the duration
        
        Returns: 
            :class:`Duration<onedrivesdk.model.duration.Duration>`:
                The duration
        """
        if "duration" in self._prop_dict:
            if isinstance(self._prop_dict["duration"], OneDriveObjectBase):
                return self._prop_dict["duration"]
            else :
                self._prop_dict["duration"] = Duration(self._prop_dict["duration"])
                return self._prop_dict["duration"]

        return None

    @duration.setter
    def duration(self, val):
        self._prop_dict["duration"] = val
