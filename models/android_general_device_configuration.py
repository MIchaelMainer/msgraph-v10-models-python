# -*- coding: utf-8 -*- 
'''
# Copyright (c) Microsoft Corporation.  All Rights Reserved.  Licensed under the MIT License.  See License in the project root for license information.
# 
#  This file was generated and any changes will be overwritten.
'''

from __future__ import unicode_literals
from ..model.app_list_item import AppListItem
from ..model.app_list_type import AppListType
from ..model.android_required_password_type import AndroidRequiredPasswordType
from ..model.web_browser_cookie_settings import WebBrowserCookieSettings
from ..one_drive_object_base import OneDriveObjectBase


class AndroidGeneralDeviceConfiguration(OneDriveObjectBase):

    def __init__(self, prop_dict={}):
        self._prop_dict = prop_dict

    @property
    def apps_block_clipboard_sharing(self):
        """
        Gets and sets the appsBlockClipboardSharing
        
        Returns:
            bool:
                The appsBlockClipboardSharing
        """
        if "appsBlockClipboardSharing" in self._prop_dict:
            return self._prop_dict["appsBlockClipboardSharing"]
        else:
            return None

    @apps_block_clipboard_sharing.setter
    def apps_block_clipboard_sharing(self, val):
        self._prop_dict["appsBlockClipboardSharing"] = val

    @property
    def apps_block_copy_paste(self):
        """
        Gets and sets the appsBlockCopyPaste
        
        Returns:
            bool:
                The appsBlockCopyPaste
        """
        if "appsBlockCopyPaste" in self._prop_dict:
            return self._prop_dict["appsBlockCopyPaste"]
        else:
            return None

    @apps_block_copy_paste.setter
    def apps_block_copy_paste(self, val):
        self._prop_dict["appsBlockCopyPaste"] = val

    @property
    def apps_block_you_tube(self):
        """
        Gets and sets the appsBlockYouTube
        
        Returns:
            bool:
                The appsBlockYouTube
        """
        if "appsBlockYouTube" in self._prop_dict:
            return self._prop_dict["appsBlockYouTube"]
        else:
            return None

    @apps_block_you_tube.setter
    def apps_block_you_tube(self, val):
        self._prop_dict["appsBlockYouTube"] = val

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
    def cellular_block_data_roaming(self):
        """
        Gets and sets the cellularBlockDataRoaming
        
        Returns:
            bool:
                The cellularBlockDataRoaming
        """
        if "cellularBlockDataRoaming" in self._prop_dict:
            return self._prop_dict["cellularBlockDataRoaming"]
        else:
            return None

    @cellular_block_data_roaming.setter
    def cellular_block_data_roaming(self, val):
        self._prop_dict["cellularBlockDataRoaming"] = val

    @property
    def cellular_block_messaging(self):
        """
        Gets and sets the cellularBlockMessaging
        
        Returns:
            bool:
                The cellularBlockMessaging
        """
        if "cellularBlockMessaging" in self._prop_dict:
            return self._prop_dict["cellularBlockMessaging"]
        else:
            return None

    @cellular_block_messaging.setter
    def cellular_block_messaging(self, val):
        self._prop_dict["cellularBlockMessaging"] = val

    @property
    def cellular_block_voice_roaming(self):
        """
        Gets and sets the cellularBlockVoiceRoaming
        
        Returns:
            bool:
                The cellularBlockVoiceRoaming
        """
        if "cellularBlockVoiceRoaming" in self._prop_dict:
            return self._prop_dict["cellularBlockVoiceRoaming"]
        else:
            return None

    @cellular_block_voice_roaming.setter
    def cellular_block_voice_roaming(self, val):
        self._prop_dict["cellularBlockVoiceRoaming"] = val

    @property
    def cellular_block_wi_fi_tethering(self):
        """
        Gets and sets the cellularBlockWiFiTethering
        
        Returns:
            bool:
                The cellularBlockWiFiTethering
        """
        if "cellularBlockWiFiTethering" in self._prop_dict:
            return self._prop_dict["cellularBlockWiFiTethering"]
        else:
            return None

    @cellular_block_wi_fi_tethering.setter
    def cellular_block_wi_fi_tethering(self, val):
        self._prop_dict["cellularBlockWiFiTethering"] = val

    @property
    def compliant_apps_list(self):
        """Gets and sets the compliantAppsList
        
        Returns: 
            :class:`CompliantAppsListCollectionPage<onedrivesdk.request.compliant_apps_list_collection.CompliantAppsListCollectionPage>`:
                The compliantAppsList
        """
        if "compliantAppsList" in self._prop_dict:
            return CompliantAppsListCollectionPage(self._prop_dict["compliantAppsList"])
        else:
            return None

    @property
    def compliant_app_list_type(self):
        """
        Gets and sets the compliantAppListType
        
        Returns: 
            :class:`AppListType<onedrivesdk.model.app_list_type.AppListType>`:
                The compliantAppListType
        """
        if "compliantAppListType" in self._prop_dict:
            if isinstance(self._prop_dict["compliantAppListType"], OneDriveObjectBase):
                return self._prop_dict["compliantAppListType"]
            else :
                self._prop_dict["compliantAppListType"] = AppListType(self._prop_dict["compliantAppListType"])
                return self._prop_dict["compliantAppListType"]

        return None

    @compliant_app_list_type.setter
    def compliant_app_list_type(self, val):
        self._prop_dict["compliantAppListType"] = val

    @property
    def diagnostic_data_block_submission(self):
        """
        Gets and sets the diagnosticDataBlockSubmission
        
        Returns:
            bool:
                The diagnosticDataBlockSubmission
        """
        if "diagnosticDataBlockSubmission" in self._prop_dict:
            return self._prop_dict["diagnosticDataBlockSubmission"]
        else:
            return None

    @diagnostic_data_block_submission.setter
    def diagnostic_data_block_submission(self, val):
        self._prop_dict["diagnosticDataBlockSubmission"] = val

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
    def google_account_block_auto_sync(self):
        """
        Gets and sets the googleAccountBlockAutoSync
        
        Returns:
            bool:
                The googleAccountBlockAutoSync
        """
        if "googleAccountBlockAutoSync" in self._prop_dict:
            return self._prop_dict["googleAccountBlockAutoSync"]
        else:
            return None

    @google_account_block_auto_sync.setter
    def google_account_block_auto_sync(self, val):
        self._prop_dict["googleAccountBlockAutoSync"] = val

    @property
    def google_play_store_blocked(self):
        """
        Gets and sets the googlePlayStoreBlocked
        
        Returns:
            bool:
                The googlePlayStoreBlocked
        """
        if "googlePlayStoreBlocked" in self._prop_dict:
            return self._prop_dict["googlePlayStoreBlocked"]
        else:
            return None

    @google_play_store_blocked.setter
    def google_play_store_blocked(self, val):
        self._prop_dict["googlePlayStoreBlocked"] = val

    @property
    def kiosk_mode_block_sleep_button(self):
        """
        Gets and sets the kioskModeBlockSleepButton
        
        Returns:
            bool:
                The kioskModeBlockSleepButton
        """
        if "kioskModeBlockSleepButton" in self._prop_dict:
            return self._prop_dict["kioskModeBlockSleepButton"]
        else:
            return None

    @kiosk_mode_block_sleep_button.setter
    def kiosk_mode_block_sleep_button(self, val):
        self._prop_dict["kioskModeBlockSleepButton"] = val

    @property
    def kiosk_mode_block_volume_buttons(self):
        """
        Gets and sets the kioskModeBlockVolumeButtons
        
        Returns:
            bool:
                The kioskModeBlockVolumeButtons
        """
        if "kioskModeBlockVolumeButtons" in self._prop_dict:
            return self._prop_dict["kioskModeBlockVolumeButtons"]
        else:
            return None

    @kiosk_mode_block_volume_buttons.setter
    def kiosk_mode_block_volume_buttons(self, val):
        self._prop_dict["kioskModeBlockVolumeButtons"] = val

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
            :class:`AndroidRequiredPasswordType<onedrivesdk.model.android_required_password_type.AndroidRequiredPasswordType>`:
                The passwordRequiredType
        """
        if "passwordRequiredType" in self._prop_dict:
            if isinstance(self._prop_dict["passwordRequiredType"], OneDriveObjectBase):
                return self._prop_dict["passwordRequiredType"]
            else :
                self._prop_dict["passwordRequiredType"] = AndroidRequiredPasswordType(self._prop_dict["passwordRequiredType"])
                return self._prop_dict["passwordRequiredType"]

        return None

    @password_required_type.setter
    def password_required_type(self, val):
        self._prop_dict["passwordRequiredType"] = val

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
    def power_off_blocked(self):
        """
        Gets and sets the powerOffBlocked
        
        Returns:
            bool:
                The powerOffBlocked
        """
        if "powerOffBlocked" in self._prop_dict:
            return self._prop_dict["powerOffBlocked"]
        else:
            return None

    @power_off_blocked.setter
    def power_off_blocked(self, val):
        self._prop_dict["powerOffBlocked"] = val

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
    def device_sharing_allowed(self):
        """
        Gets and sets the deviceSharingAllowed
        
        Returns:
            bool:
                The deviceSharingAllowed
        """
        if "deviceSharingAllowed" in self._prop_dict:
            return self._prop_dict["deviceSharingAllowed"]
        else:
            return None

    @device_sharing_allowed.setter
    def device_sharing_allowed(self, val):
        self._prop_dict["deviceSharingAllowed"] = val

    @property
    def storage_block_google_backup(self):
        """
        Gets and sets the storageBlockGoogleBackup
        
        Returns:
            bool:
                The storageBlockGoogleBackup
        """
        if "storageBlockGoogleBackup" in self._prop_dict:
            return self._prop_dict["storageBlockGoogleBackup"]
        else:
            return None

    @storage_block_google_backup.setter
    def storage_block_google_backup(self, val):
        self._prop_dict["storageBlockGoogleBackup"] = val

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
    def storage_require_device_encryption(self):
        """
        Gets and sets the storageRequireDeviceEncryption
        
        Returns:
            bool:
                The storageRequireDeviceEncryption
        """
        if "storageRequireDeviceEncryption" in self._prop_dict:
            return self._prop_dict["storageRequireDeviceEncryption"]
        else:
            return None

    @storage_require_device_encryption.setter
    def storage_require_device_encryption(self, val):
        self._prop_dict["storageRequireDeviceEncryption"] = val

    @property
    def storage_require_removable_storage_encryption(self):
        """
        Gets and sets the storageRequireRemovableStorageEncryption
        
        Returns:
            bool:
                The storageRequireRemovableStorageEncryption
        """
        if "storageRequireRemovableStorageEncryption" in self._prop_dict:
            return self._prop_dict["storageRequireRemovableStorageEncryption"]
        else:
            return None

    @storage_require_removable_storage_encryption.setter
    def storage_require_removable_storage_encryption(self, val):
        self._prop_dict["storageRequireRemovableStorageEncryption"] = val

    @property
    def voice_assistant_blocked(self):
        """
        Gets and sets the voiceAssistantBlocked
        
        Returns:
            bool:
                The voiceAssistantBlocked
        """
        if "voiceAssistantBlocked" in self._prop_dict:
            return self._prop_dict["voiceAssistantBlocked"]
        else:
            return None

    @voice_assistant_blocked.setter
    def voice_assistant_blocked(self, val):
        self._prop_dict["voiceAssistantBlocked"] = val

    @property
    def voice_dialing_blocked(self):
        """
        Gets and sets the voiceDialingBlocked
        
        Returns:
            bool:
                The voiceDialingBlocked
        """
        if "voiceDialingBlocked" in self._prop_dict:
            return self._prop_dict["voiceDialingBlocked"]
        else:
            return None

    @voice_dialing_blocked.setter
    def voice_dialing_blocked(self, val):
        self._prop_dict["voiceDialingBlocked"] = val

    @property
    def web_browser_block_popups(self):
        """
        Gets and sets the webBrowserBlockPopups
        
        Returns:
            bool:
                The webBrowserBlockPopups
        """
        if "webBrowserBlockPopups" in self._prop_dict:
            return self._prop_dict["webBrowserBlockPopups"]
        else:
            return None

    @web_browser_block_popups.setter
    def web_browser_block_popups(self, val):
        self._prop_dict["webBrowserBlockPopups"] = val

    @property
    def web_browser_block_autofill(self):
        """
        Gets and sets the webBrowserBlockAutofill
        
        Returns:
            bool:
                The webBrowserBlockAutofill
        """
        if "webBrowserBlockAutofill" in self._prop_dict:
            return self._prop_dict["webBrowserBlockAutofill"]
        else:
            return None

    @web_browser_block_autofill.setter
    def web_browser_block_autofill(self, val):
        self._prop_dict["webBrowserBlockAutofill"] = val

    @property
    def web_browser_block_java_script(self):
        """
        Gets and sets the webBrowserBlockJavaScript
        
        Returns:
            bool:
                The webBrowserBlockJavaScript
        """
        if "webBrowserBlockJavaScript" in self._prop_dict:
            return self._prop_dict["webBrowserBlockJavaScript"]
        else:
            return None

    @web_browser_block_java_script.setter
    def web_browser_block_java_script(self, val):
        self._prop_dict["webBrowserBlockJavaScript"] = val

    @property
    def web_browser_blocked(self):
        """
        Gets and sets the webBrowserBlocked
        
        Returns:
            bool:
                The webBrowserBlocked
        """
        if "webBrowserBlocked" in self._prop_dict:
            return self._prop_dict["webBrowserBlocked"]
        else:
            return None

    @web_browser_blocked.setter
    def web_browser_blocked(self, val):
        self._prop_dict["webBrowserBlocked"] = val

    @property
    def web_browser_cookie_settings(self):
        """
        Gets and sets the webBrowserCookieSettings
        
        Returns: 
            :class:`WebBrowserCookieSettings<onedrivesdk.model.web_browser_cookie_settings.WebBrowserCookieSettings>`:
                The webBrowserCookieSettings
        """
        if "webBrowserCookieSettings" in self._prop_dict:
            if isinstance(self._prop_dict["webBrowserCookieSettings"], OneDriveObjectBase):
                return self._prop_dict["webBrowserCookieSettings"]
            else :
                self._prop_dict["webBrowserCookieSettings"] = WebBrowserCookieSettings(self._prop_dict["webBrowserCookieSettings"])
                return self._prop_dict["webBrowserCookieSettings"]

        return None

    @web_browser_cookie_settings.setter
    def web_browser_cookie_settings(self, val):
        self._prop_dict["webBrowserCookieSettings"] = val

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
    def apps_install_allow_list(self):
        """Gets and sets the appsInstallAllowList
        
        Returns: 
            :class:`AppsInstallAllowListCollectionPage<onedrivesdk.request.apps_install_allow_list_collection.AppsInstallAllowListCollectionPage>`:
                The appsInstallAllowList
        """
        if "appsInstallAllowList" in self._prop_dict:
            return AppsInstallAllowListCollectionPage(self._prop_dict["appsInstallAllowList"])
        else:
            return None

    @property
    def apps_launch_block_list(self):
        """Gets and sets the appsLaunchBlockList
        
        Returns: 
            :class:`AppsLaunchBlockListCollectionPage<onedrivesdk.request.apps_launch_block_list_collection.AppsLaunchBlockListCollectionPage>`:
                The appsLaunchBlockList
        """
        if "appsLaunchBlockList" in self._prop_dict:
            return AppsLaunchBlockListCollectionPage(self._prop_dict["appsLaunchBlockList"])
        else:
            return None

    @property
    def apps_hide_list(self):
        """Gets and sets the appsHideList
        
        Returns: 
            :class:`AppsHideListCollectionPage<onedrivesdk.request.apps_hide_list_collection.AppsHideListCollectionPage>`:
                The appsHideList
        """
        if "appsHideList" in self._prop_dict:
            return AppsHideListCollectionPage(self._prop_dict["appsHideList"])
        else:
            return None

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

