# -*- coding: utf-8 -*- 
'''
# Copyright (c) Microsoft Corporation.  All Rights Reserved.  Licensed under the MIT License.  See License in the project root for license information.
# 
#  This file was generated and any changes will be overwritten.
'''

from __future__ import unicode_literals
from datetime import datetime
from ..one_drive_object_base import OneDriveObjectBase


class ItemActivityTimeSet(OneDriveObjectBase):

    def __init__(self, prop_dict={}):
        self._prop_dict = prop_dict

    @property
    def last_recorded_date_time(self):
        """Gets and sets the lastRecordedDateTime
        
        Returns: 
            datetime:
                The lastRecordedDateTime
        """
        if "lastRecordedDateTime" in self._prop_dict:
            return datetime.strptime(self._prop_dict["lastRecordedDateTime"].replace("Z", ""), "%Y-%m-%dT%H:%M:%S.%f")
        else:
            return None

    @last_recorded_date_time.setter
    def last_recorded_date_time(self, val):
        self._prop_dict["lastRecordedDateTime"] = val.isoformat()+"Z"

    @property
    def observed_date_time(self):
        """Gets and sets the observedDateTime
        
        Returns: 
            datetime:
                The observedDateTime
        """
        if "observedDateTime" in self._prop_dict:
            return datetime.strptime(self._prop_dict["observedDateTime"].replace("Z", ""), "%Y-%m-%dT%H:%M:%S.%f")
        else:
            return None

    @observed_date_time.setter
    def observed_date_time(self, val):
        self._prop_dict["observedDateTime"] = val.isoformat()+"Z"

    @property
    def recorded_date_time(self):
        """Gets and sets the recordedDateTime
        
        Returns: 
            datetime:
                The recordedDateTime
        """
        if "recordedDateTime" in self._prop_dict:
            return datetime.strptime(self._prop_dict["recordedDateTime"].replace("Z", ""), "%Y-%m-%dT%H:%M:%S.%f")
        else:
            return None

    @recorded_date_time.setter
    def recorded_date_time(self, val):
        self._prop_dict["recordedDateTime"] = val.isoformat()+"Z"

