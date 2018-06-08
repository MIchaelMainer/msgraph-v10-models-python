# -*- coding: utf-8 -*- 
'''
# Copyright (c) Microsoft Corporation.  All Rights Reserved.  Licensed under the MIT License.  See License in the project root for license information.
# 
#  This file was generated and any changes will be overwritten.
'''

from __future__ import unicode_literals
from datetime import datetime
from ..one_drive_object_base import OneDriveObjectBase


class DirectoryObject(OneDriveObjectBase):

    def __init__(self, prop_dict={}):
        self._prop_dict = prop_dict

    @property
    def deleted_date_time(self):
        """
        Gets and sets the deletedDateTime
        
        Returns:
            datetime:
                The deletedDateTime
        """
        if "deletedDateTime" in self._prop_dict:
            return datetime.strptime(self._prop_dict["deletedDateTime"].replace("Z", ""), "%Y-%m-%dT%H:%M:%S.%f")
        else:
            return None

    @deleted_date_time.setter
    def deleted_date_time(self, val):
        self._prop_dict["deletedDateTime"] = val.isoformat()+"Z"

