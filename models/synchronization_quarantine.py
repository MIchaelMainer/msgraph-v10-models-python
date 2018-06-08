# -*- coding: utf-8 -*- 
'''
# Copyright (c) Microsoft Corporation.  All Rights Reserved.  Licensed under the MIT License.  See License in the project root for license information.
# 
#  This file was generated and any changes will be overwritten.
'''

from __future__ import unicode_literals
from ..model.quarantine_reason import QuarantineReason
from datetime import datetime
from ..one_drive_object_base import OneDriveObjectBase


class SynchronizationQuarantine(OneDriveObjectBase):

    def __init__(self, prop_dict={}):
        self._prop_dict = prop_dict

    @property
    def current_began(self):
        """Gets and sets the currentBegan
        
        Returns: 
            datetime:
                The currentBegan
        """
        if "currentBegan" in self._prop_dict:
            return datetime.strptime(self._prop_dict["currentBegan"].replace("Z", ""), "%Y-%m-%dT%H:%M:%S.%f")
        else:
            return None

    @current_began.setter
    def current_began(self, val):
        self._prop_dict["currentBegan"] = val.isoformat()+"Z"

    @property
    def next_attempt(self):
        """Gets and sets the nextAttempt
        
        Returns: 
            datetime:
                The nextAttempt
        """
        if "nextAttempt" in self._prop_dict:
            return datetime.strptime(self._prop_dict["nextAttempt"].replace("Z", ""), "%Y-%m-%dT%H:%M:%S.%f")
        else:
            return None

    @next_attempt.setter
    def next_attempt(self, val):
        self._prop_dict["nextAttempt"] = val.isoformat()+"Z"

    @property
    def reason(self):
        """
        Gets and sets the reason
        
        Returns: 
            :class:`QuarantineReason<onedrivesdk.model.quarantine_reason.QuarantineReason>`:
                The reason
        """
        if "reason" in self._prop_dict:
            if isinstance(self._prop_dict["reason"], OneDriveObjectBase):
                return self._prop_dict["reason"]
            else :
                self._prop_dict["reason"] = QuarantineReason(self._prop_dict["reason"])
                return self._prop_dict["reason"]

        return None

    @reason.setter
    def reason(self, val):
        self._prop_dict["reason"] = val
    @property
    def series_began(self):
        """Gets and sets the seriesBegan
        
        Returns: 
            datetime:
                The seriesBegan
        """
        if "seriesBegan" in self._prop_dict:
            return datetime.strptime(self._prop_dict["seriesBegan"].replace("Z", ""), "%Y-%m-%dT%H:%M:%S.%f")
        else:
            return None

    @series_began.setter
    def series_began(self, val):
        self._prop_dict["seriesBegan"] = val.isoformat()+"Z"

    @property
    def series_count(self):
        """Gets and sets the seriesCount
        
        Returns: 
            int:
                The seriesCount
        """
        if "seriesCount" in self._prop_dict:
            return self._prop_dict["seriesCount"]
        else:
            return None

    @series_count.setter
    def series_count(self, val):
        self._prop_dict["seriesCount"] = val

