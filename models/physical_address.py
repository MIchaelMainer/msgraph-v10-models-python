# -*- coding: utf-8 -*- 
'''
# Copyright (c) Microsoft Corporation.  All Rights Reserved.  Licensed under the MIT License.  See License in the project root for license information.
# 
#  This file was generated and any changes will be overwritten.
'''

from __future__ import unicode_literals
from ..model.physical_address_type import PhysicalAddressType
from ..one_drive_object_base import OneDriveObjectBase


class PhysicalAddress(OneDriveObjectBase):

    def __init__(self, prop_dict={}):
        self._prop_dict = prop_dict

    @property
    def type(self):
        """
        Gets and sets the type
        
        Returns: 
            :class:`PhysicalAddressType<onedrivesdk.model.physical_address_type.PhysicalAddressType>`:
                The type
        """
        if "type" in self._prop_dict:
            if isinstance(self._prop_dict["type"], OneDriveObjectBase):
                return self._prop_dict["type"]
            else :
                self._prop_dict["type"] = PhysicalAddressType(self._prop_dict["type"])
                return self._prop_dict["type"]

        return None

    @type.setter
    def type(self, val):
        self._prop_dict["type"] = val
    @property
    def post_office_box(self):
        """Gets and sets the postOfficeBox
        
        Returns: 
            str:
                The postOfficeBox
        """
        if "postOfficeBox" in self._prop_dict:
            return self._prop_dict["postOfficeBox"]
        else:
            return None

    @post_office_box.setter
    def post_office_box(self, val):
        self._prop_dict["postOfficeBox"] = val

    @property
    def street(self):
        """Gets and sets the street
        
        Returns: 
            str:
                The street
        """
        if "street" in self._prop_dict:
            return self._prop_dict["street"]
        else:
            return None

    @street.setter
    def street(self, val):
        self._prop_dict["street"] = val

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
    def postal_code(self):
        """Gets and sets the postalCode
        
        Returns: 
            str:
                The postalCode
        """
        if "postalCode" in self._prop_dict:
            return self._prop_dict["postalCode"]
        else:
            return None

    @postal_code.setter
    def postal_code(self, val):
        self._prop_dict["postalCode"] = val

