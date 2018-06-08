# -*- coding: utf-8 -*- 
'''
# Copyright (c) Microsoft Corporation.  All Rights Reserved.  Licensed under the MIT License.  See License in the project root for license information.
# 
#  This file was generated and any changes will be overwritten.
'''

from __future__ import unicode_literals
from ..model.action_state import ActionState
from datetime import datetime
from ..one_drive_object_base import OneDriveObjectBase


class VppTokenActionResult(OneDriveObjectBase):

    def __init__(self, prop_dict={}):
        self._prop_dict = prop_dict

    @property
    def action_name(self):
        """Gets and sets the actionName
        
        Returns: 
            str:
                The actionName
        """
        if "actionName" in self._prop_dict:
            return self._prop_dict["actionName"]
        else:
            return None

    @action_name.setter
    def action_name(self, val):
        self._prop_dict["actionName"] = val

    @property
    def action_state(self):
        """
        Gets and sets the actionState
        
        Returns: 
            :class:`ActionState<onedrivesdk.model.action_state.ActionState>`:
                The actionState
        """
        if "actionState" in self._prop_dict:
            if isinstance(self._prop_dict["actionState"], OneDriveObjectBase):
                return self._prop_dict["actionState"]
            else :
                self._prop_dict["actionState"] = ActionState(self._prop_dict["actionState"])
                return self._prop_dict["actionState"]

        return None

    @action_state.setter
    def action_state(self, val):
        self._prop_dict["actionState"] = val
    @property
    def start_date_time(self):
        """Gets and sets the startDateTime
        
        Returns: 
            datetime:
                The startDateTime
        """
        if "startDateTime" in self._prop_dict:
            return datetime.strptime(self._prop_dict["startDateTime"].replace("Z", ""), "%Y-%m-%dT%H:%M:%S.%f")
        else:
            return None

    @start_date_time.setter
    def start_date_time(self, val):
        self._prop_dict["startDateTime"] = val.isoformat()+"Z"

    @property
    def last_updated_date_time(self):
        """Gets and sets the lastUpdatedDateTime
        
        Returns: 
            datetime:
                The lastUpdatedDateTime
        """
        if "lastUpdatedDateTime" in self._prop_dict:
            return datetime.strptime(self._prop_dict["lastUpdatedDateTime"].replace("Z", ""), "%Y-%m-%dT%H:%M:%S.%f")
        else:
            return None

    @last_updated_date_time.setter
    def last_updated_date_time(self, val):
        self._prop_dict["lastUpdatedDateTime"] = val.isoformat()+"Z"

