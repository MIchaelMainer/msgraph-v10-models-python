# -*- coding: utf-8 -*- 
'''
# Copyright (c) Microsoft Corporation.  All Rights Reserved.  Licensed under the MIT License.  See License in the project root for license information.
# 
#  This file was generated and any changes will be overwritten.
'''

from __future__ import unicode_literals
from ..model.sign_in_assistant_options import SignInAssistantOptions
from ..model.diagnostic_data_submission_mode import DiagnosticDataSubmissionMode
from ..model.ink_access_setting import InkAccessSetting
from ..model.edge_cookie_policy import EdgeCookiePolicy
from ..model.configuration_usage import ConfigurationUsage
from ..model.defender_detected_malware_actions import DefenderDetectedMalwareActions
from ..model.weekly_schedule import WeeklySchedule
from ..model.defender_monitor_file_activity import DefenderMonitorFileActivity
from ..model.defender_potentially_unwanted_app_action import DefenderPotentiallyUnwantedAppAction
from ..model.defender_prompt_for_sample_submission import DefenderPromptForSampleSubmission
from ..model.defender_scan_type import DefenderScanType
from ..model.time_of_day import TimeOfDay
from ..model.defender_cloud_block_level_type import DefenderCloudBlockLevelType
from ..model.defender_schedule_scan_day import DefenderScheduleScanDay
from ..model.defender_submit_samples_consent_type import DefenderSubmitSamplesConsentType
from ..model.required_password_type import RequiredPasswordType
from ..model.state_management_setting import StateManagementSetting
from ..model.windows_start_menu_app_list_visibility_type import WindowsStartMenuAppListVisibilityType
from ..model.windows_start_menu_mode_type import WindowsStartMenuModeType
from ..model.visibility_setting import VisibilitySetting
from ..model.windows_spotlight_enablement_settings import WindowsSpotlightEnablementSettings
from ..model.windows10_network_proxy_server import Windows10NetworkProxyServer
from ..model.safe_search_filter_type import SafeSearchFilterType
from ..model.edge_search_engine_base import EdgeSearchEngineBase
from ..model.windows_assigned_access_profile import WindowsAssignedAccessProfile
from ..model.windows_privacy_data_access_control_item import WindowsPrivacyDataAccessControlItem
from ..one_drive_object_base import OneDriveObjectBase


