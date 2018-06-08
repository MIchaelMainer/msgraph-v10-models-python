# -*- coding: utf-8 -*- 
'''
# Copyright (c) Microsoft Corporation.  All Rights Reserved.  Licensed under the MIT License.  See License in the project root for license information.
# 
#  This file was generated and any changes will be overwritten.
'''

from __future__ import unicode_literals
from ..model.location_constraint_item import LocationConstraintItem
from ..one_drive_object_base import OneDriveObjectBase


class LocationConstraint(OneDriveObjectBase):

    def __init__(self, prop_dict={}):
        self._prop_dict = prop_dict

    @property
    def is_required(self):
        """Gets and sets the isRequired
        
        Returns: 
            bool:
                The isRequired
        """
        if "isRequired" in self._prop_dict:
            return self._prop_dict["isRequired"]
        else:
            return None

    @is_required.setter
    def is_required(self, val):
        self._prop_dict["isRequired"] = val

    @property
    def suggest_location(self):
        """Gets and sets the suggestLocation
        
        Returns: 
            bool:
                The suggestLocation
        """
        if "suggestLocation" in self._prop_dict:
            return self._prop_dict["suggestLocation"]
        else:
            return None

    @suggest_location.setter
    def suggest_location(self, val):
        self._prop_dict["suggestLocation"] = val

    @property
    def locations(self):
        """
        Gets and sets the locations
        
        Returns: 
            :class:`LocationConstraintItem<onedrivesdk.model.location_constraint_item.LocationConstraintItem>`:
                The locations
        """
        if "locations" in self._prop_dict:
            if isinstance(self._prop_dict["locations"], OneDriveObjectBase):
                return self._prop_dict["locations"]
            else :
                self._prop_dict["locations"] = LocationConstraintItem(self._prop_dict["locations"])
                return self._prop_dict["locations"]

        return None

    @locations.setter
    def locations(self, val):
        self._prop_dict["locations"] = val
