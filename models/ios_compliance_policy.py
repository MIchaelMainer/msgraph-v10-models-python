# -*- coding: utf-8 -*- 
'''
# Copyright (c) Microsoft Corporation.  All Rights Reserved.  Licensed under the MIT License.  See License in the project root for license information.
# 
#  This file was generated and any changes will be overwritten.
'''

from __future__ import unicode_literals
from ..model.required_password_type import RequiredPasswordType
from ..model.device_threat_protection_level import DeviceThreatProtectionLevel
from ..one_drive_object_base import OneDriveObjectBase


class IosCompliancePolicy(OneDriveObjectBase):

    def __init__(self, prop_dict={}):
        self._prop_dict = prop_dict

    @property
    def passcode_block_simple(self):
        """
        Gets and sets the passcodeBlockSimple
        
        Returns:
            bool:
                The passcodeBlockSimple
        """
        if "passcodeBlockSimple" in self._prop_dict:
            return self._prop_dict["passcodeBlockSimple"]
        else:
            return None

    @passcode_block_simple.setter
    def passcode_block_simple(self, val):
        self._prop_dict["passcodeBlockSimple"] = val

    @property
    def passcode_expiration_days(self):
        """
        Gets and sets the passcodeExpirationDays
        
        Returns:
            int:
                The passcodeExpirationDays
        """
        if "passcodeExpirationDays" in self._prop_dict:
            return self._prop_dict["passcodeExpirationDays"]
        else:
            return None

    @passcode_expiration_days.setter
    def passcode_expiration_days(self, val):
        self._prop_dict["passcodeExpirationDays"] = val

    @property
    def passcode_minimum_length(self):
        """
        Gets and sets the passcodeMinimumLength
        
        Returns:
            int:
                The passcodeMinimumLength
        """
        if "passcodeMinimumLength" in self._prop_dict:
            return self._prop_dict["passcodeMinimumLength"]
        else:
            return None

    @passcode_minimum_length.setter
    def passcode_minimum_length(self, val):
        self._prop_dict["passcodeMinimumLength"] = val

    @property
    def passcode_minutes_of_inactivity_before_lock(self):
        """
        Gets and sets the passcodeMinutesOfInactivityBeforeLock
        
        Returns:
            int:
                The passcodeMinutesOfInactivityBeforeLock
        """
        if "passcodeMinutesOfInactivityBeforeLock" in self._prop_dict:
            return self._prop_dict["passcodeMinutesOfInactivityBeforeLock"]
        else:
            return None

    @passcode_minutes_of_inactivity_before_lock.setter
    def passcode_minutes_of_inactivity_before_lock(self, val):
        self._prop_dict["passcodeMinutesOfInactivityBeforeLock"] = val

    @property
    def passcode_previous_passcode_block_count(self):
        """
        Gets and sets the passcodePreviousPasscodeBlockCount
        
        Returns:
            int:
                The passcodePreviousPasscodeBlockCount
        """
        if "passcodePreviousPasscodeBlockCount" in self._prop_dict:
            return self._prop_dict["passcodePreviousPasscodeBlockCount"]
        else:
            return None

    @passcode_previous_passcode_block_count.setter
    def passcode_previous_passcode_block_count(self, val):
        self._prop_dict["passcodePreviousPasscodeBlockCount"] = val

    @property
    def passcode_minimum_character_set_count(self):
        """
        Gets and sets the passcodeMinimumCharacterSetCount
        
        Returns:
            int:
                The passcodeMinimumCharacterSetCount
        """
        if "passcodeMinimumCharacterSetCount" in self._prop_dict:
            return self._prop_dict["passcodeMinimumCharacterSetCount"]
        else:
            return None

    @passcode_minimum_character_set_count.setter
    def passcode_minimum_character_set_count(self, val):
        self._prop_dict["passcodeMinimumCharacterSetCount"] = val

    @property
    def passcode_required_type(self):
        """
        Gets and sets the passcodeRequiredType
        
        Returns: 
            :class:`RequiredPasswordType<onedrivesdk.model.required_password_type.RequiredPasswordType>`:
                The passcodeRequiredType
        """
        if "passcodeRequiredType" in self._prop_dict:
            if isinstance(self._prop_dict["passcodeRequiredType"], OneDriveObjectBase):
                return self._prop_dict["passcodeRequiredType"]
            else :
                self._prop_dict["passcodeRequiredType"] = RequiredPasswordType(self._prop_dict["passcodeRequiredType"])
                return self._prop_dict["passcodeRequiredType"]

        return None

    @passcode_required_type.setter
    def passcode_required_type(self, val):
        self._prop_dict["passcodeRequiredType"] = val

    @property
    def passcode_required(self):
        """
        Gets and sets the passcodeRequired
        
        Returns:
            bool:
                The passcodeRequired
        """
        if "passcodeRequired" in self._prop_dict:
            return self._prop_dict["passcodeRequired"]
        else:
            return None

    @passcode_required.setter
    def passcode_required(self, val):
        self._prop_dict["passcodeRequired"] = val

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
    def managed_email_profile_required(self):
        """
        Gets and sets the managedEmailProfileRequired
        
        Returns:
            bool:
                The managedEmailProfileRequired
        """
        if "managedEmailProfileRequired" in self._prop_dict:
            return self._prop_dict["managedEmailProfileRequired"]
        else:
            return None

    @managed_email_profile_required.setter
    def managed_email_profile_required(self, val):
        self._prop_dict["managedEmailProfileRequired"] = val

