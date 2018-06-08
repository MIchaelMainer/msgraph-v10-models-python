# -*- coding: utf-8 -*- 
'''
# Copyright (c) Microsoft Corporation.  All Rights Reserved.  Licensed under the MIT License.  See License in the project root for license information.
# 
#  This file was generated and any changes will be overwritten.
'''

from __future__ import unicode_literals
from ..model.configuration_usage import ConfigurationUsage
from ..model.bit_locker_recovery_information_type import BitLockerRecoveryInformationType
from ..one_drive_object_base import OneDriveObjectBase


class BitLockerRecoveryOptions(OneDriveObjectBase):

    def __init__(self, prop_dict={}):
        self._prop_dict = prop_dict

    @property
    def block_data_recovery_agent(self):
        """Gets and sets the blockDataRecoveryAgent
        
        Returns: 
            bool:
                The blockDataRecoveryAgent
        """
        if "blockDataRecoveryAgent" in self._prop_dict:
            return self._prop_dict["blockDataRecoveryAgent"]
        else:
            return None

    @block_data_recovery_agent.setter
    def block_data_recovery_agent(self, val):
        self._prop_dict["blockDataRecoveryAgent"] = val

    @property
    def recovery_password_usage(self):
        """
        Gets and sets the recoveryPasswordUsage
        
        Returns: 
            :class:`ConfigurationUsage<onedrivesdk.model.configuration_usage.ConfigurationUsage>`:
                The recoveryPasswordUsage
        """
        if "recoveryPasswordUsage" in self._prop_dict:
            if isinstance(self._prop_dict["recoveryPasswordUsage"], OneDriveObjectBase):
                return self._prop_dict["recoveryPasswordUsage"]
            else :
                self._prop_dict["recoveryPasswordUsage"] = ConfigurationUsage(self._prop_dict["recoveryPasswordUsage"])
                return self._prop_dict["recoveryPasswordUsage"]

        return None

    @recovery_password_usage.setter
    def recovery_password_usage(self, val):
        self._prop_dict["recoveryPasswordUsage"] = val
    @property
    def recovery_key_usage(self):
        """
        Gets and sets the recoveryKeyUsage
        
        Returns: 
            :class:`ConfigurationUsage<onedrivesdk.model.configuration_usage.ConfigurationUsage>`:
                The recoveryKeyUsage
        """
        if "recoveryKeyUsage" in self._prop_dict:
            if isinstance(self._prop_dict["recoveryKeyUsage"], OneDriveObjectBase):
                return self._prop_dict["recoveryKeyUsage"]
            else :
                self._prop_dict["recoveryKeyUsage"] = ConfigurationUsage(self._prop_dict["recoveryKeyUsage"])
                return self._prop_dict["recoveryKeyUsage"]

        return None

    @recovery_key_usage.setter
    def recovery_key_usage(self, val):
        self._prop_dict["recoveryKeyUsage"] = val
    @property
    def hide_recovery_options(self):
        """Gets and sets the hideRecoveryOptions
        
        Returns: 
            bool:
                The hideRecoveryOptions
        """
        if "hideRecoveryOptions" in self._prop_dict:
            return self._prop_dict["hideRecoveryOptions"]
        else:
            return None

    @hide_recovery_options.setter
    def hide_recovery_options(self, val):
        self._prop_dict["hideRecoveryOptions"] = val

    @property
    def enable_recovery_information_save_to_store(self):
        """Gets and sets the enableRecoveryInformationSaveToStore
        
        Returns: 
            bool:
                The enableRecoveryInformationSaveToStore
        """
        if "enableRecoveryInformationSaveToStore" in self._prop_dict:
            return self._prop_dict["enableRecoveryInformationSaveToStore"]
        else:
            return None

    @enable_recovery_information_save_to_store.setter
    def enable_recovery_information_save_to_store(self, val):
        self._prop_dict["enableRecoveryInformationSaveToStore"] = val

    @property
    def recovery_information_to_store(self):
        """
        Gets and sets the recoveryInformationToStore
        
        Returns: 
            :class:`BitLockerRecoveryInformationType<onedrivesdk.model.bit_locker_recovery_information_type.BitLockerRecoveryInformationType>`:
                The recoveryInformationToStore
        """
        if "recoveryInformationToStore" in self._prop_dict:
            if isinstance(self._prop_dict["recoveryInformationToStore"], OneDriveObjectBase):
                return self._prop_dict["recoveryInformationToStore"]
            else :
                self._prop_dict["recoveryInformationToStore"] = BitLockerRecoveryInformationType(self._prop_dict["recoveryInformationToStore"])
                return self._prop_dict["recoveryInformationToStore"]

        return None

    @recovery_information_to_store.setter
    def recovery_information_to_store(self, val):
        self._prop_dict["recoveryInformationToStore"] = val
    @property
    def enable_bit_locker_after_recovery_information_to_store(self):
        """Gets and sets the enableBitLockerAfterRecoveryInformationToStore
        
        Returns: 
            bool:
                The enableBitLockerAfterRecoveryInformationToStore
        """
        if "enableBitLockerAfterRecoveryInformationToStore" in self._prop_dict:
            return self._prop_dict["enableBitLockerAfterRecoveryInformationToStore"]
        else:
            return None

    @enable_bit_locker_after_recovery_information_to_store.setter
    def enable_bit_locker_after_recovery_information_to_store(self, val):
        self._prop_dict["enableBitLockerAfterRecoveryInformationToStore"] = val

