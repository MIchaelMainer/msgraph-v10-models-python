# -*- coding: utf-8 -*- 
'''
# Copyright (c) Microsoft Corporation.  All Rights Reserved.  Licensed under the MIT License.  See License in the project root for license information.
# 
#  This file was generated and any changes will be overwritten.
'''

from __future__ import unicode_literals
from ..one_drive_object_base import OneDriveObjectBase


class OutlookGeoCoordinates(OneDriveObjectBase):

    def __init__(self, prop_dict={}):
        self._prop_dict = prop_dict

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
    def accuracy(self):
        """Gets and sets the accuracy
        
        Returns: 
            float:
                The accuracy
        """
        if "accuracy" in self._prop_dict:
            return self._prop_dict["accuracy"]
        else:
            return None

    @accuracy.setter
    def accuracy(self, val):
        self._prop_dict["accuracy"] = val

    @property
    def altitude_accuracy(self):
        """Gets and sets the altitudeAccuracy
        
        Returns: 
            float:
                The altitudeAccuracy
        """
        if "altitudeAccuracy" in self._prop_dict:
            return self._prop_dict["altitudeAccuracy"]
        else:
            return None

    @altitude_accuracy.setter
    def altitude_accuracy(self, val):
        self._prop_dict["altitudeAccuracy"] = val

