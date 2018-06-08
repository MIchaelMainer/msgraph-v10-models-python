# -*- coding: utf-8 -*- 
'''
# Copyright (c) Microsoft Corporation.  All Rights Reserved.  Licensed under the MIT License.  See License in the project root for license information.
# 
#  This file was generated and any changes will be overwritten.
'''

from __future__ import unicode_literals
from ..model.identity_set import IdentitySet
from datetime import datetime
from ..one_drive_object_base import OneDriveObjectBase


class Shared(OneDriveObjectBase):

    def __init__(self, prop_dict={}):
        self._prop_dict = prop_dict

    @property
    def owner(self):
        """
        Gets and sets the owner
        
        Returns: 
            :class:`IdentitySet<onedrivesdk.model.identity_set.IdentitySet>`:
                The owner
        """
        if "owner" in self._prop_dict:
            if isinstance(self._prop_dict["owner"], OneDriveObjectBase):
                return self._prop_dict["owner"]
            else :
                self._prop_dict["owner"] = IdentitySet(self._prop_dict["owner"])
                return self._prop_dict["owner"]

        return None

    @owner.setter
    def owner(self, val):
        self._prop_dict["owner"] = val
    @property
    def scope(self):
        """Gets and sets the scope
        
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
    def shared_by(self):
        """
        Gets and sets the sharedBy
        
        Returns: 
            :class:`IdentitySet<onedrivesdk.model.identity_set.IdentitySet>`:
                The sharedBy
        """
        if "sharedBy" in self._prop_dict:
            if isinstance(self._prop_dict["sharedBy"], OneDriveObjectBase):
                return self._prop_dict["sharedBy"]
            else :
                self._prop_dict["sharedBy"] = IdentitySet(self._prop_dict["sharedBy"])
                return self._prop_dict["sharedBy"]

        return None

    @shared_by.setter
    def shared_by(self, val):
        self._prop_dict["sharedBy"] = val
    @property
    def shared_date_time(self):
        """Gets and sets the sharedDateTime
        
        Returns: 
            datetime:
                The sharedDateTime
        """
        if "sharedDateTime" in self._prop_dict:
            return datetime.strptime(self._prop_dict["sharedDateTime"].replace("Z", ""), "%Y-%m-%dT%H:%M:%S.%f")
        else:
            return None

    @shared_date_time.setter
    def shared_date_time(self, val):
        self._prop_dict["sharedDateTime"] = val.isoformat()+"Z"

