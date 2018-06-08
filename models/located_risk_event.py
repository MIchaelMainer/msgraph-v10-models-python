# -*- coding: utf-8 -*- 
'''
# Copyright (c) Microsoft Corporation.  All Rights Reserved.  Licensed under the MIT License.  See License in the project root for license information.
# 
#  This file was generated and any changes will be overwritten.
'''

from __future__ import unicode_literals
from ..model.sign_in_location import SignInLocation
from ..one_drive_object_base import OneDriveObjectBase


class LocatedRiskEvent(OneDriveObjectBase):

    def __init__(self, prop_dict={}):
        self._prop_dict = prop_dict

    @property
    def location(self):
        """
        Gets and sets the location
        
        Returns: 
            :class:`SignInLocation<onedrivesdk.model.sign_in_location.SignInLocation>`:
                The location
        """
        if "location" in self._prop_dict:
            if isinstance(self._prop_dict["location"], OneDriveObjectBase):
                return self._prop_dict["location"]
            else :
                self._prop_dict["location"] = SignInLocation(self._prop_dict["location"])
                return self._prop_dict["location"]

        return None

    @location.setter
    def location(self, val):
        self._prop_dict["location"] = val

    @property
    def ip_address(self):
        """
        Gets and sets the ipAddress
        
        Returns:
            str:
                The ipAddress
        """
        if "ipAddress" in self._prop_dict:
            return self._prop_dict["ipAddress"]
        else:
            return None

    @ip_address.setter
    def ip_address(self, val):
        self._prop_dict["ipAddress"] = val

