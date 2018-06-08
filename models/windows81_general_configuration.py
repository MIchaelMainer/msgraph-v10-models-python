# -*- coding: utf-8 -*- 
'''
# Copyright (c) Microsoft Corporation.  All Rights Reserved.  Licensed under the MIT License.  See License in the project root for license information.
# 
#  This file was generated and any changes will be overwritten.
'''

from __future__ import unicode_literals
from ..model.internet_site_security_level import InternetSiteSecurityLevel
from ..model.site_security_level import SiteSecurityLevel
from ..model.required_password_type import RequiredPasswordType
from ..model.windows_user_account_control_settings import WindowsUserAccountControlSettings
from ..one_drive_object_base import OneDriveObjectBase


class Windows81GeneralConfiguration(OneDriveObjectBase):

    def __init__(self, prop_dict={}):
        self._prop_dict = prop_dict

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
    def apply_only_to_windows81(self):
        """
        Gets and sets the applyOnlyToWindows81
        
        Returns:
            bool:
                The applyOnlyToWindows81
        """
        if "applyOnlyToWindows81" in self._prop_dict:
            return self._prop_dict["applyOnlyToWindows81"]
        else:
            return None

    @apply_only_to_windows81.setter
    def apply_only_to_windows81(self, val):
        self._prop_dict["applyOnlyToWindows81"] = val

    @property
    def browser_block_autofill(self):
        """
        Gets and sets the browserBlockAutofill
        
        Returns:
            bool:
                The browserBlockAutofill
        """
        if "browserBlockAutofill" in self._prop_dict:
            return self._prop_dict["browserBlockAutofill"]
        else:
            return None

    @browser_block_autofill.setter
    def browser_block_autofill(self, val):
        self._prop_dict["browserBlockAutofill"] = val

    @property
    def browser_block_automatic_detection_of_intranet_sites(self):
        """
        Gets and sets the browserBlockAutomaticDetectionOfIntranetSites
        
        Returns:
            bool:
                The browserBlockAutomaticDetectionOfIntranetSites
        """
        if "browserBlockAutomaticDetectionOfIntranetSites" in self._prop_dict:
            return self._prop_dict["browserBlockAutomaticDetectionOfIntranetSites"]
        else:
            return None

    @browser_block_automatic_detection_of_intranet_sites.setter
    def browser_block_automatic_detection_of_intranet_sites(self, val):
        self._prop_dict["browserBlockAutomaticDetectionOfIntranetSites"] = val

    @property
    def browser_block_enterprise_mode_access(self):
        """
        Gets and sets the browserBlockEnterpriseModeAccess
        
        Returns:
            bool:
                The browserBlockEnterpriseModeAccess
        """
        if "browserBlockEnterpriseModeAccess" in self._prop_dict:
            return self._prop_dict["browserBlockEnterpriseModeAccess"]
        else:
            return None

    @browser_block_enterprise_mode_access.setter
    def browser_block_enterprise_mode_access(self, val):
        self._prop_dict["browserBlockEnterpriseModeAccess"] = val

    @property
    def browser_block_java_script(self):
        """
        Gets and sets the browserBlockJavaScript
        
        Returns:
            bool:
                The browserBlockJavaScript
        """
        if "browserBlockJavaScript" in self._prop_dict:
            return self._prop_dict["browserBlockJavaScript"]
        else:
            return None

    @browser_block_java_script.setter
    def browser_block_java_script(self, val):
        self._prop_dict["browserBlockJavaScript"] = val

    @property
    def browser_block_plugins(self):
        """
        Gets and sets the browserBlockPlugins
        
        Returns:
            bool:
                The browserBlockPlugins
        """
        if "browserBlockPlugins" in self._prop_dict:
            return self._prop_dict["browserBlockPlugins"]
        else:
            return None

    @browser_block_plugins.setter
    def browser_block_plugins(self, val):
        self._prop_dict["browserBlockPlugins"] = val

    @property
    def browser_block_popups(self):
        """
        Gets and sets the browserBlockPopups
        
        Returns:
            bool:
                The browserBlockPopups
        """
        if "browserBlockPopups" in self._prop_dict:
            return self._prop_dict["browserBlockPopups"]
        else:
            return None

    @browser_block_popups.setter
    def browser_block_popups(self, val):
        self._prop_dict["browserBlockPopups"] = val

    @property
    def browser_block_sending_do_not_track_header(self):
        """
        Gets and sets the browserBlockSendingDoNotTrackHeader
        
        Returns:
            bool:
                The browserBlockSendingDoNotTrackHeader
        """
        if "browserBlockSendingDoNotTrackHeader" in self._prop_dict:
            return self._prop_dict["browserBlockSendingDoNotTrackHeader"]
        else:
            return None

    @browser_block_sending_do_not_track_header.setter
    def browser_block_sending_do_not_track_header(self, val):
        self._prop_dict["browserBlockSendingDoNotTrackHeader"] = val

    @property
    def browser_block_single_word_entry_on_intranet_sites(self):
        """
        Gets and sets the browserBlockSingleWordEntryOnIntranetSites
        
        Returns:
            bool:
                The browserBlockSingleWordEntryOnIntranetSites
        """
        if "browserBlockSingleWordEntryOnIntranetSites" in self._prop_dict:
            return self._prop_dict["browserBlockSingleWordEntryOnIntranetSites"]
        else:
            return None

    @browser_block_single_word_entry_on_intranet_sites.setter
    def browser_block_single_word_entry_on_intranet_sites(self, val):
        self._prop_dict["browserBlockSingleWordEntryOnIntranetSites"] = val

    @property
    def browser_require_smart_screen(self):
        """
        Gets and sets the browserRequireSmartScreen
        
        Returns:
            bool:
                The browserRequireSmartScreen
        """
        if "browserRequireSmartScreen" in self._prop_dict:
            return self._prop_dict["browserRequireSmartScreen"]
        else:
            return None

    @browser_require_smart_screen.setter
    def browser_require_smart_screen(self, val):
        self._prop_dict["browserRequireSmartScreen"] = val

    @property
    def browser_enterprise_mode_site_list_location(self):
        """
        Gets and sets the browserEnterpriseModeSiteListLocation
        
        Returns:
            str:
                The browserEnterpriseModeSiteListLocation
        """
        if "browserEnterpriseModeSiteListLocation" in self._prop_dict:
            return self._prop_dict["browserEnterpriseModeSiteListLocation"]
        else:
            return None

    @browser_enterprise_mode_site_list_location.setter
    def browser_enterprise_mode_site_list_location(self, val):
        self._prop_dict["browserEnterpriseModeSiteListLocation"] = val

    @property
    def browser_internet_security_level(self):
        """
        Gets and sets the browserInternetSecurityLevel
        
        Returns: 
            :class:`InternetSiteSecurityLevel<onedrivesdk.model.internet_site_security_level.InternetSiteSecurityLevel>`:
                The browserInternetSecurityLevel
        """
        if "browserInternetSecurityLevel" in self._prop_dict:
            if isinstance(self._prop_dict["browserInternetSecurityLevel"], OneDriveObjectBase):
                return self._prop_dict["browserInternetSecurityLevel"]
            else :
                self._prop_dict["browserInternetSecurityLevel"] = InternetSiteSecurityLevel(self._prop_dict["browserInternetSecurityLevel"])
                return self._prop_dict["browserInternetSecurityLevel"]

        return None

    @browser_internet_security_level.setter
    def browser_internet_security_level(self, val):
        self._prop_dict["browserInternetSecurityLevel"] = val

    @property
    def browser_intranet_security_level(self):
        """
        Gets and sets the browserIntranetSecurityLevel
        
        Returns: 
            :class:`SiteSecurityLevel<onedrivesdk.model.site_security_level.SiteSecurityLevel>`:
                The browserIntranetSecurityLevel
        """
        if "browserIntranetSecurityLevel" in self._prop_dict:
            if isinstance(self._prop_dict["browserIntranetSecurityLevel"], OneDriveObjectBase):
                return self._prop_dict["browserIntranetSecurityLevel"]
            else :
                self._prop_dict["browserIntranetSecurityLevel"] = SiteSecurityLevel(self._prop_dict["browserIntranetSecurityLevel"])
                return self._prop_dict["browserIntranetSecurityLevel"]

        return None

    @browser_intranet_security_level.setter
    def browser_intranet_security_level(self, val):
        self._prop_dict["browserIntranetSecurityLevel"] = val

    @property
    def browser_logging_report_location(self):
        """
        Gets and sets the browserLoggingReportLocation
        
        Returns:
            str:
                The browserLoggingReportLocation
        """
        if "browserLoggingReportLocation" in self._prop_dict:
            return self._prop_dict["browserLoggingReportLocation"]
        else:
            return None

    @browser_logging_report_location.setter
    def browser_logging_report_location(self, val):
        self._prop_dict["browserLoggingReportLocation"] = val

    @property
    def browser_require_high_security_for_restricted_sites(self):
        """
        Gets and sets the browserRequireHighSecurityForRestrictedSites
        
        Returns:
            bool:
                The browserRequireHighSecurityForRestrictedSites
        """
        if "browserRequireHighSecurityForRestrictedSites" in self._prop_dict:
            return self._prop_dict["browserRequireHighSecurityForRestrictedSites"]
        else:
            return None

    @browser_require_high_security_for_restricted_sites.setter
    def browser_require_high_security_for_restricted_sites(self, val):
        self._prop_dict["browserRequireHighSecurityForRestrictedSites"] = val

    @property
    def browser_require_firewall(self):
        """
        Gets and sets the browserRequireFirewall
        
        Returns:
            bool:
                The browserRequireFirewall
        """
        if "browserRequireFirewall" in self._prop_dict:
            return self._prop_dict["browserRequireFirewall"]
        else:
            return None

    @browser_require_firewall.setter
    def browser_require_firewall(self, val):
        self._prop_dict["browserRequireFirewall"] = val

    @property
    def browser_require_fraud_warning(self):
        """
        Gets and sets the browserRequireFraudWarning
        
        Returns:
            bool:
                The browserRequireFraudWarning
        """
        if "browserRequireFraudWarning" in self._prop_dict:
            return self._prop_dict["browserRequireFraudWarning"]
        else:
            return None

    @browser_require_fraud_warning.setter
    def browser_require_fraud_warning(self, val):
        self._prop_dict["browserRequireFraudWarning"] = val

    @property
    def browser_trusted_sites_security_level(self):
        """
        Gets and sets the browserTrustedSitesSecurityLevel
        
        Returns: 
            :class:`SiteSecurityLevel<onedrivesdk.model.site_security_level.SiteSecurityLevel>`:
                The browserTrustedSitesSecurityLevel
        """
        if "browserTrustedSitesSecurityLevel" in self._prop_dict:
            if isinstance(self._prop_dict["browserTrustedSitesSecurityLevel"], OneDriveObjectBase):
                return self._prop_dict["browserTrustedSitesSecurityLevel"]
            else :
                self._prop_dict["browserTrustedSitesSecurityLevel"] = SiteSecurityLevel(self._prop_dict["browserTrustedSitesSecurityLevel"])
                return self._prop_dict["browserTrustedSitesSecurityLevel"]

        return None

    @browser_trusted_sites_security_level.setter
    def browser_trusted_sites_security_level(self, val):
        self._prop_dict["browserTrustedSitesSecurityLevel"] = val

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
    def diagnostics_block_data_submission(self):
        """
        Gets and sets the diagnosticsBlockDataSubmission
        
        Returns:
            bool:
                The diagnosticsBlockDataSubmission
        """
        if "diagnosticsBlockDataSubmission" in self._prop_dict:
            return self._prop_dict["diagnosticsBlockDataSubmission"]
        else:
            return None

    @diagnostics_block_data_submission.setter
    def diagnostics_block_data_submission(self, val):
        self._prop_dict["diagnosticsBlockDataSubmission"] = val

    @property
    def password_block_picture_password_and_pin(self):
        """
        Gets and sets the passwordBlockPicturePasswordAndPin
        
        Returns:
            bool:
                The passwordBlockPicturePasswordAndPin
        """
        if "passwordBlockPicturePasswordAndPin" in self._prop_dict:
            return self._prop_dict["passwordBlockPicturePasswordAndPin"]
        else:
            return None

    @password_block_picture_password_and_pin.setter
    def password_block_picture_password_and_pin(self, val):
        self._prop_dict["passwordBlockPicturePasswordAndPin"] = val

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
    def updates_require_automatic_updates(self):
        """
        Gets and sets the updatesRequireAutomaticUpdates
        
        Returns:
            bool:
                The updatesRequireAutomaticUpdates
        """
        if "updatesRequireAutomaticUpdates" in self._prop_dict:
            return self._prop_dict["updatesRequireAutomaticUpdates"]
        else:
            return None

    @updates_require_automatic_updates.setter
    def updates_require_automatic_updates(self, val):
        self._prop_dict["updatesRequireAutomaticUpdates"] = val

    @property
    def user_account_control_settings(self):
        """
        Gets and sets the userAccountControlSettings
        
        Returns: 
            :class:`WindowsUserAccountControlSettings<onedrivesdk.model.windows_user_account_control_settings.WindowsUserAccountControlSettings>`:
                The userAccountControlSettings
        """
        if "userAccountControlSettings" in self._prop_dict:
            if isinstance(self._prop_dict["userAccountControlSettings"], OneDriveObjectBase):
                return self._prop_dict["userAccountControlSettings"]
            else :
                self._prop_dict["userAccountControlSettings"] = WindowsUserAccountControlSettings(self._prop_dict["userAccountControlSettings"])
                return self._prop_dict["userAccountControlSettings"]

        return None

    @user_account_control_settings.setter
    def user_account_control_settings(self, val):
        self._prop_dict["userAccountControlSettings"] = val

    @property
    def work_folders_url(self):
        """
        Gets and sets the workFoldersUrl
        
        Returns:
            str:
                The workFoldersUrl
        """
        if "workFoldersUrl" in self._prop_dict:
            return self._prop_dict["workFoldersUrl"]
        else:
            return None

    @work_folders_url.setter
    def work_folders_url(self, val):
        self._prop_dict["workFoldersUrl"] = val

