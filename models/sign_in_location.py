# -*- coding: utf-8 -*- 
'''
# Copyright (c) Microsoft Corporation.  All Rights Reserved.  Licensed under the MIT License.  See License in the project root for license information.
# 
#  This file was generated and any changes will be overwritten.
'''

from __future__ import unicode_literals
from ..model.geo_coordinates import GeoCoordinates
from ..one_drive_object_base import OneDriveObjectBase


class SignInLocation(OneDriveObjectBase):

    def __init__(self, prop_dict={}):
        self._prop_dict = prop_dict

    @property
    def city(self):
        """Gets and sets the city
        
        Returns: 
            str:
                The city
        """
        if "city" in self._prop_dict:
            return self._prop_dict["city"]
        else:
            return None

    @city.setter
    def city(self, val):
        self._prop_dict["city"] = val

    @property
    def state(self):
        """Gets and sets the state
        
        Returns: 
            str:
                The state
        """
        if "state" in self._prop_dict:
            return self._prop_dict["state"]
        else:
            return None

    @state.setter
    def state(self, val):
        self._prop_dict["state"] = val

    @property
    def country_or_region(self):
        """Gets and sets the countryOrRegion
        
        Returns: 
            str:
                The countryOrRegion
        """
        if "countryOrRegion" in self._prop_dict:
            return self._prop_dict["countryOrRegion"]
        else:
            return None

    @country_or_region.setter
    def country_or_region(self, val):
        self._prop_dict["countryOrRegion"] = val

    @property
    def geo_coordinates(self):
        """
        Gets and sets the geoCoordinates
        
        Returns: 
            :class:`GeoCoordinates<onedrivesdk.model.geo_coordinates.GeoCoordinates>`:
                The geoCoordinates
        """
        if "geoCoordinates" in self._prop_dict:
            if isinstance(self._prop_dict["geoCoordinates"], OneDriveObjectBase):
                return self._prop_dict["geoCoordinates"]
            else :
                self._prop_dict["geoCoordinates"] = GeoCoordinates(self._prop_dict["geoCoordinates"])
                return self._prop_dict["geoCoordinates"]

        return None

    @geo_coordinates.setter
    def geo_coordinates(self, val):
        self._prop_dict["geoCoordinates"] = val
