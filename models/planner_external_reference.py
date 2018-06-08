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


class PlannerExternalReference(OneDriveObjectBase):

    def __init__(self, prop_dict={}):
        self._prop_dict = prop_dict

    @property
    def alias(self):
        """Gets and sets the alias
        
        Returns: 
            str:
                The alias
        """
        if "alias" in self._prop_dict:
            return self._prop_dict["alias"]
        else:
            return None

    @alias.setter
    def alias(self, val):
        self._prop_dict["alias"] = val

    @property
    def type(self):
        """Gets and sets the type
        
        Returns: 
            str:
                The type
        """
        if "type" in self._prop_dict:
            return self._prop_dict["type"]
        else:
            return None

    @type.setter
    def type(self, val):
        self._prop_dict["type"] = val

    @property
    def preview_priority(self):
        """Gets and sets the previewPriority
        
        Returns: 
            str:
                The previewPriority
        """
        if "previewPriority" in self._prop_dict:
            return self._prop_dict["previewPriority"]
        else:
            return None

    @preview_priority.setter
    def preview_priority(self, val):
        self._prop_dict["previewPriority"] = val

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
        """Gets and sets the lastModifiedDateTime
        
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

