# -*- coding: utf-8 -*- 
'''
# Copyright (c) Microsoft Corporation.  All Rights Reserved.  Licensed under the MIT License.  See License in the project root for license information.
# 
#  This file was generated and any changes will be overwritten.
'''

from __future__ import unicode_literals
from ..model.key_value import KeyValue
from ..one_drive_object_base import OneDriveObjectBase


class GovernanceRoleAssignmentRequestStatus(OneDriveObjectBase):

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
    def sub_status(self):
        """Gets and sets the subStatus
        
        Returns: 
            str:
                The subStatus
        """
        if "subStatus" in self._prop_dict:
            return self._prop_dict["subStatus"]
        else:
            return None

    @sub_status.setter
    def sub_status(self, val):
        self._prop_dict["subStatus"] = val

    @property
    def status_details(self):
        """
        Gets and sets the statusDetails
        
        Returns: 
            :class:`KeyValue<onedrivesdk.model.key_value.KeyValue>`:
                The statusDetails
        """
        if "statusDetails" in self._prop_dict:
            if isinstance(self._prop_dict["statusDetails"], OneDriveObjectBase):
                return self._prop_dict["statusDetails"]
            else :
                self._prop_dict["statusDetails"] = KeyValue(self._prop_dict["statusDetails"])
                return self._prop_dict["statusDetails"]

        return None

    @status_details.setter
    def status_details(self, val):
        self._prop_dict["statusDetails"] = val
