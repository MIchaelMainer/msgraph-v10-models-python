# -*- coding: utf-8 -*- 
'''
# Copyright (c) Microsoft Corporation.  All Rights Reserved.  Licensed under the MIT License.  See License in the project root for license information.
# 
#  This file was generated and any changes will be overwritten.
'''

from __future__ import unicode_literals
from ..model.android_required_password_type import AndroidRequiredPasswordType
from ..model.device_threat_protection_level import DeviceThreatProtectionLevel
from ..one_drive_object_base import OneDriveObjectBase


class AndroidForWorkCompliancePolicy(OneDriveObjectBase):

    def __init__(self, prop_dict={}):
        self._prop_dict = prop_dict

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
    def password_minutes_of_inactivity_before_lock(self):
        """
        Gets and sets the passwordMinutesOfInactivityBeforeLock
        
        Returns:
            int:
                The passwordMinutesOfInactivityBeforeLock
        """
        if "passwordMinutesOfInactivityBeforeLock" in self._prop_dict:
            return self._prop_dict["passwordMinutesOfInactivityBeforeLock"]
        else:
            return None

    @password_minutes_of_inactivity_before_lock.setter
    def password_minutes_of_inactivity_before_lock(self, val):
        self._prop_dict["passwordMinutesOfInactivityBeforeLock"] = val

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
    def security_prevent_install_apps_from_unknown_sources(self):
        """
        Gets and sets the securityPreventInstallAppsFromUnknownSources
        
        Returns:
            bool:
                The securityPreventInstallAppsFromUnknownSources
        """
        if "securityPreventInstallAppsFromUnknownSources" in self._prop_dict:
            return self._prop_dict["securityPreventInstallAppsFromUnknownSources"]
        else:
            return None

    @security_prevent_install_apps_from_unknown_sources.setter
    def security_prevent_install_apps_from_unknown_sources(self, val):
        self._prop_dict["securityPreventInstallAppsFromUnknownSources"] = val

    @property
    def security_disable_usb_debugging(self):
        """
        Gets and sets the securityDisableUsbDebugging
        
        Returns:
            bool:
                The securityDisableUsbDebugging
        """
        if "securityDisableUsbDebugging" in self._prop_dict:
            return self._prop_dict["securityDisableUsbDebugging"]
        else:
            return None

    @security_disable_usb_debugging.setter
    def security_disable_usb_debugging(self, val):
        self._prop_dict["securityDisableUsbDebugging"] = val

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

    @property
    def device_threat_protection_enabled(self):
        """
        Gets and sets the deviceThreatProtectionEnabled
        
        Returns:
            bool:
                The deviceThreatProtectionEnabled
        """
        if "deviceThreatProtectionEnabled" in self._prop_dict:
            return self._prop_dict["deviceThreatProtectionEnabled"]
        else:
            return None

    @device_threat_protection_enabled.setter
    def device_threat_protection_enabled(self, val):
        self._prop_dict["deviceThreatProtectionEnabled"] = val

    @property
    def device_threat_protection_required_security_level(self):
        """
        Gets and sets the deviceThreatProtectionRequiredSecurityLevel
        
        Returns: 
            :class:`DeviceThreatProtectionLevel<onedrivesdk.model.device_threat_protection_level.DeviceThreatProtectionLevel>`:
                The deviceThreatProtectionRequiredSecurityLevel
        """
        if "deviceThreatProtectionRequiredSecurityLevel" in self._prop_dict:
            if isinstance(self._prop_dict["deviceThreatProtectionRequiredSecurityLevel"], OneDriveObjectBase):
                return self._prop_dict["deviceThreatProtectionRequiredSecurityLevel"]
            else :
                self._prop_dict["deviceThreatProtectionRequiredSecurityLevel"] = DeviceThreatProtectionLevel(self._prop_dict["deviceThreatProtectionRequiredSecurityLevel"])
                return self._prop_dict["deviceThreatProtectionRequiredSecurityLevel"]

        return None

    @device_threat_protection_required_security_level.setter
    def device_threat_protection_required_security_level(self, val):
        self._prop_dict["deviceThreatProtectionRequiredSecurityLevel"] = val

    @property
    def security_block_jailbroken_devices(self):
        """
        Gets and sets the securityBlockJailbrokenDevices
        
        Returns:
            bool:
                The securityBlockJailbrokenDevices
        """
        if "securityBlockJailbrokenDevices" in self._prop_dict:
            return self._prop_dict["securityBlockJailbrokenDevices"]
        else:
            return None

    @security_block_jailbroken_devices.setter
    def security_block_jailbroken_devices(self, val):
        self._prop_dict["securityBlockJailbrokenDevices"] = val

    @property
    def os_minimum_version(self):
        """
        Gets and sets the osMinimumVersion
        
        Returns:
            str:
                The osMinimumVersion
        """
        if "osMinimumVersion" in self._prop_dict:
            return self._prop_dict["osMinimumVersion"]
        else:
            return None

    @os_minimum_version.setter
    def os_minimum_version(self, val):
        self._prop_dict["osMinimumVersion"] = val

    @property
    def os_maximum_version(self):
        """
        Gets and sets the osMaximumVersion
        
        Returns:
            str:
                The osMaximumVersion
        """
        if "osMaximumVersion" in self._prop_dict:
            return self._prop_dict["osMaximumVersion"]
        else:
            return None

    @os_maximum_version.setter
    def os_maximum_version(self, val):
        self._prop_dict["osMaximumVersion"] = val

    @property
    def min_android_security_patch_level(self):
        """
        Gets and sets the minAndroidSecurityPatchLevel
        
        Returns:
            str:
                The minAndroidSecurityPatchLevel
        """
        if "minAndroidSecurityPatchLevel" in self._prop_dict:
            return self._prop_dict["minAndroidSecurityPatchLevel"]
        else:
            return None

    @min_android_security_patch_level.setter
    def min_android_security_patch_level(self, val):
        self._prop_dict["minAndroidSecurityPatchLevel"] = val

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
    def security_require_safety_net_attestation_basic_integrity(self):
        """
        Gets and sets the securityRequireSafetyNetAttestationBasicIntegrity
        
        Returns:
            bool:
                The securityRequireSafetyNetAttestationBasicIntegrity
        """
        if "securityRequireSafetyNetAttestationBasicIntegrity" in self._prop_dict:
            return self._prop_dict["securityRequireSafetyNetAttestationBasicIntegrity"]
        else:
            return None

    @security_require_safety_net_attestation_basic_integrity.setter
    def security_require_safety_net_attestation_basic_integrity(self, val):
        self._prop_dict["securityRequireSafetyNetAttestationBasicIntegrity"] = val

    @property
    def security_require_safety_net_attestation_certified_device(self):
        """
        Gets and sets the securityRequireSafetyNetAttestationCertifiedDevice
        
        Returns:
            bool:
                The securityRequireSafetyNetAttestationCertifiedDevice
        """
        if "securityRequireSafetyNetAttestationCertifiedDevice" in self._prop_dict:
            return self._prop_dict["securityRequireSafetyNetAttestationCertifiedDevice"]
        else:
            return None

    @security_require_safety_net_attestation_certified_device.setter
    def security_require_safety_net_attestation_certified_device(self, val):
        self._prop_dict["securityRequireSafetyNetAttestationCertifiedDevice"] = val

    @property
    def security_require_google_play_services(self):
        """
        Gets and sets the securityRequireGooglePlayServices
        
        Returns:
            bool:
                The securityRequireGooglePlayServices
        """
        if "securityRequireGooglePlayServices" in self._prop_dict:
            return self._prop_dict["securityRequireGooglePlayServices"]
        else:
            return None

    @security_require_google_play_services.setter
    def security_require_google_play_services(self, val):
        self._prop_dict["securityRequireGooglePlayServices"] = val

    @property
    def security_require_up_to_date_security_providers(self):
        """
        Gets and sets the securityRequireUpToDateSecurityProviders
        
        Returns:
            bool:
                The securityRequireUpToDateSecurityProviders
        """
        if "securityRequireUpToDateSecurityProviders" in self._prop_dict:
            return self._prop_dict["securityRequireUpToDateSecurityProviders"]
        else:
            return None

    @security_require_up_to_date_security_providers.setter
    def security_require_up_to_date_security_providers(self, val):
        self._prop_dict["securityRequireUpToDateSecurityProviders"] = val

    @property
    def security_require_company_portal_app_integrity(self):
        """
        Gets and sets the securityRequireCompanyPortalAppIntegrity
        
        Returns:
            bool:
                The securityRequireCompanyPortalAppIntegrity
        """
        if "securityRequireCompanyPortalAppIntegrity" in self._prop_dict:
            return self._prop_dict["securityRequireCompanyPortalAppIntegrity"]
        else:
            return None

    @security_require_company_portal_app_integrity.setter
    def security_require_company_portal_app_integrity(self, val):
        self._prop_dict["securityRequireCompanyPortalAppIntegrity"] = val

