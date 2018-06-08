# -*- coding: utf-8 -*- 
'''
# Copyright (c) Microsoft Corporation.  All Rights Reserved.  Licensed under the MIT License.  See License in the project root for license information.
# 
#  This file was generated and any changes will be overwritten.
'''

from __future__ import unicode_literals
from datetime import datetime
from ..one_drive_object_base import OneDriveObjectBase


class DeviceGeoLocation(OneDriveObjectBase):

    def __init__(self, prop_dict={}):
        self._prop_dict = prop_dict

    @property
    def last_collected_date_time_utc(self):
        """Gets and sets the lastCollectedDateTimeUtc
        
        Returns: 
            datetime:
                The lastCollectedDateTimeUtc
        """
        if "lastCollectedDateTimeUtc" in self._prop_dict:
            return datetime.strptime(self._prop_dict["lastCollectedDateTimeUtc"].replace("Z", ""), "%Y-%m-%dT%H:%M:%S.%f")
        else:
            return None

    @last_collected_date_time_utc.setter
    def last_collected_date_time_utc(self, val):
        self._prop_dict["lastCollectedDateTimeUtc"] = val.isoformat()+"Z"

    @property
    def last_collected_date_time(self):
        """Gets and sets the lastCollectedDateTime
        
        Returns: 
            datetime:
                The lastCollectedDateTime
        """
        if "lastCollectedDateTime" in self._prop_dict:
            return datetime.strptime(self._prop_dict["lastCollectedDateTime"].replace("Z", ""), "%Y-%m-%dT%H:%M:%S.%f")
        else:
            return None

    @last_collected_date_time.setter
    def last_collected_date_time(self, val):
        self._prop_dict["lastCollectedDateTime"] = val.isoformat()+"Z"

    @property
    def longitude(self):
        """Gets and sets the longitude
        
        Returns: 
            float:
                The longitude
        """
        if "longitude" in self._prop_dict:
            return self._prop_dict["longitude"]
        else:
            return None

    @longitude.setter
    def longitude(self, val):
        self._prop_dict["longitude"] = val

    @property
    def latitude(self):
        """Gets and sets the latitude
        
        Returns: 
            float:
                The latitude
        """
        if "latitude" in self._prop_dict:
            return self._prop_dict["latitude"]
        else:
            return None

    @latitude.setter
    def latitude(self, val):
        self._prop_dict["latitude"] = val

    @property
    def altitude(self):
        """Gets and sets the altitude
        
        Returns: 
            float:
                The altitude
        """
        if "altitude" in self._prop_dict:
            return self._prop_dict["altitude"]
        else:
            return None

    @altitude.setter
    def altitude(self, val):
        self._prop_dict["altitude"] = val

    @property
    def horizontal_accuracy(self):
        """Gets and sets the horizontalAccuracy
        
        Returns: 
            float:
                The horizontalAccuracy
        """
        if "horizontalAccuracy" in self._prop_dict:
            return self._prop_dict["horizontalAccuracy"]
        else:
            return None

    @horizontal_accuracy.setter
    def horizontal_accuracy(self, val):
        self._prop_dict["horizontalAccuracy"] = val

    @property
    def vertical_accuracy(self):
        """Gets and sets the verticalAccuracy
        
        Returns: 
            float:
                The verticalAccuracy
        """
        if "verticalAccuracy" in self._prop_dict:
            return self._prop_dict["verticalAccuracy"]
        else:
            return None

    @vertical_accuracy.setter
    def vertical_accuracy(self, val):
        self._prop_dict["verticalAccuracy"] = val

    @property
    def heading(self):
        """Gets and sets the heading
        
        Returns: 
            float:
                The heading
        """
        if "heading" in self._prop_dict:
            return self._prop_dict["heading"]
        else:
            return None

    @heading.setter
    def heading(self, val):
        self._prop_dict["heading"] = val

    @property
    def speed(self):
        """Gets and sets the speed
        
        Returns: 
            float:
                The speed
        """
        if "speed" in self._prop_dict:
            return self._prop_dict["speed"]
        else:
            return None

    @speed.setter
    def speed(self, val):
        self._prop_dict["speed"] = val

