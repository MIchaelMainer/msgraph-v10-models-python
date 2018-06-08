# -*- coding: utf-8 -*- 
'''
# Copyright (c) Microsoft Corporation.  All Rights Reserved.  Licensed under the MIT License.  See License in the project root for license information.
# 
#  This file was generated and any changes will be overwritten.
'''

from __future__ import unicode_literals
from datetime import datetime
from ..one_drive_object_base import OneDriveObjectBase


class UsageDetails(OneDriveObjectBase):

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

