# -*- coding: utf-8 -*- 
'''
# Copyright (c) Microsoft Corporation.  All Rights Reserved.  Licensed under the MIT License.  See License in the project root for license information.
# 
#  This file was generated and any changes will be overwritten.
'''

from __future__ import unicode_literals
from ..one_drive_object_base import OneDriveObjectBase


class PreAuthorizedApplication(OneDriveObjectBase):

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
    def permission_ids(self):
        """Gets and sets the permissionIds
        
        Returns: 
            str:
                The permissionIds
        """
        if "permissionIds" in self._prop_dict:
            return self._prop_dict["permissionIds"]
        else:
            return None

    @permission_ids.setter
    def permission_ids(self, val):
        self._prop_dict["permissionIds"] = val

