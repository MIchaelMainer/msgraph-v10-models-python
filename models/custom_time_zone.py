# -*- coding: utf-8 -*- 
'''
# Copyright (c) Microsoft Corporation.  All Rights Reserved.  Licensed under the MIT License.  See License in the project root for license information.
# 
#  This file was generated and any changes will be overwritten.
'''

from __future__ import unicode_literals
from ..model.standard_time_zone_offset import StandardTimeZoneOffset
from ..model.daylight_time_zone_offset import DaylightTimeZoneOffset
from ..one_drive_object_base import OneDriveObjectBase


class CustomTimeZone(OneDriveObjectBase):

    def __init__(self, prop_dict={}):
        self._prop_dict = prop_dict

    @property
    def bias(self):
        """Gets and sets the bias
        
        Returns: 
            int:
                The bias
        """
        if "bias" in self._prop_dict:
            return self._prop_dict["bias"]
        else:
            return None

    @bias.setter
    def bias(self, val):
        self._prop_dict["bias"] = val

    @property
    def standard_offset(self):
        """
        Gets and sets the standardOffset
        
        Returns: 
            :class:`StandardTimeZoneOffset<onedrivesdk.model.standard_time_zone_offset.StandardTimeZoneOffset>`:
                The standardOffset
        """
        if "standardOffset" in self._prop_dict:
            if isinstance(self._prop_dict["standardOffset"], OneDriveObjectBase):
                return self._prop_dict["standardOffset"]
            else :
                self._prop_dict["standardOffset"] = StandardTimeZoneOffset(self._prop_dict["standardOffset"])
                return self._prop_dict["standardOffset"]

        return None

    @standard_offset.setter
    def standard_offset(self, val):
        self._prop_dict["standardOffset"] = val
    @property
    def daylight_offset(self):
        """
        Gets and sets the daylightOffset
        
        Returns: 
            :class:`DaylightTimeZoneOffset<onedrivesdk.model.daylight_time_zone_offset.DaylightTimeZoneOffset>`:
                The daylightOffset
        """
        if "daylightOffset" in self._prop_dict:
            if isinstance(self._prop_dict["daylightOffset"], OneDriveObjectBase):
                return self._prop_dict["daylightOffset"]
            else :
                self._prop_dict["daylightOffset"] = DaylightTimeZoneOffset(self._prop_dict["daylightOffset"])
                return self._prop_dict["daylightOffset"]

        return None

    @daylight_offset.setter
    def daylight_offset(self, val):
        self._prop_dict["daylightOffset"] = val
