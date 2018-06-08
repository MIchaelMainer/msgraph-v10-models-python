# -*- coding: utf-8 -*- 
'''
# Copyright (c) Microsoft Corporation.  All Rights Reserved.  Licensed under the MIT License.  See License in the project root for license information.
# 
#  This file was generated and any changes will be overwritten.
'''

from __future__ import unicode_literals
from ..model.device_geo_location import DeviceGeoLocation
from ..one_drive_object_base import OneDriveObjectBase


class LocateDeviceActionResult(OneDriveObjectBase):

    def __init__(self, prop_dict={}):
        self._prop_dict = prop_dict

    @property
    def device_location(self):
        """
        Gets and sets the deviceLocation
        
        Returns: 
            :class:`DeviceGeoLocation<onedrivesdk.model.device_geo_location.DeviceGeoLocation>`:
                The deviceLocation
        """
        if "deviceLocation" in self._prop_dict:
            if isinstance(self._prop_dict["deviceLocation"], OneDriveObjectBase):
                return self._prop_dict["deviceLocation"]
            else :
                self._prop_dict["deviceLocation"] = DeviceGeoLocation(self._prop_dict["deviceLocation"])
                return self._prop_dict["deviceLocation"]

        return None

    @device_location.setter
    def device_location(self, val):
        self._prop_dict["deviceLocation"] = val
