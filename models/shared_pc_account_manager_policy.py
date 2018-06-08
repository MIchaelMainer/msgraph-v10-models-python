# -*- coding: utf-8 -*- 
'''
# Copyright (c) Microsoft Corporation.  All Rights Reserved.  Licensed under the MIT License.  See License in the project root for license information.
# 
#  This file was generated and any changes will be overwritten.
'''

from __future__ import unicode_literals
from ..model.shared_pc_account_deletion_policy_type import SharedPCAccountDeletionPolicyType
from ..one_drive_object_base import OneDriveObjectBase


class SharedPCAccountManagerPolicy(OneDriveObjectBase):

    def __init__(self, prop_dict={}):
        self._prop_dict = prop_dict

    @property
    def account_deletion_policy(self):
        """
        Gets and sets the accountDeletionPolicy
        
        Returns: 
            :class:`SharedPCAccountDeletionPolicyType<onedrivesdk.model.shared_pc_account_deletion_policy_type.SharedPCAccountDeletionPolicyType>`:
                The accountDeletionPolicy
        """
        if "accountDeletionPolicy" in self._prop_dict:
            if isinstance(self._prop_dict["accountDeletionPolicy"], OneDriveObjectBase):
                return self._prop_dict["accountDeletionPolicy"]
            else :
                self._prop_dict["accountDeletionPolicy"] = SharedPCAccountDeletionPolicyType(self._prop_dict["accountDeletionPolicy"])
                return self._prop_dict["accountDeletionPolicy"]

        return None

    @account_deletion_policy.setter
    def account_deletion_policy(self, val):
        self._prop_dict["accountDeletionPolicy"] = val
    @property
    def cache_accounts_above_disk_free_percentage(self):
        """Gets and sets the cacheAccountsAboveDiskFreePercentage
        
        Returns: 
            int:
                The cacheAccountsAboveDiskFreePercentage
        """
        if "cacheAccountsAboveDiskFreePercentage" in self._prop_dict:
            return self._prop_dict["cacheAccountsAboveDiskFreePercentage"]
        else:
            return None

    @cache_accounts_above_disk_free_percentage.setter
    def cache_accounts_above_disk_free_percentage(self, val):
        self._prop_dict["cacheAccountsAboveDiskFreePercentage"] = val

    @property
    def inactive_threshold_days(self):
        """Gets and sets the inactiveThresholdDays
        
        Returns: 
            int:
                The inactiveThresholdDays
        """
        if "inactiveThresholdDays" in self._prop_dict:
            return self._prop_dict["inactiveThresholdDays"]
        else:
            return None

    @inactive_threshold_days.setter
    def inactive_threshold_days(self, val):
        self._prop_dict["inactiveThresholdDays"] = val

    @property
    def remove_accounts_below_disk_free_percentage(self):
        """Gets and sets the removeAccountsBelowDiskFreePercentage
        
        Returns: 
            int:
                The removeAccountsBelowDiskFreePercentage
        """
        if "removeAccountsBelowDiskFreePercentage" in self._prop_dict:
            return self._prop_dict["removeAccountsBelowDiskFreePercentage"]
        else:
            return None

    @remove_accounts_below_disk_free_percentage.setter
    def remove_accounts_below_disk_free_percentage(self, val):
        self._prop_dict["removeAccountsBelowDiskFreePercentage"] = val

