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


class PlannerAssignment(OneDriveObjectBase):

    def __init__(self, prop_dict={}):
        self._prop_dict = prop_dict

    @property
    def assigned_by(self):
        """
        Gets and sets the assignedBy
        
        Returns: 
            :class:`IdentitySet<onedrivesdk.model.identity_set.IdentitySet>`:
                The assignedBy
        """
        if "assignedBy" in self._prop_dict:
            if isinstance(self._prop_dict["assignedBy"], OneDriveObjectBase):
                return self._prop_dict["assignedBy"]
            else :
                self._prop_dict["assignedBy"] = IdentitySet(self._prop_dict["assignedBy"])
                return self._prop_dict["assignedBy"]

        return None

    @assigned_by.setter
    def assigned_by(self, val):
        self._prop_dict["assignedBy"] = val
    @property
    def assigned_date_time(self):
        """Gets and sets the assignedDateTime
        
        Returns: 
            datetime:
                The assignedDateTime
        """
        if "assignedDateTime" in self._prop_dict:
            return datetime.strptime(self._prop_dict["assignedDateTime"].replace("Z", ""), "%Y-%m-%dT%H:%M:%S.%f")
        else:
            return None

    @assigned_date_time.setter
    def assigned_date_time(self, val):
        self._prop_dict["assignedDateTime"] = val.isoformat()+"Z"

    @property
    def order_hint(self):
        """Gets and sets the orderHint
        
        Returns: 
            str:
                The orderHint
        """
        if "orderHint" in self._prop_dict:
            return self._prop_dict["orderHint"]
        else:
            return None

    @order_hint.setter
    def order_hint(self, val):
        self._prop_dict["orderHint"] = val

