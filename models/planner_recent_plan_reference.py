# -*- coding: utf-8 -*- 
'''
# Copyright (c) Microsoft Corporation.  All Rights Reserved.  Licensed under the MIT License.  See License in the project root for license information.
# 
#  This file was generated and any changes will be overwritten.
'''

from __future__ import unicode_literals
from datetime import datetime
from ..one_drive_object_base import OneDriveObjectBase


class PlannerRecentPlanReference(OneDriveObjectBase):

    def __init__(self, prop_dict={}):
        self._prop_dict = prop_dict

    @property
    def last_accessed_date_time(self):
        """Gets and sets the lastAccessedDateTime
        
        Returns: 
            datetime:
                The lastAccessedDateTime
        """
        if "lastAccessedDateTime" in self._prop_dict:
            return datetime.strptime(self._prop_dict["lastAccessedDateTime"].replace("Z", ""), "%Y-%m-%dT%H:%M:%S.%f")
        else:
            return None

    @last_accessed_date_time.setter
    def last_accessed_date_time(self, val):
        self._prop_dict["lastAccessedDateTime"] = val.isoformat()+"Z"

    @property
    def plan_title(self):
        """Gets and sets the planTitle
        
        Returns: 
            str:
                The planTitle
        """
        if "planTitle" in self._prop_dict:
            return self._prop_dict["planTitle"]
        else:
            return None

    @plan_title.setter
    def plan_title(self, val):
        self._prop_dict["planTitle"] = val

