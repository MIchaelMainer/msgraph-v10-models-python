# -*- coding: utf-8 -*- 
'''
# Copyright (c) Microsoft Corporation.  All Rights Reserved.  Licensed under the MIT License.  See License in the project root for license information.
# 
#  This file was generated and any changes will be overwritten.
'''

from __future__ import unicode_literals
from ..model.user_risk_level import UserRiskLevel
from datetime import datetime
from ..one_drive_object_base import OneDriveObjectBase


class IdentityUserRisk(OneDriveObjectBase):

    def __init__(self, prop_dict={}):
        self._prop_dict = prop_dict

    @property
    def level(self):
        """
        Gets and sets the level
        
        Returns: 
            :class:`UserRiskLevel<onedrivesdk.model.user_risk_level.UserRiskLevel>`:
                The level
        """
        if "level" in self._prop_dict:
            if isinstance(self._prop_dict["level"], OneDriveObjectBase):
                return self._prop_dict["level"]
            else :
                self._prop_dict["level"] = UserRiskLevel(self._prop_dict["level"])
                return self._prop_dict["level"]

        return None

    @level.setter
    def level(self, val):
        self._prop_dict["level"] = val
    @property
    def last_changed_date_time(self):
        """Gets and sets the lastChangedDateTime
        
        Returns: 
            datetime:
                The lastChangedDateTime
        """
        if "lastChangedDateTime" in self._prop_dict:
            return datetime.strptime(self._prop_dict["lastChangedDateTime"].replace("Z", ""), "%Y-%m-%dT%H:%M:%S.%f")
        else:
            return None

    @last_changed_date_time.setter
    def last_changed_date_time(self, val):
        self._prop_dict["lastChangedDateTime"] = val.isoformat()+"Z"

