# -*- coding: utf-8 -*- 
'''
# Copyright (c) Microsoft Corporation.  All Rights Reserved.  Licensed under the MIT License.  See License in the project root for license information.
# 
#  This file was generated and any changes will be overwritten.
'''

from __future__ import unicode_literals
from datetime import datetime
from ..one_drive_object_base import OneDriveObjectBase


class AppRoleAssignment(OneDriveObjectBase):

    def __init__(self, prop_dict={}):
        self._prop_dict = prop_dict

    @property
    def creation_timestamp(self):
        """
        Gets and sets the creationTimestamp
        
        Returns:
            datetime:
                The creationTimestamp
        """
        if "creationTimestamp" in self._prop_dict:
            return datetime.strptime(self._prop_dict["creationTimestamp"].replace("Z", ""), "%Y-%m-%dT%H:%M:%S.%f")
        else:
            return None

    @creation_timestamp.setter
    def creation_timestamp(self, val):
        self._prop_dict["creationTimestamp"] = val.isoformat()+"Z"

    @property
    def principal_display_name(self):
        """
        Gets and sets the principalDisplayName
        
        Returns:
            str:
                The principalDisplayName
        """
        if "principalDisplayName" in self._prop_dict:
            return self._prop_dict["principalDisplayName"]
        else:
            return None

    @principal_display_name.setter
    def principal_display_name(self, val):
        self._prop_dict["principalDisplayName"] = val

    @property
    def principal_id(self):
        """
        Gets and sets the principalId
        
        Returns:
            UUID:
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
    def principal_type(self):
        """
        Gets and sets the principalType
        
        Returns:
            str:
                The principalType
        """
        if "principalType" in self._prop_dict:
            return self._prop_dict["principalType"]
        else:
            return None

    @principal_type.setter
    def principal_type(self, val):
        self._prop_dict["principalType"] = val

    @property
    def resource_display_name(self):
        """
        Gets and sets the resourceDisplayName
        
        Returns:
            str:
                The resourceDisplayName
        """
        if "resourceDisplayName" in self._prop_dict:
            return self._prop_dict["resourceDisplayName"]
        else:
            return None

    @resource_display_name.setter
    def resource_display_name(self, val):
        self._prop_dict["resourceDisplayName"] = val

    @property
    def resource_id(self):
        """
        Gets and sets the resourceId
        
        Returns:
            UUID:
                The resourceId
        """
        if "resourceId" in self._prop_dict:
            return self._prop_dict["resourceId"]
        else:
            return None

    @resource_id.setter
    def resource_id(self, val):
        self._prop_dict["resourceId"] = val

