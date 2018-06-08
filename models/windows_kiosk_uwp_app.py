# -*- coding: utf-8 -*- 
'''
# Copyright (c) Microsoft Corporation.  All Rights Reserved.  Licensed under the MIT License.  See License in the project root for license information.
# 
#  This file was generated and any changes will be overwritten.
'''

from __future__ import unicode_literals
from ..one_drive_object_base import OneDriveObjectBase


class WindowsKioskUWPApp(OneDriveObjectBase):

    def __init__(self, prop_dict={}):
        self._prop_dict = prop_dict

    @property
    def app_user_model_id(self):
        """Gets and sets the appUserModelId
        
        Returns: 
            str:
                The appUserModelId
        """
        if "appUserModelId" in self._prop_dict:
            return self._prop_dict["appUserModelId"]
        else:
            return None

    @app_user_model_id.setter
    def app_user_model_id(self, val):
        self._prop_dict["appUserModelId"] = val

    @property
    def app_id(self):
        """Gets and sets the appId
        
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
    def contained_app_id(self):
        """Gets and sets the containedAppId
        
        Returns: 
            str:
                The containedAppId
        """
        if "containedAppId" in self._prop_dict:
            return self._prop_dict["containedAppId"]
        else:
            return None

    @contained_app_id.setter
    def contained_app_id(self, val):
        self._prop_dict["containedAppId"] = val

