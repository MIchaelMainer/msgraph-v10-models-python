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


class OnenoteEntityHierarchyModel(OneDriveObjectBase):

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
    def created_by(self):
        """
        Gets and sets the createdBy
        
        Returns: 
            :class:`IdentitySet<onedrivesdk.model.identity_set.IdentitySet>`:
                The createdBy
        """
        if "createdBy" in self._prop_dict:
            if isinstance(self._prop_dict["createdBy"], OneDriveObjectBase):
                return self._prop_dict["createdBy"]
            else :
                self._prop_dict["createdBy"] = IdentitySet(self._prop_dict["createdBy"])
                return self._prop_dict["createdBy"]

        return None

    @created_by.setter
    def created_by(self, val):
        self._prop_dict["createdBy"] = val

    @property
    def last_modified_by(self):
        """
        Gets and sets the lastModifiedBy
        
        Returns: 
            :class:`IdentitySet<onedrivesdk.model.identity_set.IdentitySet>`:
                The lastModifiedBy
        """
        if "lastModifiedBy" in self._prop_dict:
            if isinstance(self._prop_dict["lastModifiedBy"], OneDriveObjectBase):
                return self._prop_dict["lastModifiedBy"]
            else :
                self._prop_dict["lastModifiedBy"] = IdentitySet(self._prop_dict["lastModifiedBy"])
                return self._prop_dict["lastModifiedBy"]

        return None

    @last_modified_by.setter
    def last_modified_by(self, val):
        self._prop_dict["lastModifiedBy"] = val

    @property
    def last_modified_date_time(self):
        """
        Gets and sets the lastModifiedDateTime
        
        Returns:
            datetime:
                The lastModifiedDateTime
        """
        if "lastModifiedDateTime" in self._prop_dict:
            return datetime.strptime(self._prop_dict["lastModifiedDateTime"].replace("Z", ""), "%Y-%m-%dT%H:%M:%S.%f")
        else:
            return None

    @last_modified_date_time.setter
    def last_modified_date_time(self, val):
        self._prop_dict["lastModifiedDateTime"] = val.isoformat()+"Z"

