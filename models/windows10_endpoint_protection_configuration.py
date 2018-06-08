# -*- coding: utf-8 -*- 
'''
# Copyright (c) Microsoft Corporation.  All Rights Reserved.  Licensed under the MIT License.  See License in the project root for license information.
# 
#  This file was generated and any changes will be overwritten.
'''

from __future__ import unicode_literals
from ..model.local_security_options_format_and_eject_of_removable_media_allowed_user_type import LocalSecurityOptionsFormatAndEjectOfRemovableMediaAllowedUserType
from ..model.local_security_options_administrator_elevation_prompt_behavior_type import LocalSecurityOptionsAdministratorElevationPromptBehaviorType
from ..model.local_security_options_standard_user_elevation_prompt_behavior_type import LocalSecurityOptionsStandardUserElevationPromptBehaviorType
from ..model.local_security_options_information_shown_on_lock_screen_type import LocalSecurityOptionsInformationShownOnLockScreenType
from ..model.local_security_options_information_displayed_on_lock_screen_type import LocalSecurityOptionsInformationDisplayedOnLockScreenType
from ..model.local_security_options_smart_card_removal_behavior_type import LocalSecurityOptionsSmartCardRemovalBehaviorType
from ..model.defender_security_center_notifications_from_app_type import DefenderSecurityCenterNotificationsFromAppType
from ..model.defender_security_center_it_contact_display_type import DefenderSecurityCenterITContactDisplayType
from ..model.firewall_pre_shared_key_encoding_method_type import FirewallPreSharedKeyEncodingMethodType
from ..model.firewall_certificate_revocation_list_check_method_type import FirewallCertificateRevocationListCheckMethodType
from ..model.firewall_packet_queueing_method_type import FirewallPacketQueueingMethodType
from ..model.windows_firewall_network_profile import WindowsFirewallNetworkProfile
from ..model.defender_attack_surface_type import DefenderAttackSurfaceType
from ..model.defender_protection_type import DefenderProtectionType
from ..model.folder_protection_type import FolderProtectionType
from ..model.app_locker_application_control_type import AppLockerApplicationControlType
from ..model.device_guard_local_system_authority_credential_guard_type import DeviceGuardLocalSystemAuthorityCredentialGuardType
from ..model.application_guard_block_file_transfer_type import ApplicationGuardBlockFileTransferType
from ..model.application_guard_block_clipboard_sharing_type import ApplicationGuardBlockClipboardSharingType
from ..model.bit_locker_system_drive_policy import BitLockerSystemDrivePolicy
from ..model.bit_locker_fixed_drive_policy import BitLockerFixedDrivePolicy
from ..model.bit_locker_removable_drive_policy import BitLockerRemovableDrivePolicy
from ..one_drive_object_base import OneDriveObjectBase


