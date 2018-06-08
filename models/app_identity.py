# -*- coding: utf-8 -*- 
'''
# Copyright (c) Microsoft Corporation.  All Rights Reserved.  Licensed under the MIT License.  See License in the project root for license information.
# 
#  This file was generated and any changes will be overwritten.
'''

from __future__ import unicode_literals
from ..one_drive_object_base import OneDriveObjectBase


class AppIdentity(OneDriveObjectBase):

    def __init__(self, prop_dict={}):
        self._prop_dict = prop_dict

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
    def service_principal_id(self):
        """Gets and sets the servicePrincipalId
        
        Returns: 
            str:
                The servicePrincipalId
        """
        if "servicePrincipalId" in self._prop_dict:
            return self._prop_dict["servicePrincipalId"]
        else:
            return None

    @service_principal_id.setter
    def service_principal_id(self, val):
        self._prop_dict["servicePrincipalId"] = val

    @property
    def service_principal_name(self):
        """Gets and sets the servicePrincipalName
        
        Returns: 
            str:
                The servicePrincipalName
        """
        if "servicePrincipalName" in self._prop_dict:
            return self._prop_dict["servicePrincipalName"]
        else:
            return None

    @service_principal_name.setter
    def service_principal_name(self, val):
        self._prop_dict["servicePrincipalName"] = val

