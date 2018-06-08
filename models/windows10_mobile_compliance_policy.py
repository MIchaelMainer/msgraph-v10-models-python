# -*- coding: utf-8 -*- 
'''
# Copyright (c) Microsoft Corporation.  All Rights Reserved.  Licensed under the MIT License.  See License in the project root for license information.
# 
#  This file was generated and any changes will be overwritten.
'''

from __future__ import unicode_literals
from ..model.required_password_type import RequiredPasswordType
from ..one_drive_object_base import OneDriveObjectBase


class Windows10MobileCompliancePolicy(OneDriveObjectBase):

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
    def password_require_to_unlock_from_idle(self):
        """
        Gets and sets the passwordRequireToUnlockFromIdle
        
        Returns:
            bool:
                The passwordRequireToUnlockFromIdle
        """
        if "passwordRequireToUnlockFromIdle" in self._prop_dict:
            return self._prop_dict["passwordRequireToUnlockFromIdle"]
        else:
            return None

    @password_require_to_unlock_from_idle.setter
    def password_require_to_unlock_from_idle(self, val):
        self._prop_dict["passwordRequireToUnlockFromIdle"] = val

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
    def early_launch_anti_malware_driver_enabled(self):
        """
        Gets and sets the earlyLaunchAntiMalwareDriverEnabled
        
        Returns:
            bool:
                The earlyLaunchAntiMalwareDriverEnabled
        """
        if "earlyLaunchAntiMalwareDriverEnabled" in self._prop_dict:
            return self._prop_dict["earlyLaunchAntiMalwareDriverEnabled"]
        else:
            return None

    @early_launch_anti_malware_driver_enabled.setter
    def early_launch_anti_malware_driver_enabled(self, val):
        self._prop_dict["earlyLaunchAntiMalwareDriverEnabled"] = val

    @property
    def bit_locker_enabled(self):
        """
        Gets and sets the bitLockerEnabled
        
        Returns:
            bool:
                The bitLockerEnabled
        """
        if "bitLockerEnabled" in self._prop_dict:
            return self._prop_dict["bitLockerEnabled"]
        else:
            return None

    @bit_locker_enabled.setter
    def bit_locker_enabled(self, val):
        self._prop_dict["bitLockerEnabled"] = val

    @property
    def secure_boot_enabled(self):
        """
        Gets and sets the secureBootEnabled
        
        Returns:
            bool:
                The secureBootEnabled
        """
        if "secureBootEnabled" in self._prop_dict:
            return self._prop_dict["secureBootEnabled"]
        else:
            return None

    @secure_boot_enabled.setter
    def secure_boot_enabled(self, val):
        self._prop_dict["secureBootEnabled"] = val

    @property
    def code_integrity_enabled(self):
        """
        Gets and sets the codeIntegrityEnabled
        
        Returns:
            bool:
                The codeIntegrityEnabled
        """
        if "codeIntegrityEnabled" in self._prop_dict:
            return self._prop_dict["codeIntegrityEnabled"]
        else:
            return None

    @code_integrity_enabled.setter
    def code_integrity_enabled(self, val):
        self._prop_dict["codeIntegrityEnabled"] = val

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

