# -*- coding: utf-8 -*- 
'''
# Copyright (c) Microsoft Corporation.  All Rights Reserved.  Licensed under the MIT License.  See License in the project root for license information.
# 
#  This file was generated and any changes will be overwritten.
'''

from __future__ import unicode_literals
from ..model.permission_scope import PermissionScope
from ..one_drive_object_base import OneDriveObjectBase


class Api(OneDriveObjectBase):

    def __init__(self, prop_dict={}):
        self._prop_dict = prop_dict

    @property
    def accepted_access_token_version(self):
        """Gets and sets the acceptedAccessTokenVersion
        
        Returns: 
            int:
                The acceptedAccessTokenVersion
        """
        if "acceptedAccessTokenVersion" in self._prop_dict:
            return self._prop_dict["acceptedAccessTokenVersion"]
        else:
            return None

    @accepted_access_token_version.setter
    def accepted_access_token_version(self, val):
        self._prop_dict["acceptedAccessTokenVersion"] = val

    @property
    def published_permission_scopes(self):
        """
        Gets and sets the publishedPermissionScopes
        
        Returns: 
            :class:`PermissionScope<onedrivesdk.model.permission_scope.PermissionScope>`:
                The publishedPermissionScopes
        """
        if "publishedPermissionScopes" in self._prop_dict:
            if isinstance(self._prop_dict["publishedPermissionScopes"], OneDriveObjectBase):
                return self._prop_dict["publishedPermissionScopes"]
            else :
                self._prop_dict["publishedPermissionScopes"] = PermissionScope(self._prop_dict["publishedPermissionScopes"])
                return self._prop_dict["publishedPermissionScopes"]

        return None

    @published_permission_scopes.setter
    def published_permission_scopes(self, val):
        self._prop_dict["publishedPermissionScopes"] = val