class Windows10GeneralConfiguration(OneDriveObjectBase):

    def __init__(self, prop_dict={}):
        self._prop_dict = prop_dict

    @property
    def enable_automatic_redeployment(self):
        """
        Gets and sets the enableAutomaticRedeployment
        
        Returns:
            bool:
                The enableAutomaticRedeployment
        """
        if "enableAutomaticRedeployment" in self._prop_dict:
            return self._prop_dict["enableAutomaticRedeployment"]
        else:
            return None

    @enable_automatic_redeployment.setter
    def enable_automatic_redeployment(self, val):
        self._prop_dict["enableAutomaticRedeployment"] = val

    @property
    def assigned_access_single_mode_user_name(self):
        """
        Gets and sets the assignedAccessSingleModeUserName
        
        Returns:
            str:
                The assignedAccessSingleModeUserName
        """
        if "assignedAccessSingleModeUserName" in self._prop_dict:
            return self._prop_dict["assignedAccessSingleModeUserName"]
        else:
            return None

    @assigned_access_single_mode_user_name.setter
    def assigned_access_single_mode_user_name(self, val):
        self._prop_dict["assignedAccessSingleModeUserName"] = val

    @property
    def assigned_access_single_mode_app_user_model_id(self):
        """
        Gets and sets the assignedAccessSingleModeAppUserModelId
        
        Returns:
            str:
                The assignedAccessSingleModeAppUserModelId
        """
        if "assignedAccessSingleModeAppUserModelId" in self._prop_dict:
            return self._prop_dict["assignedAccessSingleModeAppUserModelId"]
        else:
            return None

    @assigned_access_single_mode_app_user_model_id.setter
    def assigned_access_single_mode_app_user_model_id(self, val):
        self._prop_dict["assignedAccessSingleModeAppUserModelId"] = val

    @property
    def microsoft_account_sign_in_assistant_settings(self):
        """
        Gets and sets the microsoftAccountSignInAssistantSettings
        
        Returns: 
            :class:`SignInAssistantOptions<onedrivesdk.model.sign_in_assistant_options.SignInAssistantOptions>`:
                The microsoftAccountSignInAssistantSettings
        """
        if "microsoftAccountSignInAssistantSettings" in self._prop_dict:
            if isinstance(self._prop_dict["microsoftAccountSignInAssistantSettings"], OneDriveObjectBase):
                return self._prop_dict["microsoftAccountSignInAssistantSettings"]
            else :
                self._prop_dict["microsoftAccountSignInAssistantSettings"] = SignInAssistantOptions(self._prop_dict["microsoftAccountSignInAssistantSettings"])
                return self._prop_dict["microsoftAccountSignInAssistantSettings"]

        return None

    @microsoft_account_sign_in_assistant_settings.setter
    def microsoft_account_sign_in_assistant_settings(self, val):
        self._prop_dict["microsoftAccountSignInAssistantSettings"] = val

    @property
    def authentication_allow_secondary_device(self):
        """
        Gets and sets the authenticationAllowSecondaryDevice
        
        Returns:
            bool:
                The authenticationAllowSecondaryDevice
        """
        if "authenticationAllowSecondaryDevice" in self._prop_dict:
            return self._prop_dict["authenticationAllowSecondaryDevice"]
        else:
            return None

    @authentication_allow_secondary_device.setter
    def authentication_allow_secondary_device(self, val):
        self._prop_dict["authenticationAllowSecondaryDevice"] = val

    @property
    def authentication_allow_fido_device(self):
        """
        Gets and sets the authenticationAllowFIDODevice
        
        Returns:
            bool:
                The authenticationAllowFIDODevice
        """
        if "authenticationAllowFIDODevice" in self._prop_dict:
            return self._prop_dict["authenticationAllowFIDODevice"]
        else:
            return None

    @authentication_allow_fido_device.setter
    def authentication_allow_fido_device(self, val):
        self._prop_dict["authenticationAllowFIDODevice"] = val

    @property
    def cryptography_allow_fips_algorithm_policy(self):
        """
        Gets and sets the cryptographyAllowFipsAlgorithmPolicy
        
        Returns:
            bool:
                The cryptographyAllowFipsAlgorithmPolicy
        """
        if "cryptographyAllowFipsAlgorithmPolicy" in self._prop_dict:
            return self._prop_dict["cryptographyAllowFipsAlgorithmPolicy"]
        else:
            return None

    @cryptography_allow_fips_algorithm_policy.setter
    def cryptography_allow_fips_algorithm_policy(self, val):
        self._prop_dict["cryptographyAllowFipsAlgorithmPolicy"] = val

    @property
    def display_app_list_with_gdi_dpi_scaling_turned_on(self):
        """
        Gets and sets the displayAppListWithGdiDPIScalingTurnedOn
        
        Returns:
            str:
                The displayAppListWithGdiDPIScalingTurnedOn
        """
        if "displayAppListWithGdiDPIScalingTurnedOn" in self._prop_dict:
            return self._prop_dict["displayAppListWithGdiDPIScalingTurnedOn"]
        else:
            return None

    @display_app_list_with_gdi_dpi_scaling_turned_on.setter
    def display_app_list_with_gdi_dpi_scaling_turned_on(self, val):
        self._prop_dict["displayAppListWithGdiDPIScalingTurnedOn"] = val

    @property
    def display_app_list_with_gdi_dpi_scaling_turned_off(self):
        """
        Gets and sets the displayAppListWithGdiDPIScalingTurnedOff
        
        Returns:
            str:
                The displayAppListWithGdiDPIScalingTurnedOff
        """
        if "displayAppListWithGdiDPIScalingTurnedOff" in self._prop_dict:
            return self._prop_dict["displayAppListWithGdiDPIScalingTurnedOff"]
        else:
            return None

    @display_app_list_with_gdi_dpi_scaling_turned_off.setter
    def display_app_list_with_gdi_dpi_scaling_turned_off(self, val):
        self._prop_dict["displayAppListWithGdiDPIScalingTurnedOff"] = val

    @property
    def enterprise_cloud_print_discovery_end_point(self):
        """
        Gets and sets the enterpriseCloudPrintDiscoveryEndPoint
        
        Returns:
            str:
                The enterpriseCloudPrintDiscoveryEndPoint
        """
        if "enterpriseCloudPrintDiscoveryEndPoint" in self._prop_dict:
            return self._prop_dict["enterpriseCloudPrintDiscoveryEndPoint"]
        else:
            return None

    @enterprise_cloud_print_discovery_end_point.setter
    def enterprise_cloud_print_discovery_end_point(self, val):
        self._prop_dict["enterpriseCloudPrintDiscoveryEndPoint"] = val

    @property
    def enterprise_cloud_print_o_auth_authority(self):
        """
        Gets and sets the enterpriseCloudPrintOAuthAuthority
        
        Returns:
            str:
                The enterpriseCloudPrintOAuthAuthority
        """
        if "enterpriseCloudPrintOAuthAuthority" in self._prop_dict:
            return self._prop_dict["enterpriseCloudPrintOAuthAuthority"]
        else:
            return None

    @enterprise_cloud_print_o_auth_authority.setter
    def enterprise_cloud_print_o_auth_authority(self, val):
        self._prop_dict["enterpriseCloudPrintOAuthAuthority"] = val

    @property
    def enterprise_cloud_print_o_auth_client_identifier(self):
        """
        Gets and sets the enterpriseCloudPrintOAuthClientIdentifier
        
        Returns:
            str:
                The enterpriseCloudPrintOAuthClientIdentifier
        """
        if "enterpriseCloudPrintOAuthClientIdentifier" in self._prop_dict:
            return self._prop_dict["enterpriseCloudPrintOAuthClientIdentifier"]
        else:
            return None

    @enterprise_cloud_print_o_auth_client_identifier.setter
    def enterprise_cloud_print_o_auth_client_identifier(self, val):
        self._prop_dict["enterpriseCloudPrintOAuthClientIdentifier"] = val

    @property
    def enterprise_cloud_print_resource_identifier(self):
        """
        Gets and sets the enterpriseCloudPrintResourceIdentifier
        
        Returns:
            str:
                The enterpriseCloudPrintResourceIdentifier
        """
        if "enterpriseCloudPrintResourceIdentifier" in self._prop_dict:
            return self._prop_dict["enterpriseCloudPrintResourceIdentifier"]
        else:
            return None

    @enterprise_cloud_print_resource_identifier.setter
    def enterprise_cloud_print_resource_identifier(self, val):
        self._prop_dict["enterpriseCloudPrintResourceIdentifier"] = val

    @property
    def enterprise_cloud_print_discovery_max_limit(self):
        """
        Gets and sets the enterpriseCloudPrintDiscoveryMaxLimit
        
        Returns:
            int:
                The enterpriseCloudPrintDiscoveryMaxLimit
        """
        if "enterpriseCloudPrintDiscoveryMaxLimit" in self._prop_dict:
            return self._prop_dict["enterpriseCloudPrintDiscoveryMaxLimit"]
        else:
            return None

    @enterprise_cloud_print_discovery_max_limit.setter
    def enterprise_cloud_print_discovery_max_limit(self, val):
        self._prop_dict["enterpriseCloudPrintDiscoveryMaxLimit"] = val

    @property
    def enterprise_cloud_print_mopria_discovery_resource_identifier(self):
        """
        Gets and sets the enterpriseCloudPrintMopriaDiscoveryResourceIdentifier
        
        Returns:
            str:
                The enterpriseCloudPrintMopriaDiscoveryResourceIdentifier
        """
        if "enterpriseCloudPrintMopriaDiscoveryResourceIdentifier" in self._prop_dict:
            return self._prop_dict["enterpriseCloudPrintMopriaDiscoveryResourceIdentifier"]
        else:
            return None

    @enterprise_cloud_print_mopria_discovery_resource_identifier.setter
    def enterprise_cloud_print_mopria_discovery_resource_identifier(self, val):
        self._prop_dict["enterpriseCloudPrintMopriaDiscoveryResourceIdentifier"] = val

    @property
    def messaging_block_sync(self):
        """
        Gets and sets the messagingBlockSync
        
        Returns:
            bool:
                The messagingBlockSync
        """
        if "messagingBlockSync" in self._prop_dict:
            return self._prop_dict["messagingBlockSync"]
        else:
            return None

    @messaging_block_sync.setter
    def messaging_block_sync(self, val):
        self._prop_dict["messagingBlockSync"] = val

    @property
    def messaging_block_mms(self):
        """
        Gets and sets the messagingBlockMMS
        
        Returns:
            bool:
                The messagingBlockMMS
        """
        if "messagingBlockMMS" in self._prop_dict:
            return self._prop_dict["messagingBlockMMS"]
        else:
            return None

    @messaging_block_mms.setter
    def messaging_block_mms(self, val):
        self._prop_dict["messagingBlockMMS"] = val

    @property
    def messaging_block_rich_communication_services(self):
        """
        Gets and sets the messagingBlockRichCommunicationServices
        
        Returns:
            bool:
                The messagingBlockRichCommunicationServices
        """
        if "messagingBlockRichCommunicationServices" in self._prop_dict:
            return self._prop_dict["messagingBlockRichCommunicationServices"]
        else:
            return None

    @messaging_block_rich_communication_services.setter
    def messaging_block_rich_communication_services(self, val):
        self._prop_dict["messagingBlockRichCommunicationServices"] = val

    @property
    def printer_names(self):
        """
        Gets and sets the printerNames
        
        Returns:
            str:
                The printerNames
        """
        if "printerNames" in self._prop_dict:
            return self._prop_dict["printerNames"]
        else:
            return None

    @printer_names.setter
    def printer_names(self, val):
        self._prop_dict["printerNames"] = val

    @property
    def printer_default_name(self):
        """
        Gets and sets the printerDefaultName
        
        Returns:
            str:
                The printerDefaultName
        """
        if "printerDefaultName" in self._prop_dict:
            return self._prop_dict["printerDefaultName"]
        else:
            return None

    @printer_default_name.setter
    def printer_default_name(self, val):
        self._prop_dict["printerDefaultName"] = val

    @property
    def printer_block_addition(self):
        """
        Gets and sets the printerBlockAddition
        
        Returns:
            bool:
                The printerBlockAddition
        """
        if "printerBlockAddition" in self._prop_dict:
            return self._prop_dict["printerBlockAddition"]
        else:
            return None

    @printer_block_addition.setter
    def printer_block_addition(self, val):
        self._prop_dict["printerBlockAddition"] = val

    @property
    def search_block_diacritics(self):
        """
        Gets and sets the searchBlockDiacritics
        
        Returns:
            bool:
                The searchBlockDiacritics
        """
        if "searchBlockDiacritics" in self._prop_dict:
            return self._prop_dict["searchBlockDiacritics"]
        else:
            return None

    @search_block_diacritics.setter
    def search_block_diacritics(self, val):
        self._prop_dict["searchBlockDiacritics"] = val

    @property
    def search_disable_auto_language_detection(self):
        """
        Gets and sets the searchDisableAutoLanguageDetection
        
        Returns:
            bool:
                The searchDisableAutoLanguageDetection
        """
        if "searchDisableAutoLanguageDetection" in self._prop_dict:
            return self._prop_dict["searchDisableAutoLanguageDetection"]
        else:
            return None

    @search_disable_auto_language_detection.setter
    def search_disable_auto_language_detection(self, val):
        self._prop_dict["searchDisableAutoLanguageDetection"] = val

    @property
    def search_disable_indexing_encrypted_items(self):
        """
        Gets and sets the searchDisableIndexingEncryptedItems
        
        Returns:
            bool:
                The searchDisableIndexingEncryptedItems
        """
        if "searchDisableIndexingEncryptedItems" in self._prop_dict:
            return self._prop_dict["searchDisableIndexingEncryptedItems"]
        else:
            return None

    @search_disable_indexing_encrypted_items.setter
    def search_disable_indexing_encrypted_items(self, val):
        self._prop_dict["searchDisableIndexingEncryptedItems"] = val

    @property
    def search_enable_remote_queries(self):
        """
        Gets and sets the searchEnableRemoteQueries
        
        Returns:
            bool:
                The searchEnableRemoteQueries
        """
        if "searchEnableRemoteQueries" in self._prop_dict:
            return self._prop_dict["searchEnableRemoteQueries"]
        else:
            return None

    @search_enable_remote_queries.setter
    def search_enable_remote_queries(self, val):
        self._prop_dict["searchEnableRemoteQueries"] = val

    @property
    def search_disable_use_location(self):
        """
        Gets and sets the searchDisableUseLocation
        
        Returns:
            bool:
                The searchDisableUseLocation
        """
        if "searchDisableUseLocation" in self._prop_dict:
            return self._prop_dict["searchDisableUseLocation"]
        else:
            return None

    @search_disable_use_location.setter
    def search_disable_use_location(self, val):
        self._prop_dict["searchDisableUseLocation"] = val

    @property
    def search_disable_indexer_backoff(self):
        """
        Gets and sets the searchDisableIndexerBackoff
        
        Returns:
            bool:
                The searchDisableIndexerBackoff
        """
        if "searchDisableIndexerBackoff" in self._prop_dict:
            return self._prop_dict["searchDisableIndexerBackoff"]
        else:
            return None

    @search_disable_indexer_backoff.setter
    def search_disable_indexer_backoff(self, val):
        self._prop_dict["searchDisableIndexerBackoff"] = val

    @property
    def search_disable_indexing_removable_drive(self):
        """
        Gets and sets the searchDisableIndexingRemovableDrive
        
        Returns:
            bool:
                The searchDisableIndexingRemovableDrive
        """
        if "searchDisableIndexingRemovableDrive" in self._prop_dict:
            return self._prop_dict["searchDisableIndexingRemovableDrive"]
        else:
            return None

    @search_disable_indexing_removable_drive.setter
    def search_disable_indexing_removable_drive(self, val):
        self._prop_dict["searchDisableIndexingRemovableDrive"] = val

    @property
    def search_enable_automatic_index_size_manangement(self):
        """
        Gets and sets the searchEnableAutomaticIndexSizeManangement
        
        Returns:
            bool:
                The searchEnableAutomaticIndexSizeManangement
        """
        if "searchEnableAutomaticIndexSizeManangement" in self._prop_dict:
            return self._prop_dict["searchEnableAutomaticIndexSizeManangement"]
        else:
            return None

    @search_enable_automatic_index_size_manangement.setter
    def search_enable_automatic_index_size_manangement(self, val):
        self._prop_dict["searchEnableAutomaticIndexSizeManangement"] = val

    @property
    def search_block_web_results(self):
        """
        Gets and sets the searchBlockWebResults
        
        Returns:
            bool:
                The searchBlockWebResults
        """
        if "searchBlockWebResults" in self._prop_dict:
            return self._prop_dict["searchBlockWebResults"]
        else:
            return None

    @search_block_web_results.setter
    def search_block_web_results(self, val):
        self._prop_dict["searchBlockWebResults"] = val

    @property
    def security_block_azure_ad_joined_devices_auto_encryption(self):
        """
        Gets and sets the securityBlockAzureADJoinedDevicesAutoEncryption
        
        Returns:
            bool:
                The securityBlockAzureADJoinedDevicesAutoEncryption
        """
        if "securityBlockAzureADJoinedDevicesAutoEncryption" in self._prop_dict:
            return self._prop_dict["securityBlockAzureADJoinedDevicesAutoEncryption"]
        else:
            return None

    @security_block_azure_ad_joined_devices_auto_encryption.setter
    def security_block_azure_ad_joined_devices_auto_encryption(self, val):
        self._prop_dict["securityBlockAzureADJoinedDevicesAutoEncryption"] = val

    @property
    def diagnostics_data_submission_mode(self):
        """
        Gets and sets the diagnosticsDataSubmissionMode
        
        Returns: 
            :class:`DiagnosticDataSubmissionMode<onedrivesdk.model.diagnostic_data_submission_mode.DiagnosticDataSubmissionMode>`:
                The diagnosticsDataSubmissionMode
        """
        if "diagnosticsDataSubmissionMode" in self._prop_dict:
            if isinstance(self._prop_dict["diagnosticsDataSubmissionMode"], OneDriveObjectBase):
                return self._prop_dict["diagnosticsDataSubmissionMode"]
            else :
                self._prop_dict["diagnosticsDataSubmissionMode"] = DiagnosticDataSubmissionMode(self._prop_dict["diagnosticsDataSubmissionMode"])
                return self._prop_dict["diagnosticsDataSubmissionMode"]

        return None

    @diagnostics_data_submission_mode.setter
    def diagnostics_data_submission_mode(self, val):
        self._prop_dict["diagnosticsDataSubmissionMode"] = val

    @property
    def one_drive_disable_file_sync(self):
        """
        Gets and sets the oneDriveDisableFileSync
        
        Returns:
            bool:
                The oneDriveDisableFileSync
        """
        if "oneDriveDisableFileSync" in self._prop_dict:
            return self._prop_dict["oneDriveDisableFileSync"]
        else:
            return None

    @one_drive_disable_file_sync.setter
    def one_drive_disable_file_sync(self, val):
        self._prop_dict["oneDriveDisableFileSync"] = val

    @property
    def system_telemetry_proxy_server(self):
        """
        Gets and sets the systemTelemetryProxyServer
        
        Returns:
            str:
                The systemTelemetryProxyServer
        """
        if "systemTelemetryProxyServer" in self._prop_dict:
            return self._prop_dict["systemTelemetryProxyServer"]
        else:
            return None

    @system_telemetry_proxy_server.setter
    def system_telemetry_proxy_server(self, val):
        self._prop_dict["systemTelemetryProxyServer"] = val

    @property
    def ink_workspace_access(self):
        """
        Gets and sets the inkWorkspaceAccess
        
        Returns: 
            :class:`InkAccessSetting<onedrivesdk.model.ink_access_setting.InkAccessSetting>`:
                The inkWorkspaceAccess
        """
        if "inkWorkspaceAccess" in self._prop_dict:
            if isinstance(self._prop_dict["inkWorkspaceAccess"], OneDriveObjectBase):
                return self._prop_dict["inkWorkspaceAccess"]
            else :
                self._prop_dict["inkWorkspaceAccess"] = InkAccessSetting(self._prop_dict["inkWorkspaceAccess"])
                return self._prop_dict["inkWorkspaceAccess"]

        return None

    @ink_workspace_access.setter
    def ink_workspace_access(self, val):
        self._prop_dict["inkWorkspaceAccess"] = val

    @property
    def ink_workspace_block_suggested_apps(self):
        """
        Gets and sets the inkWorkspaceBlockSuggestedApps
        
        Returns:
            bool:
                The inkWorkspaceBlockSuggestedApps
        """
        if "inkWorkspaceBlockSuggestedApps" in self._prop_dict:
            return self._prop_dict["inkWorkspaceBlockSuggestedApps"]
        else:
            return None

    @ink_workspace_block_suggested_apps.setter
    def ink_workspace_block_suggested_apps(self, val):
        self._prop_dict["inkWorkspaceBlockSuggestedApps"] = val

    @property
    def smart_screen_enable_app_install_control(self):
        """
        Gets and sets the smartScreenEnableAppInstallControl
        
        Returns:
            bool:
                The smartScreenEnableAppInstallControl
        """
        if "smartScreenEnableAppInstallControl" in self._prop_dict:
            return self._prop_dict["smartScreenEnableAppInstallControl"]
        else:
            return None

    @smart_screen_enable_app_install_control.setter
    def smart_screen_enable_app_install_control(self, val):
        self._prop_dict["smartScreenEnableAppInstallControl"] = val

    @property
    def personalization_desktop_image_url(self):
        """
        Gets and sets the personalizationDesktopImageUrl
        
        Returns:
            str:
                The personalizationDesktopImageUrl
        """
        if "personalizationDesktopImageUrl" in self._prop_dict:
            return self._prop_dict["personalizationDesktopImageUrl"]
        else:
            return None

    @personalization_desktop_image_url.setter
    def personalization_desktop_image_url(self, val):
        self._prop_dict["personalizationDesktopImageUrl"] = val

    @property
    def personalization_lock_screen_image_url(self):
        """
        Gets and sets the personalizationLockScreenImageUrl
        
        Returns:
            str:
                The personalizationLockScreenImageUrl
        """
        if "personalizationLockScreenImageUrl" in self._prop_dict:
            return self._prop_dict["personalizationLockScreenImageUrl"]
        else:
            return None

    @personalization_lock_screen_image_url.setter
    def personalization_lock_screen_image_url(self, val):
        self._prop_dict["personalizationLockScreenImageUrl"] = val

    @property
    def bluetooth_allowed_services(self):
        """
        Gets and sets the bluetoothAllowedServices
        
        Returns:
            str:
                The bluetoothAllowedServices
        """
        if "bluetoothAllowedServices" in self._prop_dict:
            return self._prop_dict["bluetoothAllowedServices"]
        else:
            return None

    @bluetooth_allowed_services.setter
    def bluetooth_allowed_services(self, val):
        self._prop_dict["bluetoothAllowedServices"] = val

    @property
    def bluetooth_block_advertising(self):
        """
        Gets and sets the bluetoothBlockAdvertising
        
        Returns:
            bool:
                The bluetoothBlockAdvertising
        """
        if "bluetoothBlockAdvertising" in self._prop_dict:
            return self._prop_dict["bluetoothBlockAdvertising"]
        else:
            return None

    @bluetooth_block_advertising.setter
    def bluetooth_block_advertising(self, val):
        self._prop_dict["bluetoothBlockAdvertising"] = val

    @property
    def bluetooth_block_discoverable_mode(self):
        """
        Gets and sets the bluetoothBlockDiscoverableMode
        
        Returns:
            bool:
                The bluetoothBlockDiscoverableMode
        """
        if "bluetoothBlockDiscoverableMode" in self._prop_dict:
            return self._prop_dict["bluetoothBlockDiscoverableMode"]
        else:
            return None

    @bluetooth_block_discoverable_mode.setter
    def bluetooth_block_discoverable_mode(self, val):
        self._prop_dict["bluetoothBlockDiscoverableMode"] = val

    @property
    def bluetooth_block_pre_pairing(self):
        """
        Gets and sets the bluetoothBlockPrePairing
        
        Returns:
            bool:
                The bluetoothBlockPrePairing
        """
        if "bluetoothBlockPrePairing" in self._prop_dict:
            return self._prop_dict["bluetoothBlockPrePairing"]
        else:
            return None

    @bluetooth_block_pre_pairing.setter
    def bluetooth_block_pre_pairing(self, val):
        self._prop_dict["bluetoothBlockPrePairing"] = val

    @property
    def edge_block_autofill(self):
        """
        Gets and sets the edgeBlockAutofill
        
        Returns:
            bool:
                The edgeBlockAutofill
        """
        if "edgeBlockAutofill" in self._prop_dict:
            return self._prop_dict["edgeBlockAutofill"]
        else:
            return None

    @edge_block_autofill.setter
    def edge_block_autofill(self, val):
        self._prop_dict["edgeBlockAutofill"] = val

    @property
    def edge_blocked(self):
        """
        Gets and sets the edgeBlocked
        
        Returns:
            bool:
                The edgeBlocked
        """
        if "edgeBlocked" in self._prop_dict:
            return self._prop_dict["edgeBlocked"]
        else:
            return None

    @edge_blocked.setter
    def edge_blocked(self, val):
        self._prop_dict["edgeBlocked"] = val

    @property
    def edge_cookie_policy(self):
        """
        Gets and sets the edgeCookiePolicy
        
        Returns: 
            :class:`EdgeCookiePolicy<onedrivesdk.model.edge_cookie_policy.EdgeCookiePolicy>`:
                The edgeCookiePolicy
        """
        if "edgeCookiePolicy" in self._prop_dict:
            if isinstance(self._prop_dict["edgeCookiePolicy"], OneDriveObjectBase):
                return self._prop_dict["edgeCookiePolicy"]
            else :
                self._prop_dict["edgeCookiePolicy"] = EdgeCookiePolicy(self._prop_dict["edgeCookiePolicy"])
                return self._prop_dict["edgeCookiePolicy"]

        return None

    @edge_cookie_policy.setter
    def edge_cookie_policy(self, val):
        self._prop_dict["edgeCookiePolicy"] = val

    @property
    def edge_block_developer_tools(self):
        """
        Gets and sets the edgeBlockDeveloperTools
        
        Returns:
            bool:
                The edgeBlockDeveloperTools
        """
        if "edgeBlockDeveloperTools" in self._prop_dict:
            return self._prop_dict["edgeBlockDeveloperTools"]
        else:
            return None

    @edge_block_developer_tools.setter
    def edge_block_developer_tools(self, val):
        self._prop_dict["edgeBlockDeveloperTools"] = val

    @property
    def edge_block_sending_do_not_track_header(self):
        """
        Gets and sets the edgeBlockSendingDoNotTrackHeader
        
        Returns:
            bool:
                The edgeBlockSendingDoNotTrackHeader
        """
        if "edgeBlockSendingDoNotTrackHeader" in self._prop_dict:
            return self._prop_dict["edgeBlockSendingDoNotTrackHeader"]
        else:
            return None

    @edge_block_sending_do_not_track_header.setter
    def edge_block_sending_do_not_track_header(self, val):
        self._prop_dict["edgeBlockSendingDoNotTrackHeader"] = val

    @property
    def edge_block_extensions(self):
        """
        Gets and sets the edgeBlockExtensions
        
        Returns:
            bool:
                The edgeBlockExtensions
        """
        if "edgeBlockExtensions" in self._prop_dict:
            return self._prop_dict["edgeBlockExtensions"]
        else:
            return None

    @edge_block_extensions.setter
    def edge_block_extensions(self, val):
        self._prop_dict["edgeBlockExtensions"] = val

    @property
    def edge_block_in_private_browsing(self):
        """
        Gets and sets the edgeBlockInPrivateBrowsing
        
        Returns:
            bool:
                The edgeBlockInPrivateBrowsing
        """
        if "edgeBlockInPrivateBrowsing" in self._prop_dict:
            return self._prop_dict["edgeBlockInPrivateBrowsing"]
        else:
            return None

    @edge_block_in_private_browsing.setter
    def edge_block_in_private_browsing(self, val):
        self._prop_dict["edgeBlockInPrivateBrowsing"] = val

    @property
    def edge_block_java_script(self):
        """
        Gets and sets the edgeBlockJavaScript
        
        Returns:
            bool:
                The edgeBlockJavaScript
        """
        if "edgeBlockJavaScript" in self._prop_dict:
            return self._prop_dict["edgeBlockJavaScript"]
        else:
            return None

    @edge_block_java_script.setter
    def edge_block_java_script(self, val):
        self._prop_dict["edgeBlockJavaScript"] = val

    @property
    def edge_block_password_manager(self):
        """
        Gets and sets the edgeBlockPasswordManager
        
        Returns:
            bool:
                The edgeBlockPasswordManager
        """
        if "edgeBlockPasswordManager" in self._prop_dict:
            return self._prop_dict["edgeBlockPasswordManager"]
        else:
            return None

    @edge_block_password_manager.setter
    def edge_block_password_manager(self, val):
        self._prop_dict["edgeBlockPasswordManager"] = val

    @property
    def edge_block_address_bar_dropdown(self):
        """
        Gets and sets the edgeBlockAddressBarDropdown
        
        Returns:
            bool:
                The edgeBlockAddressBarDropdown
        """
        if "edgeBlockAddressBarDropdown" in self._prop_dict:
            return self._prop_dict["edgeBlockAddressBarDropdown"]
        else:
            return None

    @edge_block_address_bar_dropdown.setter
    def edge_block_address_bar_dropdown(self, val):
        self._prop_dict["edgeBlockAddressBarDropdown"] = val

    @property
    def edge_block_compatibility_list(self):
        """
        Gets and sets the edgeBlockCompatibilityList
        
        Returns:
            bool:
                The edgeBlockCompatibilityList
        """
        if "edgeBlockCompatibilityList" in self._prop_dict:
            return self._prop_dict["edgeBlockCompatibilityList"]
        else:
            return None

    @edge_block_compatibility_list.setter
    def edge_block_compatibility_list(self, val):
        self._prop_dict["edgeBlockCompatibilityList"] = val

    @property
    def edge_clear_browsing_data_on_exit(self):
        """
        Gets and sets the edgeClearBrowsingDataOnExit
        
        Returns:
            bool:
                The edgeClearBrowsingDataOnExit
        """
        if "edgeClearBrowsingDataOnExit" in self._prop_dict:
            return self._prop_dict["edgeClearBrowsingDataOnExit"]
        else:
            return None

    @edge_clear_browsing_data_on_exit.setter
    def edge_clear_browsing_data_on_exit(self, val):
        self._prop_dict["edgeClearBrowsingDataOnExit"] = val

    @property
    def edge_allow_start_pages_modification(self):
        """
        Gets and sets the edgeAllowStartPagesModification
        
        Returns:
            bool:
                The edgeAllowStartPagesModification
        """
        if "edgeAllowStartPagesModification" in self._prop_dict:
            return self._prop_dict["edgeAllowStartPagesModification"]
        else:
            return None

    @edge_allow_start_pages_modification.setter
    def edge_allow_start_pages_modification(self, val):
        self._prop_dict["edgeAllowStartPagesModification"] = val

    @property
    def edge_disable_first_run_page(self):
        """
        Gets and sets the edgeDisableFirstRunPage
        
        Returns:
            bool:
                The edgeDisableFirstRunPage
        """
        if "edgeDisableFirstRunPage" in self._prop_dict:
            return self._prop_dict["edgeDisableFirstRunPage"]
        else:
            return None

    @edge_disable_first_run_page.setter
    def edge_disable_first_run_page(self, val):
        self._prop_dict["edgeDisableFirstRunPage"] = val

    @property
    def edge_block_live_tile_data_collection(self):
        """
        Gets and sets the edgeBlockLiveTileDataCollection
        
        Returns:
            bool:
                The edgeBlockLiveTileDataCollection
        """
        if "edgeBlockLiveTileDataCollection" in self._prop_dict:
            return self._prop_dict["edgeBlockLiveTileDataCollection"]
        else:
            return None

    @edge_block_live_tile_data_collection.setter
    def edge_block_live_tile_data_collection(self, val):
        self._prop_dict["edgeBlockLiveTileDataCollection"] = val

    @property
    def edge_sync_favorites_with_internet_explorer(self):
        """
        Gets and sets the edgeSyncFavoritesWithInternetExplorer
        
        Returns:
            bool:
                The edgeSyncFavoritesWithInternetExplorer
        """
        if "edgeSyncFavoritesWithInternetExplorer" in self._prop_dict:
            return self._prop_dict["edgeSyncFavoritesWithInternetExplorer"]
        else:
            return None

    @edge_sync_favorites_with_internet_explorer.setter
    def edge_sync_favorites_with_internet_explorer(self, val):
        self._prop_dict["edgeSyncFavoritesWithInternetExplorer"] = val

    @property
    def edge_favorites_list_location(self):
        """
        Gets and sets the edgeFavoritesListLocation
        
        Returns:
            str:
                The edgeFavoritesListLocation
        """
        if "edgeFavoritesListLocation" in self._prop_dict:
            return self._prop_dict["edgeFavoritesListLocation"]
        else:
            return None

    @edge_favorites_list_location.setter
    def edge_favorites_list_location(self, val):
        self._prop_dict["edgeFavoritesListLocation"] = val

    @property
    def edge_block_edit_favorites(self):
        """
        Gets and sets the edgeBlockEditFavorites
        
        Returns:
            bool:
                The edgeBlockEditFavorites
        """
        if "edgeBlockEditFavorites" in self._prop_dict:
            return self._prop_dict["edgeBlockEditFavorites"]
        else:
            return None

    @edge_block_edit_favorites.setter
    def edge_block_edit_favorites(self, val):
        self._prop_dict["edgeBlockEditFavorites"] = val

    @property
    def cellular_block_data_when_roaming(self):
        """
        Gets and sets the cellularBlockDataWhenRoaming
        
        Returns:
            bool:
                The cellularBlockDataWhenRoaming
        """
        if "cellularBlockDataWhenRoaming" in self._prop_dict:
            return self._prop_dict["cellularBlockDataWhenRoaming"]
        else:
            return None

    @cellular_block_data_when_roaming.setter
    def cellular_block_data_when_roaming(self, val):
        self._prop_dict["cellularBlockDataWhenRoaming"] = val

    @property
    def cellular_block_vpn(self):
        """
        Gets and sets the cellularBlockVpn
        
        Returns:
            bool:
                The cellularBlockVpn
        """
        if "cellularBlockVpn" in self._prop_dict:
            return self._prop_dict["cellularBlockVpn"]
        else:
            return None

    @cellular_block_vpn.setter
    def cellular_block_vpn(self, val):
        self._prop_dict["cellularBlockVpn"] = val

    @property
    def cellular_block_vpn_when_roaming(self):
        """
        Gets and sets the cellularBlockVpnWhenRoaming
        
        Returns:
            bool:
                The cellularBlockVpnWhenRoaming
        """
        if "cellularBlockVpnWhenRoaming" in self._prop_dict:
            return self._prop_dict["cellularBlockVpnWhenRoaming"]
        else:
            return None

    @cellular_block_vpn_when_roaming.setter
    def cellular_block_vpn_when_roaming(self, val):
        self._prop_dict["cellularBlockVpnWhenRoaming"] = val

    @property
    def cellular_data(self):
        """
        Gets and sets the cellularData
        
        Returns: 
            :class:`ConfigurationUsage<onedrivesdk.model.configuration_usage.ConfigurationUsage>`:
                The cellularData
        """
        if "cellularData" in self._prop_dict:
            if isinstance(self._prop_dict["cellularData"], OneDriveObjectBase):
                return self._prop_dict["cellularData"]
            else :
                self._prop_dict["cellularData"] = ConfigurationUsage(self._prop_dict["cellularData"])
                return self._prop_dict["cellularData"]

        return None

    @cellular_data.setter
    def cellular_data(self, val):
        self._prop_dict["cellularData"] = val

    @property
    def defender_block_end_user_access(self):
        """
        Gets and sets the defenderBlockEndUserAccess
        
        Returns:
            bool:
                The defenderBlockEndUserAccess
        """
        if "defenderBlockEndUserAccess" in self._prop_dict:
            return self._prop_dict["defenderBlockEndUserAccess"]
        else:
            return None

    @defender_block_end_user_access.setter
    def defender_block_end_user_access(self, val):
        self._prop_dict["defenderBlockEndUserAccess"] = val

    @property
    def defender_days_before_deleting_quarantined_malware(self):
        """
        Gets and sets the defenderDaysBeforeDeletingQuarantinedMalware
        
        Returns:
            int:
                The defenderDaysBeforeDeletingQuarantinedMalware
        """
        if "defenderDaysBeforeDeletingQuarantinedMalware" in self._prop_dict:
            return self._prop_dict["defenderDaysBeforeDeletingQuarantinedMalware"]
        else:
            return None

    @defender_days_before_deleting_quarantined_malware.setter
    def defender_days_before_deleting_quarantined_malware(self, val):
        self._prop_dict["defenderDaysBeforeDeletingQuarantinedMalware"] = val

    @property
    def defender_detected_malware_actions(self):
        """
        Gets and sets the defenderDetectedMalwareActions
        
        Returns: 
            :class:`DefenderDetectedMalwareActions<onedrivesdk.model.defender_detected_malware_actions.DefenderDetectedMalwareActions>`:
                The defenderDetectedMalwareActions
        """
        if "defenderDetectedMalwareActions" in self._prop_dict:
            if isinstance(self._prop_dict["defenderDetectedMalwareActions"], OneDriveObjectBase):
                return self._prop_dict["defenderDetectedMalwareActions"]
            else :
                self._prop_dict["defenderDetectedMalwareActions"] = DefenderDetectedMalwareActions(self._prop_dict["defenderDetectedMalwareActions"])
                return self._prop_dict["defenderDetectedMalwareActions"]

        return None

    @defender_detected_malware_actions.setter
    def defender_detected_malware_actions(self, val):
        self._prop_dict["defenderDetectedMalwareActions"] = val

    @property
    def defender_system_scan_schedule(self):
        """
        Gets and sets the defenderSystemScanSchedule
        
        Returns: 
            :class:`WeeklySchedule<onedrivesdk.model.weekly_schedule.WeeklySchedule>`:
                The defenderSystemScanSchedule
        """
        if "defenderSystemScanSchedule" in self._prop_dict:
            if isinstance(self._prop_dict["defenderSystemScanSchedule"], OneDriveObjectBase):
                return self._prop_dict["defenderSystemScanSchedule"]
            else :
                self._prop_dict["defenderSystemScanSchedule"] = WeeklySchedule(self._prop_dict["defenderSystemScanSchedule"])
                return self._prop_dict["defenderSystemScanSchedule"]

        return None

    @defender_system_scan_schedule.setter
    def defender_system_scan_schedule(self, val):
        self._prop_dict["defenderSystemScanSchedule"] = val

    @property
    def defender_files_and_folders_to_exclude(self):
        """
        Gets and sets the defenderFilesAndFoldersToExclude
        
        Returns:
            str:
                The defenderFilesAndFoldersToExclude
        """
        if "defenderFilesAndFoldersToExclude" in self._prop_dict:
            return self._prop_dict["defenderFilesAndFoldersToExclude"]
        else:
            return None

    @defender_files_and_folders_to_exclude.setter
    def defender_files_and_folders_to_exclude(self, val):
        self._prop_dict["defenderFilesAndFoldersToExclude"] = val

    @property
    def defender_file_extensions_to_exclude(self):
        """
        Gets and sets the defenderFileExtensionsToExclude
        
        Returns:
            str:
                The defenderFileExtensionsToExclude
        """
        if "defenderFileExtensionsToExclude" in self._prop_dict:
            return self._prop_dict["defenderFileExtensionsToExclude"]
        else:
            return None

    @defender_file_extensions_to_exclude.setter
    def defender_file_extensions_to_exclude(self, val):
        self._prop_dict["defenderFileExtensionsToExclude"] = val

    @property
    def defender_scan_max_cpu(self):
        """
        Gets and sets the defenderScanMaxCpu
        
        Returns:
            int:
                The defenderScanMaxCpu
        """
        if "defenderScanMaxCpu" in self._prop_dict:
            return self._prop_dict["defenderScanMaxCpu"]
        else:
            return None

    @defender_scan_max_cpu.setter
    def defender_scan_max_cpu(self, val):
        self._prop_dict["defenderScanMaxCpu"] = val

    @property
    def defender_monitor_file_activity(self):
        """
        Gets and sets the defenderMonitorFileActivity
        
        Returns: 
            :class:`DefenderMonitorFileActivity<onedrivesdk.model.defender_monitor_file_activity.DefenderMonitorFileActivity>`:
                The defenderMonitorFileActivity
        """
        if "defenderMonitorFileActivity" in self._prop_dict:
            if isinstance(self._prop_dict["defenderMonitorFileActivity"], OneDriveObjectBase):
                return self._prop_dict["defenderMonitorFileActivity"]
            else :
                self._prop_dict["defenderMonitorFileActivity"] = DefenderMonitorFileActivity(self._prop_dict["defenderMonitorFileActivity"])
                return self._prop_dict["defenderMonitorFileActivity"]

        return None

    @defender_monitor_file_activity.setter
    def defender_monitor_file_activity(self, val):
        self._prop_dict["defenderMonitorFileActivity"] = val

    @property
    def defender_potentially_unwanted_app_action(self):
        """
        Gets and sets the defenderPotentiallyUnwantedAppAction
        
        Returns: 
            :class:`DefenderPotentiallyUnwantedAppAction<onedrivesdk.model.defender_potentially_unwanted_app_action.DefenderPotentiallyUnwantedAppAction>`:
                The defenderPotentiallyUnwantedAppAction
        """
        if "defenderPotentiallyUnwantedAppAction" in self._prop_dict:
            if isinstance(self._prop_dict["defenderPotentiallyUnwantedAppAction"], OneDriveObjectBase):
                return self._prop_dict["defenderPotentiallyUnwantedAppAction"]
            else :
                self._prop_dict["defenderPotentiallyUnwantedAppAction"] = DefenderPotentiallyUnwantedAppAction(self._prop_dict["defenderPotentiallyUnwantedAppAction"])
                return self._prop_dict["defenderPotentiallyUnwantedAppAction"]

        return None

    @defender_potentially_unwanted_app_action.setter
    def defender_potentially_unwanted_app_action(self, val):
        self._prop_dict["defenderPotentiallyUnwantedAppAction"] = val

    @property
    def defender_processes_to_exclude(self):
        """
        Gets and sets the defenderProcessesToExclude
        
        Returns:
            str:
                The defenderProcessesToExclude
        """
        if "defenderProcessesToExclude" in self._prop_dict:
            return self._prop_dict["defenderProcessesToExclude"]
        else:
            return None

    @defender_processes_to_exclude.setter
    def defender_processes_to_exclude(self, val):
        self._prop_dict["defenderProcessesToExclude"] = val

    @property
    def defender_prompt_for_sample_submission(self):
        """
        Gets and sets the defenderPromptForSampleSubmission
        
        Returns: 
            :class:`DefenderPromptForSampleSubmission<onedrivesdk.model.defender_prompt_for_sample_submission.DefenderPromptForSampleSubmission>`:
                The defenderPromptForSampleSubmission
        """
        if "defenderPromptForSampleSubmission" in self._prop_dict:
            if isinstance(self._prop_dict["defenderPromptForSampleSubmission"], OneDriveObjectBase):
                return self._prop_dict["defenderPromptForSampleSubmission"]
            else :
                self._prop_dict["defenderPromptForSampleSubmission"] = DefenderPromptForSampleSubmission(self._prop_dict["defenderPromptForSampleSubmission"])
                return self._prop_dict["defenderPromptForSampleSubmission"]

        return None

    @defender_prompt_for_sample_submission.setter
    def defender_prompt_for_sample_submission(self, val):
        self._prop_dict["defenderPromptForSampleSubmission"] = val

    @property
    def defender_require_behavior_monitoring(self):
        """
        Gets and sets the defenderRequireBehaviorMonitoring
        
        Returns:
            bool:
                The defenderRequireBehaviorMonitoring
        """
        if "defenderRequireBehaviorMonitoring" in self._prop_dict:
            return self._prop_dict["defenderRequireBehaviorMonitoring"]
        else:
            return None

    @defender_require_behavior_monitoring.setter
    def defender_require_behavior_monitoring(self, val):
        self._prop_dict["defenderRequireBehaviorMonitoring"] = val

    @property
    def defender_require_cloud_protection(self):
        """
        Gets and sets the defenderRequireCloudProtection
        
        Returns:
            bool:
                The defenderRequireCloudProtection
        """
        if "defenderRequireCloudProtection" in self._prop_dict:
            return self._prop_dict["defenderRequireCloudProtection"]
        else:
            return None

    @defender_require_cloud_protection.setter
    def defender_require_cloud_protection(self, val):
        self._prop_dict["defenderRequireCloudProtection"] = val

    @property
    def defender_require_network_inspection_system(self):
        """
        Gets and sets the defenderRequireNetworkInspectionSystem
        
        Returns:
            bool:
                The defenderRequireNetworkInspectionSystem
        """
        if "defenderRequireNetworkInspectionSystem" in self._prop_dict:
            return self._prop_dict["defenderRequireNetworkInspectionSystem"]
        else:
            return None

    @defender_require_network_inspection_system.setter
    def defender_require_network_inspection_system(self, val):
        self._prop_dict["defenderRequireNetworkInspectionSystem"] = val

    @property
    def defender_require_real_time_monitoring(self):
        """
        Gets and sets the defenderRequireRealTimeMonitoring
        
        Returns:
            bool:
                The defenderRequireRealTimeMonitoring
        """
        if "defenderRequireRealTimeMonitoring" in self._prop_dict:
            return self._prop_dict["defenderRequireRealTimeMonitoring"]
        else:
            return None

    @defender_require_real_time_monitoring.setter
    def defender_require_real_time_monitoring(self, val):
        self._prop_dict["defenderRequireRealTimeMonitoring"] = val

    @property
    def defender_scan_archive_files(self):
        """
        Gets and sets the defenderScanArchiveFiles
        
        Returns:
            bool:
                The defenderScanArchiveFiles
        """
        if "defenderScanArchiveFiles" in self._prop_dict:
            return self._prop_dict["defenderScanArchiveFiles"]
        else:
            return None

    @defender_scan_archive_files.setter
    def defender_scan_archive_files(self, val):
        self._prop_dict["defenderScanArchiveFiles"] = val

    @property
    def defender_scan_downloads(self):
        """
        Gets and sets the defenderScanDownloads
        
        Returns:
            bool:
                The defenderScanDownloads
        """
        if "defenderScanDownloads" in self._prop_dict:
            return self._prop_dict["defenderScanDownloads"]
        else:
            return None

    @defender_scan_downloads.setter
    def defender_scan_downloads(self, val):
        self._prop_dict["defenderScanDownloads"] = val

    @property
    def defender_scan_network_files(self):
        """
        Gets and sets the defenderScanNetworkFiles
        
        Returns:
            bool:
                The defenderScanNetworkFiles
        """
        if "defenderScanNetworkFiles" in self._prop_dict:
            return self._prop_dict["defenderScanNetworkFiles"]
        else:
            return None

    @defender_scan_network_files.setter
    def defender_scan_network_files(self, val):
        self._prop_dict["defenderScanNetworkFiles"] = val

    @property
    def defender_scan_incoming_mail(self):
        """
        Gets and sets the defenderScanIncomingMail
        
        Returns:
            bool:
                The defenderScanIncomingMail
        """
        if "defenderScanIncomingMail" in self._prop_dict:
            return self._prop_dict["defenderScanIncomingMail"]
        else:
            return None

    @defender_scan_incoming_mail.setter
    def defender_scan_incoming_mail(self, val):
        self._prop_dict["defenderScanIncomingMail"] = val

    @property
    def defender_scan_mapped_network_drives_during_full_scan(self):
        """
        Gets and sets the defenderScanMappedNetworkDrivesDuringFullScan
        
        Returns:
            bool:
                The defenderScanMappedNetworkDrivesDuringFullScan
        """
        if "defenderScanMappedNetworkDrivesDuringFullScan" in self._prop_dict:
            return self._prop_dict["defenderScanMappedNetworkDrivesDuringFullScan"]
        else:
            return None

    @defender_scan_mapped_network_drives_during_full_scan.setter
    def defender_scan_mapped_network_drives_during_full_scan(self, val):
        self._prop_dict["defenderScanMappedNetworkDrivesDuringFullScan"] = val

    @property
    def defender_scan_removable_drives_during_full_scan(self):
        """
        Gets and sets the defenderScanRemovableDrivesDuringFullScan
        
        Returns:
            bool:
                The defenderScanRemovableDrivesDuringFullScan
        """
        if "defenderScanRemovableDrivesDuringFullScan" in self._prop_dict:
            return self._prop_dict["defenderScanRemovableDrivesDuringFullScan"]
        else:
            return None

    @defender_scan_removable_drives_during_full_scan.setter
    def defender_scan_removable_drives_during_full_scan(self, val):
        self._prop_dict["defenderScanRemovableDrivesDuringFullScan"] = val

    @property
    def defender_scan_scripts_loaded_in_internet_explorer(self):
        """
        Gets and sets the defenderScanScriptsLoadedInInternetExplorer
        
        Returns:
            bool:
                The defenderScanScriptsLoadedInInternetExplorer
        """
        if "defenderScanScriptsLoadedInInternetExplorer" in self._prop_dict:
            return self._prop_dict["defenderScanScriptsLoadedInInternetExplorer"]
        else:
            return None

    @defender_scan_scripts_loaded_in_internet_explorer.setter
    def defender_scan_scripts_loaded_in_internet_explorer(self, val):
        self._prop_dict["defenderScanScriptsLoadedInInternetExplorer"] = val

    @property
    def defender_signature_update_interval_in_hours(self):
        """
        Gets and sets the defenderSignatureUpdateIntervalInHours
        
        Returns:
            int:
                The defenderSignatureUpdateIntervalInHours
        """
        if "defenderSignatureUpdateIntervalInHours" in self._prop_dict:
            return self._prop_dict["defenderSignatureUpdateIntervalInHours"]
        else:
            return None

    @defender_signature_update_interval_in_hours.setter
    def defender_signature_update_interval_in_hours(self, val):
        self._prop_dict["defenderSignatureUpdateIntervalInHours"] = val

    @property
    def defender_scan_type(self):
        """
        Gets and sets the defenderScanType
        
        Returns: 
            :class:`DefenderScanType<onedrivesdk.model.defender_scan_type.DefenderScanType>`:
                The defenderScanType
        """
        if "defenderScanType" in self._prop_dict:
            if isinstance(self._prop_dict["defenderScanType"], OneDriveObjectBase):
                return self._prop_dict["defenderScanType"]
            else :
                self._prop_dict["defenderScanType"] = DefenderScanType(self._prop_dict["defenderScanType"])
                return self._prop_dict["defenderScanType"]

        return None

    @defender_scan_type.setter
    def defender_scan_type(self, val):
        self._prop_dict["defenderScanType"] = val

    @property
    def defender_scheduled_scan_time(self):
        """
        Gets and sets the defenderScheduledScanTime
        
        Returns: 
            :class:`TimeOfDay<onedrivesdk.model.time_of_day.TimeOfDay>`:
                The defenderScheduledScanTime
        """
        if "defenderScheduledScanTime" in self._prop_dict:
            if isinstance(self._prop_dict["defenderScheduledScanTime"], OneDriveObjectBase):
                return self._prop_dict["defenderScheduledScanTime"]
            else :
                self._prop_dict["defenderScheduledScanTime"] = TimeOfDay(self._prop_dict["defenderScheduledScanTime"])
                return self._prop_dict["defenderScheduledScanTime"]

        return None

    @defender_scheduled_scan_time.setter
    def defender_scheduled_scan_time(self, val):
        self._prop_dict["defenderScheduledScanTime"] = val

    @property
    def defender_scheduled_quick_scan_time(self):
        """
        Gets and sets the defenderScheduledQuickScanTime
        
        Returns: 
            :class:`TimeOfDay<onedrivesdk.model.time_of_day.TimeOfDay>`:
                The defenderScheduledQuickScanTime
        """
        if "defenderScheduledQuickScanTime" in self._prop_dict:
            if isinstance(self._prop_dict["defenderScheduledQuickScanTime"], OneDriveObjectBase):
                return self._prop_dict["defenderScheduledQuickScanTime"]
            else :
                self._prop_dict["defenderScheduledQuickScanTime"] = TimeOfDay(self._prop_dict["defenderScheduledQuickScanTime"])
                return self._prop_dict["defenderScheduledQuickScanTime"]

        return None

    @defender_scheduled_quick_scan_time.setter
    def defender_scheduled_quick_scan_time(self, val):
        self._prop_dict["defenderScheduledQuickScanTime"] = val

    @property
    def defender_cloud_block_level(self):
        """
        Gets and sets the defenderCloudBlockLevel
        
        Returns: 
            :class:`DefenderCloudBlockLevelType<onedrivesdk.model.defender_cloud_block_level_type.DefenderCloudBlockLevelType>`:
                The defenderCloudBlockLevel
        """
        if "defenderCloudBlockLevel" in self._prop_dict:
            if isinstance(self._prop_dict["defenderCloudBlockLevel"], OneDriveObjectBase):
                return self._prop_dict["defenderCloudBlockLevel"]
            else :
                self._prop_dict["defenderCloudBlockLevel"] = DefenderCloudBlockLevelType(self._prop_dict["defenderCloudBlockLevel"])
                return self._prop_dict["defenderCloudBlockLevel"]

        return None

    @defender_cloud_block_level.setter
    def defender_cloud_block_level(self, val):
        self._prop_dict["defenderCloudBlockLevel"] = val

    @property
    def defender_cloud_extended_timeout(self):
        """
        Gets and sets the defenderCloudExtendedTimeout
        
        Returns:
            int:
                The defenderCloudExtendedTimeout
        """
        if "defenderCloudExtendedTimeout" in self._prop_dict:
            return self._prop_dict["defenderCloudExtendedTimeout"]
        else:
            return None

    @defender_cloud_extended_timeout.setter
    def defender_cloud_extended_timeout(self, val):
        self._prop_dict["defenderCloudExtendedTimeout"] = val

    @property
    def defender_block_on_access_protection(self):
        """
        Gets and sets the defenderBlockOnAccessProtection
        
        Returns:
            bool:
                The defenderBlockOnAccessProtection
        """
        if "defenderBlockOnAccessProtection" in self._prop_dict:
            return self._prop_dict["defenderBlockOnAccessProtection"]
        else:
            return None

    @defender_block_on_access_protection.setter
    def defender_block_on_access_protection(self, val):
        self._prop_dict["defenderBlockOnAccessProtection"] = val

    @property
    def defender_schedule_scan_day(self):
        """
        Gets and sets the defenderScheduleScanDay
        
        Returns: 
            :class:`DefenderScheduleScanDay<onedrivesdk.model.defender_schedule_scan_day.DefenderScheduleScanDay>`:
                The defenderScheduleScanDay
        """
        if "defenderScheduleScanDay" in self._prop_dict:
            if isinstance(self._prop_dict["defenderScheduleScanDay"], OneDriveObjectBase):
                return self._prop_dict["defenderScheduleScanDay"]
            else :
                self._prop_dict["defenderScheduleScanDay"] = DefenderScheduleScanDay(self._prop_dict["defenderScheduleScanDay"])
                return self._prop_dict["defenderScheduleScanDay"]

        return None

    @defender_schedule_scan_day.setter
    def defender_schedule_scan_day(self, val):
        self._prop_dict["defenderScheduleScanDay"] = val

    @property
    def defender_submit_samples_consent_type(self):
        """
        Gets and sets the defenderSubmitSamplesConsentType
        
        Returns: 
            :class:`DefenderSubmitSamplesConsentType<onedrivesdk.model.defender_submit_samples_consent_type.DefenderSubmitSamplesConsentType>`:
                The defenderSubmitSamplesConsentType
        """
        if "defenderSubmitSamplesConsentType" in self._prop_dict:
            if isinstance(self._prop_dict["defenderSubmitSamplesConsentType"], OneDriveObjectBase):
                return self._prop_dict["defenderSubmitSamplesConsentType"]
            else :
                self._prop_dict["defenderSubmitSamplesConsentType"] = DefenderSubmitSamplesConsentType(self._prop_dict["defenderSubmitSamplesConsentType"])
                return self._prop_dict["defenderSubmitSamplesConsentType"]

        return None

    @defender_submit_samples_consent_type.setter
    def defender_submit_samples_consent_type(self, val):
        self._prop_dict["defenderSubmitSamplesConsentType"] = val

    @property
    def lock_screen_allow_timeout_configuration(self):
        """
        Gets and sets the lockScreenAllowTimeoutConfiguration
        
        Returns:
            bool:
                The lockScreenAllowTimeoutConfiguration
        """
        if "lockScreenAllowTimeoutConfiguration" in self._prop_dict:
            return self._prop_dict["lockScreenAllowTimeoutConfiguration"]
        else:
            return None

    @lock_screen_allow_timeout_configuration.setter
    def lock_screen_allow_timeout_configuration(self, val):
        self._prop_dict["lockScreenAllowTimeoutConfiguration"] = val

    @property
    def lock_screen_block_action_center_notifications(self):
        """
        Gets and sets the lockScreenBlockActionCenterNotifications
        
        Returns:
            bool:
                The lockScreenBlockActionCenterNotifications
        """
        if "lockScreenBlockActionCenterNotifications" in self._prop_dict:
            return self._prop_dict["lockScreenBlockActionCenterNotifications"]
        else:
            return None

    @lock_screen_block_action_center_notifications.setter
    def lock_screen_block_action_center_notifications(self, val):
        self._prop_dict["lockScreenBlockActionCenterNotifications"] = val

    @property
    def lock_screen_block_cortana(self):
        """
        Gets and sets the lockScreenBlockCortana
        
        Returns:
            bool:
                The lockScreenBlockCortana
        """
        if "lockScreenBlockCortana" in self._prop_dict:
            return self._prop_dict["lockScreenBlockCortana"]
        else:
            return None

    @lock_screen_block_cortana.setter
    def lock_screen_block_cortana(self, val):
        self._prop_dict["lockScreenBlockCortana"] = val

    @property
    def lock_screen_block_toast_notifications(self):
        """
        Gets and sets the lockScreenBlockToastNotifications
        
        Returns:
            bool:
                The lockScreenBlockToastNotifications
        """
        if "lockScreenBlockToastNotifications" in self._prop_dict:
            return self._prop_dict["lockScreenBlockToastNotifications"]
        else:
            return None

    @lock_screen_block_toast_notifications.setter
    def lock_screen_block_toast_notifications(self, val):
        self._prop_dict["lockScreenBlockToastNotifications"] = val

    @property
    def lock_screen_timeout_in_seconds(self):
        """
        Gets and sets the lockScreenTimeoutInSeconds
        
        Returns:
            int:
                The lockScreenTimeoutInSeconds
        """
        if "lockScreenTimeoutInSeconds" in self._prop_dict:
            return self._prop_dict["lockScreenTimeoutInSeconds"]
        else:
            return None

    @lock_screen_timeout_in_seconds.setter
    def lock_screen_timeout_in_seconds(self, val):
        self._prop_dict["lockScreenTimeoutInSeconds"] = val

    @property
    def password_block_simple(self):
        """
        Gets and sets the passwordBlockSimple
        
        Returns:
            bool:
                The passwordBlockSimple
        """
        if "passwordBlockSimple" in self._prop_dict:
            return self._prop_dict["passwordBlockSimple"]
        else:
            return None

    @password_block_simple.setter
    def password_block_simple(self, val):
        self._prop_dict["passwordBlockSimple"] = val

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
    def password_minimum_character_set_count(self):
        """
        Gets and sets the passwordMinimumCharacterSetCount
        
        Returns:
            int:
                The passwordMinimumCharacterSetCount
        """
        if "passwordMinimumCharacterSetCount" in self._prop_dict:
            return self._prop_dict["passwordMinimumCharacterSetCount"]
        else:
            return None

    @password_minimum_character_set_count.setter
    def password_minimum_character_set_count(self, val):
        self._prop_dict["passwordMinimumCharacterSetCount"] = val

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
    def password_required(self):
        """
        Gets and sets the passwordRequired
        
        Returns:
            bool:
                The passwordRequired
        """
        if "passwordRequired" in self._prop_dict:
            return self._prop_dict["passwordRequired"]
        else:
            return None

    @password_required.setter
    def password_required(self, val):
        self._prop_dict["passwordRequired"] = val

    @property
    def password_require_when_resume_from_idle_state(self):
        """
        Gets and sets the passwordRequireWhenResumeFromIdleState
        
        Returns:
            bool:
                The passwordRequireWhenResumeFromIdleState
        """
        if "passwordRequireWhenResumeFromIdleState" in self._prop_dict:
            return self._prop_dict["passwordRequireWhenResumeFromIdleState"]
        else:
            return None

    @password_require_when_resume_from_idle_state.setter
    def password_require_when_resume_from_idle_state(self, val):
        self._prop_dict["passwordRequireWhenResumeFromIdleState"] = val

    @property
    def password_required_type(self):
        """
        Gets and sets the passwordRequiredType
        
        Returns: 
            :class:`RequiredPasswordType<onedrivesdk.model.required_password_type.RequiredPasswordType>`:
                The passwordRequiredType
        """
        if "passwordRequiredType" in self._prop_dict:
            if isinstance(self._prop_dict["passwordRequiredType"], OneDriveObjectBase):
                return self._prop_dict["passwordRequiredType"]
            else :
                self._prop_dict["passwordRequiredType"] = RequiredPasswordType(self._prop_dict["passwordRequiredType"])
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
    def privacy_advertising_id(self):
        """
        Gets and sets the privacyAdvertisingId
        
        Returns: 
            :class:`StateManagementSetting<onedrivesdk.model.state_management_setting.StateManagementSetting>`:
                The privacyAdvertisingId
        """
        if "privacyAdvertisingId" in self._prop_dict:
            if isinstance(self._prop_dict["privacyAdvertisingId"], OneDriveObjectBase):
                return self._prop_dict["privacyAdvertisingId"]
            else :
                self._prop_dict["privacyAdvertisingId"] = StateManagementSetting(self._prop_dict["privacyAdvertisingId"])
                return self._prop_dict["privacyAdvertisingId"]

        return None

    @privacy_advertising_id.setter
    def privacy_advertising_id(self, val):
        self._prop_dict["privacyAdvertisingId"] = val

    @property
    def privacy_auto_accept_pairing_and_consent_prompts(self):
        """
        Gets and sets the privacyAutoAcceptPairingAndConsentPrompts
        
        Returns:
            bool:
                The privacyAutoAcceptPairingAndConsentPrompts
        """
        if "privacyAutoAcceptPairingAndConsentPrompts" in self._prop_dict:
            return self._prop_dict["privacyAutoAcceptPairingAndConsentPrompts"]
        else:
            return None

    @privacy_auto_accept_pairing_and_consent_prompts.setter
    def privacy_auto_accept_pairing_and_consent_prompts(self, val):
        self._prop_dict["privacyAutoAcceptPairingAndConsentPrompts"] = val

    @property
    def privacy_block_input_personalization(self):
        """
        Gets and sets the privacyBlockInputPersonalization
        
        Returns:
            bool:
                The privacyBlockInputPersonalization
        """
        if "privacyBlockInputPersonalization" in self._prop_dict:
            return self._prop_dict["privacyBlockInputPersonalization"]
        else:
            return None

    @privacy_block_input_personalization.setter
    def privacy_block_input_personalization(self, val):
        self._prop_dict["privacyBlockInputPersonalization"] = val

    @property
    def privacy_block_publish_user_activities(self):
        """
        Gets and sets the privacyBlockPublishUserActivities
        
        Returns:
            bool:
                The privacyBlockPublishUserActivities
        """
        if "privacyBlockPublishUserActivities" in self._prop_dict:
            return self._prop_dict["privacyBlockPublishUserActivities"]
        else:
            return None

    @privacy_block_publish_user_activities.setter
    def privacy_block_publish_user_activities(self, val):
        self._prop_dict["privacyBlockPublishUserActivities"] = val

    @property
    def privacy_block_activity_feed(self):
        """
        Gets and sets the privacyBlockActivityFeed
        
        Returns:
            bool:
                The privacyBlockActivityFeed
        """
        if "privacyBlockActivityFeed" in self._prop_dict:
            return self._prop_dict["privacyBlockActivityFeed"]
        else:
            return None

    @privacy_block_activity_feed.setter
    def privacy_block_activity_feed(self, val):
        self._prop_dict["privacyBlockActivityFeed"] = val

    @property
    def start_block_unpinning_apps_from_taskbar(self):
        """
        Gets and sets the startBlockUnpinningAppsFromTaskbar
        
        Returns:
            bool:
                The startBlockUnpinningAppsFromTaskbar
        """
        if "startBlockUnpinningAppsFromTaskbar" in self._prop_dict:
            return self._prop_dict["startBlockUnpinningAppsFromTaskbar"]
        else:
            return None

    @start_block_unpinning_apps_from_taskbar.setter
    def start_block_unpinning_apps_from_taskbar(self, val):
        self._prop_dict["startBlockUnpinningAppsFromTaskbar"] = val

    @property
    def start_menu_app_list_visibility(self):
        """
        Gets and sets the startMenuAppListVisibility
        
        Returns: 
            :class:`WindowsStartMenuAppListVisibilityType<onedrivesdk.model.windows_start_menu_app_list_visibility_type.WindowsStartMenuAppListVisibilityType>`:
                The startMenuAppListVisibility
        """
        if "startMenuAppListVisibility" in self._prop_dict:
            if isinstance(self._prop_dict["startMenuAppListVisibility"], OneDriveObjectBase):
                return self._prop_dict["startMenuAppListVisibility"]
            else :
                self._prop_dict["startMenuAppListVisibility"] = WindowsStartMenuAppListVisibilityType(self._prop_dict["startMenuAppListVisibility"])
                return self._prop_dict["startMenuAppListVisibility"]

        return None

    @start_menu_app_list_visibility.setter
    def start_menu_app_list_visibility(self, val):
        self._prop_dict["startMenuAppListVisibility"] = val

    @property
    def start_menu_hide_change_account_settings(self):
        """
        Gets and sets the startMenuHideChangeAccountSettings
        
        Returns:
            bool:
                The startMenuHideChangeAccountSettings
        """
        if "startMenuHideChangeAccountSettings" in self._prop_dict:
            return self._prop_dict["startMenuHideChangeAccountSettings"]
        else:
            return None

    @start_menu_hide_change_account_settings.setter
    def start_menu_hide_change_account_settings(self, val):
        self._prop_dict["startMenuHideChangeAccountSettings"] = val

    @property
    def start_menu_hide_frequently_used_apps(self):
        """
        Gets and sets the startMenuHideFrequentlyUsedApps
        
        Returns:
            bool:
                The startMenuHideFrequentlyUsedApps
        """
        if "startMenuHideFrequentlyUsedApps" in self._prop_dict:
            return self._prop_dict["startMenuHideFrequentlyUsedApps"]
        else:
            return None

    @start_menu_hide_frequently_used_apps.setter
    def start_menu_hide_frequently_used_apps(self, val):
        self._prop_dict["startMenuHideFrequentlyUsedApps"] = val

    @property
    def start_menu_hide_hibernate(self):
        """
        Gets and sets the startMenuHideHibernate
        
        Returns:
            bool:
                The startMenuHideHibernate
        """
        if "startMenuHideHibernate" in self._prop_dict:
            return self._prop_dict["startMenuHideHibernate"]
        else:
            return None

    @start_menu_hide_hibernate.setter
    def start_menu_hide_hibernate(self, val):
        self._prop_dict["startMenuHideHibernate"] = val

    @property
    def start_menu_hide_lock(self):
        """
        Gets and sets the startMenuHideLock
        
        Returns:
            bool:
                The startMenuHideLock
        """
        if "startMenuHideLock" in self._prop_dict:
            return self._prop_dict["startMenuHideLock"]
        else:
            return None

    @start_menu_hide_lock.setter
    def start_menu_hide_lock(self, val):
        self._prop_dict["startMenuHideLock"] = val

    @property
    def start_menu_hide_power_button(self):
        """
        Gets and sets the startMenuHidePowerButton
        
        Returns:
            bool:
                The startMenuHidePowerButton
        """
        if "startMenuHidePowerButton" in self._prop_dict:
            return self._prop_dict["startMenuHidePowerButton"]
        else:
            return None

    @start_menu_hide_power_button.setter
    def start_menu_hide_power_button(self, val):
        self._prop_dict["startMenuHidePowerButton"] = val

    @property
    def start_menu_hide_recent_jump_lists(self):
        """
        Gets and sets the startMenuHideRecentJumpLists
        
        Returns:
            bool:
                The startMenuHideRecentJumpLists
        """
        if "startMenuHideRecentJumpLists" in self._prop_dict:
            return self._prop_dict["startMenuHideRecentJumpLists"]
        else:
            return None

    @start_menu_hide_recent_jump_lists.setter
    def start_menu_hide_recent_jump_lists(self, val):
        self._prop_dict["startMenuHideRecentJumpLists"] = val

    @property
    def start_menu_hide_recently_added_apps(self):
        """
        Gets and sets the startMenuHideRecentlyAddedApps
        
        Returns:
            bool:
                The startMenuHideRecentlyAddedApps
        """
        if "startMenuHideRecentlyAddedApps" in self._prop_dict:
            return self._prop_dict["startMenuHideRecentlyAddedApps"]
        else:
            return None

    @start_menu_hide_recently_added_apps.setter
    def start_menu_hide_recently_added_apps(self, val):
        self._prop_dict["startMenuHideRecentlyAddedApps"] = val

    @property
    def start_menu_hide_restart_options(self):
        """
        Gets and sets the startMenuHideRestartOptions
        
        Returns:
            bool:
                The startMenuHideRestartOptions
        """
        if "startMenuHideRestartOptions" in self._prop_dict:
            return self._prop_dict["startMenuHideRestartOptions"]
        else:
            return None

    @start_menu_hide_restart_options.setter
    def start_menu_hide_restart_options(self, val):
        self._prop_dict["startMenuHideRestartOptions"] = val

    @property
    def start_menu_hide_shut_down(self):
        """
        Gets and sets the startMenuHideShutDown
        
        Returns:
            bool:
                The startMenuHideShutDown
        """
        if "startMenuHideShutDown" in self._prop_dict:
            return self._prop_dict["startMenuHideShutDown"]
        else:
            return None

    @start_menu_hide_shut_down.setter
    def start_menu_hide_shut_down(self, val):
        self._prop_dict["startMenuHideShutDown"] = val

    @property
    def start_menu_hide_sign_out(self):
        """
        Gets and sets the startMenuHideSignOut
        
        Returns:
            bool:
                The startMenuHideSignOut
        """
        if "startMenuHideSignOut" in self._prop_dict:
            return self._prop_dict["startMenuHideSignOut"]
        else:
            return None

    @start_menu_hide_sign_out.setter
    def start_menu_hide_sign_out(self, val):
        self._prop_dict["startMenuHideSignOut"] = val

    @property
    def start_menu_hide_sleep(self):
        """
        Gets and sets the startMenuHideSleep
        
        Returns:
            bool:
                The startMenuHideSleep
        """
        if "startMenuHideSleep" in self._prop_dict:
            return self._prop_dict["startMenuHideSleep"]
        else:
            return None

    @start_menu_hide_sleep.setter
    def start_menu_hide_sleep(self, val):
        self._prop_dict["startMenuHideSleep"] = val

    @property
    def start_menu_hide_switch_account(self):
        """
        Gets and sets the startMenuHideSwitchAccount
        
        Returns:
            bool:
                The startMenuHideSwitchAccount
        """
        if "startMenuHideSwitchAccount" in self._prop_dict:
            return self._prop_dict["startMenuHideSwitchAccount"]
        else:
            return None

    @start_menu_hide_switch_account.setter
    def start_menu_hide_switch_account(self, val):
        self._prop_dict["startMenuHideSwitchAccount"] = val

    @property
    def start_menu_hide_user_tile(self):
        """
        Gets and sets the startMenuHideUserTile
        
        Returns:
            bool:
                The startMenuHideUserTile
        """
        if "startMenuHideUserTile" in self._prop_dict:
            return self._prop_dict["startMenuHideUserTile"]
        else:
            return None

    @start_menu_hide_user_tile.setter
    def start_menu_hide_user_tile(self, val):
        self._prop_dict["startMenuHideUserTile"] = val

    @property
    def start_menu_mode(self):
        """
        Gets and sets the startMenuMode
        
        Returns: 
            :class:`WindowsStartMenuModeType<onedrivesdk.model.windows_start_menu_mode_type.WindowsStartMenuModeType>`:
                The startMenuMode
        """
        if "startMenuMode" in self._prop_dict:
            if isinstance(self._prop_dict["startMenuMode"], OneDriveObjectBase):
                return self._prop_dict["startMenuMode"]
            else :
                self._prop_dict["startMenuMode"] = WindowsStartMenuModeType(self._prop_dict["startMenuMode"])
                return self._prop_dict["startMenuMode"]

        return None

    @start_menu_mode.setter
    def start_menu_mode(self, val):
        self._prop_dict["startMenuMode"] = val

    @property
    def start_menu_pinned_folder_documents(self):
        """
        Gets and sets the startMenuPinnedFolderDocuments
        
        Returns: 
            :class:`VisibilitySetting<onedrivesdk.model.visibility_setting.VisibilitySetting>`:
                The startMenuPinnedFolderDocuments
        """
        if "startMenuPinnedFolderDocuments" in self._prop_dict:
            if isinstance(self._prop_dict["startMenuPinnedFolderDocuments"], OneDriveObjectBase):
                return self._prop_dict["startMenuPinnedFolderDocuments"]
            else :
                self._prop_dict["startMenuPinnedFolderDocuments"] = VisibilitySetting(self._prop_dict["startMenuPinnedFolderDocuments"])
                return self._prop_dict["startMenuPinnedFolderDocuments"]

        return None

    @start_menu_pinned_folder_documents.setter
    def start_menu_pinned_folder_documents(self, val):
        self._prop_dict["startMenuPinnedFolderDocuments"] = val

    @property
    def start_menu_pinned_folder_downloads(self):
        """
        Gets and sets the startMenuPinnedFolderDownloads
        
        Returns: 
            :class:`VisibilitySetting<onedrivesdk.model.visibility_setting.VisibilitySetting>`:
                The startMenuPinnedFolderDownloads
        """
        if "startMenuPinnedFolderDownloads" in self._prop_dict:
            if isinstance(self._prop_dict["startMenuPinnedFolderDownloads"], OneDriveObjectBase):
                return self._prop_dict["startMenuPinnedFolderDownloads"]
            else :
                self._prop_dict["startMenuPinnedFolderDownloads"] = VisibilitySetting(self._prop_dict["startMenuPinnedFolderDownloads"])
                return self._prop_dict["startMenuPinnedFolderDownloads"]

        return None

    @start_menu_pinned_folder_downloads.setter
    def start_menu_pinned_folder_downloads(self, val):
        self._prop_dict["startMenuPinnedFolderDownloads"] = val

    @property
    def start_menu_pinned_folder_file_explorer(self):
        """
        Gets and sets the startMenuPinnedFolderFileExplorer
        
        Returns: 
            :class:`VisibilitySetting<onedrivesdk.model.visibility_setting.VisibilitySetting>`:
                The startMenuPinnedFolderFileExplorer
        """
        if "startMenuPinnedFolderFileExplorer" in self._prop_dict:
            if isinstance(self._prop_dict["startMenuPinnedFolderFileExplorer"], OneDriveObjectBase):
                return self._prop_dict["startMenuPinnedFolderFileExplorer"]
            else :
                self._prop_dict["startMenuPinnedFolderFileExplorer"] = VisibilitySetting(self._prop_dict["startMenuPinnedFolderFileExplorer"])
                return self._prop_dict["startMenuPinnedFolderFileExplorer"]

        return None

    @start_menu_pinned_folder_file_explorer.setter
    def start_menu_pinned_folder_file_explorer(self, val):
        self._prop_dict["startMenuPinnedFolderFileExplorer"] = val

    @property
    def start_menu_pinned_folder_home_group(self):
        """
        Gets and sets the startMenuPinnedFolderHomeGroup
        
        Returns: 
            :class:`VisibilitySetting<onedrivesdk.model.visibility_setting.VisibilitySetting>`:
                The startMenuPinnedFolderHomeGroup
        """
        if "startMenuPinnedFolderHomeGroup" in self._prop_dict:
            if isinstance(self._prop_dict["startMenuPinnedFolderHomeGroup"], OneDriveObjectBase):
                return self._prop_dict["startMenuPinnedFolderHomeGroup"]
            else :
                self._prop_dict["startMenuPinnedFolderHomeGroup"] = VisibilitySetting(self._prop_dict["startMenuPinnedFolderHomeGroup"])
                return self._prop_dict["startMenuPinnedFolderHomeGroup"]

        return None

    @start_menu_pinned_folder_home_group.setter
    def start_menu_pinned_folder_home_group(self, val):
        self._prop_dict["startMenuPinnedFolderHomeGroup"] = val

    @property
    def start_menu_pinned_folder_music(self):
        """
        Gets and sets the startMenuPinnedFolderMusic
        
        Returns: 
            :class:`VisibilitySetting<onedrivesdk.model.visibility_setting.VisibilitySetting>`:
                The startMenuPinnedFolderMusic
        """
        if "startMenuPinnedFolderMusic" in self._prop_dict:
            if isinstance(self._prop_dict["startMenuPinnedFolderMusic"], OneDriveObjectBase):
                return self._prop_dict["startMenuPinnedFolderMusic"]
            else :
                self._prop_dict["startMenuPinnedFolderMusic"] = VisibilitySetting(self._prop_dict["startMenuPinnedFolderMusic"])
                return self._prop_dict["startMenuPinnedFolderMusic"]

        return None

    @start_menu_pinned_folder_music.setter
    def start_menu_pinned_folder_music(self, val):
        self._prop_dict["startMenuPinnedFolderMusic"] = val

    @property
    def start_menu_pinned_folder_network(self):
        """
        Gets and sets the startMenuPinnedFolderNetwork
        
        Returns: 
            :class:`VisibilitySetting<onedrivesdk.model.visibility_setting.VisibilitySetting>`:
                The startMenuPinnedFolderNetwork
        """
        if "startMenuPinnedFolderNetwork" in self._prop_dict:
            if isinstance(self._prop_dict["startMenuPinnedFolderNetwork"], OneDriveObjectBase):
                return self._prop_dict["startMenuPinnedFolderNetwork"]
            else :
                self._prop_dict["startMenuPinnedFolderNetwork"] = VisibilitySetting(self._prop_dict["startMenuPinnedFolderNetwork"])
                return self._prop_dict["startMenuPinnedFolderNetwork"]

        return None

    @start_menu_pinned_folder_network.setter
    def start_menu_pinned_folder_network(self, val):
        self._prop_dict["startMenuPinnedFolderNetwork"] = val

    @property
    def start_menu_pinned_folder_personal_folder(self):
        """
        Gets and sets the startMenuPinnedFolderPersonalFolder
        
        Returns: 
            :class:`VisibilitySetting<onedrivesdk.model.visibility_setting.VisibilitySetting>`:
                The startMenuPinnedFolderPersonalFolder
        """
        if "startMenuPinnedFolderPersonalFolder" in self._prop_dict:
            if isinstance(self._prop_dict["startMenuPinnedFolderPersonalFolder"], OneDriveObjectBase):
                return self._prop_dict["startMenuPinnedFolderPersonalFolder"]
            else :
                self._prop_dict["startMenuPinnedFolderPersonalFolder"] = VisibilitySetting(self._prop_dict["startMenuPinnedFolderPersonalFolder"])
                return self._prop_dict["startMenuPinnedFolderPersonalFolder"]

        return None

    @start_menu_pinned_folder_personal_folder.setter
    def start_menu_pinned_folder_personal_folder(self, val):
        self._prop_dict["startMenuPinnedFolderPersonalFolder"] = val

    @property
    def start_menu_pinned_folder_pictures(self):
        """
        Gets and sets the startMenuPinnedFolderPictures
        
        Returns: 
            :class:`VisibilitySetting<onedrivesdk.model.visibility_setting.VisibilitySetting>`:
                The startMenuPinnedFolderPictures
        """
        if "startMenuPinnedFolderPictures" in self._prop_dict:
            if isinstance(self._prop_dict["startMenuPinnedFolderPictures"], OneDriveObjectBase):
                return self._prop_dict["startMenuPinnedFolderPictures"]
            else :
                self._prop_dict["startMenuPinnedFolderPictures"] = VisibilitySetting(self._prop_dict["startMenuPinnedFolderPictures"])
                return self._prop_dict["startMenuPinnedFolderPictures"]

        return None

    @start_menu_pinned_folder_pictures.setter
    def start_menu_pinned_folder_pictures(self, val):
        self._prop_dict["startMenuPinnedFolderPictures"] = val

    @property
    def start_menu_pinned_folder_settings(self):
        """
        Gets and sets the startMenuPinnedFolderSettings
        
        Returns: 
            :class:`VisibilitySetting<onedrivesdk.model.visibility_setting.VisibilitySetting>`:
                The startMenuPinnedFolderSettings
        """
        if "startMenuPinnedFolderSettings" in self._prop_dict:
            if isinstance(self._prop_dict["startMenuPinnedFolderSettings"], OneDriveObjectBase):
                return self._prop_dict["startMenuPinnedFolderSettings"]
            else :
                self._prop_dict["startMenuPinnedFolderSettings"] = VisibilitySetting(self._prop_dict["startMenuPinnedFolderSettings"])
                return self._prop_dict["startMenuPinnedFolderSettings"]

        return None

    @start_menu_pinned_folder_settings.setter
    def start_menu_pinned_folder_settings(self, val):
        self._prop_dict["startMenuPinnedFolderSettings"] = val

    @property
    def start_menu_pinned_folder_videos(self):
        """
        Gets and sets the startMenuPinnedFolderVideos
        
        Returns: 
            :class:`VisibilitySetting<onedrivesdk.model.visibility_setting.VisibilitySetting>`:
                The startMenuPinnedFolderVideos
        """
        if "startMenuPinnedFolderVideos" in self._prop_dict:
            if isinstance(self._prop_dict["startMenuPinnedFolderVideos"], OneDriveObjectBase):
                return self._prop_dict["startMenuPinnedFolderVideos"]
            else :
                self._prop_dict["startMenuPinnedFolderVideos"] = VisibilitySetting(self._prop_dict["startMenuPinnedFolderVideos"])
                return self._prop_dict["startMenuPinnedFolderVideos"]

        return None

    @start_menu_pinned_folder_videos.setter
    def start_menu_pinned_folder_videos(self, val):
        self._prop_dict["startMenuPinnedFolderVideos"] = val

    @property
    def settings_block_settings_app(self):
        """
        Gets and sets the settingsBlockSettingsApp
        
        Returns:
            bool:
                The settingsBlockSettingsApp
        """
        if "settingsBlockSettingsApp" in self._prop_dict:
            return self._prop_dict["settingsBlockSettingsApp"]
        else:
            return None

    @settings_block_settings_app.setter
    def settings_block_settings_app(self, val):
        self._prop_dict["settingsBlockSettingsApp"] = val

    @property
    def settings_block_system_page(self):
        """
        Gets and sets the settingsBlockSystemPage
        
        Returns:
            bool:
                The settingsBlockSystemPage
        """
        if "settingsBlockSystemPage" in self._prop_dict:
            return self._prop_dict["settingsBlockSystemPage"]
        else:
            return None

    @settings_block_system_page.setter
    def settings_block_system_page(self, val):
        self._prop_dict["settingsBlockSystemPage"] = val

    @property
    def settings_block_devices_page(self):
        """
        Gets and sets the settingsBlockDevicesPage
        
        Returns:
            bool:
                The settingsBlockDevicesPage
        """
        if "settingsBlockDevicesPage" in self._prop_dict:
            return self._prop_dict["settingsBlockDevicesPage"]
        else:
            return None

    @settings_block_devices_page.setter
    def settings_block_devices_page(self, val):
        self._prop_dict["settingsBlockDevicesPage"] = val

    @property
    def settings_block_network_internet_page(self):
        """
        Gets and sets the settingsBlockNetworkInternetPage
        
        Returns:
            bool:
                The settingsBlockNetworkInternetPage
        """
        if "settingsBlockNetworkInternetPage" in self._prop_dict:
            return self._prop_dict["settingsBlockNetworkInternetPage"]
        else:
            return None

    @settings_block_network_internet_page.setter
    def settings_block_network_internet_page(self, val):
        self._prop_dict["settingsBlockNetworkInternetPage"] = val

    @property
    def settings_block_personalization_page(self):
        """
        Gets and sets the settingsBlockPersonalizationPage
        
        Returns:
            bool:
                The settingsBlockPersonalizationPage
        """
        if "settingsBlockPersonalizationPage" in self._prop_dict:
            return self._prop_dict["settingsBlockPersonalizationPage"]
        else:
            return None

    @settings_block_personalization_page.setter
    def settings_block_personalization_page(self, val):
        self._prop_dict["settingsBlockPersonalizationPage"] = val

    @property
    def settings_block_accounts_page(self):
        """
        Gets and sets the settingsBlockAccountsPage
        
        Returns:
            bool:
                The settingsBlockAccountsPage
        """
        if "settingsBlockAccountsPage" in self._prop_dict:
            return self._prop_dict["settingsBlockAccountsPage"]
        else:
            return None

    @settings_block_accounts_page.setter
    def settings_block_accounts_page(self, val):
        self._prop_dict["settingsBlockAccountsPage"] = val

    @property
    def settings_block_time_language_page(self):
        """
        Gets and sets the settingsBlockTimeLanguagePage
        
        Returns:
            bool:
                The settingsBlockTimeLanguagePage
        """
        if "settingsBlockTimeLanguagePage" in self._prop_dict:
            return self._prop_dict["settingsBlockTimeLanguagePage"]
        else:
            return None

    @settings_block_time_language_page.setter
    def settings_block_time_language_page(self, val):
        self._prop_dict["settingsBlockTimeLanguagePage"] = val

    @property
    def settings_block_ease_of_access_page(self):
        """
        Gets and sets the settingsBlockEaseOfAccessPage
        
        Returns:
            bool:
                The settingsBlockEaseOfAccessPage
        """
        if "settingsBlockEaseOfAccessPage" in self._prop_dict:
            return self._prop_dict["settingsBlockEaseOfAccessPage"]
        else:
            return None

    @settings_block_ease_of_access_page.setter
    def settings_block_ease_of_access_page(self, val):
        self._prop_dict["settingsBlockEaseOfAccessPage"] = val

    @property
    def settings_block_privacy_page(self):
        """
        Gets and sets the settingsBlockPrivacyPage
        
        Returns:
            bool:
                The settingsBlockPrivacyPage
        """
        if "settingsBlockPrivacyPage" in self._prop_dict:
            return self._prop_dict["settingsBlockPrivacyPage"]
        else:
            return None

    @settings_block_privacy_page.setter
    def settings_block_privacy_page(self, val):
        self._prop_dict["settingsBlockPrivacyPage"] = val

    @property
    def settings_block_update_security_page(self):
        """
        Gets and sets the settingsBlockUpdateSecurityPage
        
        Returns:
            bool:
                The settingsBlockUpdateSecurityPage
        """
        if "settingsBlockUpdateSecurityPage" in self._prop_dict:
            return self._prop_dict["settingsBlockUpdateSecurityPage"]
        else:
            return None

    @settings_block_update_security_page.setter
    def settings_block_update_security_page(self, val):
        self._prop_dict["settingsBlockUpdateSecurityPage"] = val

    @property
    def settings_block_apps_page(self):
        """
        Gets and sets the settingsBlockAppsPage
        
        Returns:
            bool:
                The settingsBlockAppsPage
        """
        if "settingsBlockAppsPage" in self._prop_dict:
            return self._prop_dict["settingsBlockAppsPage"]
        else:
            return None

    @settings_block_apps_page.setter
    def settings_block_apps_page(self, val):
        self._prop_dict["settingsBlockAppsPage"] = val

    @property
    def settings_block_gaming_page(self):
        """
        Gets and sets the settingsBlockGamingPage
        
        Returns:
            bool:
                The settingsBlockGamingPage
        """
        if "settingsBlockGamingPage" in self._prop_dict:
            return self._prop_dict["settingsBlockGamingPage"]
        else:
            return None

    @settings_block_gaming_page.setter
    def settings_block_gaming_page(self, val):
        self._prop_dict["settingsBlockGamingPage"] = val

    @property
    def windows_spotlight_block_consumer_specific_features(self):
        """
        Gets and sets the windowsSpotlightBlockConsumerSpecificFeatures
        
        Returns:
            bool:
                The windowsSpotlightBlockConsumerSpecificFeatures
        """
        if "windowsSpotlightBlockConsumerSpecificFeatures" in self._prop_dict:
            return self._prop_dict["windowsSpotlightBlockConsumerSpecificFeatures"]
        else:
            return None

    @windows_spotlight_block_consumer_specific_features.setter
    def windows_spotlight_block_consumer_specific_features(self, val):
        self._prop_dict["windowsSpotlightBlockConsumerSpecificFeatures"] = val

    @property
    def windows_spotlight_blocked(self):
        """
        Gets and sets the windowsSpotlightBlocked
        
        Returns:
            bool:
                The windowsSpotlightBlocked
        """
        if "windowsSpotlightBlocked" in self._prop_dict:
            return self._prop_dict["windowsSpotlightBlocked"]
        else:
            return None

    @windows_spotlight_blocked.setter
    def windows_spotlight_blocked(self, val):
        self._prop_dict["windowsSpotlightBlocked"] = val

    @property
    def windows_spotlight_block_on_action_center(self):
        """
        Gets and sets the windowsSpotlightBlockOnActionCenter
        
        Returns:
            bool:
                The windowsSpotlightBlockOnActionCenter
        """
        if "windowsSpotlightBlockOnActionCenter" in self._prop_dict:
            return self._prop_dict["windowsSpotlightBlockOnActionCenter"]
        else:
            return None

    @windows_spotlight_block_on_action_center.setter
    def windows_spotlight_block_on_action_center(self, val):
        self._prop_dict["windowsSpotlightBlockOnActionCenter"] = val

    @property
    def windows_spotlight_block_tailored_experiences(self):
        """
        Gets and sets the windowsSpotlightBlockTailoredExperiences
        
        Returns:
            bool:
                The windowsSpotlightBlockTailoredExperiences
        """
        if "windowsSpotlightBlockTailoredExperiences" in self._prop_dict:
            return self._prop_dict["windowsSpotlightBlockTailoredExperiences"]
        else:
            return None

    @windows_spotlight_block_tailored_experiences.setter
    def windows_spotlight_block_tailored_experiences(self, val):
        self._prop_dict["windowsSpotlightBlockTailoredExperiences"] = val

    @property
    def windows_spotlight_block_third_party_notifications(self):
        """
        Gets and sets the windowsSpotlightBlockThirdPartyNotifications
        
        Returns:
            bool:
                The windowsSpotlightBlockThirdPartyNotifications
        """
        if "windowsSpotlightBlockThirdPartyNotifications" in self._prop_dict:
            return self._prop_dict["windowsSpotlightBlockThirdPartyNotifications"]
        else:
            return None

    @windows_spotlight_block_third_party_notifications.setter
    def windows_spotlight_block_third_party_notifications(self, val):
        self._prop_dict["windowsSpotlightBlockThirdPartyNotifications"] = val

    @property
    def windows_spotlight_block_welcome_experience(self):
        """
        Gets and sets the windowsSpotlightBlockWelcomeExperience
        
        Returns:
            bool:
                The windowsSpotlightBlockWelcomeExperience
        """
        if "windowsSpotlightBlockWelcomeExperience" in self._prop_dict:
            return self._prop_dict["windowsSpotlightBlockWelcomeExperience"]
        else:
            return None

    @windows_spotlight_block_welcome_experience.setter
    def windows_spotlight_block_welcome_experience(self, val):
        self._prop_dict["windowsSpotlightBlockWelcomeExperience"] = val

    @property
    def windows_spotlight_block_windows_tips(self):
        """
        Gets and sets the windowsSpotlightBlockWindowsTips
        
        Returns:
            bool:
                The windowsSpotlightBlockWindowsTips
        """
        if "windowsSpotlightBlockWindowsTips" in self._prop_dict:
            return self._prop_dict["windowsSpotlightBlockWindowsTips"]
        else:
            return None

    @windows_spotlight_block_windows_tips.setter
    def windows_spotlight_block_windows_tips(self, val):
        self._prop_dict["windowsSpotlightBlockWindowsTips"] = val

    @property
    def windows_spotlight_configure_on_lock_screen(self):
        """
        Gets and sets the windowsSpotlightConfigureOnLockScreen
        
        Returns: 
            :class:`WindowsSpotlightEnablementSettings<onedrivesdk.model.windows_spotlight_enablement_settings.WindowsSpotlightEnablementSettings>`:
                The windowsSpotlightConfigureOnLockScreen
        """
        if "windowsSpotlightConfigureOnLockScreen" in self._prop_dict:
            if isinstance(self._prop_dict["windowsSpotlightConfigureOnLockScreen"], OneDriveObjectBase):
                return self._prop_dict["windowsSpotlightConfigureOnLockScreen"]
            else :
                self._prop_dict["windowsSpotlightConfigureOnLockScreen"] = WindowsSpotlightEnablementSettings(self._prop_dict["windowsSpotlightConfigureOnLockScreen"])
                return self._prop_dict["windowsSpotlightConfigureOnLockScreen"]

        return None

    @windows_spotlight_configure_on_lock_screen.setter
    def windows_spotlight_configure_on_lock_screen(self, val):
        self._prop_dict["windowsSpotlightConfigureOnLockScreen"] = val

    @property
    def network_proxy_apply_settings_device_wide(self):
        """
        Gets and sets the networkProxyApplySettingsDeviceWide
        
        Returns:
            bool:
                The networkProxyApplySettingsDeviceWide
        """
        if "networkProxyApplySettingsDeviceWide" in self._prop_dict:
            return self._prop_dict["networkProxyApplySettingsDeviceWide"]
        else:
            return None

    @network_proxy_apply_settings_device_wide.setter
    def network_proxy_apply_settings_device_wide(self, val):
        self._prop_dict["networkProxyApplySettingsDeviceWide"] = val

    @property
    def network_proxy_disable_auto_detect(self):
        """
        Gets and sets the networkProxyDisableAutoDetect
        
        Returns:
            bool:
                The networkProxyDisableAutoDetect
        """
        if "networkProxyDisableAutoDetect" in self._prop_dict:
            return self._prop_dict["networkProxyDisableAutoDetect"]
        else:
            return None

    @network_proxy_disable_auto_detect.setter
    def network_proxy_disable_auto_detect(self, val):
        self._prop_dict["networkProxyDisableAutoDetect"] = val

    @property
    def network_proxy_automatic_configuration_url(self):
        """
        Gets and sets the networkProxyAutomaticConfigurationUrl
        
        Returns:
            str:
                The networkProxyAutomaticConfigurationUrl
        """
        if "networkProxyAutomaticConfigurationUrl" in self._prop_dict:
            return self._prop_dict["networkProxyAutomaticConfigurationUrl"]
        else:
            return None

    @network_proxy_automatic_configuration_url.setter
    def network_proxy_automatic_configuration_url(self, val):
        self._prop_dict["networkProxyAutomaticConfigurationUrl"] = val

    @property
    def network_proxy_server(self):
        """
        Gets and sets the networkProxyServer
        
        Returns: 
            :class:`Windows10NetworkProxyServer<onedrivesdk.model.windows10_network_proxy_server.Windows10NetworkProxyServer>`:
                The networkProxyServer
        """
        if "networkProxyServer" in self._prop_dict:
            if isinstance(self._prop_dict["networkProxyServer"], OneDriveObjectBase):
                return self._prop_dict["networkProxyServer"]
            else :
                self._prop_dict["networkProxyServer"] = Windows10NetworkProxyServer(self._prop_dict["networkProxyServer"])
                return self._prop_dict["networkProxyServer"]

        return None

    @network_proxy_server.setter
    def network_proxy_server(self, val):
        self._prop_dict["networkProxyServer"] = val

    @property
    def accounts_block_adding_non_microsoft_account_email(self):
        """
        Gets and sets the accountsBlockAddingNonMicrosoftAccountEmail
        
        Returns:
            bool:
                The accountsBlockAddingNonMicrosoftAccountEmail
        """
        if "accountsBlockAddingNonMicrosoftAccountEmail" in self._prop_dict:
            return self._prop_dict["accountsBlockAddingNonMicrosoftAccountEmail"]
        else:
            return None

    @accounts_block_adding_non_microsoft_account_email.setter
    def accounts_block_adding_non_microsoft_account_email(self, val):
        self._prop_dict["accountsBlockAddingNonMicrosoftAccountEmail"] = val

    @property
    def anti_theft_mode_blocked(self):
        """
        Gets and sets the antiTheftModeBlocked
        
        Returns:
            bool:
                The antiTheftModeBlocked
        """
        if "antiTheftModeBlocked" in self._prop_dict:
            return self._prop_dict["antiTheftModeBlocked"]
        else:
            return None

    @anti_theft_mode_blocked.setter
    def anti_theft_mode_blocked(self, val):
        self._prop_dict["antiTheftModeBlocked"] = val

    @property
    def bluetooth_blocked(self):
        """
        Gets and sets the bluetoothBlocked
        
        Returns:
            bool:
                The bluetoothBlocked
        """
        if "bluetoothBlocked" in self._prop_dict:
            return self._prop_dict["bluetoothBlocked"]
        else:
            return None

    @bluetooth_blocked.setter
    def bluetooth_blocked(self, val):
        self._prop_dict["bluetoothBlocked"] = val

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
    def connected_devices_service_blocked(self):
        """
        Gets and sets the connectedDevicesServiceBlocked
        
        Returns:
            bool:
                The connectedDevicesServiceBlocked
        """
        if "connectedDevicesServiceBlocked" in self._prop_dict:
            return self._prop_dict["connectedDevicesServiceBlocked"]
        else:
            return None

    @connected_devices_service_blocked.setter
    def connected_devices_service_blocked(self, val):
        self._prop_dict["connectedDevicesServiceBlocked"] = val

    @property
    def certificates_block_manual_root_certificate_installation(self):
        """
        Gets and sets the certificatesBlockManualRootCertificateInstallation
        
        Returns:
            bool:
                The certificatesBlockManualRootCertificateInstallation
        """
        if "certificatesBlockManualRootCertificateInstallation" in self._prop_dict:
            return self._prop_dict["certificatesBlockManualRootCertificateInstallation"]
        else:
            return None

    @certificates_block_manual_root_certificate_installation.setter
    def certificates_block_manual_root_certificate_installation(self, val):
        self._prop_dict["certificatesBlockManualRootCertificateInstallation"] = val

    @property
    def copy_paste_blocked(self):
        """
        Gets and sets the copyPasteBlocked
        
        Returns:
            bool:
                The copyPasteBlocked
        """
        if "copyPasteBlocked" in self._prop_dict:
            return self._prop_dict["copyPasteBlocked"]
        else:
            return None

    @copy_paste_blocked.setter
    def copy_paste_blocked(self, val):
        self._prop_dict["copyPasteBlocked"] = val

    @property
    def cortana_blocked(self):
        """
        Gets and sets the cortanaBlocked
        
        Returns:
            bool:
                The cortanaBlocked
        """
        if "cortanaBlocked" in self._prop_dict:
            return self._prop_dict["cortanaBlocked"]
        else:
            return None

    @cortana_blocked.setter
    def cortana_blocked(self, val):
        self._prop_dict["cortanaBlocked"] = val

    @property
    def device_management_block_factory_reset_on_mobile(self):
        """
        Gets and sets the deviceManagementBlockFactoryResetOnMobile
        
        Returns:
            bool:
                The deviceManagementBlockFactoryResetOnMobile
        """
        if "deviceManagementBlockFactoryResetOnMobile" in self._prop_dict:
            return self._prop_dict["deviceManagementBlockFactoryResetOnMobile"]
        else:
            return None

    @device_management_block_factory_reset_on_mobile.setter
    def device_management_block_factory_reset_on_mobile(self, val):
        self._prop_dict["deviceManagementBlockFactoryResetOnMobile"] = val

    @property
    def device_management_block_manual_unenroll(self):
        """
        Gets and sets the deviceManagementBlockManualUnenroll
        
        Returns:
            bool:
                The deviceManagementBlockManualUnenroll
        """
        if "deviceManagementBlockManualUnenroll" in self._prop_dict:
            return self._prop_dict["deviceManagementBlockManualUnenroll"]
        else:
            return None

    @device_management_block_manual_unenroll.setter
    def device_management_block_manual_unenroll(self, val):
        self._prop_dict["deviceManagementBlockManualUnenroll"] = val

    @property
    def safe_search_filter(self):
        """
        Gets and sets the safeSearchFilter
        
        Returns: 
            :class:`SafeSearchFilterType<onedrivesdk.model.safe_search_filter_type.SafeSearchFilterType>`:
                The safeSearchFilter
        """
        if "safeSearchFilter" in self._prop_dict:
            if isinstance(self._prop_dict["safeSearchFilter"], OneDriveObjectBase):
                return self._prop_dict["safeSearchFilter"]
            else :
                self._prop_dict["safeSearchFilter"] = SafeSearchFilterType(self._prop_dict["safeSearchFilter"])
                return self._prop_dict["safeSearchFilter"]

        return None

    @safe_search_filter.setter
    def safe_search_filter(self, val):
        self._prop_dict["safeSearchFilter"] = val

    @property
    def edge_block_popups(self):
        """
        Gets and sets the edgeBlockPopups
        
        Returns:
            bool:
                The edgeBlockPopups
        """
        if "edgeBlockPopups" in self._prop_dict:
            return self._prop_dict["edgeBlockPopups"]
        else:
            return None

    @edge_block_popups.setter
    def edge_block_popups(self, val):
        self._prop_dict["edgeBlockPopups"] = val

    @property
    def edge_block_search_suggestions(self):
        """
        Gets and sets the edgeBlockSearchSuggestions
        
        Returns:
            bool:
                The edgeBlockSearchSuggestions
        """
        if "edgeBlockSearchSuggestions" in self._prop_dict:
            return self._prop_dict["edgeBlockSearchSuggestions"]
        else:
            return None

    @edge_block_search_suggestions.setter
    def edge_block_search_suggestions(self, val):
        self._prop_dict["edgeBlockSearchSuggestions"] = val

    @property
    def edge_block_sending_intranet_traffic_to_internet_explorer(self):
        """
        Gets and sets the edgeBlockSendingIntranetTrafficToInternetExplorer
        
        Returns:
            bool:
                The edgeBlockSendingIntranetTrafficToInternetExplorer
        """
        if "edgeBlockSendingIntranetTrafficToInternetExplorer" in self._prop_dict:
            return self._prop_dict["edgeBlockSendingIntranetTrafficToInternetExplorer"]
        else:
            return None

    @edge_block_sending_intranet_traffic_to_internet_explorer.setter
    def edge_block_sending_intranet_traffic_to_internet_explorer(self, val):
        self._prop_dict["edgeBlockSendingIntranetTrafficToInternetExplorer"] = val

    @property
    def edge_require_smart_screen(self):
        """
        Gets and sets the edgeRequireSmartScreen
        
        Returns:
            bool:
                The edgeRequireSmartScreen
        """
        if "edgeRequireSmartScreen" in self._prop_dict:
            return self._prop_dict["edgeRequireSmartScreen"]
        else:
            return None

    @edge_require_smart_screen.setter
    def edge_require_smart_screen(self, val):
        self._prop_dict["edgeRequireSmartScreen"] = val

    @property
    def edge_enterprise_mode_site_list_location(self):
        """
        Gets and sets the edgeEnterpriseModeSiteListLocation
        
        Returns:
            str:
                The edgeEnterpriseModeSiteListLocation
        """
        if "edgeEnterpriseModeSiteListLocation" in self._prop_dict:
            return self._prop_dict["edgeEnterpriseModeSiteListLocation"]
        else:
            return None

    @edge_enterprise_mode_site_list_location.setter
    def edge_enterprise_mode_site_list_location(self, val):
        self._prop_dict["edgeEnterpriseModeSiteListLocation"] = val

    @property
    def edge_first_run_url(self):
        """
        Gets and sets the edgeFirstRunUrl
        
        Returns:
            str:
                The edgeFirstRunUrl
        """
        if "edgeFirstRunUrl" in self._prop_dict:
            return self._prop_dict["edgeFirstRunUrl"]
        else:
            return None

    @edge_first_run_url.setter
    def edge_first_run_url(self, val):
        self._prop_dict["edgeFirstRunUrl"] = val

    @property
    def edge_search_engine(self):
        """
        Gets and sets the edgeSearchEngine
        
        Returns: 
            :class:`EdgeSearchEngineBase<onedrivesdk.model.edge_search_engine_base.EdgeSearchEngineBase>`:
                The edgeSearchEngine
        """
        if "edgeSearchEngine" in self._prop_dict:
            if isinstance(self._prop_dict["edgeSearchEngine"], OneDriveObjectBase):
                return self._prop_dict["edgeSearchEngine"]
            else :
                self._prop_dict["edgeSearchEngine"] = EdgeSearchEngineBase(self._prop_dict["edgeSearchEngine"])
                return self._prop_dict["edgeSearchEngine"]

        return None

    @edge_search_engine.setter
    def edge_search_engine(self, val):
        self._prop_dict["edgeSearchEngine"] = val

    @property
    def edge_homepage_urls(self):
        """
        Gets and sets the edgeHomepageUrls
        
        Returns:
            str:
                The edgeHomepageUrls
        """
        if "edgeHomepageUrls" in self._prop_dict:
            return self._prop_dict["edgeHomepageUrls"]
        else:
            return None

    @edge_homepage_urls.setter
    def edge_homepage_urls(self, val):
        self._prop_dict["edgeHomepageUrls"] = val

    @property
    def edge_block_access_to_about_flags(self):
        """
        Gets and sets the edgeBlockAccessToAboutFlags
        
        Returns:
            bool:
                The edgeBlockAccessToAboutFlags
        """
        if "edgeBlockAccessToAboutFlags" in self._prop_dict:
            return self._prop_dict["edgeBlockAccessToAboutFlags"]
        else:
            return None

    @edge_block_access_to_about_flags.setter
    def edge_block_access_to_about_flags(self, val):
        self._prop_dict["edgeBlockAccessToAboutFlags"] = val

    @property
    def smart_screen_block_prompt_override(self):
        """
        Gets and sets the smartScreenBlockPromptOverride
        
        Returns:
            bool:
                The smartScreenBlockPromptOverride
        """
        if "smartScreenBlockPromptOverride" in self._prop_dict:
            return self._prop_dict["smartScreenBlockPromptOverride"]
        else:
            return None

    @smart_screen_block_prompt_override.setter
    def smart_screen_block_prompt_override(self, val):
        self._prop_dict["smartScreenBlockPromptOverride"] = val

    @property
    def smart_screen_block_prompt_override_for_files(self):
        """
        Gets and sets the smartScreenBlockPromptOverrideForFiles
        
        Returns:
            bool:
                The smartScreenBlockPromptOverrideForFiles
        """
        if "smartScreenBlockPromptOverrideForFiles" in self._prop_dict:
            return self._prop_dict["smartScreenBlockPromptOverrideForFiles"]
        else:
            return None

    @smart_screen_block_prompt_override_for_files.setter
    def smart_screen_block_prompt_override_for_files(self, val):
        self._prop_dict["smartScreenBlockPromptOverrideForFiles"] = val

    @property
    def web_rtc_block_localhost_ip_address(self):
        """
        Gets and sets the webRtcBlockLocalhostIpAddress
        
        Returns:
            bool:
                The webRtcBlockLocalhostIpAddress
        """
        if "webRtcBlockLocalhostIpAddress" in self._prop_dict:
            return self._prop_dict["webRtcBlockLocalhostIpAddress"]
        else:
            return None

    @web_rtc_block_localhost_ip_address.setter
    def web_rtc_block_localhost_ip_address(self, val):
        self._prop_dict["webRtcBlockLocalhostIpAddress"] = val

    @property
    def internet_sharing_blocked(self):
        """
        Gets and sets the internetSharingBlocked
        
        Returns:
            bool:
                The internetSharingBlocked
        """
        if "internetSharingBlocked" in self._prop_dict:
            return self._prop_dict["internetSharingBlocked"]
        else:
            return None

    @internet_sharing_blocked.setter
    def internet_sharing_blocked(self, val):
        self._prop_dict["internetSharingBlocked"] = val

    @property
    def settings_block_add_provisioning_package(self):
        """
        Gets and sets the settingsBlockAddProvisioningPackage
        
        Returns:
            bool:
                The settingsBlockAddProvisioningPackage
        """
        if "settingsBlockAddProvisioningPackage" in self._prop_dict:
            return self._prop_dict["settingsBlockAddProvisioningPackage"]
        else:
            return None

    @settings_block_add_provisioning_package.setter
    def settings_block_add_provisioning_package(self, val):
        self._prop_dict["settingsBlockAddProvisioningPackage"] = val

    @property
    def settings_block_remove_provisioning_package(self):
        """
        Gets and sets the settingsBlockRemoveProvisioningPackage
        
        Returns:
            bool:
                The settingsBlockRemoveProvisioningPackage
        """
        if "settingsBlockRemoveProvisioningPackage" in self._prop_dict:
            return self._prop_dict["settingsBlockRemoveProvisioningPackage"]
        else:
            return None

    @settings_block_remove_provisioning_package.setter
    def settings_block_remove_provisioning_package(self, val):
        self._prop_dict["settingsBlockRemoveProvisioningPackage"] = val

    @property
    def settings_block_change_system_time(self):
        """
        Gets and sets the settingsBlockChangeSystemTime
        
        Returns:
            bool:
                The settingsBlockChangeSystemTime
        """
        if "settingsBlockChangeSystemTime" in self._prop_dict:
            return self._prop_dict["settingsBlockChangeSystemTime"]
        else:
            return None

    @settings_block_change_system_time.setter
    def settings_block_change_system_time(self, val):
        self._prop_dict["settingsBlockChangeSystemTime"] = val

    @property
    def settings_block_edit_device_name(self):
        """
        Gets and sets the settingsBlockEditDeviceName
        
        Returns:
            bool:
                The settingsBlockEditDeviceName
        """
        if "settingsBlockEditDeviceName" in self._prop_dict:
            return self._prop_dict["settingsBlockEditDeviceName"]
        else:
            return None

    @settings_block_edit_device_name.setter
    def settings_block_edit_device_name(self, val):
        self._prop_dict["settingsBlockEditDeviceName"] = val

    @property
    def settings_block_change_region(self):
        """
        Gets and sets the settingsBlockChangeRegion
        
        Returns:
            bool:
                The settingsBlockChangeRegion
        """
        if "settingsBlockChangeRegion" in self._prop_dict:
            return self._prop_dict["settingsBlockChangeRegion"]
        else:
            return None

    @settings_block_change_region.setter
    def settings_block_change_region(self, val):
        self._prop_dict["settingsBlockChangeRegion"] = val

    @property
    def settings_block_change_language(self):
        """
        Gets and sets the settingsBlockChangeLanguage
        
        Returns:
            bool:
                The settingsBlockChangeLanguage
        """
        if "settingsBlockChangeLanguage" in self._prop_dict:
            return self._prop_dict["settingsBlockChangeLanguage"]
        else:
            return None

    @settings_block_change_language.setter
    def settings_block_change_language(self, val):
        self._prop_dict["settingsBlockChangeLanguage"] = val

    @property
    def settings_block_change_power_sleep(self):
        """
        Gets and sets the settingsBlockChangePowerSleep
        
        Returns:
            bool:
                The settingsBlockChangePowerSleep
        """
        if "settingsBlockChangePowerSleep" in self._prop_dict:
            return self._prop_dict["settingsBlockChangePowerSleep"]
        else:
            return None

    @settings_block_change_power_sleep.setter
    def settings_block_change_power_sleep(self, val):
        self._prop_dict["settingsBlockChangePowerSleep"] = val

    @property
    def location_services_blocked(self):
        """
        Gets and sets the locationServicesBlocked
        
        Returns:
            bool:
                The locationServicesBlocked
        """
        if "locationServicesBlocked" in self._prop_dict:
            return self._prop_dict["locationServicesBlocked"]
        else:
            return None

    @location_services_blocked.setter
    def location_services_blocked(self, val):
        self._prop_dict["locationServicesBlocked"] = val

    @property
    def microsoft_account_blocked(self):
        """
        Gets and sets the microsoftAccountBlocked
        
        Returns:
            bool:
                The microsoftAccountBlocked
        """
        if "microsoftAccountBlocked" in self._prop_dict:
            return self._prop_dict["microsoftAccountBlocked"]
        else:
            return None

    @microsoft_account_blocked.setter
    def microsoft_account_blocked(self, val):
        self._prop_dict["microsoftAccountBlocked"] = val

    @property
    def microsoft_account_block_settings_sync(self):
        """
        Gets and sets the microsoftAccountBlockSettingsSync
        
        Returns:
            bool:
                The microsoftAccountBlockSettingsSync
        """
        if "microsoftAccountBlockSettingsSync" in self._prop_dict:
            return self._prop_dict["microsoftAccountBlockSettingsSync"]
        else:
            return None

    @microsoft_account_block_settings_sync.setter
    def microsoft_account_block_settings_sync(self, val):
        self._prop_dict["microsoftAccountBlockSettingsSync"] = val

    @property
    def nfc_blocked(self):
        """
        Gets and sets the nfcBlocked
        
        Returns:
            bool:
                The nfcBlocked
        """
        if "nfcBlocked" in self._prop_dict:
            return self._prop_dict["nfcBlocked"]
        else:
            return None

    @nfc_blocked.setter
    def nfc_blocked(self, val):
        self._prop_dict["nfcBlocked"] = val

    @property
    def reset_protection_mode_blocked(self):
        """
        Gets and sets the resetProtectionModeBlocked
        
        Returns:
            bool:
                The resetProtectionModeBlocked
        """
        if "resetProtectionModeBlocked" in self._prop_dict:
            return self._prop_dict["resetProtectionModeBlocked"]
        else:
            return None

    @reset_protection_mode_blocked.setter
    def reset_protection_mode_blocked(self, val):
        self._prop_dict["resetProtectionModeBlocked"] = val

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
    def storage_block_removable_storage(self):
        """
        Gets and sets the storageBlockRemovableStorage
        
        Returns:
            bool:
                The storageBlockRemovableStorage
        """
        if "storageBlockRemovableStorage" in self._prop_dict:
            return self._prop_dict["storageBlockRemovableStorage"]
        else:
            return None

    @storage_block_removable_storage.setter
    def storage_block_removable_storage(self, val):
        self._prop_dict["storageBlockRemovableStorage"] = val

    @property
    def storage_require_mobile_device_encryption(self):
        """
        Gets and sets the storageRequireMobileDeviceEncryption
        
        Returns:
            bool:
                The storageRequireMobileDeviceEncryption
        """
        if "storageRequireMobileDeviceEncryption" in self._prop_dict:
            return self._prop_dict["storageRequireMobileDeviceEncryption"]
        else:
            return None

    @storage_require_mobile_device_encryption.setter
    def storage_require_mobile_device_encryption(self, val):
        self._prop_dict["storageRequireMobileDeviceEncryption"] = val

    @property
    def usb_blocked(self):
        """
        Gets and sets the usbBlocked
        
        Returns:
            bool:
                The usbBlocked
        """
        if "usbBlocked" in self._prop_dict:
            return self._prop_dict["usbBlocked"]
        else:
            return None

    @usb_blocked.setter
    def usb_blocked(self, val):
        self._prop_dict["usbBlocked"] = val

    @property
    def voice_recording_blocked(self):
        """
        Gets and sets the voiceRecordingBlocked
        
        Returns:
            bool:
                The voiceRecordingBlocked
        """
        if "voiceRecordingBlocked" in self._prop_dict:
            return self._prop_dict["voiceRecordingBlocked"]
        else:
            return None

    @voice_recording_blocked.setter
    def voice_recording_blocked(self, val):
        self._prop_dict["voiceRecordingBlocked"] = val

    @property
    def wi_fi_block_automatic_connect_hotspots(self):
        """
        Gets and sets the wiFiBlockAutomaticConnectHotspots
        
        Returns:
            bool:
                The wiFiBlockAutomaticConnectHotspots
        """
        if "wiFiBlockAutomaticConnectHotspots" in self._prop_dict:
            return self._prop_dict["wiFiBlockAutomaticConnectHotspots"]
        else:
            return None

    @wi_fi_block_automatic_connect_hotspots.setter
    def wi_fi_block_automatic_connect_hotspots(self, val):
        self._prop_dict["wiFiBlockAutomaticConnectHotspots"] = val

    @property
    def wi_fi_blocked(self):
        """
        Gets and sets the wiFiBlocked
        
        Returns:
            bool:
                The wiFiBlocked
        """
        if "wiFiBlocked" in self._prop_dict:
            return self._prop_dict["wiFiBlocked"]
        else:
            return None

    @wi_fi_blocked.setter
    def wi_fi_blocked(self, val):
        self._prop_dict["wiFiBlocked"] = val

    @property
    def wi_fi_block_manual_configuration(self):
        """
        Gets and sets the wiFiBlockManualConfiguration
        
        Returns:
            bool:
                The wiFiBlockManualConfiguration
        """
        if "wiFiBlockManualConfiguration" in self._prop_dict:
            return self._prop_dict["wiFiBlockManualConfiguration"]
        else:
            return None

    @wi_fi_block_manual_configuration.setter
    def wi_fi_block_manual_configuration(self, val):
        self._prop_dict["wiFiBlockManualConfiguration"] = val

    @property
    def wi_fi_scan_interval(self):
        """
        Gets and sets the wiFiScanInterval
        
        Returns:
            int:
                The wiFiScanInterval
        """
        if "wiFiScanInterval" in self._prop_dict:
            return self._prop_dict["wiFiScanInterval"]
        else:
            return None

    @wi_fi_scan_interval.setter
    def wi_fi_scan_interval(self, val):
        self._prop_dict["wiFiScanInterval"] = val

    @property
    def wireless_display_block_projection_to_this_device(self):
        """
        Gets and sets the wirelessDisplayBlockProjectionToThisDevice
        
        Returns:
            bool:
                The wirelessDisplayBlockProjectionToThisDevice
        """
        if "wirelessDisplayBlockProjectionToThisDevice" in self._prop_dict:
            return self._prop_dict["wirelessDisplayBlockProjectionToThisDevice"]
        else:
            return None

    @wireless_display_block_projection_to_this_device.setter
    def wireless_display_block_projection_to_this_device(self, val):
        self._prop_dict["wirelessDisplayBlockProjectionToThisDevice"] = val

    @property
    def wireless_display_block_user_input_from_receiver(self):
        """
        Gets and sets the wirelessDisplayBlockUserInputFromReceiver
        
        Returns:
            bool:
                The wirelessDisplayBlockUserInputFromReceiver
        """
        if "wirelessDisplayBlockUserInputFromReceiver" in self._prop_dict:
            return self._prop_dict["wirelessDisplayBlockUserInputFromReceiver"]
        else:
            return None

    @wireless_display_block_user_input_from_receiver.setter
    def wireless_display_block_user_input_from_receiver(self, val):
        self._prop_dict["wirelessDisplayBlockUserInputFromReceiver"] = val

    @property
    def wireless_display_require_pin_for_pairing(self):
        """
        Gets and sets the wirelessDisplayRequirePinForPairing
        
        Returns:
            bool:
                The wirelessDisplayRequirePinForPairing
        """
        if "wirelessDisplayRequirePinForPairing" in self._prop_dict:
            return self._prop_dict["wirelessDisplayRequirePinForPairing"]
        else:
            return None

    @wireless_display_require_pin_for_pairing.setter
    def wireless_display_require_pin_for_pairing(self, val):
        self._prop_dict["wirelessDisplayRequirePinForPairing"] = val

    @property
    def windows_store_blocked(self):
        """
        Gets and sets the windowsStoreBlocked
        
        Returns:
            bool:
                The windowsStoreBlocked
        """
        if "windowsStoreBlocked" in self._prop_dict:
            return self._prop_dict["windowsStoreBlocked"]
        else:
            return None

    @windows_store_blocked.setter
    def windows_store_blocked(self, val):
        self._prop_dict["windowsStoreBlocked"] = val

    @property
    def apps_allow_trusted_apps_sideloading(self):
        """
        Gets and sets the appsAllowTrustedAppsSideloading
        
        Returns: 
            :class:`StateManagementSetting<onedrivesdk.model.state_management_setting.StateManagementSetting>`:
                The appsAllowTrustedAppsSideloading
        """
        if "appsAllowTrustedAppsSideloading" in self._prop_dict:
            if isinstance(self._prop_dict["appsAllowTrustedAppsSideloading"], OneDriveObjectBase):
                return self._prop_dict["appsAllowTrustedAppsSideloading"]
            else :
                self._prop_dict["appsAllowTrustedAppsSideloading"] = StateManagementSetting(self._prop_dict["appsAllowTrustedAppsSideloading"])
                return self._prop_dict["appsAllowTrustedAppsSideloading"]

        return None

    @apps_allow_trusted_apps_sideloading.setter
    def apps_allow_trusted_apps_sideloading(self, val):
        self._prop_dict["appsAllowTrustedAppsSideloading"] = val

    @property
    def windows_store_block_auto_update(self):
        """
        Gets and sets the windowsStoreBlockAutoUpdate
        
        Returns:
            bool:
                The windowsStoreBlockAutoUpdate
        """
        if "windowsStoreBlockAutoUpdate" in self._prop_dict:
            return self._prop_dict["windowsStoreBlockAutoUpdate"]
        else:
            return None

    @windows_store_block_auto_update.setter
    def windows_store_block_auto_update(self, val):
        self._prop_dict["windowsStoreBlockAutoUpdate"] = val

    @property
    def developer_unlock_setting(self):
        """
        Gets and sets the developerUnlockSetting
        
        Returns: 
            :class:`StateManagementSetting<onedrivesdk.model.state_management_setting.StateManagementSetting>`:
                The developerUnlockSetting
        """
        if "developerUnlockSetting" in self._prop_dict:
            if isinstance(self._prop_dict["developerUnlockSetting"], OneDriveObjectBase):
                return self._prop_dict["developerUnlockSetting"]
            else :
                self._prop_dict["developerUnlockSetting"] = StateManagementSetting(self._prop_dict["developerUnlockSetting"])
                return self._prop_dict["developerUnlockSetting"]

        return None

    @developer_unlock_setting.setter
    def developer_unlock_setting(self, val):
        self._prop_dict["developerUnlockSetting"] = val

    @property
    def shared_user_app_data_allowed(self):
        """
        Gets and sets the sharedUserAppDataAllowed
        
        Returns:
            bool:
                The sharedUserAppDataAllowed
        """
        if "sharedUserAppDataAllowed" in self._prop_dict:
            return self._prop_dict["sharedUserAppDataAllowed"]
        else:
            return None

    @shared_user_app_data_allowed.setter
    def shared_user_app_data_allowed(self, val):
        self._prop_dict["sharedUserAppDataAllowed"] = val

    @property
    def apps_block_windows_store_originated_apps(self):
        """
        Gets and sets the appsBlockWindowsStoreOriginatedApps
        
        Returns:
            bool:
                The appsBlockWindowsStoreOriginatedApps
        """
        if "appsBlockWindowsStoreOriginatedApps" in self._prop_dict:
            return self._prop_dict["appsBlockWindowsStoreOriginatedApps"]
        else:
            return None

    @apps_block_windows_store_originated_apps.setter
    def apps_block_windows_store_originated_apps(self, val):
        self._prop_dict["appsBlockWindowsStoreOriginatedApps"] = val

    @property
    def windows_store_enable_private_store_only(self):
        """
        Gets and sets the windowsStoreEnablePrivateStoreOnly
        
        Returns:
            bool:
                The windowsStoreEnablePrivateStoreOnly
        """
        if "windowsStoreEnablePrivateStoreOnly" in self._prop_dict:
            return self._prop_dict["windowsStoreEnablePrivateStoreOnly"]
        else:
            return None

    @windows_store_enable_private_store_only.setter
    def windows_store_enable_private_store_only(self, val):
        self._prop_dict["windowsStoreEnablePrivateStoreOnly"] = val

    @property
    def storage_restrict_app_data_to_system_volume(self):
        """
        Gets and sets the storageRestrictAppDataToSystemVolume
        
        Returns:
            bool:
                The storageRestrictAppDataToSystemVolume
        """
        if "storageRestrictAppDataToSystemVolume" in self._prop_dict:
            return self._prop_dict["storageRestrictAppDataToSystemVolume"]
        else:
            return None

    @storage_restrict_app_data_to_system_volume.setter
    def storage_restrict_app_data_to_system_volume(self, val):
        self._prop_dict["storageRestrictAppDataToSystemVolume"] = val

    @property
    def storage_restrict_app_install_to_system_volume(self):
        """
        Gets and sets the storageRestrictAppInstallToSystemVolume
        
        Returns:
            bool:
                The storageRestrictAppInstallToSystemVolume
        """
        if "storageRestrictAppInstallToSystemVolume" in self._prop_dict:
            return self._prop_dict["storageRestrictAppInstallToSystemVolume"]
        else:
            return None

    @storage_restrict_app_install_to_system_volume.setter
    def storage_restrict_app_install_to_system_volume(self, val):
        self._prop_dict["storageRestrictAppInstallToSystemVolume"] = val

    @property
    def game_dvr_blocked(self):
        """
        Gets and sets the gameDvrBlocked
        
        Returns:
            bool:
                The gameDvrBlocked
        """
        if "gameDvrBlocked" in self._prop_dict:
            return self._prop_dict["gameDvrBlocked"]
        else:
            return None

    @game_dvr_blocked.setter
    def game_dvr_blocked(self, val):
        self._prop_dict["gameDvrBlocked"] = val

    @property
    def experience_block_device_discovery(self):
        """
        Gets and sets the experienceBlockDeviceDiscovery
        
        Returns:
            bool:
                The experienceBlockDeviceDiscovery
        """
        if "experienceBlockDeviceDiscovery" in self._prop_dict:
            return self._prop_dict["experienceBlockDeviceDiscovery"]
        else:
            return None

    @experience_block_device_discovery.setter
    def experience_block_device_discovery(self, val):
        self._prop_dict["experienceBlockDeviceDiscovery"] = val

    @property
    def experience_block_error_dialog_when_no_sim(self):
        """
        Gets and sets the experienceBlockErrorDialogWhenNoSIM
        
        Returns:
            bool:
                The experienceBlockErrorDialogWhenNoSIM
        """
        if "experienceBlockErrorDialogWhenNoSIM" in self._prop_dict:
            return self._prop_dict["experienceBlockErrorDialogWhenNoSIM"]
        else:
            return None

    @experience_block_error_dialog_when_no_sim.setter
    def experience_block_error_dialog_when_no_sim(self, val):
        self._prop_dict["experienceBlockErrorDialogWhenNoSIM"] = val

    @property
    def experience_block_task_switcher(self):
        """
        Gets and sets the experienceBlockTaskSwitcher
        
        Returns:
            bool:
                The experienceBlockTaskSwitcher
        """
        if "experienceBlockTaskSwitcher" in self._prop_dict:
            return self._prop_dict["experienceBlockTaskSwitcher"]
        else:
            return None

    @experience_block_task_switcher.setter
    def experience_block_task_switcher(self, val):
        self._prop_dict["experienceBlockTaskSwitcher"] = val

    @property
    def logon_block_fast_user_switching(self):
        """
        Gets and sets the logonBlockFastUserSwitching
        
        Returns:
            bool:
                The logonBlockFastUserSwitching
        """
        if "logonBlockFastUserSwitching" in self._prop_dict:
            return self._prop_dict["logonBlockFastUserSwitching"]
        else:
            return None

    @logon_block_fast_user_switching.setter
    def logon_block_fast_user_switching(self, val):
        self._prop_dict["logonBlockFastUserSwitching"] = val

    @property
    def assigned_access_multi_mode_profiles(self):
        """Gets and sets the assignedAccessMultiModeProfiles
        
        Returns: 
            :class:`AssignedAccessMultiModeProfilesCollectionPage<onedrivesdk.request.assigned_access_multi_mode_profiles_collection.AssignedAccessMultiModeProfilesCollectionPage>`:
                The assignedAccessMultiModeProfiles
        """
        if "assignedAccessMultiModeProfiles" in self._prop_dict:
            return AssignedAccessMultiModeProfilesCollectionPage(self._prop_dict["assignedAccessMultiModeProfiles"])
        else:
            return None

    @property
    def privacy_access_controls(self):
        """Gets and sets the privacyAccessControls
        
        Returns: 
            :class:`PrivacyAccessControlsCollectionPage<onedrivesdk.request.privacy_access_controls_collection.PrivacyAccessControlsCollectionPage>`:
                The privacyAccessControls
        """
        if "privacyAccessControls" in self._prop_dict:
            return PrivacyAccessControlsCollectionPage(self._prop_dict["privacyAccessControls"])
        else:
            return None

