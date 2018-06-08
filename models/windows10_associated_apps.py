# -*- coding: utf-8 -*- 
'''
# Copyright (c) Microsoft Corporation.  All Rights Reserved.  Licensed under the MIT License.  See License in the project root for license information.
# 
#  This file was generated and any changes will be overwritten.
'''

from __future__ import unicode_literals
from ..model.windows10_app_type import Windows10AppType
from ..one_drive_object_base import OneDriveObjectBase


class Windows10AssociatedApps(OneDriveObjectBase):

    def __init__(self, prop_dict={}):
        self._prop_dict = prop_dict

    @property
    def app_type(self):
        """
        Gets and sets the appType
        
        Returns: 
            :class:`Windows10AppType<onedrivesdk.model.windows10_app_type.Windows10AppType>`:
                The appType
        """
        if "appType" in self._prop_dict:
            if isinstance(self._prop_dict["appType"], OneDriveObjectBase):
                return self._prop_dict["appType"]
            else :
                self._prop_dict["appType"] = Windows10AppType(self._prop_dict["appType"])
                return self._prop_dict["appType"]

        return None

    @app_type.setter
    def app_type(self, val):
        self._prop_dict["appType"] = val
    @property
    def identifier(self):
        """Gets and sets the identifier
        
        Returns: 
            str:
                The identifier
        """
        if "identifier" in self._prop_dict:
            return self._prop_dict["identifier"]
        else:
            return None

    @identifier.setter
    def identifier(self, val):
        self._prop_dict["identifier"] = val

