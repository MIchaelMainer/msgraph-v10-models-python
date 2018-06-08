# -*- coding: utf-8 -*- 
'''
# Copyright (c) Microsoft Corporation.  All Rights Reserved.  Licensed under the MIT License.  See License in the project root for license information.
# 
#  This file was generated and any changes will be overwritten.
'''

from __future__ import unicode_literals
from ..model.bit_locker_encryption_method import BitLockerEncryptionMethod
from ..model.configuration_usage import ConfigurationUsage
from ..model.bit_locker_recovery_options import BitLockerRecoveryOptions
from ..one_drive_object_base import OneDriveObjectBase


class BitLockerSystemDrivePolicy(OneDriveObjectBase):

    def __init__(self, prop_dict={}):
        self._prop_dict = prop_dict

    @property
    def encryption_method(self):
        """
        Gets and sets the encryptionMethod
        
        Returns: 
            :class:`BitLockerEncryptionMethod<onedrivesdk.model.bit_locker_encryption_method.BitLockerEncryptionMethod>`:
                The encryptionMethod
        """
        if "encryptionMethod" in self._prop_dict:
            if isinstance(self._prop_dict["encryptionMethod"], OneDriveObjectBase):
                return self._prop_dict["encryptionMethod"]
            else :
                self._prop_dict["encryptionMethod"] = BitLockerEncryptionMethod(self._prop_dict["encryptionMethod"])
                return self._prop_dict["encryptionMethod"]

        return None

    @encryption_method.setter
    def encryption_method(self, val):
        self._prop_dict["encryptionMethod"] = val
    @property
    def startup_authentication_required(self):
        """Gets and sets the startupAuthenticationRequired
        
        Returns: 
            bool:
                The startupAuthenticationRequired
        """
        if "startupAuthenticationRequired" in self._prop_dict:
            return self._prop_dict["startupAuthenticationRequired"]
        else:
            return None

    @startup_authentication_required.setter
    def startup_authentication_required(self, val):
        self._prop_dict["startupAuthenticationRequired"] = val

    @property
    def startup_authentication_block_without_tpm_chip(self):
        """Gets and sets the startupAuthenticationBlockWithoutTpmChip
        
        Returns: 
            bool:
                The startupAuthenticationBlockWithoutTpmChip
        """
        if "startupAuthenticationBlockWithoutTpmChip" in self._prop_dict:
            return self._prop_dict["startupAuthenticationBlockWithoutTpmChip"]
        else:
            return None

    @startup_authentication_block_without_tpm_chip.setter
    def startup_authentication_block_without_tpm_chip(self, val):
        self._prop_dict["startupAuthenticationBlockWithoutTpmChip"] = val

    @property
    def startup_authentication_tpm_usage(self):
        """
        Gets and sets the startupAuthenticationTpmUsage
        
        Returns: 
            :class:`ConfigurationUsage<onedrivesdk.model.configuration_usage.ConfigurationUsage>`:
                The startupAuthenticationTpmUsage
        """
        if "startupAuthenticationTpmUsage" in self._prop_dict:
            if isinstance(self._prop_dict["startupAuthenticationTpmUsage"], OneDriveObjectBase):
                return self._prop_dict["startupAuthenticationTpmUsage"]
            else :
                self._prop_dict["startupAuthenticationTpmUsage"] = ConfigurationUsage(self._prop_dict["startupAuthenticationTpmUsage"])
                return self._prop_dict["startupAuthenticationTpmUsage"]

        return None

    @startup_authentication_tpm_usage.setter
    def startup_authentication_tpm_usage(self, val):
        self._prop_dict["startupAuthenticationTpmUsage"] = val
    @property
    def startup_authentication_tpm_pin_usage(self):
        """
        Gets and sets the startupAuthenticationTpmPinUsage
        
        Returns: 
            :class:`ConfigurationUsage<onedrivesdk.model.configuration_usage.ConfigurationUsage>`:
                The startupAuthenticationTpmPinUsage
        """
        if "startupAuthenticationTpmPinUsage" in self._prop_dict:
            if isinstance(self._prop_dict["startupAuthenticationTpmPinUsage"], OneDriveObjectBase):
                return self._prop_dict["startupAuthenticationTpmPinUsage"]
            else :
                self._prop_dict["startupAuthenticationTpmPinUsage"] = ConfigurationUsage(self._prop_dict["startupAuthenticationTpmPinUsage"])
                return self._prop_dict["startupAuthenticationTpmPinUsage"]

        return None

    @startup_authentication_tpm_pin_usage.setter
    def startup_authentication_tpm_pin_usage(self, val):
        self._prop_dict["startupAuthenticationTpmPinUsage"] = val
    @property
    def startup_authentication_tpm_key_usage(self):
        """
        Gets and sets the startupAuthenticationTpmKeyUsage
        
        Returns: 
            :class:`ConfigurationUsage<onedrivesdk.model.configuration_usage.ConfigurationUsage>`:
                The startupAuthenticationTpmKeyUsage
        """
        if "startupAuthenticationTpmKeyUsage" in self._prop_dict:
            if isinstance(self._prop_dict["startupAuthenticationTpmKeyUsage"], OneDriveObjectBase):
                return self._prop_dict["startupAuthenticationTpmKeyUsage"]
            else :
                self._prop_dict["startupAuthenticationTpmKeyUsage"] = ConfigurationUsage(self._prop_dict["startupAuthenticationTpmKeyUsage"])
                return self._prop_dict["startupAuthenticationTpmKeyUsage"]

        return None

    @startup_authentication_tpm_key_usage.setter
    def startup_authentication_tpm_key_usage(self, val):
        self._prop_dict["startupAuthenticationTpmKeyUsage"] = val
    @property
    def startup_authentication_tpm_pin_and_key_usage(self):
        """
        Gets and sets the startupAuthenticationTpmPinAndKeyUsage
        
        Returns: 
            :class:`ConfigurationUsage<onedrivesdk.model.configuration_usage.ConfigurationUsage>`:
                The startupAuthenticationTpmPinAndKeyUsage
        """
        if "startupAuthenticationTpmPinAndKeyUsage" in self._prop_dict:
            if isinstance(self._prop_dict["startupAuthenticationTpmPinAndKeyUsage"], OneDriveObjectBase):
                return self._prop_dict["startupAuthenticationTpmPinAndKeyUsage"]
            else :
                self._prop_dict["startupAuthenticationTpmPinAndKeyUsage"] = ConfigurationUsage(self._prop_dict["startupAuthenticationTpmPinAndKeyUsage"])
                return self._prop_dict["startupAuthenticationTpmPinAndKeyUsage"]

        return None

    @startup_authentication_tpm_pin_and_key_usage.setter
    def startup_authentication_tpm_pin_and_key_usage(self, val):
        self._prop_dict["startupAuthenticationTpmPinAndKeyUsage"] = val
    @property
    def minimum_pin_length(self):
        """Gets and sets the minimumPinLength
        
        Returns: 
            int:
                The minimumPinLength
        """
        if "minimumPinLength" in self._prop_dict:
            return self._prop_dict["minimumPinLength"]
        else:
            return None

    @minimum_pin_length.setter
    def minimum_pin_length(self, val):
        self._prop_dict["minimumPinLength"] = val

    @property
    def recovery_options(self):
        """
        Gets and sets the recoveryOptions
        
        Returns: 
            :class:`BitLockerRecoveryOptions<onedrivesdk.model.bit_locker_recovery_options.BitLockerRecoveryOptions>`:
                The recoveryOptions
        """
        if "recoveryOptions" in self._prop_dict:
            if isinstance(self._prop_dict["recoveryOptions"], OneDriveObjectBase):
                return self._prop_dict["recoveryOptions"]
            else :
                self._prop_dict["recoveryOptions"] = BitLockerRecoveryOptions(self._prop_dict["recoveryOptions"])
                return self._prop_dict["recoveryOptions"]

        return None

    @recovery_options.setter
    def recovery_options(self, val):
        self._prop_dict["recoveryOptions"] = val
    @property
    def preboot_recovery_enable_message_and_url(self):
        """Gets and sets the prebootRecoveryEnableMessageAndUrl
        
        Returns: 
            bool:
                The prebootRecoveryEnableMessageAndUrl
        """
        if "prebootRecoveryEnableMessageAndUrl" in self._prop_dict:
            return self._prop_dict["prebootRecoveryEnableMessageAndUrl"]
        else:
            return None

    @preboot_recovery_enable_message_and_url.setter
    def preboot_recovery_enable_message_and_url(self, val):
        self._prop_dict["prebootRecoveryEnableMessageAndUrl"] = val

    @property
    def preboot_recovery_message(self):
        """Gets and sets the prebootRecoveryMessage
        
        Returns: 
            str:
                The prebootRecoveryMessage
        """
        if "prebootRecoveryMessage" in self._prop_dict:
            return self._prop_dict["prebootRecoveryMessage"]
        else:
            return None

    @preboot_recovery_message.setter
    def preboot_recovery_message(self, val):
        self._prop_dict["prebootRecoveryMessage"] = val

    @property
    def preboot_recovery_url(self):
        """Gets and sets the prebootRecoveryUrl
        
        Returns: 
            str:
                The prebootRecoveryUrl
        """
        if "prebootRecoveryUrl" in self._prop_dict:
            return self._prop_dict["prebootRecoveryUrl"]
        else:
            return None

    @preboot_recovery_url.setter
    def preboot_recovery_url(self, val):
        self._prop_dict["prebootRecoveryUrl"] = val