class Windows10EndpointProtectionConfiguration(OneDriveObjectBase):

    def __init__(self, prop_dict={}):
        self._prop_dict = prop_dict

    @property
    def local_security_options_block_microsoft_accounts(self):
        """
        Gets and sets the localSecurityOptionsBlockMicrosoftAccounts
        
        Returns:
            bool:
                The localSecurityOptionsBlockMicrosoftAccounts
        """
        if "localSecurityOptionsBlockMicrosoftAccounts" in self._prop_dict:
            return self._prop_dict["localSecurityOptionsBlockMicrosoftAccounts"]
        else:
            return None

    @local_security_options_block_microsoft_accounts.setter
    def local_security_options_block_microsoft_accounts(self, val):
        self._prop_dict["localSecurityOptionsBlockMicrosoftAccounts"] = val

    @property
    def local_security_options_block_remote_logon_with_blank_password(self):
        """
        Gets and sets the localSecurityOptionsBlockRemoteLogonWithBlankPassword
        
        Returns:
            bool:
                The localSecurityOptionsBlockRemoteLogonWithBlankPassword
        """
        if "localSecurityOptionsBlockRemoteLogonWithBlankPassword" in self._prop_dict:
            return self._prop_dict["localSecurityOptionsBlockRemoteLogonWithBlankPassword"]
        else:
            return None

    @local_security_options_block_remote_logon_with_blank_password.setter
    def local_security_options_block_remote_logon_with_blank_password(self, val):
        self._prop_dict["localSecurityOptionsBlockRemoteLogonWithBlankPassword"] = val

    @property
    def local_security_options_enable_administrator_account(self):
        """
        Gets and sets the localSecurityOptionsEnableAdministratorAccount
        
        Returns:
            bool:
                The localSecurityOptionsEnableAdministratorAccount
        """
        if "localSecurityOptionsEnableAdministratorAccount" in self._prop_dict:
            return self._prop_dict["localSecurityOptionsEnableAdministratorAccount"]
        else:
            return None

    @local_security_options_enable_administrator_account.setter
    def local_security_options_enable_administrator_account(self, val):
        self._prop_dict["localSecurityOptionsEnableAdministratorAccount"] = val

    @property
    def local_security_options_administrator_account_name(self):
        """
        Gets and sets the localSecurityOptionsAdministratorAccountName
        
        Returns:
            str:
                The localSecurityOptionsAdministratorAccountName
        """
        if "localSecurityOptionsAdministratorAccountName" in self._prop_dict:
            return self._prop_dict["localSecurityOptionsAdministratorAccountName"]
        else:
            return None

    @local_security_options_administrator_account_name.setter
    def local_security_options_administrator_account_name(self, val):
        self._prop_dict["localSecurityOptionsAdministratorAccountName"] = val

    @property
    def local_security_options_enable_guest_account(self):
        """
        Gets and sets the localSecurityOptionsEnableGuestAccount
        
        Returns:
            bool:
                The localSecurityOptionsEnableGuestAccount
        """
        if "localSecurityOptionsEnableGuestAccount" in self._prop_dict:
            return self._prop_dict["localSecurityOptionsEnableGuestAccount"]
        else:
            return None

    @local_security_options_enable_guest_account.setter
    def local_security_options_enable_guest_account(self, val):
        self._prop_dict["localSecurityOptionsEnableGuestAccount"] = val

    @property
    def local_security_options_guest_account_name(self):
        """
        Gets and sets the localSecurityOptionsGuestAccountName
        
        Returns:
            str:
                The localSecurityOptionsGuestAccountName
        """
        if "localSecurityOptionsGuestAccountName" in self._prop_dict:
            return self._prop_dict["localSecurityOptionsGuestAccountName"]
        else:
            return None

    @local_security_options_guest_account_name.setter
    def local_security_options_guest_account_name(self, val):
        self._prop_dict["localSecurityOptionsGuestAccountName"] = val

    @property
    def local_security_options_allow_undock_without_having_to_logon(self):
        """
        Gets and sets the localSecurityOptionsAllowUndockWithoutHavingToLogon
        
        Returns:
            bool:
                The localSecurityOptionsAllowUndockWithoutHavingToLogon
        """
        if "localSecurityOptionsAllowUndockWithoutHavingToLogon" in self._prop_dict:
            return self._prop_dict["localSecurityOptionsAllowUndockWithoutHavingToLogon"]
        else:
            return None

    @local_security_options_allow_undock_without_having_to_logon.setter
    def local_security_options_allow_undock_without_having_to_logon(self, val):
        self._prop_dict["localSecurityOptionsAllowUndockWithoutHavingToLogon"] = val

    @property
    def local_security_options_block_users_installing_printer_drivers(self):
        """
        Gets and sets the localSecurityOptionsBlockUsersInstallingPrinterDrivers
        
        Returns:
            bool:
                The localSecurityOptionsBlockUsersInstallingPrinterDrivers
        """
        if "localSecurityOptionsBlockUsersInstallingPrinterDrivers" in self._prop_dict:
            return self._prop_dict["localSecurityOptionsBlockUsersInstallingPrinterDrivers"]
        else:
            return None

    @local_security_options_block_users_installing_printer_drivers.setter
    def local_security_options_block_users_installing_printer_drivers(self, val):
        self._prop_dict["localSecurityOptionsBlockUsersInstallingPrinterDrivers"] = val

    @property
    def local_security_options_block_remote_optical_drive_access(self):
        """
        Gets and sets the localSecurityOptionsBlockRemoteOpticalDriveAccess
        
        Returns:
            bool:
                The localSecurityOptionsBlockRemoteOpticalDriveAccess
        """
        if "localSecurityOptionsBlockRemoteOpticalDriveAccess" in self._prop_dict:
            return self._prop_dict["localSecurityOptionsBlockRemoteOpticalDriveAccess"]
        else:
            return None

    @local_security_options_block_remote_optical_drive_access.setter
    def local_security_options_block_remote_optical_drive_access(self, val):
        self._prop_dict["localSecurityOptionsBlockRemoteOpticalDriveAccess"] = val

    @property
    def local_security_options_format_and_eject_of_removable_media_allowed_user(self):
        """
        Gets and sets the localSecurityOptionsFormatAndEjectOfRemovableMediaAllowedUser
        
        Returns: 
            :class:`LocalSecurityOptionsFormatAndEjectOfRemovableMediaAllowedUserType<onedrivesdk.model.local_security_options_format_and_eject_of_removable_media_allowed_user_type.LocalSecurityOptionsFormatAndEjectOfRemovableMediaAllowedUserType>`:
                The localSecurityOptionsFormatAndEjectOfRemovableMediaAllowedUser
        """
        if "localSecurityOptionsFormatAndEjectOfRemovableMediaAllowedUser" in self._prop_dict:
            if isinstance(self._prop_dict["localSecurityOptionsFormatAndEjectOfRemovableMediaAllowedUser"], OneDriveObjectBase):
                return self._prop_dict["localSecurityOptionsFormatAndEjectOfRemovableMediaAllowedUser"]
            else :
                self._prop_dict["localSecurityOptionsFormatAndEjectOfRemovableMediaAllowedUser"] = LocalSecurityOptionsFormatAndEjectOfRemovableMediaAllowedUserType(self._prop_dict["localSecurityOptionsFormatAndEjectOfRemovableMediaAllowedUser"])
                return self._prop_dict["localSecurityOptionsFormatAndEjectOfRemovableMediaAllowedUser"]

        return None

    @local_security_options_format_and_eject_of_removable_media_allowed_user.setter
    def local_security_options_format_and_eject_of_removable_media_allowed_user(self, val):
        self._prop_dict["localSecurityOptionsFormatAndEjectOfRemovableMediaAllowedUser"] = val

    @property
    def local_security_options_machine_inactivity_limit(self):
        """
        Gets and sets the localSecurityOptionsMachineInactivityLimit
        
        Returns:
            int:
                The localSecurityOptionsMachineInactivityLimit
        """
        if "localSecurityOptionsMachineInactivityLimit" in self._prop_dict:
            return self._prop_dict["localSecurityOptionsMachineInactivityLimit"]
        else:
            return None

    @local_security_options_machine_inactivity_limit.setter
    def local_security_options_machine_inactivity_limit(self, val):
        self._prop_dict["localSecurityOptionsMachineInactivityLimit"] = val

    @property
    def local_security_options_machine_inactivity_limit_in_minutes(self):
        """
        Gets and sets the localSecurityOptionsMachineInactivityLimitInMinutes
        
        Returns:
            int:
                The localSecurityOptionsMachineInactivityLimitInMinutes
        """
        if "localSecurityOptionsMachineInactivityLimitInMinutes" in self._prop_dict:
            return self._prop_dict["localSecurityOptionsMachineInactivityLimitInMinutes"]
        else:
            return None

    @local_security_options_machine_inactivity_limit_in_minutes.setter
    def local_security_options_machine_inactivity_limit_in_minutes(self, val):
        self._prop_dict["localSecurityOptionsMachineInactivityLimitInMinutes"] = val

    @property
    def local_security_options_do_not_require_ctrl_alt_del(self):
        """
        Gets and sets the localSecurityOptionsDoNotRequireCtrlAltDel
        
        Returns:
            bool:
                The localSecurityOptionsDoNotRequireCtrlAltDel
        """
        if "localSecurityOptionsDoNotRequireCtrlAltDel" in self._prop_dict:
            return self._prop_dict["localSecurityOptionsDoNotRequireCtrlAltDel"]
        else:
            return None

    @local_security_options_do_not_require_ctrl_alt_del.setter
    def local_security_options_do_not_require_ctrl_alt_del(self, val):
        self._prop_dict["localSecurityOptionsDoNotRequireCtrlAltDel"] = val

    @property
    def local_security_options_hide_last_signed_in_user(self):
        """
        Gets and sets the localSecurityOptionsHideLastSignedInUser
        
        Returns:
            bool:
                The localSecurityOptionsHideLastSignedInUser
        """
        if "localSecurityOptionsHideLastSignedInUser" in self._prop_dict:
            return self._prop_dict["localSecurityOptionsHideLastSignedInUser"]
        else:
            return None

    @local_security_options_hide_last_signed_in_user.setter
    def local_security_options_hide_last_signed_in_user(self, val):
        self._prop_dict["localSecurityOptionsHideLastSignedInUser"] = val

    @property
    def local_security_options_hide_username_at_sign_in(self):
        """
        Gets and sets the localSecurityOptionsHideUsernameAtSignIn
        
        Returns:
            bool:
                The localSecurityOptionsHideUsernameAtSignIn
        """
        if "localSecurityOptionsHideUsernameAtSignIn" in self._prop_dict:
            return self._prop_dict["localSecurityOptionsHideUsernameAtSignIn"]
        else:
            return None

    @local_security_options_hide_username_at_sign_in.setter
    def local_security_options_hide_username_at_sign_in(self, val):
        self._prop_dict["localSecurityOptionsHideUsernameAtSignIn"] = val

    @property
    def local_security_options_log_on_message_title(self):
        """
        Gets and sets the localSecurityOptionsLogOnMessageTitle
        
        Returns:
            str:
                The localSecurityOptionsLogOnMessageTitle
        """
        if "localSecurityOptionsLogOnMessageTitle" in self._prop_dict:
            return self._prop_dict["localSecurityOptionsLogOnMessageTitle"]
        else:
            return None

    @local_security_options_log_on_message_title.setter
    def local_security_options_log_on_message_title(self, val):
        self._prop_dict["localSecurityOptionsLogOnMessageTitle"] = val

    @property
    def local_security_options_log_on_message_text(self):
        """
        Gets and sets the localSecurityOptionsLogOnMessageText
        
        Returns:
            str:
                The localSecurityOptionsLogOnMessageText
        """
        if "localSecurityOptionsLogOnMessageText" in self._prop_dict:
            return self._prop_dict["localSecurityOptionsLogOnMessageText"]
        else:
            return None

    @local_security_options_log_on_message_text.setter
    def local_security_options_log_on_message_text(self, val):
        self._prop_dict["localSecurityOptionsLogOnMessageText"] = val

    @property
    def local_security_options_allow_pku2_u_authentication_requests(self):
        """
        Gets and sets the localSecurityOptionsAllowPKU2UAuthenticationRequests
        
        Returns:
            bool:
                The localSecurityOptionsAllowPKU2UAuthenticationRequests
        """
        if "localSecurityOptionsAllowPKU2UAuthenticationRequests" in self._prop_dict:
            return self._prop_dict["localSecurityOptionsAllowPKU2UAuthenticationRequests"]
        else:
            return None

    @local_security_options_allow_pku2_u_authentication_requests.setter
    def local_security_options_allow_pku2_u_authentication_requests(self, val):
        self._prop_dict["localSecurityOptionsAllowPKU2UAuthenticationRequests"] = val

    @property
    def local_security_options_allow_remote_calls_to_security_accounts_manager_helper_bool(self):
        """
        Gets and sets the localSecurityOptionsAllowRemoteCallsToSecurityAccountsManagerHelperBool
        
        Returns:
            bool:
                The localSecurityOptionsAllowRemoteCallsToSecurityAccountsManagerHelperBool
        """
        if "localSecurityOptionsAllowRemoteCallsToSecurityAccountsManagerHelperBool" in self._prop_dict:
            return self._prop_dict["localSecurityOptionsAllowRemoteCallsToSecurityAccountsManagerHelperBool"]
        else:
            return None

    @local_security_options_allow_remote_calls_to_security_accounts_manager_helper_bool.setter
    def local_security_options_allow_remote_calls_to_security_accounts_manager_helper_bool(self, val):
        self._prop_dict["localSecurityOptionsAllowRemoteCallsToSecurityAccountsManagerHelperBool"] = val

    @property
    def local_security_options_allow_remote_calls_to_security_accounts_manager(self):
        """
        Gets and sets the localSecurityOptionsAllowRemoteCallsToSecurityAccountsManager
        
        Returns:
            str:
                The localSecurityOptionsAllowRemoteCallsToSecurityAccountsManager
        """
        if "localSecurityOptionsAllowRemoteCallsToSecurityAccountsManager" in self._prop_dict:
            return self._prop_dict["localSecurityOptionsAllowRemoteCallsToSecurityAccountsManager"]
        else:
            return None

    @local_security_options_allow_remote_calls_to_security_accounts_manager.setter
    def local_security_options_allow_remote_calls_to_security_accounts_manager(self, val):
        self._prop_dict["localSecurityOptionsAllowRemoteCallsToSecurityAccountsManager"] = val

    @property
    def local_security_options_clear_virtual_memory_page_file(self):
        """
        Gets and sets the localSecurityOptionsClearVirtualMemoryPageFile
        
        Returns:
            bool:
                The localSecurityOptionsClearVirtualMemoryPageFile
        """
        if "localSecurityOptionsClearVirtualMemoryPageFile" in self._prop_dict:
            return self._prop_dict["localSecurityOptionsClearVirtualMemoryPageFile"]
        else:
            return None

    @local_security_options_clear_virtual_memory_page_file.setter
    def local_security_options_clear_virtual_memory_page_file(self, val):
        self._prop_dict["localSecurityOptionsClearVirtualMemoryPageFile"] = val

    @property
    def local_security_options_allow_system_to_be_shut_down_without_having_to_log_on(self):
        """
        Gets and sets the localSecurityOptionsAllowSystemToBeShutDownWithoutHavingToLogOn
        
        Returns:
            bool:
                The localSecurityOptionsAllowSystemToBeShutDownWithoutHavingToLogOn
        """
        if "localSecurityOptionsAllowSystemToBeShutDownWithoutHavingToLogOn" in self._prop_dict:
            return self._prop_dict["localSecurityOptionsAllowSystemToBeShutDownWithoutHavingToLogOn"]
        else:
            return None

    @local_security_options_allow_system_to_be_shut_down_without_having_to_log_on.setter
    def local_security_options_allow_system_to_be_shut_down_without_having_to_log_on(self, val):
        self._prop_dict["localSecurityOptionsAllowSystemToBeShutDownWithoutHavingToLogOn"] = val

    @property
    def local_security_options_allow_ui_access_application_elevation(self):
        """
        Gets and sets the localSecurityOptionsAllowUIAccessApplicationElevation
        
        Returns:
            bool:
                The localSecurityOptionsAllowUIAccessApplicationElevation
        """
        if "localSecurityOptionsAllowUIAccessApplicationElevation" in self._prop_dict:
            return self._prop_dict["localSecurityOptionsAllowUIAccessApplicationElevation"]
        else:
            return None

    @local_security_options_allow_ui_access_application_elevation.setter
    def local_security_options_allow_ui_access_application_elevation(self, val):
        self._prop_dict["localSecurityOptionsAllowUIAccessApplicationElevation"] = val

    @property
    def local_security_options_virtualize_file_and_registry_write_failures_to_per_user_locations(self):
        """
        Gets and sets the localSecurityOptionsVirtualizeFileAndRegistryWriteFailuresToPerUserLocations
        
        Returns:
            bool:
                The localSecurityOptionsVirtualizeFileAndRegistryWriteFailuresToPerUserLocations
        """
        if "localSecurityOptionsVirtualizeFileAndRegistryWriteFailuresToPerUserLocations" in self._prop_dict:
            return self._prop_dict["localSecurityOptionsVirtualizeFileAndRegistryWriteFailuresToPerUserLocations"]
        else:
            return None

    @local_security_options_virtualize_file_and_registry_write_failures_to_per_user_locations.setter
    def local_security_options_virtualize_file_and_registry_write_failures_to_per_user_locations(self, val):
        self._prop_dict["localSecurityOptionsVirtualizeFileAndRegistryWriteFailuresToPerUserLocations"] = val

    @property
    def local_security_options_only_elevate_signed_executables(self):
        """
        Gets and sets the localSecurityOptionsOnlyElevateSignedExecutables
        
        Returns:
            bool:
                The localSecurityOptionsOnlyElevateSignedExecutables
        """
        if "localSecurityOptionsOnlyElevateSignedExecutables" in self._prop_dict:
            return self._prop_dict["localSecurityOptionsOnlyElevateSignedExecutables"]
        else:
            return None

    @local_security_options_only_elevate_signed_executables.setter
    def local_security_options_only_elevate_signed_executables(self, val):
        self._prop_dict["localSecurityOptionsOnlyElevateSignedExecutables"] = val

    @property
    def local_security_options_administrator_elevation_prompt_behavior(self):
        """
        Gets and sets the localSecurityOptionsAdministratorElevationPromptBehavior
        
        Returns: 
            :class:`LocalSecurityOptionsAdministratorElevationPromptBehaviorType<onedrivesdk.model.local_security_options_administrator_elevation_prompt_behavior_type.LocalSecurityOptionsAdministratorElevationPromptBehaviorType>`:
                The localSecurityOptionsAdministratorElevationPromptBehavior
        """
        if "localSecurityOptionsAdministratorElevationPromptBehavior" in self._prop_dict:
            if isinstance(self._prop_dict["localSecurityOptionsAdministratorElevationPromptBehavior"], OneDriveObjectBase):
                return self._prop_dict["localSecurityOptionsAdministratorElevationPromptBehavior"]
            else :
                self._prop_dict["localSecurityOptionsAdministratorElevationPromptBehavior"] = LocalSecurityOptionsAdministratorElevationPromptBehaviorType(self._prop_dict["localSecurityOptionsAdministratorElevationPromptBehavior"])
                return self._prop_dict["localSecurityOptionsAdministratorElevationPromptBehavior"]

        return None

    @local_security_options_administrator_elevation_prompt_behavior.setter
    def local_security_options_administrator_elevation_prompt_behavior(self, val):
        self._prop_dict["localSecurityOptionsAdministratorElevationPromptBehavior"] = val

    @property
    def local_security_options_standard_user_elevation_prompt_behavior(self):
        """
        Gets and sets the localSecurityOptionsStandardUserElevationPromptBehavior
        
        Returns: 
            :class:`LocalSecurityOptionsStandardUserElevationPromptBehaviorType<onedrivesdk.model.local_security_options_standard_user_elevation_prompt_behavior_type.LocalSecurityOptionsStandardUserElevationPromptBehaviorType>`:
                The localSecurityOptionsStandardUserElevationPromptBehavior
        """
        if "localSecurityOptionsStandardUserElevationPromptBehavior" in self._prop_dict:
            if isinstance(self._prop_dict["localSecurityOptionsStandardUserElevationPromptBehavior"], OneDriveObjectBase):
                return self._prop_dict["localSecurityOptionsStandardUserElevationPromptBehavior"]
            else :
                self._prop_dict["localSecurityOptionsStandardUserElevationPromptBehavior"] = LocalSecurityOptionsStandardUserElevationPromptBehaviorType(self._prop_dict["localSecurityOptionsStandardUserElevationPromptBehavior"])
                return self._prop_dict["localSecurityOptionsStandardUserElevationPromptBehavior"]

        return None

    @local_security_options_standard_user_elevation_prompt_behavior.setter
    def local_security_options_standard_user_elevation_prompt_behavior(self, val):
        self._prop_dict["localSecurityOptionsStandardUserElevationPromptBehavior"] = val

    @property
    def local_security_options_switch_to_secure_desktop_when_prompting_for_elevation(self):
        """
        Gets and sets the localSecurityOptionsSwitchToSecureDesktopWhenPromptingForElevation
        
        Returns:
            bool:
                The localSecurityOptionsSwitchToSecureDesktopWhenPromptingForElevation
        """
        if "localSecurityOptionsSwitchToSecureDesktopWhenPromptingForElevation" in self._prop_dict:
            return self._prop_dict["localSecurityOptionsSwitchToSecureDesktopWhenPromptingForElevation"]
        else:
            return None

    @local_security_options_switch_to_secure_desktop_when_prompting_for_elevation.setter
    def local_security_options_switch_to_secure_desktop_when_prompting_for_elevation(self, val):
        self._prop_dict["localSecurityOptionsSwitchToSecureDesktopWhenPromptingForElevation"] = val

    @property
    def local_security_options_detect_application_installations_and_prompt_for_elevation(self):
        """
        Gets and sets the localSecurityOptionsDetectApplicationInstallationsAndPromptForElevation
        
        Returns:
            bool:
                The localSecurityOptionsDetectApplicationInstallationsAndPromptForElevation
        """
        if "localSecurityOptionsDetectApplicationInstallationsAndPromptForElevation" in self._prop_dict:
            return self._prop_dict["localSecurityOptionsDetectApplicationInstallationsAndPromptForElevation"]
        else:
            return None

    @local_security_options_detect_application_installations_and_prompt_for_elevation.setter
    def local_security_options_detect_application_installations_and_prompt_for_elevation(self, val):
        self._prop_dict["localSecurityOptionsDetectApplicationInstallationsAndPromptForElevation"] = val

    @property
    def local_security_options_allow_ui_access_applications_for_secure_locations(self):
        """
        Gets and sets the localSecurityOptionsAllowUIAccessApplicationsForSecureLocations
        
        Returns:
            bool:
                The localSecurityOptionsAllowUIAccessApplicationsForSecureLocations
        """
        if "localSecurityOptionsAllowUIAccessApplicationsForSecureLocations" in self._prop_dict:
            return self._prop_dict["localSecurityOptionsAllowUIAccessApplicationsForSecureLocations"]
        else:
            return None

    @local_security_options_allow_ui_access_applications_for_secure_locations.setter
    def local_security_options_allow_ui_access_applications_for_secure_locations(self, val):
        self._prop_dict["localSecurityOptionsAllowUIAccessApplicationsForSecureLocations"] = val

    @property
    def local_security_options_use_admin_approval_mode(self):
        """
        Gets and sets the localSecurityOptionsUseAdminApprovalMode
        
        Returns:
            bool:
                The localSecurityOptionsUseAdminApprovalMode
        """
        if "localSecurityOptionsUseAdminApprovalMode" in self._prop_dict:
            return self._prop_dict["localSecurityOptionsUseAdminApprovalMode"]
        else:
            return None

    @local_security_options_use_admin_approval_mode.setter
    def local_security_options_use_admin_approval_mode(self, val):
        self._prop_dict["localSecurityOptionsUseAdminApprovalMode"] = val

    @property
    def local_security_options_use_admin_approval_mode_for_administrators(self):
        """
        Gets and sets the localSecurityOptionsUseAdminApprovalModeForAdministrators
        
        Returns:
            bool:
                The localSecurityOptionsUseAdminApprovalModeForAdministrators
        """
        if "localSecurityOptionsUseAdminApprovalModeForAdministrators" in self._prop_dict:
            return self._prop_dict["localSecurityOptionsUseAdminApprovalModeForAdministrators"]
        else:
            return None

    @local_security_options_use_admin_approval_mode_for_administrators.setter
    def local_security_options_use_admin_approval_mode_for_administrators(self, val):
        self._prop_dict["localSecurityOptionsUseAdminApprovalModeForAdministrators"] = val

    @property
    def local_security_options_information_shown_on_lock_screen(self):
        """
        Gets and sets the localSecurityOptionsInformationShownOnLockScreen
        
        Returns: 
            :class:`LocalSecurityOptionsInformationShownOnLockScreenType<onedrivesdk.model.local_security_options_information_shown_on_lock_screen_type.LocalSecurityOptionsInformationShownOnLockScreenType>`:
                The localSecurityOptionsInformationShownOnLockScreen
        """
        if "localSecurityOptionsInformationShownOnLockScreen" in self._prop_dict:
            if isinstance(self._prop_dict["localSecurityOptionsInformationShownOnLockScreen"], OneDriveObjectBase):
                return self._prop_dict["localSecurityOptionsInformationShownOnLockScreen"]
            else :
                self._prop_dict["localSecurityOptionsInformationShownOnLockScreen"] = LocalSecurityOptionsInformationShownOnLockScreenType(self._prop_dict["localSecurityOptionsInformationShownOnLockScreen"])
                return self._prop_dict["localSecurityOptionsInformationShownOnLockScreen"]

        return None

    @local_security_options_information_shown_on_lock_screen.setter
    def local_security_options_information_shown_on_lock_screen(self, val):
        self._prop_dict["localSecurityOptionsInformationShownOnLockScreen"] = val

    @property
    def local_security_options_information_displayed_on_lock_screen(self):
        """
        Gets and sets the localSecurityOptionsInformationDisplayedOnLockScreen
        
        Returns: 
            :class:`LocalSecurityOptionsInformationDisplayedOnLockScreenType<onedrivesdk.model.local_security_options_information_displayed_on_lock_screen_type.LocalSecurityOptionsInformationDisplayedOnLockScreenType>`:
                The localSecurityOptionsInformationDisplayedOnLockScreen
        """
        if "localSecurityOptionsInformationDisplayedOnLockScreen" in self._prop_dict:
            if isinstance(self._prop_dict["localSecurityOptionsInformationDisplayedOnLockScreen"], OneDriveObjectBase):
                return self._prop_dict["localSecurityOptionsInformationDisplayedOnLockScreen"]
            else :
                self._prop_dict["localSecurityOptionsInformationDisplayedOnLockScreen"] = LocalSecurityOptionsInformationDisplayedOnLockScreenType(self._prop_dict["localSecurityOptionsInformationDisplayedOnLockScreen"])
                return self._prop_dict["localSecurityOptionsInformationDisplayedOnLockScreen"]

        return None

    @local_security_options_information_displayed_on_lock_screen.setter
    def local_security_options_information_displayed_on_lock_screen(self, val):
        self._prop_dict["localSecurityOptionsInformationDisplayedOnLockScreen"] = val

    @property
    def local_security_options_disable_client_digitally_sign_communications_if_server_agrees(self):
        """
        Gets and sets the localSecurityOptionsDisableClientDigitallySignCommunicationsIfServerAgrees
        
        Returns:
            bool:
                The localSecurityOptionsDisableClientDigitallySignCommunicationsIfServerAgrees
        """
        if "localSecurityOptionsDisableClientDigitallySignCommunicationsIfServerAgrees" in self._prop_dict:
            return self._prop_dict["localSecurityOptionsDisableClientDigitallySignCommunicationsIfServerAgrees"]
        else:
            return None

    @local_security_options_disable_client_digitally_sign_communications_if_server_agrees.setter
    def local_security_options_disable_client_digitally_sign_communications_if_server_agrees(self, val):
        self._prop_dict["localSecurityOptionsDisableClientDigitallySignCommunicationsIfServerAgrees"] = val

    @property
    def local_security_options_client_send_unencrypted_password_to_third_party_smb_servers(self):
        """
        Gets and sets the localSecurityOptionsClientSendUnencryptedPasswordToThirdPartySMBServers
        
        Returns:
            bool:
                The localSecurityOptionsClientSendUnencryptedPasswordToThirdPartySMBServers
        """
        if "localSecurityOptionsClientSendUnencryptedPasswordToThirdPartySMBServers" in self._prop_dict:
            return self._prop_dict["localSecurityOptionsClientSendUnencryptedPasswordToThirdPartySMBServers"]
        else:
            return None

    @local_security_options_client_send_unencrypted_password_to_third_party_smb_servers.setter
    def local_security_options_client_send_unencrypted_password_to_third_party_smb_servers(self, val):
        self._prop_dict["localSecurityOptionsClientSendUnencryptedPasswordToThirdPartySMBServers"] = val

    @property
    def local_security_options_disable_server_digitally_sign_communications_always(self):
        """
        Gets and sets the localSecurityOptionsDisableServerDigitallySignCommunicationsAlways
        
        Returns:
            bool:
                The localSecurityOptionsDisableServerDigitallySignCommunicationsAlways
        """
        if "localSecurityOptionsDisableServerDigitallySignCommunicationsAlways" in self._prop_dict:
            return self._prop_dict["localSecurityOptionsDisableServerDigitallySignCommunicationsAlways"]
        else:
            return None

    @local_security_options_disable_server_digitally_sign_communications_always.setter
    def local_security_options_disable_server_digitally_sign_communications_always(self, val):
        self._prop_dict["localSecurityOptionsDisableServerDigitallySignCommunicationsAlways"] = val

    @property
    def local_security_options_disable_server_digitally_sign_communications_if_client_agrees(self):
        """
        Gets and sets the localSecurityOptionsDisableServerDigitallySignCommunicationsIfClientAgrees
        
        Returns:
            bool:
                The localSecurityOptionsDisableServerDigitallySignCommunicationsIfClientAgrees
        """
        if "localSecurityOptionsDisableServerDigitallySignCommunicationsIfClientAgrees" in self._prop_dict:
            return self._prop_dict["localSecurityOptionsDisableServerDigitallySignCommunicationsIfClientAgrees"]
        else:
            return None

    @local_security_options_disable_server_digitally_sign_communications_if_client_agrees.setter
    def local_security_options_disable_server_digitally_sign_communications_if_client_agrees(self, val):
        self._prop_dict["localSecurityOptionsDisableServerDigitallySignCommunicationsIfClientAgrees"] = val

    @property
    def local_security_options_restrict_anonymous_access_to_named_pipes_and_shares(self):
        """
        Gets and sets the localSecurityOptionsRestrictAnonymousAccessToNamedPipesAndShares
        
        Returns:
            bool:
                The localSecurityOptionsRestrictAnonymousAccessToNamedPipesAndShares
        """
        if "localSecurityOptionsRestrictAnonymousAccessToNamedPipesAndShares" in self._prop_dict:
            return self._prop_dict["localSecurityOptionsRestrictAnonymousAccessToNamedPipesAndShares"]
        else:
            return None

    @local_security_options_restrict_anonymous_access_to_named_pipes_and_shares.setter
    def local_security_options_restrict_anonymous_access_to_named_pipes_and_shares(self, val):
        self._prop_dict["localSecurityOptionsRestrictAnonymousAccessToNamedPipesAndShares"] = val

    @property
    def local_security_options_do_not_allow_anonymous_enumeration_of_sam_accounts(self):
        """
        Gets and sets the localSecurityOptionsDoNotAllowAnonymousEnumerationOfSAMAccounts
        
        Returns:
            bool:
                The localSecurityOptionsDoNotAllowAnonymousEnumerationOfSAMAccounts
        """
        if "localSecurityOptionsDoNotAllowAnonymousEnumerationOfSAMAccounts" in self._prop_dict:
            return self._prop_dict["localSecurityOptionsDoNotAllowAnonymousEnumerationOfSAMAccounts"]
        else:
            return None

    @local_security_options_do_not_allow_anonymous_enumeration_of_sam_accounts.setter
    def local_security_options_do_not_allow_anonymous_enumeration_of_sam_accounts(self, val):
        self._prop_dict["localSecurityOptionsDoNotAllowAnonymousEnumerationOfSAMAccounts"] = val

    @property
    def local_security_options_allow_anonymous_enumeration_of_sam_accounts_and_shares(self):
        """
        Gets and sets the localSecurityOptionsAllowAnonymousEnumerationOfSAMAccountsAndShares
        
        Returns:
            bool:
                The localSecurityOptionsAllowAnonymousEnumerationOfSAMAccountsAndShares
        """
        if "localSecurityOptionsAllowAnonymousEnumerationOfSAMAccountsAndShares" in self._prop_dict:
            return self._prop_dict["localSecurityOptionsAllowAnonymousEnumerationOfSAMAccountsAndShares"]
        else:
            return None

    @local_security_options_allow_anonymous_enumeration_of_sam_accounts_and_shares.setter
    def local_security_options_allow_anonymous_enumeration_of_sam_accounts_and_shares(self, val):
        self._prop_dict["localSecurityOptionsAllowAnonymousEnumerationOfSAMAccountsAndShares"] = val

    @property
    def local_security_options_do_not_store_lan_manager_hash_value_on_next_password_change(self):
        """
        Gets and sets the localSecurityOptionsDoNotStoreLANManagerHashValueOnNextPasswordChange
        
        Returns:
            bool:
                The localSecurityOptionsDoNotStoreLANManagerHashValueOnNextPasswordChange
        """
        if "localSecurityOptionsDoNotStoreLANManagerHashValueOnNextPasswordChange" in self._prop_dict:
            return self._prop_dict["localSecurityOptionsDoNotStoreLANManagerHashValueOnNextPasswordChange"]
        else:
            return None

    @local_security_options_do_not_store_lan_manager_hash_value_on_next_password_change.setter
    def local_security_options_do_not_store_lan_manager_hash_value_on_next_password_change(self, val):
        self._prop_dict["localSecurityOptionsDoNotStoreLANManagerHashValueOnNextPasswordChange"] = val

    @property
    def local_security_options_smart_card_removal_behavior(self):
        """
        Gets and sets the localSecurityOptionsSmartCardRemovalBehavior
        
        Returns: 
            :class:`LocalSecurityOptionsSmartCardRemovalBehaviorType<onedrivesdk.model.local_security_options_smart_card_removal_behavior_type.LocalSecurityOptionsSmartCardRemovalBehaviorType>`:
                The localSecurityOptionsSmartCardRemovalBehavior
        """
        if "localSecurityOptionsSmartCardRemovalBehavior" in self._prop_dict:
            if isinstance(self._prop_dict["localSecurityOptionsSmartCardRemovalBehavior"], OneDriveObjectBase):
                return self._prop_dict["localSecurityOptionsSmartCardRemovalBehavior"]
            else :
                self._prop_dict["localSecurityOptionsSmartCardRemovalBehavior"] = LocalSecurityOptionsSmartCardRemovalBehaviorType(self._prop_dict["localSecurityOptionsSmartCardRemovalBehavior"])
                return self._prop_dict["localSecurityOptionsSmartCardRemovalBehavior"]

        return None

    @local_security_options_smart_card_removal_behavior.setter
    def local_security_options_smart_card_removal_behavior(self, val):
        self._prop_dict["localSecurityOptionsSmartCardRemovalBehavior"] = val

    @property
    def defender_security_center_disable_app_browser_ui(self):
        """
        Gets and sets the defenderSecurityCenterDisableAppBrowserUI
        
        Returns:
            bool:
                The defenderSecurityCenterDisableAppBrowserUI
        """
        if "defenderSecurityCenterDisableAppBrowserUI" in self._prop_dict:
            return self._prop_dict["defenderSecurityCenterDisableAppBrowserUI"]
        else:
            return None

    @defender_security_center_disable_app_browser_ui.setter
    def defender_security_center_disable_app_browser_ui(self, val):
        self._prop_dict["defenderSecurityCenterDisableAppBrowserUI"] = val

    @property
    def defender_security_center_disable_family_ui(self):
        """
        Gets and sets the defenderSecurityCenterDisableFamilyUI
        
        Returns:
            bool:
                The defenderSecurityCenterDisableFamilyUI
        """
        if "defenderSecurityCenterDisableFamilyUI" in self._prop_dict:
            return self._prop_dict["defenderSecurityCenterDisableFamilyUI"]
        else:
            return None

    @defender_security_center_disable_family_ui.setter
    def defender_security_center_disable_family_ui(self, val):
        self._prop_dict["defenderSecurityCenterDisableFamilyUI"] = val

    @property
    def defender_security_center_disable_health_ui(self):
        """
        Gets and sets the defenderSecurityCenterDisableHealthUI
        
        Returns:
            bool:
                The defenderSecurityCenterDisableHealthUI
        """
        if "defenderSecurityCenterDisableHealthUI" in self._prop_dict:
            return self._prop_dict["defenderSecurityCenterDisableHealthUI"]
        else:
            return None

    @defender_security_center_disable_health_ui.setter
    def defender_security_center_disable_health_ui(self, val):
        self._prop_dict["defenderSecurityCenterDisableHealthUI"] = val

    @property
    def defender_security_center_disable_network_ui(self):
        """
        Gets and sets the defenderSecurityCenterDisableNetworkUI
        
        Returns:
            bool:
                The defenderSecurityCenterDisableNetworkUI
        """
        if "defenderSecurityCenterDisableNetworkUI" in self._prop_dict:
            return self._prop_dict["defenderSecurityCenterDisableNetworkUI"]
        else:
            return None

    @defender_security_center_disable_network_ui.setter
    def defender_security_center_disable_network_ui(self, val):
        self._prop_dict["defenderSecurityCenterDisableNetworkUI"] = val

    @property
    def defender_security_center_disable_virus_ui(self):
        """
        Gets and sets the defenderSecurityCenterDisableVirusUI
        
        Returns:
            bool:
                The defenderSecurityCenterDisableVirusUI
        """
        if "defenderSecurityCenterDisableVirusUI" in self._prop_dict:
            return self._prop_dict["defenderSecurityCenterDisableVirusUI"]
        else:
            return None

    @defender_security_center_disable_virus_ui.setter
    def defender_security_center_disable_virus_ui(self, val):
        self._prop_dict["defenderSecurityCenterDisableVirusUI"] = val

    @property
    def defender_security_center_disable_account_ui(self):
        """
        Gets and sets the defenderSecurityCenterDisableAccountUI
        
        Returns:
            bool:
                The defenderSecurityCenterDisableAccountUI
        """
        if "defenderSecurityCenterDisableAccountUI" in self._prop_dict:
            return self._prop_dict["defenderSecurityCenterDisableAccountUI"]
        else:
            return None

    @defender_security_center_disable_account_ui.setter
    def defender_security_center_disable_account_ui(self, val):
        self._prop_dict["defenderSecurityCenterDisableAccountUI"] = val

    @property
    def defender_security_center_disable_hardware_ui(self):
        """
        Gets and sets the defenderSecurityCenterDisableHardwareUI
        
        Returns:
            bool:
                The defenderSecurityCenterDisableHardwareUI
        """
        if "defenderSecurityCenterDisableHardwareUI" in self._prop_dict:
            return self._prop_dict["defenderSecurityCenterDisableHardwareUI"]
        else:
            return None

    @defender_security_center_disable_hardware_ui.setter
    def defender_security_center_disable_hardware_ui(self, val):
        self._prop_dict["defenderSecurityCenterDisableHardwareUI"] = val

    @property
    def defender_security_center_disable_ransomware_ui(self):
        """
        Gets and sets the defenderSecurityCenterDisableRansomwareUI
        
        Returns:
            bool:
                The defenderSecurityCenterDisableRansomwareUI
        """
        if "defenderSecurityCenterDisableRansomwareUI" in self._prop_dict:
            return self._prop_dict["defenderSecurityCenterDisableRansomwareUI"]
        else:
            return None

    @defender_security_center_disable_ransomware_ui.setter
    def defender_security_center_disable_ransomware_ui(self, val):
        self._prop_dict["defenderSecurityCenterDisableRansomwareUI"] = val

    @property
    def defender_security_center_disable_secure_boot_ui(self):
        """
        Gets and sets the defenderSecurityCenterDisableSecureBootUI
        
        Returns:
            bool:
                The defenderSecurityCenterDisableSecureBootUI
        """
        if "defenderSecurityCenterDisableSecureBootUI" in self._prop_dict:
            return self._prop_dict["defenderSecurityCenterDisableSecureBootUI"]
        else:
            return None

    @defender_security_center_disable_secure_boot_ui.setter
    def defender_security_center_disable_secure_boot_ui(self, val):
        self._prop_dict["defenderSecurityCenterDisableSecureBootUI"] = val

    @property
    def defender_security_center_disable_troubleshooting_ui(self):
        """
        Gets and sets the defenderSecurityCenterDisableTroubleshootingUI
        
        Returns:
            bool:
                The defenderSecurityCenterDisableTroubleshootingUI
        """
        if "defenderSecurityCenterDisableTroubleshootingUI" in self._prop_dict:
            return self._prop_dict["defenderSecurityCenterDisableTroubleshootingUI"]
        else:
            return None

    @defender_security_center_disable_troubleshooting_ui.setter
    def defender_security_center_disable_troubleshooting_ui(self, val):
        self._prop_dict["defenderSecurityCenterDisableTroubleshootingUI"] = val

    @property
    def defender_security_center_organization_display_name(self):
        """
        Gets and sets the defenderSecurityCenterOrganizationDisplayName
        
        Returns:
            str:
                The defenderSecurityCenterOrganizationDisplayName
        """
        if "defenderSecurityCenterOrganizationDisplayName" in self._prop_dict:
            return self._prop_dict["defenderSecurityCenterOrganizationDisplayName"]
        else:
            return None

    @defender_security_center_organization_display_name.setter
    def defender_security_center_organization_display_name(self, val):
        self._prop_dict["defenderSecurityCenterOrganizationDisplayName"] = val

    @property
    def defender_security_center_help_email(self):
        """
        Gets and sets the defenderSecurityCenterHelpEmail
        
        Returns:
            str:
                The defenderSecurityCenterHelpEmail
        """
        if "defenderSecurityCenterHelpEmail" in self._prop_dict:
            return self._prop_dict["defenderSecurityCenterHelpEmail"]
        else:
            return None

    @defender_security_center_help_email.setter
    def defender_security_center_help_email(self, val):
        self._prop_dict["defenderSecurityCenterHelpEmail"] = val

    @property
    def defender_security_center_help_phone(self):
        """
        Gets and sets the defenderSecurityCenterHelpPhone
        
        Returns:
            str:
                The defenderSecurityCenterHelpPhone
        """
        if "defenderSecurityCenterHelpPhone" in self._prop_dict:
            return self._prop_dict["defenderSecurityCenterHelpPhone"]
        else:
            return None

    @defender_security_center_help_phone.setter
    def defender_security_center_help_phone(self, val):
        self._prop_dict["defenderSecurityCenterHelpPhone"] = val

    @property
    def defender_security_center_help_url(self):
        """
        Gets and sets the defenderSecurityCenterHelpURL
        
        Returns:
            str:
                The defenderSecurityCenterHelpURL
        """
        if "defenderSecurityCenterHelpURL" in self._prop_dict:
            return self._prop_dict["defenderSecurityCenterHelpURL"]
        else:
            return None

    @defender_security_center_help_url.setter
    def defender_security_center_help_url(self, val):
        self._prop_dict["defenderSecurityCenterHelpURL"] = val

    @property
    def defender_security_center_notifications_from_app(self):
        """
        Gets and sets the defenderSecurityCenterNotificationsFromApp
        
        Returns: 
            :class:`DefenderSecurityCenterNotificationsFromAppType<onedrivesdk.model.defender_security_center_notifications_from_app_type.DefenderSecurityCenterNotificationsFromAppType>`:
                The defenderSecurityCenterNotificationsFromApp
        """
        if "defenderSecurityCenterNotificationsFromApp" in self._prop_dict:
            if isinstance(self._prop_dict["defenderSecurityCenterNotificationsFromApp"], OneDriveObjectBase):
                return self._prop_dict["defenderSecurityCenterNotificationsFromApp"]
            else :
                self._prop_dict["defenderSecurityCenterNotificationsFromApp"] = DefenderSecurityCenterNotificationsFromAppType(self._prop_dict["defenderSecurityCenterNotificationsFromApp"])
                return self._prop_dict["defenderSecurityCenterNotificationsFromApp"]

        return None

    @defender_security_center_notifications_from_app.setter
    def defender_security_center_notifications_from_app(self, val):
        self._prop_dict["defenderSecurityCenterNotificationsFromApp"] = val

    @property
    def defender_security_center_it_contact_display(self):
        """
        Gets and sets the defenderSecurityCenterITContactDisplay
        
        Returns: 
            :class:`DefenderSecurityCenterITContactDisplayType<onedrivesdk.model.defender_security_center_it_contact_display_type.DefenderSecurityCenterITContactDisplayType>`:
                The defenderSecurityCenterITContactDisplay
        """
        if "defenderSecurityCenterITContactDisplay" in self._prop_dict:
            if isinstance(self._prop_dict["defenderSecurityCenterITContactDisplay"], OneDriveObjectBase):
                return self._prop_dict["defenderSecurityCenterITContactDisplay"]
            else :
                self._prop_dict["defenderSecurityCenterITContactDisplay"] = DefenderSecurityCenterITContactDisplayType(self._prop_dict["defenderSecurityCenterITContactDisplay"])
                return self._prop_dict["defenderSecurityCenterITContactDisplay"]

        return None

    @defender_security_center_it_contact_display.setter
    def defender_security_center_it_contact_display(self, val):
        self._prop_dict["defenderSecurityCenterITContactDisplay"] = val

    @property
    def firewall_block_stateful_ftp(self):
        """
        Gets and sets the firewallBlockStatefulFTP
        
        Returns:
            bool:
                The firewallBlockStatefulFTP
        """
        if "firewallBlockStatefulFTP" in self._prop_dict:
            return self._prop_dict["firewallBlockStatefulFTP"]
        else:
            return None

    @firewall_block_stateful_ftp.setter
    def firewall_block_stateful_ftp(self, val):
        self._prop_dict["firewallBlockStatefulFTP"] = val

    @property
    def firewall_idle_timeout_for_security_association_in_seconds(self):
        """
        Gets and sets the firewallIdleTimeoutForSecurityAssociationInSeconds
        
        Returns:
            int:
                The firewallIdleTimeoutForSecurityAssociationInSeconds
        """
        if "firewallIdleTimeoutForSecurityAssociationInSeconds" in self._prop_dict:
            return self._prop_dict["firewallIdleTimeoutForSecurityAssociationInSeconds"]
        else:
            return None

    @firewall_idle_timeout_for_security_association_in_seconds.setter
    def firewall_idle_timeout_for_security_association_in_seconds(self, val):
        self._prop_dict["firewallIdleTimeoutForSecurityAssociationInSeconds"] = val

    @property
    def firewall_pre_shared_key_encoding_method(self):
        """
        Gets and sets the firewallPreSharedKeyEncodingMethod
        
        Returns: 
            :class:`FirewallPreSharedKeyEncodingMethodType<onedrivesdk.model.firewall_pre_shared_key_encoding_method_type.FirewallPreSharedKeyEncodingMethodType>`:
                The firewallPreSharedKeyEncodingMethod
        """
        if "firewallPreSharedKeyEncodingMethod" in self._prop_dict:
            if isinstance(self._prop_dict["firewallPreSharedKeyEncodingMethod"], OneDriveObjectBase):
                return self._prop_dict["firewallPreSharedKeyEncodingMethod"]
            else :
                self._prop_dict["firewallPreSharedKeyEncodingMethod"] = FirewallPreSharedKeyEncodingMethodType(self._prop_dict["firewallPreSharedKeyEncodingMethod"])
                return self._prop_dict["firewallPreSharedKeyEncodingMethod"]

        return None

    @firewall_pre_shared_key_encoding_method.setter
    def firewall_pre_shared_key_encoding_method(self, val):
        self._prop_dict["firewallPreSharedKeyEncodingMethod"] = val

    @property
    def firewall_ip_sec_exemptions_allow_neighbor_discovery(self):
        """
        Gets and sets the firewallIPSecExemptionsAllowNeighborDiscovery
        
        Returns:
            bool:
                The firewallIPSecExemptionsAllowNeighborDiscovery
        """
        if "firewallIPSecExemptionsAllowNeighborDiscovery" in self._prop_dict:
            return self._prop_dict["firewallIPSecExemptionsAllowNeighborDiscovery"]
        else:
            return None

    @firewall_ip_sec_exemptions_allow_neighbor_discovery.setter
    def firewall_ip_sec_exemptions_allow_neighbor_discovery(self, val):
        self._prop_dict["firewallIPSecExemptionsAllowNeighborDiscovery"] = val

    @property
    def firewall_ip_sec_exemptions_allow_icmp(self):
        """
        Gets and sets the firewallIPSecExemptionsAllowICMP
        
        Returns:
            bool:
                The firewallIPSecExemptionsAllowICMP
        """
        if "firewallIPSecExemptionsAllowICMP" in self._prop_dict:
            return self._prop_dict["firewallIPSecExemptionsAllowICMP"]
        else:
            return None

    @firewall_ip_sec_exemptions_allow_icmp.setter
    def firewall_ip_sec_exemptions_allow_icmp(self, val):
        self._prop_dict["firewallIPSecExemptionsAllowICMP"] = val

    @property
    def firewall_ip_sec_exemptions_allow_router_discovery(self):
        """
        Gets and sets the firewallIPSecExemptionsAllowRouterDiscovery
        
        Returns:
            bool:
                The firewallIPSecExemptionsAllowRouterDiscovery
        """
        if "firewallIPSecExemptionsAllowRouterDiscovery" in self._prop_dict:
            return self._prop_dict["firewallIPSecExemptionsAllowRouterDiscovery"]
        else:
            return None

    @firewall_ip_sec_exemptions_allow_router_discovery.setter
    def firewall_ip_sec_exemptions_allow_router_discovery(self, val):
        self._prop_dict["firewallIPSecExemptionsAllowRouterDiscovery"] = val

    @property
    def firewall_ip_sec_exemptions_allow_dhcp(self):
        """
        Gets and sets the firewallIPSecExemptionsAllowDHCP
        
        Returns:
            bool:
                The firewallIPSecExemptionsAllowDHCP
        """
        if "firewallIPSecExemptionsAllowDHCP" in self._prop_dict:
            return self._prop_dict["firewallIPSecExemptionsAllowDHCP"]
        else:
            return None

    @firewall_ip_sec_exemptions_allow_dhcp.setter
    def firewall_ip_sec_exemptions_allow_dhcp(self, val):
        self._prop_dict["firewallIPSecExemptionsAllowDHCP"] = val

    @property
    def firewall_certificate_revocation_list_check_method(self):
        """
        Gets and sets the firewallCertificateRevocationListCheckMethod
        
        Returns: 
            :class:`FirewallCertificateRevocationListCheckMethodType<onedrivesdk.model.firewall_certificate_revocation_list_check_method_type.FirewallCertificateRevocationListCheckMethodType>`:
                The firewallCertificateRevocationListCheckMethod
        """
        if "firewallCertificateRevocationListCheckMethod" in self._prop_dict:
            if isinstance(self._prop_dict["firewallCertificateRevocationListCheckMethod"], OneDriveObjectBase):
                return self._prop_dict["firewallCertificateRevocationListCheckMethod"]
            else :
                self._prop_dict["firewallCertificateRevocationListCheckMethod"] = FirewallCertificateRevocationListCheckMethodType(self._prop_dict["firewallCertificateRevocationListCheckMethod"])
                return self._prop_dict["firewallCertificateRevocationListCheckMethod"]

        return None

    @firewall_certificate_revocation_list_check_method.setter
    def firewall_certificate_revocation_list_check_method(self, val):
        self._prop_dict["firewallCertificateRevocationListCheckMethod"] = val

    @property
    def firewall_merge_keying_module_settings(self):
        """
        Gets and sets the firewallMergeKeyingModuleSettings
        
        Returns:
            bool:
                The firewallMergeKeyingModuleSettings
        """
        if "firewallMergeKeyingModuleSettings" in self._prop_dict:
            return self._prop_dict["firewallMergeKeyingModuleSettings"]
        else:
            return None

    @firewall_merge_keying_module_settings.setter
    def firewall_merge_keying_module_settings(self, val):
        self._prop_dict["firewallMergeKeyingModuleSettings"] = val

    @property
    def firewall_packet_queueing_method(self):
        """
        Gets and sets the firewallPacketQueueingMethod
        
        Returns: 
            :class:`FirewallPacketQueueingMethodType<onedrivesdk.model.firewall_packet_queueing_method_type.FirewallPacketQueueingMethodType>`:
                The firewallPacketQueueingMethod
        """
        if "firewallPacketQueueingMethod" in self._prop_dict:
            if isinstance(self._prop_dict["firewallPacketQueueingMethod"], OneDriveObjectBase):
                return self._prop_dict["firewallPacketQueueingMethod"]
            else :
                self._prop_dict["firewallPacketQueueingMethod"] = FirewallPacketQueueingMethodType(self._prop_dict["firewallPacketQueueingMethod"])
                return self._prop_dict["firewallPacketQueueingMethod"]

        return None

    @firewall_packet_queueing_method.setter
    def firewall_packet_queueing_method(self, val):
        self._prop_dict["firewallPacketQueueingMethod"] = val

    @property
    def firewall_profile_domain(self):
        """
        Gets and sets the firewallProfileDomain
        
        Returns: 
            :class:`WindowsFirewallNetworkProfile<onedrivesdk.model.windows_firewall_network_profile.WindowsFirewallNetworkProfile>`:
                The firewallProfileDomain
        """
        if "firewallProfileDomain" in self._prop_dict:
            if isinstance(self._prop_dict["firewallProfileDomain"], OneDriveObjectBase):
                return self._prop_dict["firewallProfileDomain"]
            else :
                self._prop_dict["firewallProfileDomain"] = WindowsFirewallNetworkProfile(self._prop_dict["firewallProfileDomain"])
                return self._prop_dict["firewallProfileDomain"]

        return None

    @firewall_profile_domain.setter
    def firewall_profile_domain(self, val):
        self._prop_dict["firewallProfileDomain"] = val

    @property
    def firewall_profile_public(self):
        """
        Gets and sets the firewallProfilePublic
        
        Returns: 
            :class:`WindowsFirewallNetworkProfile<onedrivesdk.model.windows_firewall_network_profile.WindowsFirewallNetworkProfile>`:
                The firewallProfilePublic
        """
        if "firewallProfilePublic" in self._prop_dict:
            if isinstance(self._prop_dict["firewallProfilePublic"], OneDriveObjectBase):
                return self._prop_dict["firewallProfilePublic"]
            else :
                self._prop_dict["firewallProfilePublic"] = WindowsFirewallNetworkProfile(self._prop_dict["firewallProfilePublic"])
                return self._prop_dict["firewallProfilePublic"]

        return None

    @firewall_profile_public.setter
    def firewall_profile_public(self, val):
        self._prop_dict["firewallProfilePublic"] = val

    @property
    def firewall_profile_private(self):
        """
        Gets and sets the firewallProfilePrivate
        
        Returns: 
            :class:`WindowsFirewallNetworkProfile<onedrivesdk.model.windows_firewall_network_profile.WindowsFirewallNetworkProfile>`:
                The firewallProfilePrivate
        """
        if "firewallProfilePrivate" in self._prop_dict:
            if isinstance(self._prop_dict["firewallProfilePrivate"], OneDriveObjectBase):
                return self._prop_dict["firewallProfilePrivate"]
            else :
                self._prop_dict["firewallProfilePrivate"] = WindowsFirewallNetworkProfile(self._prop_dict["firewallProfilePrivate"])
                return self._prop_dict["firewallProfilePrivate"]

        return None

    @firewall_profile_private.setter
    def firewall_profile_private(self, val):
        self._prop_dict["firewallProfilePrivate"] = val

    @property
    def defender_attack_surface_reduction_excluded_paths(self):
        """
        Gets and sets the defenderAttackSurfaceReductionExcludedPaths
        
        Returns:
            str:
                The defenderAttackSurfaceReductionExcludedPaths
        """
        if "defenderAttackSurfaceReductionExcludedPaths" in self._prop_dict:
            return self._prop_dict["defenderAttackSurfaceReductionExcludedPaths"]
        else:
            return None

    @defender_attack_surface_reduction_excluded_paths.setter
    def defender_attack_surface_reduction_excluded_paths(self, val):
        self._prop_dict["defenderAttackSurfaceReductionExcludedPaths"] = val

    @property
    def defender_office_apps_other_process_injection_type(self):
        """
        Gets and sets the defenderOfficeAppsOtherProcessInjectionType
        
        Returns: 
            :class:`DefenderAttackSurfaceType<onedrivesdk.model.defender_attack_surface_type.DefenderAttackSurfaceType>`:
                The defenderOfficeAppsOtherProcessInjectionType
        """
        if "defenderOfficeAppsOtherProcessInjectionType" in self._prop_dict:
            if isinstance(self._prop_dict["defenderOfficeAppsOtherProcessInjectionType"], OneDriveObjectBase):
                return self._prop_dict["defenderOfficeAppsOtherProcessInjectionType"]
            else :
                self._prop_dict["defenderOfficeAppsOtherProcessInjectionType"] = DefenderAttackSurfaceType(self._prop_dict["defenderOfficeAppsOtherProcessInjectionType"])
                return self._prop_dict["defenderOfficeAppsOtherProcessInjectionType"]

        return None

    @defender_office_apps_other_process_injection_type.setter
    def defender_office_apps_other_process_injection_type(self, val):
        self._prop_dict["defenderOfficeAppsOtherProcessInjectionType"] = val

    @property
    def defender_office_apps_executable_content_creation_or_launch_type(self):
        """
        Gets and sets the defenderOfficeAppsExecutableContentCreationOrLaunchType
        
        Returns: 
            :class:`DefenderAttackSurfaceType<onedrivesdk.model.defender_attack_surface_type.DefenderAttackSurfaceType>`:
                The defenderOfficeAppsExecutableContentCreationOrLaunchType
        """
        if "defenderOfficeAppsExecutableContentCreationOrLaunchType" in self._prop_dict:
            if isinstance(self._prop_dict["defenderOfficeAppsExecutableContentCreationOrLaunchType"], OneDriveObjectBase):
                return self._prop_dict["defenderOfficeAppsExecutableContentCreationOrLaunchType"]
            else :
                self._prop_dict["defenderOfficeAppsExecutableContentCreationOrLaunchType"] = DefenderAttackSurfaceType(self._prop_dict["defenderOfficeAppsExecutableContentCreationOrLaunchType"])
                return self._prop_dict["defenderOfficeAppsExecutableContentCreationOrLaunchType"]

        return None

    @defender_office_apps_executable_content_creation_or_launch_type.setter
    def defender_office_apps_executable_content_creation_or_launch_type(self, val):
        self._prop_dict["defenderOfficeAppsExecutableContentCreationOrLaunchType"] = val

    @property
    def defender_office_apps_launch_child_process_type(self):
        """
        Gets and sets the defenderOfficeAppsLaunchChildProcessType
        
        Returns: 
            :class:`DefenderAttackSurfaceType<onedrivesdk.model.defender_attack_surface_type.DefenderAttackSurfaceType>`:
                The defenderOfficeAppsLaunchChildProcessType
        """
        if "defenderOfficeAppsLaunchChildProcessType" in self._prop_dict:
            if isinstance(self._prop_dict["defenderOfficeAppsLaunchChildProcessType"], OneDriveObjectBase):
                return self._prop_dict["defenderOfficeAppsLaunchChildProcessType"]
            else :
                self._prop_dict["defenderOfficeAppsLaunchChildProcessType"] = DefenderAttackSurfaceType(self._prop_dict["defenderOfficeAppsLaunchChildProcessType"])
                return self._prop_dict["defenderOfficeAppsLaunchChildProcessType"]

        return None

    @defender_office_apps_launch_child_process_type.setter
    def defender_office_apps_launch_child_process_type(self, val):
        self._prop_dict["defenderOfficeAppsLaunchChildProcessType"] = val

    @property
    def defender_office_macro_code_allow_win32_imports_type(self):
        """
        Gets and sets the defenderOfficeMacroCodeAllowWin32ImportsType
        
        Returns: 
            :class:`DefenderAttackSurfaceType<onedrivesdk.model.defender_attack_surface_type.DefenderAttackSurfaceType>`:
                The defenderOfficeMacroCodeAllowWin32ImportsType
        """
        if "defenderOfficeMacroCodeAllowWin32ImportsType" in self._prop_dict:
            if isinstance(self._prop_dict["defenderOfficeMacroCodeAllowWin32ImportsType"], OneDriveObjectBase):
                return self._prop_dict["defenderOfficeMacroCodeAllowWin32ImportsType"]
            else :
                self._prop_dict["defenderOfficeMacroCodeAllowWin32ImportsType"] = DefenderAttackSurfaceType(self._prop_dict["defenderOfficeMacroCodeAllowWin32ImportsType"])
                return self._prop_dict["defenderOfficeMacroCodeAllowWin32ImportsType"]

        return None

    @defender_office_macro_code_allow_win32_imports_type.setter
    def defender_office_macro_code_allow_win32_imports_type(self, val):
        self._prop_dict["defenderOfficeMacroCodeAllowWin32ImportsType"] = val

    @property
    def defender_script_obfuscated_macro_code_type(self):
        """
        Gets and sets the defenderScriptObfuscatedMacroCodeType
        
        Returns: 
            :class:`DefenderAttackSurfaceType<onedrivesdk.model.defender_attack_surface_type.DefenderAttackSurfaceType>`:
                The defenderScriptObfuscatedMacroCodeType
        """
        if "defenderScriptObfuscatedMacroCodeType" in self._prop_dict:
            if isinstance(self._prop_dict["defenderScriptObfuscatedMacroCodeType"], OneDriveObjectBase):
                return self._prop_dict["defenderScriptObfuscatedMacroCodeType"]
            else :
                self._prop_dict["defenderScriptObfuscatedMacroCodeType"] = DefenderAttackSurfaceType(self._prop_dict["defenderScriptObfuscatedMacroCodeType"])
                return self._prop_dict["defenderScriptObfuscatedMacroCodeType"]

        return None

    @defender_script_obfuscated_macro_code_type.setter
    def defender_script_obfuscated_macro_code_type(self, val):
        self._prop_dict["defenderScriptObfuscatedMacroCodeType"] = val

    @property
    def defender_script_downloaded_payload_execution_type(self):
        """
        Gets and sets the defenderScriptDownloadedPayloadExecutionType
        
        Returns: 
            :class:`DefenderAttackSurfaceType<onedrivesdk.model.defender_attack_surface_type.DefenderAttackSurfaceType>`:
                The defenderScriptDownloadedPayloadExecutionType
        """
        if "defenderScriptDownloadedPayloadExecutionType" in self._prop_dict:
            if isinstance(self._prop_dict["defenderScriptDownloadedPayloadExecutionType"], OneDriveObjectBase):
                return self._prop_dict["defenderScriptDownloadedPayloadExecutionType"]
            else :
                self._prop_dict["defenderScriptDownloadedPayloadExecutionType"] = DefenderAttackSurfaceType(self._prop_dict["defenderScriptDownloadedPayloadExecutionType"])
                return self._prop_dict["defenderScriptDownloadedPayloadExecutionType"]

        return None

    @defender_script_downloaded_payload_execution_type.setter
    def defender_script_downloaded_payload_execution_type(self, val):
        self._prop_dict["defenderScriptDownloadedPayloadExecutionType"] = val

    @property
    def defender_prevent_credential_stealing_type(self):
        """
        Gets and sets the defenderPreventCredentialStealingType
        
        Returns: 
            :class:`DefenderProtectionType<onedrivesdk.model.defender_protection_type.DefenderProtectionType>`:
                The defenderPreventCredentialStealingType
        """
        if "defenderPreventCredentialStealingType" in self._prop_dict:
            if isinstance(self._prop_dict["defenderPreventCredentialStealingType"], OneDriveObjectBase):
                return self._prop_dict["defenderPreventCredentialStealingType"]
            else :
                self._prop_dict["defenderPreventCredentialStealingType"] = DefenderProtectionType(self._prop_dict["defenderPreventCredentialStealingType"])
                return self._prop_dict["defenderPreventCredentialStealingType"]

        return None

    @defender_prevent_credential_stealing_type.setter
    def defender_prevent_credential_stealing_type(self, val):
        self._prop_dict["defenderPreventCredentialStealingType"] = val

    @property
    def defender_process_creation_type(self):
        """
        Gets and sets the defenderProcessCreationType
        
        Returns: 
            :class:`DefenderAttackSurfaceType<onedrivesdk.model.defender_attack_surface_type.DefenderAttackSurfaceType>`:
                The defenderProcessCreationType
        """
        if "defenderProcessCreationType" in self._prop_dict:
            if isinstance(self._prop_dict["defenderProcessCreationType"], OneDriveObjectBase):
                return self._prop_dict["defenderProcessCreationType"]
            else :
                self._prop_dict["defenderProcessCreationType"] = DefenderAttackSurfaceType(self._prop_dict["defenderProcessCreationType"])
                return self._prop_dict["defenderProcessCreationType"]

        return None

    @defender_process_creation_type.setter
    def defender_process_creation_type(self, val):
        self._prop_dict["defenderProcessCreationType"] = val

    @property
    def defender_untrusted_usb_process_type(self):
        """
        Gets and sets the defenderUntrustedUSBProcessType
        
        Returns: 
            :class:`DefenderAttackSurfaceType<onedrivesdk.model.defender_attack_surface_type.DefenderAttackSurfaceType>`:
                The defenderUntrustedUSBProcessType
        """
        if "defenderUntrustedUSBProcessType" in self._prop_dict:
            if isinstance(self._prop_dict["defenderUntrustedUSBProcessType"], OneDriveObjectBase):
                return self._prop_dict["defenderUntrustedUSBProcessType"]
            else :
                self._prop_dict["defenderUntrustedUSBProcessType"] = DefenderAttackSurfaceType(self._prop_dict["defenderUntrustedUSBProcessType"])
                return self._prop_dict["defenderUntrustedUSBProcessType"]

        return None

    @defender_untrusted_usb_process_type.setter
    def defender_untrusted_usb_process_type(self, val):
        self._prop_dict["defenderUntrustedUSBProcessType"] = val

    @property
    def defender_untrusted_executable_type(self):
        """
        Gets and sets the defenderUntrustedExecutableType
        
        Returns: 
            :class:`DefenderAttackSurfaceType<onedrivesdk.model.defender_attack_surface_type.DefenderAttackSurfaceType>`:
                The defenderUntrustedExecutableType
        """
        if "defenderUntrustedExecutableType" in self._prop_dict:
            if isinstance(self._prop_dict["defenderUntrustedExecutableType"], OneDriveObjectBase):
                return self._prop_dict["defenderUntrustedExecutableType"]
            else :
                self._prop_dict["defenderUntrustedExecutableType"] = DefenderAttackSurfaceType(self._prop_dict["defenderUntrustedExecutableType"])
                return self._prop_dict["defenderUntrustedExecutableType"]

        return None

    @defender_untrusted_executable_type.setter
    def defender_untrusted_executable_type(self, val):
        self._prop_dict["defenderUntrustedExecutableType"] = val

    @property
    def defender_email_content_execution_type(self):
        """
        Gets and sets the defenderEmailContentExecutionType
        
        Returns: 
            :class:`DefenderAttackSurfaceType<onedrivesdk.model.defender_attack_surface_type.DefenderAttackSurfaceType>`:
                The defenderEmailContentExecutionType
        """
        if "defenderEmailContentExecutionType" in self._prop_dict:
            if isinstance(self._prop_dict["defenderEmailContentExecutionType"], OneDriveObjectBase):
                return self._prop_dict["defenderEmailContentExecutionType"]
            else :
                self._prop_dict["defenderEmailContentExecutionType"] = DefenderAttackSurfaceType(self._prop_dict["defenderEmailContentExecutionType"])
                return self._prop_dict["defenderEmailContentExecutionType"]

        return None

    @defender_email_content_execution_type.setter
    def defender_email_content_execution_type(self, val):
        self._prop_dict["defenderEmailContentExecutionType"] = val

    @property
    def defender_advanced_ransomeware_protection_type(self):
        """
        Gets and sets the defenderAdvancedRansomewareProtectionType
        
        Returns: 
            :class:`DefenderProtectionType<onedrivesdk.model.defender_protection_type.DefenderProtectionType>`:
                The defenderAdvancedRansomewareProtectionType
        """
        if "defenderAdvancedRansomewareProtectionType" in self._prop_dict:
            if isinstance(self._prop_dict["defenderAdvancedRansomewareProtectionType"], OneDriveObjectBase):
                return self._prop_dict["defenderAdvancedRansomewareProtectionType"]
            else :
                self._prop_dict["defenderAdvancedRansomewareProtectionType"] = DefenderProtectionType(self._prop_dict["defenderAdvancedRansomewareProtectionType"])
                return self._prop_dict["defenderAdvancedRansomewareProtectionType"]

        return None

    @defender_advanced_ransomeware_protection_type.setter
    def defender_advanced_ransomeware_protection_type(self, val):
        self._prop_dict["defenderAdvancedRansomewareProtectionType"] = val

    @property
    def defender_guard_my_folders_type(self):
        """
        Gets and sets the defenderGuardMyFoldersType
        
        Returns: 
            :class:`FolderProtectionType<onedrivesdk.model.folder_protection_type.FolderProtectionType>`:
                The defenderGuardMyFoldersType
        """
        if "defenderGuardMyFoldersType" in self._prop_dict:
            if isinstance(self._prop_dict["defenderGuardMyFoldersType"], OneDriveObjectBase):
                return self._prop_dict["defenderGuardMyFoldersType"]
            else :
                self._prop_dict["defenderGuardMyFoldersType"] = FolderProtectionType(self._prop_dict["defenderGuardMyFoldersType"])
                return self._prop_dict["defenderGuardMyFoldersType"]

        return None

    @defender_guard_my_folders_type.setter
    def defender_guard_my_folders_type(self, val):
        self._prop_dict["defenderGuardMyFoldersType"] = val

    @property
    def defender_guarded_folders_allowed_app_paths(self):
        """
        Gets and sets the defenderGuardedFoldersAllowedAppPaths
        
        Returns:
            str:
                The defenderGuardedFoldersAllowedAppPaths
        """
        if "defenderGuardedFoldersAllowedAppPaths" in self._prop_dict:
            return self._prop_dict["defenderGuardedFoldersAllowedAppPaths"]
        else:
            return None

    @defender_guarded_folders_allowed_app_paths.setter
    def defender_guarded_folders_allowed_app_paths(self, val):
        self._prop_dict["defenderGuardedFoldersAllowedAppPaths"] = val

    @property
    def defender_additional_guarded_folders(self):
        """
        Gets and sets the defenderAdditionalGuardedFolders
        
        Returns:
            str:
                The defenderAdditionalGuardedFolders
        """
        if "defenderAdditionalGuardedFolders" in self._prop_dict:
            return self._prop_dict["defenderAdditionalGuardedFolders"]
        else:
            return None

    @defender_additional_guarded_folders.setter
    def defender_additional_guarded_folders(self, val):
        self._prop_dict["defenderAdditionalGuardedFolders"] = val

    @property
    def defender_network_protection_type(self):
        """
        Gets and sets the defenderNetworkProtectionType
        
        Returns: 
            :class:`DefenderProtectionType<onedrivesdk.model.defender_protection_type.DefenderProtectionType>`:
                The defenderNetworkProtectionType
        """
        if "defenderNetworkProtectionType" in self._prop_dict:
            if isinstance(self._prop_dict["defenderNetworkProtectionType"], OneDriveObjectBase):
                return self._prop_dict["defenderNetworkProtectionType"]
            else :
                self._prop_dict["defenderNetworkProtectionType"] = DefenderProtectionType(self._prop_dict["defenderNetworkProtectionType"])
                return self._prop_dict["defenderNetworkProtectionType"]

        return None

    @defender_network_protection_type.setter
    def defender_network_protection_type(self, val):
        self._prop_dict["defenderNetworkProtectionType"] = val

    @property
    def defender_exploit_protection_xml_file_name(self):
        """
        Gets and sets the defenderExploitProtectionXmlFileName
        
        Returns:
            str:
                The defenderExploitProtectionXmlFileName
        """
        if "defenderExploitProtectionXmlFileName" in self._prop_dict:
            return self._prop_dict["defenderExploitProtectionXmlFileName"]
        else:
            return None

    @defender_exploit_protection_xml_file_name.setter
    def defender_exploit_protection_xml_file_name(self, val):
        self._prop_dict["defenderExploitProtectionXmlFileName"] = val

    @property
    def defender_security_center_block_exploit_protection_override(self):
        """
        Gets and sets the defenderSecurityCenterBlockExploitProtectionOverride
        
        Returns:
            bool:
                The defenderSecurityCenterBlockExploitProtectionOverride
        """
        if "defenderSecurityCenterBlockExploitProtectionOverride" in self._prop_dict:
            return self._prop_dict["defenderSecurityCenterBlockExploitProtectionOverride"]
        else:
            return None

    @defender_security_center_block_exploit_protection_override.setter
    def defender_security_center_block_exploit_protection_override(self, val):
        self._prop_dict["defenderSecurityCenterBlockExploitProtectionOverride"] = val

    @property
    def app_locker_application_control(self):
        """
        Gets and sets the appLockerApplicationControl
        
        Returns: 
            :class:`AppLockerApplicationControlType<onedrivesdk.model.app_locker_application_control_type.AppLockerApplicationControlType>`:
                The appLockerApplicationControl
        """
        if "appLockerApplicationControl" in self._prop_dict:
            if isinstance(self._prop_dict["appLockerApplicationControl"], OneDriveObjectBase):
                return self._prop_dict["appLockerApplicationControl"]
            else :
                self._prop_dict["appLockerApplicationControl"] = AppLockerApplicationControlType(self._prop_dict["appLockerApplicationControl"])
                return self._prop_dict["appLockerApplicationControl"]

        return None

    @app_locker_application_control.setter
    def app_locker_application_control(self, val):
        self._prop_dict["appLockerApplicationControl"] = val

    @property
    def device_guard_local_system_authority_credential_guard_settings(self):
        """
        Gets and sets the deviceGuardLocalSystemAuthorityCredentialGuardSettings
        
        Returns: 
            :class:`DeviceGuardLocalSystemAuthorityCredentialGuardType<onedrivesdk.model.device_guard_local_system_authority_credential_guard_type.DeviceGuardLocalSystemAuthorityCredentialGuardType>`:
                The deviceGuardLocalSystemAuthorityCredentialGuardSettings
        """
        if "deviceGuardLocalSystemAuthorityCredentialGuardSettings" in self._prop_dict:
            if isinstance(self._prop_dict["deviceGuardLocalSystemAuthorityCredentialGuardSettings"], OneDriveObjectBase):
                return self._prop_dict["deviceGuardLocalSystemAuthorityCredentialGuardSettings"]
            else :
                self._prop_dict["deviceGuardLocalSystemAuthorityCredentialGuardSettings"] = DeviceGuardLocalSystemAuthorityCredentialGuardType(self._prop_dict["deviceGuardLocalSystemAuthorityCredentialGuardSettings"])
                return self._prop_dict["deviceGuardLocalSystemAuthorityCredentialGuardSettings"]

        return None

    @device_guard_local_system_authority_credential_guard_settings.setter
    def device_guard_local_system_authority_credential_guard_settings(self, val):
        self._prop_dict["deviceGuardLocalSystemAuthorityCredentialGuardSettings"] = val

    @property
    def device_guard_enable_virtualization_based_security(self):
        """
        Gets and sets the deviceGuardEnableVirtualizationBasedSecurity
        
        Returns:
            bool:
                The deviceGuardEnableVirtualizationBasedSecurity
        """
        if "deviceGuardEnableVirtualizationBasedSecurity" in self._prop_dict:
            return self._prop_dict["deviceGuardEnableVirtualizationBasedSecurity"]
        else:
            return None

    @device_guard_enable_virtualization_based_security.setter
    def device_guard_enable_virtualization_based_security(self, val):
        self._prop_dict["deviceGuardEnableVirtualizationBasedSecurity"] = val

    @property
    def device_guard_enable_secure_boot_with_dma(self):
        """
        Gets and sets the deviceGuardEnableSecureBootWithDMA
        
        Returns:
            bool:
                The deviceGuardEnableSecureBootWithDMA
        """
        if "deviceGuardEnableSecureBootWithDMA" in self._prop_dict:
            return self._prop_dict["deviceGuardEnableSecureBootWithDMA"]
        else:
            return None

    @device_guard_enable_secure_boot_with_dma.setter
    def device_guard_enable_secure_boot_with_dma(self, val):
        self._prop_dict["deviceGuardEnableSecureBootWithDMA"] = val

    @property
    def smart_screen_enable_in_shell(self):
        """
        Gets and sets the smartScreenEnableInShell
        
        Returns:
            bool:
                The smartScreenEnableInShell
        """
        if "smartScreenEnableInShell" in self._prop_dict:
            return self._prop_dict["smartScreenEnableInShell"]
        else:
            return None

    @smart_screen_enable_in_shell.setter
    def smart_screen_enable_in_shell(self, val):
        self._prop_dict["smartScreenEnableInShell"] = val

    @property
    def smart_screen_block_override_for_files(self):
        """
        Gets and sets the smartScreenBlockOverrideForFiles
        
        Returns:
            bool:
                The smartScreenBlockOverrideForFiles
        """
        if "smartScreenBlockOverrideForFiles" in self._prop_dict:
            return self._prop_dict["smartScreenBlockOverrideForFiles"]
        else:
            return None

    @smart_screen_block_override_for_files.setter
    def smart_screen_block_override_for_files(self, val):
        self._prop_dict["smartScreenBlockOverrideForFiles"] = val

    @property
    def application_guard_enabled(self):
        """
        Gets and sets the applicationGuardEnabled
        
        Returns:
            bool:
                The applicationGuardEnabled
        """
        if "applicationGuardEnabled" in self._prop_dict:
            return self._prop_dict["applicationGuardEnabled"]
        else:
            return None

    @application_guard_enabled.setter
    def application_guard_enabled(self, val):
        self._prop_dict["applicationGuardEnabled"] = val

    @property
    def application_guard_block_file_transfer(self):
        """
        Gets and sets the applicationGuardBlockFileTransfer
        
        Returns: 
            :class:`ApplicationGuardBlockFileTransferType<onedrivesdk.model.application_guard_block_file_transfer_type.ApplicationGuardBlockFileTransferType>`:
                The applicationGuardBlockFileTransfer
        """
        if "applicationGuardBlockFileTransfer" in self._prop_dict:
            if isinstance(self._prop_dict["applicationGuardBlockFileTransfer"], OneDriveObjectBase):
                return self._prop_dict["applicationGuardBlockFileTransfer"]
            else :
                self._prop_dict["applicationGuardBlockFileTransfer"] = ApplicationGuardBlockFileTransferType(self._prop_dict["applicationGuardBlockFileTransfer"])
                return self._prop_dict["applicationGuardBlockFileTransfer"]

        return None

    @application_guard_block_file_transfer.setter
    def application_guard_block_file_transfer(self, val):
        self._prop_dict["applicationGuardBlockFileTransfer"] = val

    @property
    def application_guard_block_non_enterprise_content(self):
        """
        Gets and sets the applicationGuardBlockNonEnterpriseContent
        
        Returns:
            bool:
                The applicationGuardBlockNonEnterpriseContent
        """
        if "applicationGuardBlockNonEnterpriseContent" in self._prop_dict:
            return self._prop_dict["applicationGuardBlockNonEnterpriseContent"]
        else:
            return None

    @application_guard_block_non_enterprise_content.setter
    def application_guard_block_non_enterprise_content(self, val):
        self._prop_dict["applicationGuardBlockNonEnterpriseContent"] = val

    @property
    def application_guard_allow_persistence(self):
        """
        Gets and sets the applicationGuardAllowPersistence
        
        Returns:
            bool:
                The applicationGuardAllowPersistence
        """
        if "applicationGuardAllowPersistence" in self._prop_dict:
            return self._prop_dict["applicationGuardAllowPersistence"]
        else:
            return None

    @application_guard_allow_persistence.setter
    def application_guard_allow_persistence(self, val):
        self._prop_dict["applicationGuardAllowPersistence"] = val

    @property
    def application_guard_force_auditing(self):
        """
        Gets and sets the applicationGuardForceAuditing
        
        Returns:
            bool:
                The applicationGuardForceAuditing
        """
        if "applicationGuardForceAuditing" in self._prop_dict:
            return self._prop_dict["applicationGuardForceAuditing"]
        else:
            return None

    @application_guard_force_auditing.setter
    def application_guard_force_auditing(self, val):
        self._prop_dict["applicationGuardForceAuditing"] = val

    @property
    def application_guard_block_clipboard_sharing(self):
        """
        Gets and sets the applicationGuardBlockClipboardSharing
        
        Returns: 
            :class:`ApplicationGuardBlockClipboardSharingType<onedrivesdk.model.application_guard_block_clipboard_sharing_type.ApplicationGuardBlockClipboardSharingType>`:
                The applicationGuardBlockClipboardSharing
        """
        if "applicationGuardBlockClipboardSharing" in self._prop_dict:
            if isinstance(self._prop_dict["applicationGuardBlockClipboardSharing"], OneDriveObjectBase):
                return self._prop_dict["applicationGuardBlockClipboardSharing"]
            else :
                self._prop_dict["applicationGuardBlockClipboardSharing"] = ApplicationGuardBlockClipboardSharingType(self._prop_dict["applicationGuardBlockClipboardSharing"])
                return self._prop_dict["applicationGuardBlockClipboardSharing"]

        return None

    @application_guard_block_clipboard_sharing.setter
    def application_guard_block_clipboard_sharing(self, val):
        self._prop_dict["applicationGuardBlockClipboardSharing"] = val

    @property
    def application_guard_allow_print_to_pdf(self):
        """
        Gets and sets the applicationGuardAllowPrintToPDF
        
        Returns:
            bool:
                The applicationGuardAllowPrintToPDF
        """
        if "applicationGuardAllowPrintToPDF" in self._prop_dict:
            return self._prop_dict["applicationGuardAllowPrintToPDF"]
        else:
            return None

    @application_guard_allow_print_to_pdf.setter
    def application_guard_allow_print_to_pdf(self, val):
        self._prop_dict["applicationGuardAllowPrintToPDF"] = val

    @property
    def application_guard_allow_print_to_xps(self):
        """
        Gets and sets the applicationGuardAllowPrintToXPS
        
        Returns:
            bool:
                The applicationGuardAllowPrintToXPS
        """
        if "applicationGuardAllowPrintToXPS" in self._prop_dict:
            return self._prop_dict["applicationGuardAllowPrintToXPS"]
        else:
            return None

    @application_guard_allow_print_to_xps.setter
    def application_guard_allow_print_to_xps(self, val):
        self._prop_dict["applicationGuardAllowPrintToXPS"] = val

    @property
    def application_guard_allow_print_to_local_printers(self):
        """
        Gets and sets the applicationGuardAllowPrintToLocalPrinters
        
        Returns:
            bool:
                The applicationGuardAllowPrintToLocalPrinters
        """
        if "applicationGuardAllowPrintToLocalPrinters" in self._prop_dict:
            return self._prop_dict["applicationGuardAllowPrintToLocalPrinters"]
        else:
            return None

    @application_guard_allow_print_to_local_printers.setter
    def application_guard_allow_print_to_local_printers(self, val):
        self._prop_dict["applicationGuardAllowPrintToLocalPrinters"] = val

    @property
    def application_guard_allow_print_to_network_printers(self):
        """
        Gets and sets the applicationGuardAllowPrintToNetworkPrinters
        
        Returns:
            bool:
                The applicationGuardAllowPrintToNetworkPrinters
        """
        if "applicationGuardAllowPrintToNetworkPrinters" in self._prop_dict:
            return self._prop_dict["applicationGuardAllowPrintToNetworkPrinters"]
        else:
            return None

    @application_guard_allow_print_to_network_printers.setter
    def application_guard_allow_print_to_network_printers(self, val):
        self._prop_dict["applicationGuardAllowPrintToNetworkPrinters"] = val

    @property
    def application_guard_allow_virtual_gpu(self):
        """
        Gets and sets the applicationGuardAllowVirtualGPU
        
        Returns:
            bool:
                The applicationGuardAllowVirtualGPU
        """
        if "applicationGuardAllowVirtualGPU" in self._prop_dict:
            return self._prop_dict["applicationGuardAllowVirtualGPU"]
        else:
            return None

    @application_guard_allow_virtual_gpu.setter
    def application_guard_allow_virtual_gpu(self, val):
        self._prop_dict["applicationGuardAllowVirtualGPU"] = val

    @property
    def application_guard_allow_file_save_on_host(self):
        """
        Gets and sets the applicationGuardAllowFileSaveOnHost
        
        Returns:
            bool:
                The applicationGuardAllowFileSaveOnHost
        """
        if "applicationGuardAllowFileSaveOnHost" in self._prop_dict:
            return self._prop_dict["applicationGuardAllowFileSaveOnHost"]
        else:
            return None

    @application_guard_allow_file_save_on_host.setter
    def application_guard_allow_file_save_on_host(self, val):
        self._prop_dict["applicationGuardAllowFileSaveOnHost"] = val

    @property
    def bit_locker_disable_warning_for_other_disk_encryption(self):
        """
        Gets and sets the bitLockerDisableWarningForOtherDiskEncryption
        
        Returns:
            bool:
                The bitLockerDisableWarningForOtherDiskEncryption
        """
        if "bitLockerDisableWarningForOtherDiskEncryption" in self._prop_dict:
            return self._prop_dict["bitLockerDisableWarningForOtherDiskEncryption"]
        else:
            return None

    @bit_locker_disable_warning_for_other_disk_encryption.setter
    def bit_locker_disable_warning_for_other_disk_encryption(self, val):
        self._prop_dict["bitLockerDisableWarningForOtherDiskEncryption"] = val

    @property
    def bit_locker_enable_storage_card_encryption_on_mobile(self):
        """
        Gets and sets the bitLockerEnableStorageCardEncryptionOnMobile
        
        Returns:
            bool:
                The bitLockerEnableStorageCardEncryptionOnMobile
        """
        if "bitLockerEnableStorageCardEncryptionOnMobile" in self._prop_dict:
            return self._prop_dict["bitLockerEnableStorageCardEncryptionOnMobile"]
        else:
            return None

    @bit_locker_enable_storage_card_encryption_on_mobile.setter
    def bit_locker_enable_storage_card_encryption_on_mobile(self, val):
        self._prop_dict["bitLockerEnableStorageCardEncryptionOnMobile"] = val

    @property
    def bit_locker_encrypt_device(self):
        """
        Gets and sets the bitLockerEncryptDevice
        
        Returns:
            bool:
                The bitLockerEncryptDevice
        """
        if "bitLockerEncryptDevice" in self._prop_dict:
            return self._prop_dict["bitLockerEncryptDevice"]
        else:
            return None

    @bit_locker_encrypt_device.setter
    def bit_locker_encrypt_device(self, val):
        self._prop_dict["bitLockerEncryptDevice"] = val

    @property
    def bit_locker_system_drive_policy(self):
        """
        Gets and sets the bitLockerSystemDrivePolicy
        
        Returns: 
            :class:`BitLockerSystemDrivePolicy<onedrivesdk.model.bit_locker_system_drive_policy.BitLockerSystemDrivePolicy>`:
                The bitLockerSystemDrivePolicy
        """
        if "bitLockerSystemDrivePolicy" in self._prop_dict:
            if isinstance(self._prop_dict["bitLockerSystemDrivePolicy"], OneDriveObjectBase):
                return self._prop_dict["bitLockerSystemDrivePolicy"]
            else :
                self._prop_dict["bitLockerSystemDrivePolicy"] = BitLockerSystemDrivePolicy(self._prop_dict["bitLockerSystemDrivePolicy"])
                return self._prop_dict["bitLockerSystemDrivePolicy"]

        return None

    @bit_locker_system_drive_policy.setter
    def bit_locker_system_drive_policy(self, val):
        self._prop_dict["bitLockerSystemDrivePolicy"] = val

    @property
    def bit_locker_fixed_drive_policy(self):
        """
        Gets and sets the bitLockerFixedDrivePolicy
        
        Returns: 
            :class:`BitLockerFixedDrivePolicy<onedrivesdk.model.bit_locker_fixed_drive_policy.BitLockerFixedDrivePolicy>`:
                The bitLockerFixedDrivePolicy
        """
        if "bitLockerFixedDrivePolicy" in self._prop_dict:
            if isinstance(self._prop_dict["bitLockerFixedDrivePolicy"], OneDriveObjectBase):
                return self._prop_dict["bitLockerFixedDrivePolicy"]
            else :
                self._prop_dict["bitLockerFixedDrivePolicy"] = BitLockerFixedDrivePolicy(self._prop_dict["bitLockerFixedDrivePolicy"])
                return self._prop_dict["bitLockerFixedDrivePolicy"]

        return None

    @bit_locker_fixed_drive_policy.setter
    def bit_locker_fixed_drive_policy(self, val):
        self._prop_dict["bitLockerFixedDrivePolicy"] = val

    @property
    def bit_locker_removable_drive_policy(self):
        """
        Gets and sets the bitLockerRemovableDrivePolicy
        
        Returns: 
            :class:`BitLockerRemovableDrivePolicy<onedrivesdk.model.bit_locker_removable_drive_policy.BitLockerRemovableDrivePolicy>`:
                The bitLockerRemovableDrivePolicy
        """
        if "bitLockerRemovableDrivePolicy" in self._prop_dict:
            if isinstance(self._prop_dict["bitLockerRemovableDrivePolicy"], OneDriveObjectBase):
                return self._prop_dict["bitLockerRemovableDrivePolicy"]
            else :
                self._prop_dict["bitLockerRemovableDrivePolicy"] = BitLockerRemovableDrivePolicy(self._prop_dict["bitLockerRemovableDrivePolicy"])
                return self._prop_dict["bitLockerRemovableDrivePolicy"]

        return None

    @bit_locker_removable_drive_policy.setter
    def bit_locker_removable_drive_policy(self, val):
        self._prop_dict["bitLockerRemovableDrivePolicy"] = val

