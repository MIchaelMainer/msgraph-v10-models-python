# -*- coding: utf-8 -*- 
'''
# Copyright (c) Microsoft Corporation.  All Rights Reserved.  Licensed under the MIT License.  See License in the project root for license information.
# 
#  This file was generated and any changes will be overwritten.
'''

from __future__ import unicode_literals
from ..one_drive_object_base import OneDriveObjectBase


class LocationConstraintItem(OneDriveObjectBase):

    def __init__(self, prop_dict={}):
        self._prop_dict = prop_dict

    @property
    def resolve_availability(self):
        """Gets and sets the resolveAvailability
        
        Returns: 
            bool:
                The resolveAvailability
        """
        if "resolveAvailability" in self._prop_dict:
            return self._prop_dict["resolveAvailability"]
        else:
            return None

    @resolve_availability.setter
    def resolve_availability(self, val):
        self._prop_dict["resolveAvailability"] = val

