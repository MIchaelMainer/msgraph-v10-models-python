# -*- coding: utf-8 -*- 
'''
# Copyright (c) Microsoft Corporation.  All Rights Reserved.  Licensed under the MIT License.  See License in the project root for license information.
# 
#  This file was generated and any changes will be overwritten.
'''

from __future__ import unicode_literals
from ..one_drive_object_base import OneDriveObjectBase


class AllowedDataLocation(OneDriveObjectBase):

    def __init__(self, prop_dict={}):
        self._prop_dict = prop_dict

    @property
    def app_id(self):
        """
        Gets and sets the appId
        
        Returns:
            str:
                The appId
        """
        if "appId" in self._prop_dict:
            return self._prop_dict["appId"]
        else:
            return None

    @app_id.setter
    def app_id(self, val):
        self._prop_dict["appId"] = val

    @property
    def location(self):
        """
        Gets and sets the location
        
        Returns:
            str:
                The location
        """
        if "location" in self._prop_dict:
            return self._prop_dict["location"]
        else:
            return None

    @location.setter
    def location(self, val):
        self._prop_dict["location"] = val

    @property
    def is_default(self):
        """
        Gets and sets the isDefault
        
        Returns:
            bool:
                The isDefault
        """
        if "isDefault" in self._prop_dict:
            return self._prop_dict["isDefault"]
        else:
            return None

    @is_default.setter
    def is_default(self, val):
        self._prop_dict["isDefault"] = val

    @property
    def domain(self):
        """
        Gets and sets the domain
        
        Returns:
            str:
                The domain
        """
        if "domain" in self._prop_dict:
            return self._prop_dict["domain"]
        else:
            return None

    @domain.setter
    def domain(self, val):
        self._prop_dict["domain"] = val

