# -*- coding: utf-8 -*- 
'''
# Copyright (c) Microsoft Corporation.  All Rights Reserved.  Licensed under the MIT License.  See License in the project root for license information.
# 
#  This file was generated and any changes will be overwritten.
'''

from __future__ import unicode_literals
from ..model.education_synchronization_status import EducationSynchronizationStatus
from datetime import datetime
from ..one_drive_object_base import OneDriveObjectBase


class EducationSynchronizationProfileStatus(OneDriveObjectBase):

    def __init__(self, prop_dict={}):
        self._prop_dict = prop_dict

    @property
    def status(self):
        """
        Gets and sets the status
        
        Returns: 
            :class:`EducationSynchronizationStatus<onedrivesdk.model.education_synchronization_status.EducationSynchronizationStatus>`:
                The status
        """
        if "status" in self._prop_dict:
            if isinstance(self._prop_dict["status"], OneDriveObjectBase):
                return self._prop_dict["status"]
            else :
                self._prop_dict["status"] = EducationSynchronizationStatus(self._prop_dict["status"])
                return self._prop_dict["status"]

        return None

    @status.setter
    def status(self, val):
        self._prop_dict["status"] = val

    @property
    def last_synchronization_date_time(self):
        """
        Gets and sets the lastSynchronizationDateTime
        
        Returns:
            datetime:
                The lastSynchronizationDateTime
        """
        if "lastSynchronizationDateTime" in self._prop_dict:
            return datetime.strptime(self._prop_dict["lastSynchronizationDateTime"].replace("Z", ""), "%Y-%m-%dT%H:%M:%S.%f")
        else:
            return None

    @last_synchronization_date_time.setter
    def last_synchronization_date_time(self, val):
        self._prop_dict["lastSynchronizationDateTime"] = val.isoformat()+"Z"

