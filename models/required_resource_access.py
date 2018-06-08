# -*- coding: utf-8 -*- 
'''
# Copyright (c) Microsoft Corporation.  All Rights Reserved.  Licensed under the MIT License.  See License in the project root for license information.
# 
#  This file was generated and any changes will be overwritten.
'''

from __future__ import unicode_literals
from ..model.resource_access import ResourceAccess
from ..one_drive_object_base import OneDriveObjectBase


class RequiredResourceAccess(OneDriveObjectBase):

    def __init__(self, prop_dict={}):
        self._prop_dict = prop_dict

    @property
    def resource_app_id(self):
        """Gets and sets the resourceAppId
        
        Returns: 
            str:
                The resourceAppId
        """
        if "resourceAppId" in self._prop_dict:
            return self._prop_dict["resourceAppId"]
        else:
            return None

    @resource_app_id.setter
    def resource_app_id(self, val):
        self._prop_dict["resourceAppId"] = val

    @property
    def resource_access(self):
        """
        Gets and sets the resourceAccess
        
        Returns: 
            :class:`ResourceAccess<onedrivesdk.model.resource_access.ResourceAccess>`:
                The resourceAccess
        """
        if "resourceAccess" in self._prop_dict:
            if isinstance(self._prop_dict["resourceAccess"], OneDriveObjectBase):
                return self._prop_dict["resourceAccess"]
            else :
                self._prop_dict["resourceAccess"] = ResourceAccess(self._prop_dict["resourceAccess"])
                return self._prop_dict["resourceAccess"]

        return None

    @resource_access.setter
    def resource_access(self, val):
        self._prop_dict["resourceAccess"] = val
