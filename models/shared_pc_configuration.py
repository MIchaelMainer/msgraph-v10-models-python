# -*- coding: utf-8 -*- 
'''
# Copyright (c) Microsoft Corporation.  All Rights Reserved.  Licensed under the MIT License.  See License in the project root for license information.
# 
#  This file was generated and any changes will be overwritten.
'''

from __future__ import unicode_literals
from ..model.shared_pc_account_manager_policy import SharedPCAccountManagerPolicy
from ..model.shared_pc_allowed_account_type import SharedPCAllowedAccountType
from ..model.time_of_day import TimeOfDay
from ..one_drive_object_base import OneDriveObjectBase


class SharedPCConfiguration(OneDriveObjectBase):

    def __init__(self, prop_dict={}):
        self._prop_dict = prop_dict

    @property
    def account_manager_policy(self):
        """
        Gets and sets the accountManagerPolicy
        
        Returns: 
            :class:`SharedPCAccountManagerPolicy<onedrivesdk.model.shared_pc_account_manager_policy.SharedPCAccountManagerPolicy>`:
                The accountManagerPolicy
        """
        if "accountManagerPolicy" in self._prop_dict:
            if isinstance(self._prop_dict["accountManagerPolicy"], OneDriveObjectBase):
                return self._prop_dict["accountManagerPolicy"]
            else :
                self._prop_dict["accountManagerPolicy"] = SharedPCAccountManagerPolicy(self._prop_dict["accountManagerPolicy"])
                return self._prop_dict["accountManagerPolicy"]

        return None

    @account_manager_policy.setter
    def account_manager_policy(self, val):
        self._prop_dict["accountManagerPolicy"] = val

    @property
    def allowed_accounts(self):
        """
        Gets and sets the allowedAccounts
        
        Returns: 
            :class:`SharedPCAllowedAccountType<onedrivesdk.model.shared_pc_allowed_account_type.SharedPCAllowedAccountType>`:
                The allowedAccounts
        """
        if "allowedAccounts" in self._prop_dict:
            if isinstance(self._prop_dict["allowedAccounts"], OneDriveObjectBase):
                return self._prop_dict["allowedAccounts"]
            else :
                self._prop_dict["allowedAccounts"] = SharedPCAllowedAccountType(self._prop_dict["allowedAccounts"])
                return self._prop_dict["allowedAccounts"]

        return None

    @allowed_accounts.setter
    def allowed_accounts(self, val):
        self._prop_dict["allowedAccounts"] = val

    @property
    def allow_local_storage(self):
        """
        Gets and sets the allowLocalStorage
        
        Returns:
            bool:
                The allowLocalStorage
        """
        if "allowLocalStorage" in self._prop_dict:
            return self._prop_dict["allowLocalStorage"]
        else:
            return None

    @allow_local_storage.setter
    def allow_local_storage(self, val):
        self._prop_dict["allowLocalStorage"] = val

    @property
    def disable_account_manager(self):
        """
        Gets and sets the disableAccountManager
        
        Returns:
            bool:
                The disableAccountManager
        """
        if "disableAccountManager" in self._prop_dict:
            return self._prop_dict["disableAccountManager"]
        else:
            return None

    @disable_account_manager.setter
    def disable_account_manager(self, val):
        self._prop_dict["disableAccountManager"] = val

    @property
    def disable_edu_policies(self):
        """
        Gets and sets the disableEduPolicies
        
        Returns:
            bool:
                The disableEduPolicies
        """
        if "disableEduPolicies" in self._prop_dict:
            return self._prop_dict["disableEduPolicies"]
        else:
            return None

    @disable_edu_policies.setter
    def disable_edu_policies(self, val):
        self._prop_dict["disableEduPolicies"] = val

    @property
    def disable_power_policies(self):
        """
        Gets and sets the disablePowerPolicies
        
        Returns:
            bool:
                The disablePowerPolicies
        """
        if "disablePowerPolicies" in self._prop_dict:
            return self._prop_dict["disablePowerPolicies"]
        else:
            return None

    @disable_power_policies.setter
    def disable_power_policies(self, val):
        self._prop_dict["disablePowerPolicies"] = val

    @property
    def disable_sign_in_on_resume(self):
        """
        Gets and sets the disableSignInOnResume
        
        Returns:
            bool:
                The disableSignInOnResume
        """
        if "disableSignInOnResume" in self._prop_dict:
            return self._prop_dict["disableSignInOnResume"]
        else:
            return None

    @disable_sign_in_on_resume.setter
    def disable_sign_in_on_resume(self, val):
        self._prop_dict["disableSignInOnResume"] = val

    @property
    def enabled(self):
        """
        Gets and sets the enabled
        
        Returns:
            bool:
                The enabled
        """
        if "enabled" in self._prop_dict:
            return self._prop_dict["enabled"]
        else:
            return None

    @enabled.setter
    def enabled(self, val):
        self._prop_dict["enabled"] = val

    @property
    def idle_time_before_sleep_in_seconds(self):
        """
        Gets and sets the idleTimeBeforeSleepInSeconds
        
        Returns:
            int:
                The idleTimeBeforeSleepInSeconds
        """
        if "idleTimeBeforeSleepInSeconds" in self._prop_dict:
            return self._prop_dict["idleTimeBeforeSleepInSeconds"]
        else:
            return None

    @idle_time_before_sleep_in_seconds.setter
    def idle_time_before_sleep_in_seconds(self, val):
        self._prop_dict["idleTimeBeforeSleepInSeconds"] = val

    @property
    def kiosk_app_display_name(self):
        """
        Gets and sets the kioskAppDisplayName
        
        Returns:
            str:
                The kioskAppDisplayName
        """
        if "kioskAppDisplayName" in self._prop_dict:
            return self._prop_dict["kioskAppDisplayName"]
        else:
            return None

    @kiosk_app_display_name.setter
    def kiosk_app_display_name(self, val):
        self._prop_dict["kioskAppDisplayName"] = val

    @property
    def kiosk_app_user_model_id(self):
        """
        Gets and sets the kioskAppUserModelId
        
        Returns:
            str:
                The kioskAppUserModelId
        """
        if "kioskAppUserModelId" in self._prop_dict:
            return self._prop_dict["kioskAppUserModelId"]
        else:
            return None

    @kiosk_app_user_model_id.setter
    def kiosk_app_user_model_id(self, val):
        self._prop_dict["kioskAppUserModelId"] = val

    @property
    def maintenance_start_time(self):
        """
        Gets and sets the maintenanceStartTime
        
        Returns: 
            :class:`TimeOfDay<onedrivesdk.model.time_of_day.TimeOfDay>`:
                The maintenanceStartTime
        """
        if "maintenanceStartTime" in self._prop_dict:
            if isinstance(self._prop_dict["maintenanceStartTime"], OneDriveObjectBase):
                return self._prop_dict["maintenanceStartTime"]
            else :
                self._prop_dict["maintenanceStartTime"] = TimeOfDay(self._prop_dict["maintenanceStartTime"])
                return self._prop_dict["maintenanceStartTime"]

        return None

    @maintenance_start_time.setter
    def maintenance_start_time(self, val):
        self._prop_dict["maintenanceStartTime"] = val

