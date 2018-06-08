# -*- coding: utf-8 -*- 
'''
# Copyright (c) Microsoft Corporation.  All Rights Reserved.  Licensed under the MIT License.  See License in the project root for license information.
# 
#  This file was generated and any changes will be overwritten.
'''

from __future__ import unicode_literals
from ..model.privileged_role import PrivilegedRole
from datetime import datetime
from ..one_drive_object_base import OneDriveObjectBase


class PrivilegedRoleAssignment(OneDriveObjectBase):

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
    def is_elevated(self):
        """
        Gets and sets the isElevated
        
        Returns:
            bool:
                The isElevated
        """
        if "isElevated" in self._prop_dict:
            return self._prop_dict["isElevated"]
        else:
            return None

    @is_elevated.setter
    def is_elevated(self, val):
        self._prop_dict["isElevated"] = val

    @property
    def expiration_date_time(self):
        """
        Gets and sets the expirationDateTime
        
        Returns:
            datetime:
                The expirationDateTime
        """
        if "expirationDateTime" in self._prop_dict:
            return datetime.strptime(self._prop_dict["expirationDateTime"].replace("Z", ""), "%Y-%m-%dT%H:%M:%S.%f")
        else:
            return None

    @expiration_date_time.setter
    def expiration_date_time(self, val):
        self._prop_dict["expirationDateTime"] = val.isoformat()+"Z"

    @property
    def result_message(self):
        """
        Gets and sets the resultMessage
        
        Returns:
            str:
                The resultMessage
        """
        if "resultMessage" in self._prop_dict:
            return self._prop_dict["resultMessage"]
        else:
            return None

    @result_message.setter
    def result_message(self, val):
        self._prop_dict["resultMessage"] = val

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

