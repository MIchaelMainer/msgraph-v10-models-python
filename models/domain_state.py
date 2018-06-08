# -*- coding: utf-8 -*- 
'''
# Copyright (c) Microsoft Corporation.  All Rights Reserved.  Licensed under the MIT License.  See License in the project root for license information.
# 
#  This file was generated and any changes will be overwritten.
'''

from __future__ import unicode_literals
from datetime import datetime
from ..one_drive_object_base import OneDriveObjectBase


class DomainState(OneDriveObjectBase):

    def __init__(self, prop_dict={}):
        self._prop_dict = prop_dict

    @property
    def status(self):
        """Gets and sets the status
        
        Returns: 
            str:
                The status
        """
        if "status" in self._prop_dict:
            return self._prop_dict["status"]
        else:
            return None

    @status.setter
    def status(self, val):
        self._prop_dict["status"] = val

    @property
    def operation(self):
        """Gets and sets the operation
        
        Returns: 
            str:
                The operation
        """
        if "operation" in self._prop_dict:
            return self._prop_dict["operation"]
        else:
            return None

    @operation.setter
    def operation(self, val):
        self._prop_dict["operation"] = val

    @property
    def last_action_date_time(self):
        """Gets and sets the lastActionDateTime
        
        Returns: 
            datetime:
                The lastActionDateTime
        """
        if "lastActionDateTime" in self._prop_dict:
            return datetime.strptime(self._prop_dict["lastActionDateTime"].replace("Z", ""), "%Y-%m-%dT%H:%M:%S.%f")
        else:
            return None

    @last_action_date_time.setter
    def last_action_date_time(self, val):
        self._prop_dict["lastActionDateTime"] = val.isoformat()+"Z"

