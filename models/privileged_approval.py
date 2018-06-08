# -*- coding: utf-8 -*- 
'''
# Copyright (c) Microsoft Corporation.  All Rights Reserved.  Licensed under the MIT License.  See License in the project root for license information.
# 
#  This file was generated and any changes will be overwritten.
'''

from __future__ import unicode_literals
from ..model.approval_state import ApprovalState
from ..model.duration import Duration
from ..model.privileged_role import PrivilegedRole
from datetime import datetime
from ..one_drive_object_base import OneDriveObjectBase


class PrivilegedApproval(OneDriveObjectBase):

    def __init__(self, prop_dict={}):
        self._prop_dict = prop_dict

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
    def role_id(self):
        """
        Gets and sets the roleId
        
        Returns:
            str:
                The roleId
        """
        if "roleId" in self._prop_dict:
            return self._prop_dict["roleId"]
        else:
            return None

    @role_id.setter
    def role_id(self, val):
        self._prop_dict["roleId"] = val

    @property
    def approval_type(self):
        """
        Gets and sets the approvalType
        
        Returns:
            str:
                The approvalType
        """
        if "approvalType" in self._prop_dict:
            return self._prop_dict["approvalType"]
        else:
            return None

    @approval_type.setter
    def approval_type(self, val):
        self._prop_dict["approvalType"] = val

    @property
    def approval_state(self):
        """
        Gets and sets the approvalState
        
        Returns: 
            :class:`ApprovalState<onedrivesdk.model.approval_state.ApprovalState>`:
                The approvalState
        """
        if "approvalState" in self._prop_dict:
            if isinstance(self._prop_dict["approvalState"], OneDriveObjectBase):
                return self._prop_dict["approvalState"]
            else :
                self._prop_dict["approvalState"] = ApprovalState(self._prop_dict["approvalState"])
                return self._prop_dict["approvalState"]

        return None

    @approval_state.setter
    def approval_state(self, val):
        self._prop_dict["approvalState"] = val

    @property
    def approval_duration(self):
        """
        Gets and sets the approvalDuration
        
        Returns: 
            :class:`Duration<onedrivesdk.model.duration.Duration>`:
                The approvalDuration
        """
        if "approvalDuration" in self._prop_dict:
            if isinstance(self._prop_dict["approvalDuration"], OneDriveObjectBase):
                return self._prop_dict["approvalDuration"]
            else :
                self._prop_dict["approvalDuration"] = Duration(self._prop_dict["approvalDuration"])
                return self._prop_dict["approvalDuration"]

        return None

    @approval_duration.setter
    def approval_duration(self, val):
        self._prop_dict["approvalDuration"] = val

    @property
    def requestor_reason(self):
        """
        Gets and sets the requestorReason
        
        Returns:
            str:
                The requestorReason
        """
        if "requestorReason" in self._prop_dict:
            return self._prop_dict["requestorReason"]
        else:
            return None

    @requestor_reason.setter
    def requestor_reason(self, val):
        self._prop_dict["requestorReason"] = val

    @property
    def approver_reason(self):
        """
        Gets and sets the approverReason
        
        Returns:
            str:
                The approverReason
        """
        if "approverReason" in self._prop_dict:
            return self._prop_dict["approverReason"]
        else:
            return None

    @approver_reason.setter
    def approver_reason(self, val):
        self._prop_dict["approverReason"] = val

    @property
    def start_date_time(self):
        """
        Gets and sets the startDateTime
        
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
    def end_date_time(self):
        """
        Gets and sets the endDateTime
        
        Returns:
            datetime:
                The endDateTime
        """
        if "endDateTime" in self._prop_dict:
            return datetime.strptime(self._prop_dict["endDateTime"].replace("Z", ""), "%Y-%m-%dT%H:%M:%S.%f")
        else:
            return None

    @end_date_time.setter
    def end_date_time(self, val):
        self._prop_dict["endDateTime"] = val.isoformat()+"Z"

    @property
    def role_info(self):
        """
        Gets and sets the roleInfo
        
        Returns: 
            :class:`PrivilegedRole<onedrivesdk.model.privileged_role.PrivilegedRole>`:
                The roleInfo
        """
        if "roleInfo" in self._prop_dict:
            if isinstance(self._prop_dict["roleInfo"], OneDriveObjectBase):
                return self._prop_dict["roleInfo"]
            else :
                self._prop_dict["roleInfo"] = PrivilegedRole(self._prop_dict["roleInfo"])
                return self._prop_dict["roleInfo"]

        return None

    @role_info.setter
    def role_info(self, val):
        self._prop_dict["roleInfo"] = val

