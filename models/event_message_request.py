# -*- coding: utf-8 -*- 
'''
# Copyright (c) Microsoft Corporation.  All Rights Reserved.  Licensed under the MIT License.  See License in the project root for license information.
# 
#  This file was generated and any changes will be overwritten.
'''

from __future__ import unicode_literals
from ..model.location import Location
from ..model.date_time_time_zone import DateTimeTimeZone
from ..one_drive_object_base import OneDriveObjectBase


class EventMessageRequest(OneDriveObjectBase):

    def __init__(self, prop_dict={}):
        self._prop_dict = prop_dict

    @property
    def previous_location(self):
        """
        Gets and sets the previousLocation
        
        Returns: 
            :class:`Location<onedrivesdk.model.location.Location>`:
                The previousLocation
        """
        if "previousLocation" in self._prop_dict:
            if isinstance(self._prop_dict["previousLocation"], OneDriveObjectBase):
                return self._prop_dict["previousLocation"]
            else :
                self._prop_dict["previousLocation"] = Location(self._prop_dict["previousLocation"])
                return self._prop_dict["previousLocation"]

        return None

    @previous_location.setter
    def previous_location(self, val):
        self._prop_dict["previousLocation"] = val

    @property
    def previous_start_date_time(self):
        """
        Gets and sets the previousStartDateTime
        
        Returns: 
            :class:`DateTimeTimeZone<onedrivesdk.model.date_time_time_zone.DateTimeTimeZone>`:
                The previousStartDateTime
        """
        if "previousStartDateTime" in self._prop_dict:
            if isinstance(self._prop_dict["previousStartDateTime"], OneDriveObjectBase):
                return self._prop_dict["previousStartDateTime"]
            else :
                self._prop_dict["previousStartDateTime"] = DateTimeTimeZone(self._prop_dict["previousStartDateTime"])
                return self._prop_dict["previousStartDateTime"]

        return None

    @previous_start_date_time.setter
    def previous_start_date_time(self, val):
        self._prop_dict["previousStartDateTime"] = val

    @property
    def previous_end_date_time(self):
        """
        Gets and sets the previousEndDateTime
        
        Returns: 
            :class:`DateTimeTimeZone<onedrivesdk.model.date_time_time_zone.DateTimeTimeZone>`:
                The previousEndDateTime
        """
        if "previousEndDateTime" in self._prop_dict:
            if isinstance(self._prop_dict["previousEndDateTime"], OneDriveObjectBase):
                return self._prop_dict["previousEndDateTime"]
            else :
                self._prop_dict["previousEndDateTime"] = DateTimeTimeZone(self._prop_dict["previousEndDateTime"])
                return self._prop_dict["previousEndDateTime"]

        return None

    @previous_end_date_time.setter
    def previous_end_date_time(self, val):
        self._prop_dict["previousEndDateTime"] = val

    @property
    def response_requested(self):
        """
        Gets and sets the responseRequested
        
        Returns:
            bool:
                The responseRequested
        """
        if "responseRequested" in self._prop_dict:
            return self._prop_dict["responseRequested"]
        else:
            return None

    @response_requested.setter
    def response_requested(self, val):
        self._prop_dict["responseRequested"] = val

