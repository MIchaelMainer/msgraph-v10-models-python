# -*- coding: utf-8 -*- 
'''
# Copyright (c) Microsoft Corporation.  All Rights Reserved.  Licensed under the MIT License.  See License in the project root for license information.
# 
#  This file was generated and any changes will be overwritten.
'''

from __future__ import unicode_literals
from ..model.role_summary_status import RoleSummaryStatus
from ..one_drive_object_base import OneDriveObjectBase


class PrivilegedRoleSummary(OneDriveObjectBase):

    def __init__(self, prop_dict={}):
        self._prop_dict = prop_dict

    @property
    def status(self):
        """
        Gets and sets the status
        
        Returns: 
            :class:`RoleSummaryStatus<onedrivesdk.model.role_summary_status.RoleSummaryStatus>`:
                The status
        """
        if "status" in self._prop_dict:
            if isinstance(self._prop_dict["status"], OneDriveObjectBase):
                return self._prop_dict["status"]
            else :
                self._prop_dict["status"] = RoleSummaryStatus(self._prop_dict["status"])
                return self._prop_dict["status"]

        return None

    @status.setter
    def status(self, val):
        self._prop_dict["status"] = val

    @property
    def users_count(self):
        """
        Gets and sets the usersCount
        
        Returns:
            int:
                The usersCount
        """
        if "usersCount" in self._prop_dict:
            return self._prop_dict["usersCount"]
        else:
            return None

    @users_count.setter
    def users_count(self, val):
        self._prop_dict["usersCount"] = val

    @property
    def managed_count(self):
        """
        Gets and sets the managedCount
        
        Returns:
            int:
                The managedCount
        """
        if "managedCount" in self._prop_dict:
            return self._prop_dict["managedCount"]
        else:
            return None

    @managed_count.setter
    def managed_count(self, val):
        self._prop_dict["managedCount"] = val

    @property
    def elevated_count(self):
        """
        Gets and sets the elevatedCount
        
        Returns:
            int:
                The elevatedCount
        """
        if "elevatedCount" in self._prop_dict:
            return self._prop_dict["elevatedCount"]
        else:
            return None

    @elevated_count.setter
    def elevated_count(self, val):
        self._prop_dict["elevatedCount"] = val

    @property
    def mfa_enabled(self):
        """
        Gets and sets the mfaEnabled
        
        Returns:
            bool:
                The mfaEnabled
        """
        if "mfaEnabled" in self._prop_dict:
            return self._prop_dict["mfaEnabled"]
        else:
            return None

    @mfa_enabled.setter
    def mfa_enabled(self, val):
        self._prop_dict["mfaEnabled"] = val

