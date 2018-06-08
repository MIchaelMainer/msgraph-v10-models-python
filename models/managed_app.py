# -*- coding: utf-8 -*- 
'''
# Copyright (c) Microsoft Corporation.  All Rights Reserved.  Licensed under the MIT License.  See License in the project root for license information.
# 
#  This file was generated and any changes will be overwritten.
'''

from __future__ import unicode_literals
from ..model.managed_app_availability import ManagedAppAvailability
from ..one_drive_object_base import OneDriveObjectBase


class ManagedApp(OneDriveObjectBase):

    def __init__(self, prop_dict={}):
        self._prop_dict = prop_dict

    @property
    def app_availability(self):
        """
        Gets and sets the appAvailability
        
        Returns: 
            :class:`ManagedAppAvailability<onedrivesdk.model.managed_app_availability.ManagedAppAvailability>`:
                The appAvailability
        """
        if "appAvailability" in self._prop_dict:
            if isinstance(self._prop_dict["appAvailability"], OneDriveObjectBase):
                return self._prop_dict["appAvailability"]
            else :
                self._prop_dict["appAvailability"] = ManagedAppAvailability(self._prop_dict["appAvailability"])
                return self._prop_dict["appAvailability"]

        return None

    @app_availability.setter
    def app_availability(self, val):
        self._prop_dict["appAvailability"] = val

    @property
    def version(self):
        """
        Gets and sets the version
        
        Returns:
            str:
                The version
        """
        if "version" in self._prop_dict:
            return self._prop_dict["version"]
        else:
            return None

    @version.setter
    def version(self, val):
        self._prop_dict["version"] = val

