# -*- coding: utf-8 -*- 
'''
# Copyright (c) Microsoft Corporation.  All Rights Reserved.  Licensed under the MIT License.  See License in the project root for license information.
# 
#  This file was generated and any changes will be overwritten.
'''

from __future__ import unicode_literals
from ..model.windows_information_protection_pin_character_requirements import WindowsInformationProtectionPinCharacterRequirements
from ..one_drive_object_base import OneDriveObjectBase


class WindowsInformationProtectionPolicy(OneDriveObjectBase):

    def __init__(self, prop_dict={}):
        self._prop_dict = prop_dict

    @property
    def revoke_on_mdm_handoff_disabled(self):
        """
        Gets and sets the revokeOnMdmHandoffDisabled
        
        Returns:
            bool:
                The revokeOnMdmHandoffDisabled
        """
        if "revokeOnMdmHandoffDisabled" in self._prop_dict:
            return self._prop_dict["revokeOnMdmHandoffDisabled"]
        else:
            return None

    @revoke_on_mdm_handoff_disabled.setter
    def revoke_on_mdm_handoff_disabled(self, val):
        self._prop_dict["revokeOnMdmHandoffDisabled"] = val

    @property
    def mdm_enrollment_url(self):
        """
        Gets and sets the mdmEnrollmentUrl
        
        Returns:
            str:
                The mdmEnrollmentUrl
        """
        if "mdmEnrollmentUrl" in self._prop_dict:
            return self._prop_dict["mdmEnrollmentUrl"]
        else:
            return None

    @mdm_enrollment_url.setter
    def mdm_enrollment_url(self, val):
        self._prop_dict["mdmEnrollmentUrl"] = val

    @property
    def windows_hello_for_business_blocked(self):
        """
        Gets and sets the windowsHelloForBusinessBlocked
        
        Returns:
            bool:
                The windowsHelloForBusinessBlocked
        """
        if "windowsHelloForBusinessBlocked" in self._prop_dict:
            return self._prop_dict["windowsHelloForBusinessBlocked"]
        else:
            return None

    @windows_hello_for_business_blocked.setter
    def windows_hello_for_business_blocked(self, val):
        self._prop_dict["windowsHelloForBusinessBlocked"] = val

    @property
    def pin_minimum_length(self):
        """
        Gets and sets the pinMinimumLength
        
        Returns:
            int:
                The pinMinimumLength
        """
        if "pinMinimumLength" in self._prop_dict:
            return self._prop_dict["pinMinimumLength"]
        else:
            return None

    @pin_minimum_length.setter
    def pin_minimum_length(self, val):
        self._prop_dict["pinMinimumLength"] = val

    @property
    def pin_uppercase_letters(self):
        """
        Gets and sets the pinUppercaseLetters
        
        Returns: 
            :class:`WindowsInformationProtectionPinCharacterRequirements<onedrivesdk.model.windows_information_protection_pin_character_requirements.WindowsInformationProtectionPinCharacterRequirements>`:
                The pinUppercaseLetters
        """
        if "pinUppercaseLetters" in self._prop_dict:
            if isinstance(self._prop_dict["pinUppercaseLetters"], OneDriveObjectBase):
                return self._prop_dict["pinUppercaseLetters"]
            else :
                self._prop_dict["pinUppercaseLetters"] = WindowsInformationProtectionPinCharacterRequirements(self._prop_dict["pinUppercaseLetters"])
                return self._prop_dict["pinUppercaseLetters"]

        return None

    @pin_uppercase_letters.setter
    def pin_uppercase_letters(self, val):
        self._prop_dict["pinUppercaseLetters"] = val

    @property
    def pin_lowercase_letters(self):
        """
        Gets and sets the pinLowercaseLetters
        
        Returns: 
            :class:`WindowsInformationProtectionPinCharacterRequirements<onedrivesdk.model.windows_information_protection_pin_character_requirements.WindowsInformationProtectionPinCharacterRequirements>`:
                The pinLowercaseLetters
        """
        if "pinLowercaseLetters" in self._prop_dict:
            if isinstance(self._prop_dict["pinLowercaseLetters"], OneDriveObjectBase):
                return self._prop_dict["pinLowercaseLetters"]
            else :
                self._prop_dict["pinLowercaseLetters"] = WindowsInformationProtectionPinCharacterRequirements(self._prop_dict["pinLowercaseLetters"])
                return self._prop_dict["pinLowercaseLetters"]

        return None

    @pin_lowercase_letters.setter
    def pin_lowercase_letters(self, val):
        self._prop_dict["pinLowercaseLetters"] = val

    @property
    def pin_special_characters(self):
        """
        Gets and sets the pinSpecialCharacters
        
        Returns: 
            :class:`WindowsInformationProtectionPinCharacterRequirements<onedrivesdk.model.windows_information_protection_pin_character_requirements.WindowsInformationProtectionPinCharacterRequirements>`:
                The pinSpecialCharacters
        """
        if "pinSpecialCharacters" in self._prop_dict:
            if isinstance(self._prop_dict["pinSpecialCharacters"], OneDriveObjectBase):
                return self._prop_dict["pinSpecialCharacters"]
            else :
                self._prop_dict["pinSpecialCharacters"] = WindowsInformationProtectionPinCharacterRequirements(self._prop_dict["pinSpecialCharacters"])
                return self._prop_dict["pinSpecialCharacters"]

        return None

    @pin_special_characters.setter
    def pin_special_characters(self, val):
        self._prop_dict["pinSpecialCharacters"] = val

    @property
    def pin_expiration_days(self):
        """
        Gets and sets the pinExpirationDays
        
        Returns:
            int:
                The pinExpirationDays
        """
        if "pinExpirationDays" in self._prop_dict:
            return self._prop_dict["pinExpirationDays"]
        else:
            return None

    @pin_expiration_days.setter
    def pin_expiration_days(self, val):
        self._prop_dict["pinExpirationDays"] = val

    @property
    def number_of_past_pins_remembered(self):
        """
        Gets and sets the numberOfPastPinsRemembered
        
        Returns:
            int:
                The numberOfPastPinsRemembered
        """
        if "numberOfPastPinsRemembered" in self._prop_dict:
            return self._prop_dict["numberOfPastPinsRemembered"]
        else:
            return None

    @number_of_past_pins_remembered.setter
    def number_of_past_pins_remembered(self, val):
        self._prop_dict["numberOfPastPinsRemembered"] = val

    @property
    def password_maximum_attempt_count(self):
        """
        Gets and sets the passwordMaximumAttemptCount
        
        Returns:
            int:
                The passwordMaximumAttemptCount
        """
        if "passwordMaximumAttemptCount" in self._prop_dict:
            return self._prop_dict["passwordMaximumAttemptCount"]
        else:
            return None

    @password_maximum_attempt_count.setter
    def password_maximum_attempt_count(self, val):
        self._prop_dict["passwordMaximumAttemptCount"] = val

    @property
    def minutes_of_inactivity_before_device_lock(self):
        """
        Gets and sets the minutesOfInactivityBeforeDeviceLock
        
        Returns:
            int:
                The minutesOfInactivityBeforeDeviceLock
        """
        if "minutesOfInactivityBeforeDeviceLock" in self._prop_dict:
            return self._prop_dict["minutesOfInactivityBeforeDeviceLock"]
        else:
            return None

    @minutes_of_inactivity_before_device_lock.setter
    def minutes_of_inactivity_before_device_lock(self, val):
        self._prop_dict["minutesOfInactivityBeforeDeviceLock"] = val

    @property
    def days_without_contact_before_unenroll(self):
        """
        Gets and sets the daysWithoutContactBeforeUnenroll
        
        Returns:
            int:
                The daysWithoutContactBeforeUnenroll
        """
        if "daysWithoutContactBeforeUnenroll" in self._prop_dict:
            return self._prop_dict["daysWithoutContactBeforeUnenroll"]
        else:
            return None

    @days_without_contact_before_unenroll.setter
    def days_without_contact_before_unenroll(self, val):
        self._prop_dict["daysWithoutContactBeforeUnenroll"] = val

