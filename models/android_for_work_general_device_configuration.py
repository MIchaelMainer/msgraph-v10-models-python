# -*- coding: utf-8 -*- 
'''
# Copyright (c) Microsoft Corporation.  All Rights Reserved.  Licensed under the MIT License.  See License in the project root for license information.
# 
#  This file was generated and any changes will be overwritten.
'''

from __future__ import unicode_literals
from ..model.android_for_work_required_password_type import AndroidForWorkRequiredPasswordType
from ..model.android_for_work_cross_profile_data_sharing_type import AndroidForWorkCrossProfileDataSharingType
from ..model.android_for_work_default_app_permission_policy_type import AndroidForWorkDefaultAppPermissionPolicyType
from ..one_drive_object_base import OneDriveObjectBase


class AndroidForWorkGeneralDeviceConfiguration(OneDriveObjectBase):

    def __init__(self, prop_dict={}):
        self._prop_dict = prop_dict

    @property
    def password_block_fingerprint_unlock(self):
        """
        Gets and sets the passwordBlockFingerprintUnlock
        
        Returns:
            bool:
                The passwordBlockFingerprintUnlock
        """
        if "passwordBlockFingerprintUnlock" in self._prop_dict:
            return self._prop_dict["passwordBlockFingerprintUnlock"]
        else:
            return None

    @password_block_fingerprint_unlock.setter
    def password_block_fingerprint_unlock(self, val):
        self._prop_dict["passwordBlockFingerprintUnlock"] = val

    @property
    def password_block_trust_agents(self):
        """
        Gets and sets the passwordBlockTrustAgents
        
        Returns:
            bool:
                The passwordBlockTrustAgents
        """
        if "passwordBlockTrustAgents" in self._prop_dict:
            return self._prop_dict["passwordBlockTrustAgents"]
        else:
            return None

    @password_block_trust_agents.setter
    def password_block_trust_agents(self, val):
        self._prop_dict["passwordBlockTrustAgents"] = val

    @property
    def password_expiration_days(self):
        """
        Gets and sets the passwordExpirationDays
        
        Returns:
            int:
                The passwordExpirationDays
        """
        if "passwordExpirationDays" in self._prop_dict:
            return self._prop_dict["passwordExpirationDays"]
        else:
            return None

    @password_expiration_days.setter
    def password_expiration_days(self, val):
        self._prop_dict["passwordExpirationDays"] = val

    @property
    def password_minimum_length(self):
        """
        Gets and sets the passwordMinimumLength
        
        Returns:
            int:
                The passwordMinimumLength
        """
        if "passwordMinimumLength" in self._prop_dict:
            return self._prop_dict["passwordMinimumLength"]
        else:
            return None

    @password_minimum_length.setter
    def password_minimum_length(self, val):
        self._prop_dict["passwordMinimumLength"] = val

    @property
    def password_minutes_of_inactivity_before_screen_timeout(self):
        """
        Gets and sets the passwordMinutesOfInactivityBeforeScreenTimeout
        
        Returns:
            int:
                The passwordMinutesOfInactivityBeforeScreenTimeout
        """
        if "passwordMinutesOfInactivityBeforeScreenTimeout" in self._prop_dict:
            return self._prop_dict["passwordMinutesOfInactivityBeforeScreenTimeout"]
        else:
            return None

    @password_minutes_of_inactivity_before_screen_timeout.setter
    def password_minutes_of_inactivity_before_screen_timeout(self, val):
        self._prop_dict["passwordMinutesOfInactivityBeforeScreenTimeout"] = val

    @property
    def password_previous_password_block_count(self):
        """
        Gets and sets the passwordPreviousPasswordBlockCount
        
        Returns:
            int:
                The passwordPreviousPasswordBlockCount
        """
        if "passwordPreviousPasswordBlockCount" in self._prop_dict:
            return self._prop_dict["passwordPreviousPasswordBlockCount"]
        else:
            return None

    @password_previous_password_block_count.setter
    def password_previous_password_block_count(self, val):
        self._prop_dict["passwordPreviousPasswordBlockCount"] = val

    @property
    def password_sign_in_failure_count_before_factory_reset(self):
        """
        Gets and sets the passwordSignInFailureCountBeforeFactoryReset
        
        Returns:
            int:
                The passwordSignInFailureCountBeforeFactoryReset
        """
        if "passwordSignInFailureCountBeforeFactoryReset" in self._prop_dict:
            return self._prop_dict["passwordSignInFailureCountBeforeFactoryReset"]
        else:
            return None

    @password_sign_in_failure_count_before_factory_reset.setter
    def password_sign_in_failure_count_before_factory_reset(self, val):
        self._prop_dict["passwordSignInFailureCountBeforeFactoryReset"] = val

    @property
    def password_required_type(self):
        """
        Gets and sets the passwordRequiredType
        
        Returns: 
            :class:`AndroidForWorkRequiredPasswordType<onedrivesdk.model.android_for_work_required_password_type.AndroidForWorkRequiredPasswordType>`:
                The passwordRequiredType
        """
        if "passwordRequiredType" in self._prop_dict:
            if isinstance(self._prop_dict["passwordRequiredType"], OneDriveObjectBase):
                return self._prop_dict["passwordRequiredType"]
            else :
                self._prop_dict["passwordRequiredType"] = AndroidForWorkRequiredPasswordType(self._prop_dict["passwordRequiredType"])
                return self._prop_dict["passwordRequiredType"]

        return None

    @password_required_type.setter
    def password_required_type(self, val):
        self._prop_dict["passwordRequiredType"] = val

    @property
    def work_profile_data_sharing_type(self):
        """
        Gets and sets the workProfileDataSharingType
        
        Returns: 
            :class:`AndroidForWorkCrossProfileDataSharingType<onedrivesdk.model.android_for_work_cross_profile_data_sharing_type.AndroidForWorkCrossProfileDataSharingType>`:
                The workProfileDataSharingType
        """
        if "workProfileDataSharingType" in self._prop_dict:
            if isinstance(self._prop_dict["workProfileDataSharingType"], OneDriveObjectBase):
                return self._prop_dict["workProfileDataSharingType"]
            else :
                self._prop_dict["workProfileDataSharingType"] = AndroidForWorkCrossProfileDataSharingType(self._prop_dict["workProfileDataSharingType"])
                return self._prop_dict["workProfileDataSharingType"]

        return None

    @work_profile_data_sharing_type.setter
    def work_profile_data_sharing_type(self, val):
        self._prop_dict["workProfileDataSharingType"] = val

    @property
    def work_profile_block_notifications_while_device_locked(self):
        """
        Gets and sets the workProfileBlockNotificationsWhileDeviceLocked
        
        Returns:
            bool:
                The workProfileBlockNotificationsWhileDeviceLocked
        """
        if "workProfileBlockNotificationsWhileDeviceLocked" in self._prop_dict:
            return self._prop_dict["workProfileBlockNotificationsWhileDeviceLocked"]
        else:
            return None

    @work_profile_block_notifications_while_device_locked.setter
    def work_profile_block_notifications_while_device_locked(self, val):
        self._prop_dict["workProfileBlockNotificationsWhileDeviceLocked"] = val

    @property
    def work_profile_block_adding_accounts(self):
        """
        Gets and sets the workProfileBlockAddingAccounts
        
        Returns:
            bool:
                The workProfileBlockAddingAccounts
        """
        if "workProfileBlockAddingAccounts" in self._prop_dict:
            return self._prop_dict["workProfileBlockAddingAccounts"]
        else:
            return None

    @work_profile_block_adding_accounts.setter
    def work_profile_block_adding_accounts(self, val):
        self._prop_dict["workProfileBlockAddingAccounts"] = val

    @property
    def work_profile_bluetooth_enable_contact_sharing(self):
        """
        Gets and sets the workProfileBluetoothEnableContactSharing
        
        Returns:
            bool:
                The workProfileBluetoothEnableContactSharing
        """
        if "workProfileBluetoothEnableContactSharing" in self._prop_dict:
            return self._prop_dict["workProfileBluetoothEnableContactSharing"]
        else:
            return None

    @work_profile_bluetooth_enable_contact_sharing.setter
    def work_profile_bluetooth_enable_contact_sharing(self, val):
        self._prop_dict["workProfileBluetoothEnableContactSharing"] = val

    @property
    def work_profile_block_screen_capture(self):
        """
        Gets and sets the workProfileBlockScreenCapture
        
        Returns:
            bool:
                The workProfileBlockScreenCapture
        """
        if "workProfileBlockScreenCapture" in self._prop_dict:
            return self._prop_dict["workProfileBlockScreenCapture"]
        else:
            return None

    @work_profile_block_screen_capture.setter
    def work_profile_block_screen_capture(self, val):
        self._prop_dict["workProfileBlockScreenCapture"] = val

    @property
    def work_profile_block_cross_profile_caller_id(self):
        """
        Gets and sets the workProfileBlockCrossProfileCallerId
        
        Returns:
            bool:
                The workProfileBlockCrossProfileCallerId
        """
        if "workProfileBlockCrossProfileCallerId" in self._prop_dict:
            return self._prop_dict["workProfileBlockCrossProfileCallerId"]
        else:
            return None

    @work_profile_block_cross_profile_caller_id.setter
    def work_profile_block_cross_profile_caller_id(self, val):
        self._prop_dict["workProfileBlockCrossProfileCallerId"] = val

    @property
    def work_profile_block_camera(self):
        """
        Gets and sets the workProfileBlockCamera
        
        Returns:
            bool:
                The workProfileBlockCamera
        """
        if "workProfileBlockCamera" in self._prop_dict:
            return self._prop_dict["workProfileBlockCamera"]
        else:
            return None

    @work_profile_block_camera.setter
    def work_profile_block_camera(self, val):
        self._prop_dict["workProfileBlockCamera"] = val

    @property
    def work_profile_block_cross_profile_contacts_search(self):
        """
        Gets and sets the workProfileBlockCrossProfileContactsSearch
        
        Returns:
            bool:
                The workProfileBlockCrossProfileContactsSearch
        """
        if "workProfileBlockCrossProfileContactsSearch" in self._prop_dict:
            return self._prop_dict["workProfileBlockCrossProfileContactsSearch"]
        else:
            return None

    @work_profile_block_cross_profile_contacts_search.setter
    def work_profile_block_cross_profile_contacts_search(self, val):
        self._prop_dict["workProfileBlockCrossProfileContactsSearch"] = val

    @property
    def work_profile_block_cross_profile_copy_paste(self):
        """
        Gets and sets the workProfileBlockCrossProfileCopyPaste
        
        Returns:
            bool:
                The workProfileBlockCrossProfileCopyPaste
        """
        if "workProfileBlockCrossProfileCopyPaste" in self._prop_dict:
            return self._prop_dict["workProfileBlockCrossProfileCopyPaste"]
        else:
            return None

    @work_profile_block_cross_profile_copy_paste.setter
    def work_profile_block_cross_profile_copy_paste(self, val):
        self._prop_dict["workProfileBlockCrossProfileCopyPaste"] = val

    @property
    def work_profile_default_app_permission_policy(self):
        """
        Gets and sets the workProfileDefaultAppPermissionPolicy
        
        Returns: 
            :class:`AndroidForWorkDefaultAppPermissionPolicyType<onedrivesdk.model.android_for_work_default_app_permission_policy_type.AndroidForWorkDefaultAppPermissionPolicyType>`:
                The workProfileDefaultAppPermissionPolicy
        """
        if "workProfileDefaultAppPermissionPolicy" in self._prop_dict:
            if isinstance(self._prop_dict["workProfileDefaultAppPermissionPolicy"], OneDriveObjectBase):
                return self._prop_dict["workProfileDefaultAppPermissionPolicy"]
            else :
                self._prop_dict["workProfileDefaultAppPermissionPolicy"] = AndroidForWorkDefaultAppPermissionPolicyType(self._prop_dict["workProfileDefaultAppPermissionPolicy"])
                return self._prop_dict["workProfileDefaultAppPermissionPolicy"]

        return None

    @work_profile_default_app_permission_policy.setter
    def work_profile_default_app_permission_policy(self, val):
        self._prop_dict["workProfileDefaultAppPermissionPolicy"] = val

    @property
    def work_profile_password_block_fingerprint_unlock(self):
        """
        Gets and sets the workProfilePasswordBlockFingerprintUnlock
        
        Returns:
            bool:
                The workProfilePasswordBlockFingerprintUnlock
        """
        if "workProfilePasswordBlockFingerprintUnlock" in self._prop_dict:
            return self._prop_dict["workProfilePasswordBlockFingerprintUnlock"]
        else:
            return None

    @work_profile_password_block_fingerprint_unlock.setter
    def work_profile_password_block_fingerprint_unlock(self, val):
        self._prop_dict["workProfilePasswordBlockFingerprintUnlock"] = val

    @property
    def work_profile_password_block_trust_agents(self):
        """
        Gets and sets the workProfilePasswordBlockTrustAgents
        
        Returns:
            bool:
                The workProfilePasswordBlockTrustAgents
        """
        if "workProfilePasswordBlockTrustAgents" in self._prop_dict:
            return self._prop_dict["workProfilePasswordBlockTrustAgents"]
        else:
            return None

    @work_profile_password_block_trust_agents.setter
    def work_profile_password_block_trust_agents(self, val):
        self._prop_dict["workProfilePasswordBlockTrustAgents"] = val

    @property
    def work_profile_password_expiration_days(self):
        """
        Gets and sets the workProfilePasswordExpirationDays
        
        Returns:
            int:
                The workProfilePasswordExpirationDays
        """
        if "workProfilePasswordExpirationDays" in self._prop_dict:
            return self._prop_dict["workProfilePasswordExpirationDays"]
        else:
            return None

    @work_profile_password_expiration_days.setter
    def work_profile_password_expiration_days(self, val):
        self._prop_dict["workProfilePasswordExpirationDays"] = val

    @property
    def work_profile_password_minimum_length(self):
        """
        Gets and sets the workProfilePasswordMinimumLength
        
        Returns:
            int:
                The workProfilePasswordMinimumLength
        """
        if "workProfilePasswordMinimumLength" in self._prop_dict:
            return self._prop_dict["workProfilePasswordMinimumLength"]
        else:
            return None

    @work_profile_password_minimum_length.setter
    def work_profile_password_minimum_length(self, val):
        self._prop_dict["workProfilePasswordMinimumLength"] = val

    @property
    def work_profile_password_minutes_of_inactivity_before_screen_timeout(self):
        """
        Gets and sets the workProfilePasswordMinutesOfInactivityBeforeScreenTimeout
        
        Returns:
            int:
                The workProfilePasswordMinutesOfInactivityBeforeScreenTimeout
        """
        if "workProfilePasswordMinutesOfInactivityBeforeScreenTimeout" in self._prop_dict:
            return self._prop_dict["workProfilePasswordMinutesOfInactivityBeforeScreenTimeout"]
        else:
            return None

    @work_profile_password_minutes_of_inactivity_before_screen_timeout.setter
    def work_profile_password_minutes_of_inactivity_before_screen_timeout(self, val):
        self._prop_dict["workProfilePasswordMinutesOfInactivityBeforeScreenTimeout"] = val

    @property
    def work_profile_password_previous_password_block_count(self):
        """
        Gets and sets the workProfilePasswordPreviousPasswordBlockCount
        
        Returns:
            int:
                The workProfilePasswordPreviousPasswordBlockCount
        """
        if "workProfilePasswordPreviousPasswordBlockCount" in self._prop_dict:
            return self._prop_dict["workProfilePasswordPreviousPasswordBlockCount"]
        else:
            return None

    @work_profile_password_previous_password_block_count.setter
    def work_profile_password_previous_password_block_count(self, val):
        self._prop_dict["workProfilePasswordPreviousPasswordBlockCount"] = val

    @property
    def work_profile_password_sign_in_failure_count_before_factory_reset(self):
        """
        Gets and sets the workProfilePasswordSignInFailureCountBeforeFactoryReset
        
        Returns:
            int:
                The workProfilePasswordSignInFailureCountBeforeFactoryReset
        """
        if "workProfilePasswordSignInFailureCountBeforeFactoryReset" in self._prop_dict:
            return self._prop_dict["workProfilePasswordSignInFailureCountBeforeFactoryReset"]
        else:
            return None

    @work_profile_password_sign_in_failure_count_before_factory_reset.setter
    def work_profile_password_sign_in_failure_count_before_factory_reset(self, val):
        self._prop_dict["workProfilePasswordSignInFailureCountBeforeFactoryReset"] = val

    @property
    def work_profile_password_required_type(self):
        """
        Gets and sets the workProfilePasswordRequiredType
        
        Returns: 
            :class:`AndroidForWorkRequiredPasswordType<onedrivesdk.model.android_for_work_required_password_type.AndroidForWorkRequiredPasswordType>`:
                The workProfilePasswordRequiredType
        """
        if "workProfilePasswordRequiredType" in self._prop_dict:
            if isinstance(self._prop_dict["workProfilePasswordRequiredType"], OneDriveObjectBase):
                return self._prop_dict["workProfilePasswordRequiredType"]
            else :
                self._prop_dict["workProfilePasswordRequiredType"] = AndroidForWorkRequiredPasswordType(self._prop_dict["workProfilePasswordRequiredType"])
                return self._prop_dict["workProfilePasswordRequiredType"]

        return None

    @work_profile_password_required_type.setter
    def work_profile_password_required_type(self, val):
        self._prop_dict["workProfilePasswordRequiredType"] = val

    @property
    def work_profile_require_password(self):
        """
        Gets and sets the workProfileRequirePassword
        
        Returns:
            bool:
                The workProfileRequirePassword
        """
        if "workProfileRequirePassword" in self._prop_dict:
            return self._prop_dict["workProfileRequirePassword"]
        else:
            return None

    @work_profile_require_password.setter
    def work_profile_require_password(self, val):
        self._prop_dict["workProfileRequirePassword"] = val

    @property
    def security_require_verify_apps(self):
        """
        Gets and sets the securityRequireVerifyApps
        
        Returns:
            bool:
                The securityRequireVerifyApps
        """
        if "securityRequireVerifyApps" in self._prop_dict:
            return self._prop_dict["securityRequireVerifyApps"]
        else:
            return None

    @security_require_verify_apps.setter
    def security_require_verify_apps(self, val):
        self._prop_dict["securityRequireVerifyApps"] = val

