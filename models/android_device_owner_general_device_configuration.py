# -*- coding: utf-8 -*- 
'''
# Copyright (c) Microsoft Corporation.  All Rights Reserved.  Licensed under the MIT License.  See License in the project root for license information.
# 
#  This file was generated and any changes will be overwritten.
'''

from __future__ import unicode_literals
from ..model.android_device_owner_default_app_permission_policy_type import AndroidDeviceOwnerDefaultAppPermissionPolicyType
from ..model.app_list_item import AppListItem
from ..model.android_device_owner_required_password_type import AndroidDeviceOwnerRequiredPasswordType
from ..model.android_device_owner_battery_plugged_mode import AndroidDeviceOwnerBatteryPluggedMode
from ..one_drive_object_base import OneDriveObjectBase


class AndroidDeviceOwnerGeneralDeviceConfiguration(OneDriveObjectBase):

    def __init__(self, prop_dict={}):
        self._prop_dict = prop_dict

    @property
    def accounts_block_modification(self):
        """
        Gets and sets the accountsBlockModification
        
        Returns:
            bool:
                The accountsBlockModification
        """
        if "accountsBlockModification" in self._prop_dict:
            return self._prop_dict["accountsBlockModification"]
        else:
            return None

    @accounts_block_modification.setter
    def accounts_block_modification(self, val):
        self._prop_dict["accountsBlockModification"] = val

    @property
    def apps_allow_install_from_unknown_sources(self):
        """
        Gets and sets the appsAllowInstallFromUnknownSources
        
        Returns:
            bool:
                The appsAllowInstallFromUnknownSources
        """
        if "appsAllowInstallFromUnknownSources" in self._prop_dict:
            return self._prop_dict["appsAllowInstallFromUnknownSources"]
        else:
            return None

    @apps_allow_install_from_unknown_sources.setter
    def apps_allow_install_from_unknown_sources(self, val):
        self._prop_dict["appsAllowInstallFromUnknownSources"] = val

    @property
    def apps_default_permission_policy(self):
        """
        Gets and sets the appsDefaultPermissionPolicy
        
        Returns: 
            :class:`AndroidDeviceOwnerDefaultAppPermissionPolicyType<onedrivesdk.model.android_device_owner_default_app_permission_policy_type.AndroidDeviceOwnerDefaultAppPermissionPolicyType>`:
                The appsDefaultPermissionPolicy
        """
        if "appsDefaultPermissionPolicy" in self._prop_dict:
            if isinstance(self._prop_dict["appsDefaultPermissionPolicy"], OneDriveObjectBase):
                return self._prop_dict["appsDefaultPermissionPolicy"]
            else :
                self._prop_dict["appsDefaultPermissionPolicy"] = AndroidDeviceOwnerDefaultAppPermissionPolicyType(self._prop_dict["appsDefaultPermissionPolicy"])
                return self._prop_dict["appsDefaultPermissionPolicy"]

        return None

    @apps_default_permission_policy.setter
    def apps_default_permission_policy(self, val):
        self._prop_dict["appsDefaultPermissionPolicy"] = val

    @property
    def camera_blocked(self):
        """
        Gets and sets the cameraBlocked
        
        Returns:
            bool:
                The cameraBlocked
        """
        if "cameraBlocked" in self._prop_dict:
            return self._prop_dict["cameraBlocked"]
        else:
            return None

    @camera_blocked.setter
    def camera_blocked(self, val):
        self._prop_dict["cameraBlocked"] = val

    @property
    def factory_reset_device_administrator_emails(self):
        """
        Gets and sets the factoryResetDeviceAdministratorEmails
        
        Returns:
            str:
                The factoryResetDeviceAdministratorEmails
        """
        if "factoryResetDeviceAdministratorEmails" in self._prop_dict:
            return self._prop_dict["factoryResetDeviceAdministratorEmails"]
        else:
            return None

    @factory_reset_device_administrator_emails.setter
    def factory_reset_device_administrator_emails(self, val):
        self._prop_dict["factoryResetDeviceAdministratorEmails"] = val

    @property
    def factory_reset_blocked(self):
        """
        Gets and sets the factoryResetBlocked
        
        Returns:
            bool:
                The factoryResetBlocked
        """
        if "factoryResetBlocked" in self._prop_dict:
            return self._prop_dict["factoryResetBlocked"]
        else:
            return None

    @factory_reset_blocked.setter
    def factory_reset_blocked(self, val):
        self._prop_dict["factoryResetBlocked"] = val

    @property
    def kiosk_mode_apps(self):
        """Gets and sets the kioskModeApps
        
        Returns: 
            :class:`KioskModeAppsCollectionPage<onedrivesdk.request.kiosk_mode_apps_collection.KioskModeAppsCollectionPage>`:
                The kioskModeApps
        """
        if "kioskModeApps" in self._prop_dict:
            return KioskModeAppsCollectionPage(self._prop_dict["kioskModeApps"])
        else:
            return None

    @property
    def microphone_force_mute(self):
        """
        Gets and sets the microphoneForceMute
        
        Returns:
            bool:
                The microphoneForceMute
        """
        if "microphoneForceMute" in self._prop_dict:
            return self._prop_dict["microphoneForceMute"]
        else:
            return None

    @microphone_force_mute.setter
    def microphone_force_mute(self, val):
        self._prop_dict["microphoneForceMute"] = val

    @property
    def network_escape_hatch_allowed(self):
        """
        Gets and sets the networkEscapeHatchAllowed
        
        Returns:
            bool:
                The networkEscapeHatchAllowed
        """
        if "networkEscapeHatchAllowed" in self._prop_dict:
            return self._prop_dict["networkEscapeHatchAllowed"]
        else:
            return None

    @network_escape_hatch_allowed.setter
    def network_escape_hatch_allowed(self, val):
        self._prop_dict["networkEscapeHatchAllowed"] = val

    @property
    def password_block_keyguard(self):
        """
        Gets and sets the passwordBlockKeyguard
        
        Returns:
            bool:
                The passwordBlockKeyguard
        """
        if "passwordBlockKeyguard" in self._prop_dict:
            return self._prop_dict["passwordBlockKeyguard"]
        else:
            return None

    @password_block_keyguard.setter
    def password_block_keyguard(self, val):
        self._prop_dict["passwordBlockKeyguard"] = val

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
    def password_previous_password_count_to_block(self):
        """
        Gets and sets the passwordPreviousPasswordCountToBlock
        
        Returns:
            int:
                The passwordPreviousPasswordCountToBlock
        """
        if "passwordPreviousPasswordCountToBlock" in self._prop_dict:
            return self._prop_dict["passwordPreviousPasswordCountToBlock"]
        else:
            return None

    @password_previous_password_count_to_block.setter
    def password_previous_password_count_to_block(self, val):
        self._prop_dict["passwordPreviousPasswordCountToBlock"] = val

    @property
    def password_required_type(self):
        """
        Gets and sets the passwordRequiredType
        
        Returns: 
            :class:`AndroidDeviceOwnerRequiredPasswordType<onedrivesdk.model.android_device_owner_required_password_type.AndroidDeviceOwnerRequiredPasswordType>`:
                The passwordRequiredType
        """
        if "passwordRequiredType" in self._prop_dict:
            if isinstance(self._prop_dict["passwordRequiredType"], OneDriveObjectBase):
                return self._prop_dict["passwordRequiredType"]
            else :
                self._prop_dict["passwordRequiredType"] = AndroidDeviceOwnerRequiredPasswordType(self._prop_dict["passwordRequiredType"])
                return self._prop_dict["passwordRequiredType"]

        return None

    @password_required_type.setter
    def password_required_type(self, val):
        self._prop_dict["passwordRequiredType"] = val

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
    def safe_boot_blocked(self):
        """
        Gets and sets the safeBootBlocked
        
        Returns:
            bool:
                The safeBootBlocked
        """
        if "safeBootBlocked" in self._prop_dict:
            return self._prop_dict["safeBootBlocked"]
        else:
            return None

    @safe_boot_blocked.setter
    def safe_boot_blocked(self, val):
        self._prop_dict["safeBootBlocked"] = val

    @property
    def screen_capture_blocked(self):
        """
        Gets and sets the screenCaptureBlocked
        
        Returns:
            bool:
                The screenCaptureBlocked
        """
        if "screenCaptureBlocked" in self._prop_dict:
            return self._prop_dict["screenCaptureBlocked"]
        else:
            return None

    @screen_capture_blocked.setter
    def screen_capture_blocked(self, val):
        self._prop_dict["screenCaptureBlocked"] = val

    @property
    def security_allow_debugging_features(self):
        """
        Gets and sets the securityAllowDebuggingFeatures
        
        Returns:
            bool:
                The securityAllowDebuggingFeatures
        """
        if "securityAllowDebuggingFeatures" in self._prop_dict:
            return self._prop_dict["securityAllowDebuggingFeatures"]
        else:
            return None

    @security_allow_debugging_features.setter
    def security_allow_debugging_features(self, val):
        self._prop_dict["securityAllowDebuggingFeatures"] = val

    @property
    def status_bar_blocked(self):
        """
        Gets and sets the statusBarBlocked
        
        Returns:
            bool:
                The statusBarBlocked
        """
        if "statusBarBlocked" in self._prop_dict:
            return self._prop_dict["statusBarBlocked"]
        else:
            return None

    @status_bar_blocked.setter
    def status_bar_blocked(self, val):
        self._prop_dict["statusBarBlocked"] = val

    @property
    def stay_on_modes(self):
        """Gets and sets the stayOnModes
        
        Returns: 
            :class:`StayOnModesCollectionPage<onedrivesdk.request.stay_on_modes_collection.StayOnModesCollectionPage>`:
                The stayOnModes
        """
        if "stayOnModes" in self._prop_dict:
            return StayOnModesCollectionPage(self._prop_dict["stayOnModes"])
        else:
            return None

    @property
    def users_block_add(self):
        """
        Gets and sets the usersBlockAdd
        
        Returns:
            bool:
                The usersBlockAdd
        """
        if "usersBlockAdd" in self._prop_dict:
            return self._prop_dict["usersBlockAdd"]
        else:
            return None

    @users_block_add.setter
    def users_block_add(self, val):
        self._prop_dict["usersBlockAdd"] = val

    @property
    def users_block_remove(self):
        """
        Gets and sets the usersBlockRemove
        
        Returns:
            bool:
                The usersBlockRemove
        """
        if "usersBlockRemove" in self._prop_dict:
            return self._prop_dict["usersBlockRemove"]
        else:
            return None

    @users_block_remove.setter
    def users_block_remove(self, val):
        self._prop_dict["usersBlockRemove"] = val

    @property
    def volume_block_adjustment(self):
        """
        Gets and sets the volumeBlockAdjustment
        
        Returns:
            bool:
                The volumeBlockAdjustment
        """
        if "volumeBlockAdjustment" in self._prop_dict:
            return self._prop_dict["volumeBlockAdjustment"]
        else:
            return None

    @volume_block_adjustment.setter
    def volume_block_adjustment(self, val):
        self._prop_dict["volumeBlockAdjustment"] = val

    @property
    def wifi_block_edit_configurations(self):
        """
        Gets and sets the wifiBlockEditConfigurations
        
        Returns:
            bool:
                The wifiBlockEditConfigurations
        """
        if "wifiBlockEditConfigurations" in self._prop_dict:
            return self._prop_dict["wifiBlockEditConfigurations"]
        else:
            return None

    @wifi_block_edit_configurations.setter
    def wifi_block_edit_configurations(self, val):
        self._prop_dict["wifiBlockEditConfigurations"] = val

    @property
    def wifi_block_edit_policy_defined_configurations(self):
        """
        Gets and sets the wifiBlockEditPolicyDefinedConfigurations
        
        Returns:
            bool:
                The wifiBlockEditPolicyDefinedConfigurations
        """
        if "wifiBlockEditPolicyDefinedConfigurations" in self._prop_dict:
            return self._prop_dict["wifiBlockEditPolicyDefinedConfigurations"]
        else:
            return None

    @wifi_block_edit_policy_defined_configurations.setter
    def wifi_block_edit_policy_defined_configurations(self, val):
        self._prop_dict["wifiBlockEditPolicyDefinedConfigurations"] = val

