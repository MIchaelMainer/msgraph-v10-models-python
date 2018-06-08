# -*- coding: utf-8 -*- 
'''
# Copyright (c) Microsoft Corporation.  All Rights Reserved.  Licensed under the MIT License.  See License in the project root for license information.
# 
#  This file was generated and any changes will be overwritten.
'''

from __future__ import unicode_literals
from ..one_drive_object_base import OneDriveObjectBase


class WebApp(OneDriveObjectBase):

    def __init__(self, prop_dict={}):
        self._prop_dict = prop_dict

    @property
    def app_url(self):
        """
        Gets and sets the appUrl
        
        Returns:
            str:
                The appUrl
        """
        if "appUrl" in self._prop_dict:
            return self._prop_dict["appUrl"]
        else:
            return None

    @app_url.setter
    def app_url(self, val):
        self._prop_dict["appUrl"] = val

    @property
    def use_managed_browser(self):
        """
        Gets and sets the useManagedBrowser
        
        Returns:
            bool:
                The useManagedBrowser
        """
        if "useManagedBrowser" in self._prop_dict:
            return self._prop_dict["useManagedBrowser"]
        else:
            return None

    @use_managed_browser.setter
    def use_managed_browser(self, val):
        self._prop_dict["useManagedBrowser"] = val

