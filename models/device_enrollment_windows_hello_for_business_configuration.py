# -*- coding: utf-8 -*- 
'''
# Copyright (c) Microsoft Corporation.  All Rights Reserved.  Licensed under the MIT License.  See License in the project root for license information.
# 
#  This file was generated and any changes will be overwritten.
'''

from __future__ import unicode_literals
from ..model.windows_hello_for_business_pin_usage import WindowsHelloForBusinessPinUsage
from ..model.enablement import Enablement
from ..one_drive_object_base import OneDriveObjectBase


class DeviceEnrollmentWindowsHelloForBusinessConfiguration(OneDriveObjectBase):

    def __init__(self, prop_dict={}):
        self._prop_dict = prop_dict

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
    def pin_maximum_length(self):
        """
        Gets and sets the pinMaximumLength
        
        Returns:
            int:
                The pinMaximumLength
        """
        if "pinMaximumLength" in self._prop_dict:
            return self._prop_dict["pinMaximumLength"]
        else:
            return None

    @pin_maximum_length.setter
    def pin_maximum_length(self, val):
        self._prop_dict["pinMaximumLength"] = val

    @property
    def pin_uppercase_characters_usage(self):
        """
        Gets and sets the pinUppercaseCharactersUsage
        
        Returns: 
            :class:`WindowsHelloForBusinessPinUsage<onedrivesdk.model.windows_hello_for_business_pin_usage.WindowsHelloForBusinessPinUsage>`:
                The pinUppercaseCharactersUsage
        """
        if "pinUppercaseCharactersUsage" in self._prop_dict:
            if isinstance(self._prop_dict["pinUppercaseCharactersUsage"], OneDriveObjectBase):
                return self._prop_dict["pinUppercaseCharactersUsage"]
            else :
                self._prop_dict["pinUppercaseCharactersUsage"] = WindowsHelloForBusinessPinUsage(self._prop_dict["pinUppercaseCharactersUsage"])
                return self._prop_dict["pinUppercaseCharactersUsage"]

        return None

    @pin_uppercase_characters_usage.setter
    def pin_uppercase_characters_usage(self, val):
        self._prop_dict["pinUppercaseCharactersUsage"] = val

    @property
    def pin_lowercase_characters_usage(self):
        """
        Gets and sets the pinLowercaseCharactersUsage
        
        Returns: 
            :class:`WindowsHelloForBusinessPinUsage<onedrivesdk.model.windows_hello_for_business_pin_usage.WindowsHelloForBusinessPinUsage>`:
                The pinLowercaseCharactersUsage
        """
        if "pinLowercaseCharactersUsage" in self._prop_dict:
            if isinstance(self._prop_dict["pinLowercaseCharactersUsage"], OneDriveObjectBase):
                return self._prop_dict["pinLowercaseCharactersUsage"]
            else :
                self._prop_dict["pinLowercaseCharactersUsage"] = WindowsHelloForBusinessPinUsage(self._prop_dict["pinLowercaseCharactersUsage"])
                return self._prop_dict["pinLowercaseCharactersUsage"]

        return None

    @pin_lowercase_characters_usage.setter
    def pin_lowercase_characters_usage(self, val):
        self._prop_dict["pinLowercaseCharactersUsage"] = val

    @property
    def pin_special_characters_usage(self):
        """
        Gets and sets the pinSpecialCharactersUsage
        
        Returns: 
            :class:`WindowsHelloForBusinessPinUsage<onedrivesdk.model.windows_hello_for_business_pin_usage.WindowsHelloForBusinessPinUsage>`:
                The pinSpecialCharactersUsage
        """
        if "pinSpecialCharactersUsage" in self._prop_dict:
            if isinstance(self._prop_dict["pinSpecialCharactersUsage"], OneDriveObjectBase):
                return self._prop_dict["pinSpecialCharactersUsage"]
            else :
                self._prop_dict["pinSpecialCharactersUsage"] = WindowsHelloForBusinessPinUsage(self._prop_dict["pinSpecialCharactersUsage"])
                return self._prop_dict["pinSpecialCharactersUsage"]

        return None

    @pin_special_characters_usage.setter
    def pin_special_characters_usage(self, val):
        self._prop_dict["pinSpecialCharactersUsage"] = val

    @property
    def state(self):
        """
        Gets and sets the state
        
        Returns: 
            :class:`Enablement<onedrivesdk.model.enablement.Enablement>`:
                The state
        """
        if "state" in self._prop_dict:
            if isinstance(self._prop_dict["state"], OneDriveObjectBase):
                return self._prop_dict["state"]
            else :
                self._prop_dict["state"] = Enablement(self._prop_dict["state"])
                return self._prop_dict["state"]

        return None

    @state.setter
    def state(self, val):
        self._prop_dict["state"] = val

    @property
    def security_device_required(self):
        """
        Gets and sets the securityDeviceRequired
        
        Returns:
            bool:
                The securityDeviceRequired
        """
        if "securityDeviceRequired" in self._prop_dict:
            return self._prop_dict["securityDeviceRequired"]
        else:
            return None

    @security_device_required.setter
    def security_device_required(self, val):
        self._prop_dict["securityDeviceRequired"] = val

    @property
    def unlock_with_biometrics_enabled(self):
        """
        Gets and sets the unlockWithBiometricsEnabled
        
        Returns:
            bool:
                The unlockWithBiometricsEnabled
        """
        if "unlockWithBiometricsEnabled" in self._prop_dict:
            return self._prop_dict["unlockWithBiometricsEnabled"]
        else:
            return None

    @unlock_with_biometrics_enabled.setter
    def unlock_with_biometrics_enabled(self, val):
        self._prop_dict["unlockWithBiometricsEnabled"] = val

    @property
    def remote_passport_enabled(self):
        """
        Gets and sets the remotePassportEnabled
        
        Returns:
            bool:
                The remotePassportEnabled
        """
        if "remotePassportEnabled" in self._prop_dict:
            return self._prop_dict["remotePassportEnabled"]
        else:
            return None

    @remote_passport_enabled.setter
    def remote_passport_enabled(self, val):
        self._prop_dict["remotePassportEnabled"] = val

    @property
    def pin_previous_block_count(self):
        """
        Gets and sets the pinPreviousBlockCount
        
        Returns:
            int:
                The pinPreviousBlockCount
        """
        if "pinPreviousBlockCount" in self._prop_dict:
            return self._prop_dict["pinPreviousBlockCount"]
        else:
            return None

    @pin_previous_block_count.setter
    def pin_previous_block_count(self, val):
        self._prop_dict["pinPreviousBlockCount"] = val

    @property
    def pin_expiration_in_days(self):
        """
        Gets and sets the pinExpirationInDays
        
        Returns:
            int:
                The pinExpirationInDays
        """
        if "pinExpirationInDays" in self._prop_dict:
            return self._prop_dict["pinExpirationInDays"]
        else:
            return None

    @pin_expiration_in_days.setter
    def pin_expiration_in_days(self, val):
        self._prop_dict["pinExpirationInDays"] = val

    @property
    def enhanced_biometrics_state(self):
        """
        Gets and sets the enhancedBiometricsState
        
        Returns: 
            :class:`Enablement<onedrivesdk.model.enablement.Enablement>`:
                The enhancedBiometricsState
        """
        if "enhancedBiometricsState" in self._prop_dict:
            if isinstance(self._prop_dict["enhancedBiometricsState"], OneDriveObjectBase):
                return self._prop_dict["enhancedBiometricsState"]
            else :
                self._prop_dict["enhancedBiometricsState"] = Enablement(self._prop_dict["enhancedBiometricsState"])
                return self._prop_dict["enhancedBiometricsState"]

        return None

    @enhanced_biometrics_state.setter
    def enhanced_biometrics_state(self, val):
        self._prop_dict["enhancedBiometricsState"] = val

