# -*- coding: utf-8 -*- 
'''
# Copyright (c) Microsoft Corporation.  All Rights Reserved.  Licensed under the MIT License.  See License in the project root for license information.
# 
#  This file was generated and any changes will be overwritten.
'''

from __future__ import unicode_literals
from datetime import datetime
from ..one_drive_object_base import OneDriveObjectBase


class TelecomExpenseManagementPartner(OneDriveObjectBase):

    def __init__(self, prop_dict={}):
        self._prop_dict = prop_dict

    @property
    def display_name(self):
        """
        Gets and sets the displayName
        
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
    def url(self):
        """
        Gets and sets the url
        
        Returns:
            str:
                The url
        """
        if "url" in self._prop_dict:
            return self._prop_dict["url"]
        else:
            return None

    @url.setter
    def url(self, val):
        self._prop_dict["url"] = val

    @property
    def app_authorized(self):
        """
        Gets and sets the appAuthorized
        
        Returns:
            bool:
                The appAuthorized
        """
        if "appAuthorized" in self._prop_dict:
            return self._prop_dict["appAuthorized"]
        else:
            return None

    @app_authorized.setter
    def app_authorized(self, val):
        self._prop_dict["appAuthorized"] = val

    @property
    def enabled(self):
        """
        Gets and sets the enabled
        
        Returns:
            bool:
                The enabled
        """
        if "enabled" in self._prop_dict:
            return self._prop_dict["enabled"]
        else:
            return None

    @enabled.setter
    def enabled(self, val):
        self._prop_dict["enabled"] = val

    @property
    def last_connection_date_time(self):
        """
        Gets and sets the lastConnectionDateTime
        
        Returns:
            datetime:
                The lastConnectionDateTime
        """
        if "lastConnectionDateTime" in self._prop_dict:
            return datetime.strptime(self._prop_dict["lastConnectionDateTime"].replace("Z", ""), "%Y-%m-%dT%H:%M:%S.%f")
        else:
            return None

    @last_connection_date_time.setter
    def last_connection_date_time(self, val):
        self._prop_dict["lastConnectionDateTime"] = val.isoformat()+"Z"

