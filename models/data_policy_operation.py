# -*- coding: utf-8 -*- 
'''
# Copyright (c) Microsoft Corporation.  All Rights Reserved.  Licensed under the MIT License.  See License in the project root for license information.
# 
#  This file was generated and any changes will be overwritten.
'''

from __future__ import unicode_literals
from ..model.data_policy_operation_status import DataPolicyOperationStatus
from datetime import datetime
from ..one_drive_object_base import OneDriveObjectBase


class DataPolicyOperation(OneDriveObjectBase):

    def __init__(self, prop_dict={}):
        self._prop_dict = prop_dict

    @property
    def completed_date_time(self):
        """
        Gets and sets the completedDateTime
        
        Returns:
            datetime:
                The completedDateTime
        """
        if "completedDateTime" in self._prop_dict:
            return datetime.strptime(self._prop_dict["completedDateTime"].replace("Z", ""), "%Y-%m-%dT%H:%M:%S.%f")
        else:
            return None

    @completed_date_time.setter
    def completed_date_time(self, val):
        self._prop_dict["completedDateTime"] = val.isoformat()+"Z"

    @property
    def status(self):
        """
        Gets and sets the status
        
        Returns: 
            :class:`DataPolicyOperationStatus<onedrivesdk.model.data_policy_operation_status.DataPolicyOperationStatus>`:
                The status
        """
        if "status" in self._prop_dict:
            if isinstance(self._prop_dict["status"], OneDriveObjectBase):
                return self._prop_dict["status"]
            else :
                self._prop_dict["status"] = DataPolicyOperationStatus(self._prop_dict["status"])
                return self._prop_dict["status"]

        return None

    @status.setter
    def status(self, val):
        self._prop_dict["status"] = val

    @property
    def storage_location(self):
        """
        Gets and sets the storageLocation
        
        Returns:
            str:
                The storageLocation
        """
        if "storageLocation" in self._prop_dict:
            return self._prop_dict["storageLocation"]
        else:
            return None

    @storage_location.setter
    def storage_location(self, val):
        self._prop_dict["storageLocation"] = val

    @property
    def user_id(self):
        """
        Gets and sets the userId
        
        Returns:
            str:
                The userId
        """
        if "userId" in self._prop_dict:
            return self._prop_dict["userId"]
        else:
            return None

    @user_id.setter
    def user_id(self, val):
        self._prop_dict["userId"] = val

    @property
    def submitted_date_time(self):
        """
        Gets and sets the submittedDateTime
        
        Returns:
            datetime:
                The submittedDateTime
        """
        if "submittedDateTime" in self._prop_dict:
            return datetime.strptime(self._prop_dict["submittedDateTime"].replace("Z", ""), "%Y-%m-%dT%H:%M:%S.%f")
        else:
            return None

    @submitted_date_time.setter
    def submitted_date_time(self, val):
        self._prop_dict["submittedDateTime"] = val.isoformat()+"Z"

