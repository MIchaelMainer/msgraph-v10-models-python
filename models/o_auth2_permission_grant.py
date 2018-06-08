# -*- coding: utf-8 -*- 
'''
# Copyright (c) Microsoft Corporation.  All Rights Reserved.  Licensed under the MIT License.  See License in the project root for license information.
# 
#  This file was generated and any changes will be overwritten.
'''

from __future__ import unicode_literals
from datetime import datetime
from ..one_drive_object_base import OneDriveObjectBase


class OAuth2PermissionGrant(OneDriveObjectBase):

    def __init__(self, prop_dict={}):
        self._prop_dict = prop_dict

    @property
    def client_id(self):
        """
        Gets and sets the clientId
        
        Returns:
            str:
                The clientId
        """
        if "clientId" in self._prop_dict:
            return self._prop_dict["clientId"]
        else:
            return None

    @client_id.setter
    def client_id(self, val):
        self._prop_dict["clientId"] = val

    @property
    def consent_type(self):
        """
        Gets and sets the consentType
        
        Returns:
            str:
                The consentType
        """
        if "consentType" in self._prop_dict:
            return self._prop_dict["consentType"]
        else:
            return None

    @consent_type.setter
    def consent_type(self, val):
        self._prop_dict["consentType"] = val

    @property
    def expiry_time(self):
        """
        Gets and sets the expiryTime
        
        Returns:
            datetime:
                The expiryTime
        """
        if "expiryTime" in self._prop_dict:
            return datetime.strptime(self._prop_dict["expiryTime"].replace("Z", ""), "%Y-%m-%dT%H:%M:%S.%f")
        else:
            return None

    @expiry_time.setter
    def expiry_time(self, val):
        self._prop_dict["expiryTime"] = val.isoformat()+"Z"

    @property
    def principal_id(self):
        """
        Gets and sets the principalId
        
        Returns:
            str:
                The principalId
        """
        if "principalId" in self._prop_dict:
            return self._prop_dict["principalId"]
        else:
            return None

    @principal_id.setter
    def principal_id(self, val):
        self._prop_dict["principalId"] = val

    @property
    def resource_id(self):
        """
        Gets and sets the resourceId
        
        Returns:
            str:
                The resourceId
        """
        if "resourceId" in self._prop_dict:
            return self._prop_dict["resourceId"]
        else:
            return None

    @resource_id.setter
    def resource_id(self, val):
        self._prop_dict["resourceId"] = val

    @property
    def scope(self):
        """
        Gets and sets the scope
        
        Returns:
            str:
                The scope
        """
        if "scope" in self._prop_dict:
            return self._prop_dict["scope"]
        else:
            return None

    @scope.setter
    def scope(self, val):
        self._prop_dict["scope"] = val

    @property
    def start_time(self):
        """
        Gets and sets the startTime
        
        Returns:
            datetime:
                The startTime
        """
        if "startTime" in self._prop_dict:
            return datetime.strptime(self._prop_dict["startTime"].replace("Z", ""), "%Y-%m-%dT%H:%M:%S.%f")
        else:
            return None

    @start_time.setter
    def start_time(self, val):
        self._prop_dict["startTime"] = val.isoformat()+"Z"

