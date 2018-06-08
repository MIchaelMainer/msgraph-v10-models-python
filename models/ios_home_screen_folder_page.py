# -*- coding: utf-8 -*- 
'''
# Copyright (c) Microsoft Corporation.  All Rights Reserved.  Licensed under the MIT License.  See License in the project root for license information.
# 
#  This file was generated and any changes will be overwritten.
'''

from __future__ import unicode_literals
from ..model.ios_home_screen_app import IosHomeScreenApp
from ..one_drive_object_base import OneDriveObjectBase


class IosHomeScreenFolderPage(OneDriveObjectBase):

    def __init__(self, prop_dict={}):
        self._prop_dict = prop_dict

    @property
    def display_name(self):
        """Gets and sets the displayName
        
        Returns: 
            str:
                The displayName
        """
        if "displayName" in self._prop_dict:
            return self._prop_dict["displayName"]
        else:
            return None

    @display_name.setter
    def display_name(self, val):
        self._prop_dict["displayName"] = val

    @property
    def apps(self):
        """
        Gets and sets the apps
        
        Returns: 
            :class:`IosHomeScreenApp<onedrivesdk.model.ios_home_screen_app.IosHomeScreenApp>`:
                The apps
        """
        if "apps" in self._prop_dict:
            if isinstance(self._prop_dict["apps"], OneDriveObjectBase):
                return self._prop_dict["apps"]
            else :
                self._prop_dict["apps"] = IosHomeScreenApp(self._prop_dict["apps"])
                return self._prop_dict["apps"]

        return None

    @apps.setter
    def apps(self, val):
        self._prop_dict["apps"] = val
