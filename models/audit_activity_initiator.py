# -*- coding: utf-8 -*- 
'''
# Copyright (c) Microsoft Corporation.  All Rights Reserved.  Licensed under the MIT License.  See License in the project root for license information.
# 
#  This file was generated and any changes will be overwritten.
'''

from __future__ import unicode_literals
from ..model.user_identity import UserIdentity
from ..model.app_identity import AppIdentity
from ..one_drive_object_base import OneDriveObjectBase


class AuditActivityInitiator(OneDriveObjectBase):

    def __init__(self, prop_dict={}):
        self._prop_dict = prop_dict

    @property
    def user(self):
        """
        Gets and sets the user
        
        Returns: 
            :class:`UserIdentity<onedrivesdk.model.user_identity.UserIdentity>`:
                The user
        """
        if "user" in self._prop_dict:
            if isinstance(self._prop_dict["user"], OneDriveObjectBase):
                return self._prop_dict["user"]
            else :
                self._prop_dict["user"] = UserIdentity(self._prop_dict["user"])
                return self._prop_dict["user"]

        return None

    @user.setter
    def user(self, val):
        self._prop_dict["user"] = val
    @property
    def app(self):
        """
        Gets and sets the app
        
        Returns: 
            :class:`AppIdentity<onedrivesdk.model.app_identity.AppIdentity>`:
                The app
        """
        if "app" in self._prop_dict:
            if isinstance(self._prop_dict["app"], OneDriveObjectBase):
                return self._prop_dict["app"]
            else :
                self._prop_dict["app"] = AppIdentity(self._prop_dict["app"])
                return self._prop_dict["app"]

        return None

    @app.setter
    def app(self, val):
        self._prop_dict["app"] = val
