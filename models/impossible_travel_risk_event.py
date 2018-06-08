# -*- coding: utf-8 -*- 
'''
# Copyright (c) Microsoft Corporation.  All Rights Reserved.  Licensed under the MIT License.  See License in the project root for license information.
# 
#  This file was generated and any changes will be overwritten.
'''

from __future__ import unicode_literals
from ..model.sign_in_location import SignInLocation
from datetime import datetime
from ..one_drive_object_base import OneDriveObjectBase


class ImpossibleTravelRiskEvent(OneDriveObjectBase):

    def __init__(self, prop_dict={}):
        self._prop_dict = prop_dict

    @property
    def user_agent(self):
        """
        Gets and sets the userAgent
        
        Returns:
            str:
                The userAgent
        """
        if "userAgent" in self._prop_dict:
            return self._prop_dict["userAgent"]
        else:
            return None

    @user_agent.setter
    def user_agent(self, val):
        self._prop_dict["userAgent"] = val

    @property
    def device_information(self):
        """
        Gets and sets the deviceInformation
        
        Returns:
            str:
                The deviceInformation
        """
        if "deviceInformation" in self._prop_dict:
            return self._prop_dict["deviceInformation"]
        else:
            return None

    @device_information.setter
    def device_information(self, val):
        self._prop_dict["deviceInformation"] = val

    @property
    def is_atypical_location(self):
        """
        Gets and sets the isAtypicalLocation
        
        Returns:
            bool:
                The isAtypicalLocation
        """
        if "isAtypicalLocation" in self._prop_dict:
            return self._prop_dict["isAtypicalLocation"]
        else:
            return None

    @is_atypical_location.setter
    def is_atypical_location(self, val):
        self._prop_dict["isAtypicalLocation"] = val

    @property
    def previous_signin_date_time(self):
        """
        Gets and sets the previousSigninDateTime
        
        Returns:
            datetime:
                The previousSigninDateTime
        """
        if "previousSigninDateTime" in self._prop_dict:
            return datetime.strptime(self._prop_dict["previousSigninDateTime"].replace("Z", ""), "%Y-%m-%dT%H:%M:%S.%f")
        else:
            return None

    @previous_signin_date_time.setter
    def previous_signin_date_time(self, val):
        self._prop_dict["previousSigninDateTime"] = val.isoformat()+"Z"

    @property
    def previous_location(self):
        """
        Gets and sets the previousLocation
        
        Returns: 
            :class:`SignInLocation<onedrivesdk.model.sign_in_location.SignInLocation>`:
                The previousLocation
        """
        if "previousLocation" in self._prop_dict:
            if isinstance(self._prop_dict["previousLocation"], OneDriveObjectBase):
                return self._prop_dict["previousLocation"]
            else :
                self._prop_dict["previousLocation"] = SignInLocation(self._prop_dict["previousLocation"])
                return self._prop_dict["previousLocation"]

        return None

    @previous_location.setter
    def previous_location(self, val):
        self._prop_dict["previousLocation"] = val

    @property
    def previous_ip_address(self):
        """
        Gets and sets the previousIpAddress
        
        Returns:
            str:
                The previousIpAddress
        """
        if "previousIpAddress" in self._prop_dict:
            return self._prop_dict["previousIpAddress"]
        else:
            return None

    @previous_ip_address.setter
    def previous_ip_address(self, val):
        self._prop_dict["previousIpAddress"] = val

