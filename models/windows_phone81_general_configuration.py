# -*- coding: utf-8 -*- 
'''
# Copyright (c) Microsoft Corporation.  All Rights Reserved.  Licensed under the MIT License.  See License in the project root for license information.
# 
#  This file was generated and any changes will be overwritten.
'''

from __future__ import unicode_literals
from ..model.app_list_item import AppListItem
from ..model.app_list_type import AppListType
from ..model.required_password_type import RequiredPasswordType
from ..one_drive_object_base import OneDriveObjectBase


class WindowsPhone81GeneralConfiguration(OneDriveObjectBase):

    def __init__(self, prop_dict={}):
        self._prop_dict = prop_dict

    @property
    def apply_only_to_windows_phone81(self):
        """
        Gets and sets the applyOnlyToWindowsPhone81
        
        Returns:
            bool:
                The applyOnlyToWindowsPhone81
        """
        if "applyOnlyToWindowsPhone81" in self._prop_dict:
            return self._prop_dict["applyOnlyToWindowsPhone81"]
        else:
            return None

    @apply_only_to_windows_phone81.setter
    def apply_only_to_windows_phone81(self, val):
        self._prop_dict["applyOnlyToWindowsPhone81"] = val

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
    def cellular_block_wifi_tethering(self):
        """
        Gets and sets the cellularBlockWifiTethering
        
        Returns:
            bool:
                The cellularBlockWifiTethering
        """
        if "cellularBlockWifiTethering" in self._prop_dict:
            return self._prop_dict["cellularBlockWifiTethering"]
        else:
            return None

    @cellular_block_wifi_tethering.setter
    def cellular_block_wifi_tethering(self, val):
        self._prop_dict["cellularBlockWifiTethering"] = val

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
    def email_block_adding_accounts(self):
        """
        Gets and sets the emailBlockAddingAccounts
        
        Returns:
            bool:
                The emailBlockAddingAccounts
        """
        if "emailBlockAddingAccounts" in self._prop_dict:
            return self._prop_dict["emailBlockAddingAccounts"]
        else:
            return None

    @email_block_adding_accounts.setter
    def email_block_adding_accounts(self, val):
        self._prop_dict["emailBlockAddingAccounts"] = val

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
    def storage_require_encryption(self):
        """
        Gets and sets the storageRequireEncryption
        
        Returns:
            bool:
                The storageRequireEncryption
        """
        if "storageRequireEncryption" in self._prop_dict:
            return self._prop_dict["storageRequireEncryption"]
        else:
            return None

    @storage_require_encryption.setter
    def storage_require_encryption(self, val):
        self._prop_dict["storageRequireEncryption"] = val

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
    def wifi_blocked(self):
        """
        Gets and sets the wifiBlocked
        
        Returns:
            bool:
                The wifiBlocked
        """
        if "wifiBlocked" in self._prop_dict:
            return self._prop_dict["wifiBlocked"]
        else:
            return None

    @wifi_blocked.setter
    def wifi_blocked(self, val):
        self._prop_dict["wifiBlocked"] = val

    @property
    def wifi_block_automatic_connect_hotspots(self):
        """
        Gets and sets the wifiBlockAutomaticConnectHotspots
        
        Returns:
            bool:
                The wifiBlockAutomaticConnectHotspots
        """
        if "wifiBlockAutomaticConnectHotspots" in self._prop_dict:
            return self._prop_dict["wifiBlockAutomaticConnectHotspots"]
        else:
            return None

    @wifi_block_automatic_connect_hotspots.setter
    def wifi_block_automatic_connect_hotspots(self, val):
        self._prop_dict["wifiBlockAutomaticConnectHotspots"] = val

    @property
    def wifi_block_hotspot_reporting(self):
        """
        Gets and sets the wifiBlockHotspotReporting
        
        Returns:
            bool:
                The wifiBlockHotspotReporting
        """
        if "wifiBlockHotspotReporting" in self._prop_dict:
            return self._prop_dict["wifiBlockHotspotReporting"]
        else:
            return None

    @wifi_block_hotspot_reporting.setter
    def wifi_block_hotspot_reporting(self, val):
        self._prop_dict["wifiBlockHotspotReporting"] = val

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

