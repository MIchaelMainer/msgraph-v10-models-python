# -*- coding: utf-8 -*- 
'''
# Copyright (c) Microsoft Corporation.  All Rights Reserved.  Licensed under the MIT License.  See License in the project root for license information.
# 
#  This file was generated and any changes will be overwritten.
'''

from __future__ import unicode_literals
from ..model.physical_address import PhysicalAddress
from ..model.outlook_geo_coordinates import OutlookGeoCoordinates
from ..model.location_type import LocationType
from ..model.location_unique_id_type import LocationUniqueIdType
from ..one_drive_object_base import OneDriveObjectBase


class Location(OneDriveObjectBase):

    def __init__(self, prop_dict={}):
        self._prop_dict = prop_dict

    @property
    def display_name(self):
        """Gets and sets the displayName
        
        Returns: 
            str:
                The displayName
        """
        if "displayName" in self._prop_dict:
            return self._prop_dict["displayName"]
        else:
            return None

    @display_name.setter
    def display_name(self, val):
        self._prop_dict["displayName"] = val

    @property
    def location_email_address(self):
        """Gets and sets the locationEmailAddress
        
        Returns: 
            str:
                The locationEmailAddress
        """
        if "locationEmailAddress" in self._prop_dict:
            return self._prop_dict["locationEmailAddress"]
        else:
            return None

    @location_email_address.setter
    def location_email_address(self, val):
        self._prop_dict["locationEmailAddress"] = val

    @property
    def address(self):
        """
        Gets and sets the address
        
        Returns: 
            :class:`PhysicalAddress<onedrivesdk.model.physical_address.PhysicalAddress>`:
                The address
        """
        if "address" in self._prop_dict:
            if isinstance(self._prop_dict["address"], OneDriveObjectBase):
                return self._prop_dict["address"]
            else :
                self._prop_dict["address"] = PhysicalAddress(self._prop_dict["address"])
                return self._prop_dict["address"]

        return None

    @address.setter
    def address(self, val):
        self._prop_dict["address"] = val
    @property
    def coordinates(self):
        """
        Gets and sets the coordinates
        
        Returns: 
            :class:`OutlookGeoCoordinates<onedrivesdk.model.outlook_geo_coordinates.OutlookGeoCoordinates>`:
                The coordinates
        """
        if "coordinates" in self._prop_dict:
            if isinstance(self._prop_dict["coordinates"], OneDriveObjectBase):
                return self._prop_dict["coordinates"]
            else :
                self._prop_dict["coordinates"] = OutlookGeoCoordinates(self._prop_dict["coordinates"])
                return self._prop_dict["coordinates"]

        return None

    @coordinates.setter
    def coordinates(self, val):
        self._prop_dict["coordinates"] = val
    @property
    def location_uri(self):
        """Gets and sets the locationUri
        
        Returns: 
            str:
                The locationUri
        """
        if "locationUri" in self._prop_dict:
            return self._prop_dict["locationUri"]
        else:
            return None

    @location_uri.setter
    def location_uri(self, val):
        self._prop_dict["locationUri"] = val

    @property
    def location_type(self):
        """
        Gets and sets the locationType
        
        Returns: 
            :class:`LocationType<onedrivesdk.model.location_type.LocationType>`:
                The locationType
        """
        if "locationType" in self._prop_dict:
            if isinstance(self._prop_dict["locationType"], OneDriveObjectBase):
                return self._prop_dict["locationType"]
            else :
                self._prop_dict["locationType"] = LocationType(self._prop_dict["locationType"])
                return self._prop_dict["locationType"]

        return None

    @location_type.setter
    def location_type(self, val):
        self._prop_dict["locationType"] = val
    @property
    def unique_id(self):
        """Gets and sets the uniqueId
        
        Returns: 
            str:
                The uniqueId
        """
        if "uniqueId" in self._prop_dict:
            return self._prop_dict["uniqueId"]
        else:
            return None

    @unique_id.setter
    def unique_id(self, val):
        self._prop_dict["uniqueId"] = val

    @property
    def unique_id_type(self):
        """
        Gets and sets the uniqueIdType
        
        Returns: 
            :class:`LocationUniqueIdType<onedrivesdk.model.location_unique_id_type.LocationUniqueIdType>`:
                The uniqueIdType
        """
        if "uniqueIdType" in self._prop_dict:
            if isinstance(self._prop_dict["uniqueIdType"], OneDriveObjectBase):
                return self._prop_dict["uniqueIdType"]
            else :
                self._prop_dict["uniqueIdType"] = LocationUniqueIdType(self._prop_dict["uniqueIdType"])
                return self._prop_dict["uniqueIdType"]

        return None

    @unique_id_type.setter
    def unique_id_type(self, val):
        self._prop_dict["uniqueIdType"] = val
