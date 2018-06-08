# -*- coding: utf-8 -*- 
'''
# Copyright (c) Microsoft Corporation.  All Rights Reserved.  Licensed under the MIT License.  See License in the project root for license information.
# 
#  This file was generated and any changes will be overwritten.
'''

from __future__ import unicode_literals
from ..model.setup_status import SetupStatus
from ..one_drive_object_base import OneDriveObjectBase


class PrivilegedSignupStatus(OneDriveObjectBase):

    def __init__(self, prop_dict={}):
        self._prop_dict = prop_dict

    @property
    def is_registered(self):
        """
        Gets and sets the isRegistered
        
        Returns:
            bool:
                The isRegistered
        """
        if "isRegistered" in self._prop_dict:
            return self._prop_dict["isRegistered"]
        else:
            return None

    @is_registered.setter
    def is_registered(self, val):
        self._prop_dict["isRegistered"] = val

    @property
    def status(self):
        """
        Gets and sets the status
        
        Returns: 
            :class:`SetupStatus<onedrivesdk.model.setup_status.SetupStatus>`:
                The status
        """
        if "status" in self._prop_dict:
            if isinstance(self._prop_dict["status"], OneDriveObjectBase):
                return self._prop_dict["status"]
            else :
                self._prop_dict["status"] = SetupStatus(self._prop_dict["status"])
                return self._prop_dict["status"]

        return None

    @status.setter
    def status(self, val):
        self._prop_dict["status"] = val

