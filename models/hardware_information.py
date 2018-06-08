# -*- coding: utf-8 -*- 
'''
# Copyright (c) Microsoft Corporation.  All Rights Reserved.  Licensed under the MIT License.  See License in the project root for license information.
# 
#  This file was generated and any changes will be overwritten.
'''

from __future__ import unicode_literals
from ..model.shared_apple_device_user import SharedAppleDeviceUser
from ..model.device_guard_virtualization_based_security_hardware_requirement_state import DeviceGuardVirtualizationBasedSecurityHardwareRequirementState
from ..model.device_guard_virtualization_based_security_state import DeviceGuardVirtualizationBasedSecurityState
from ..model.device_guard_local_system_authority_credential_guard_state import DeviceGuardLocalSystemAuthorityCredentialGuardState
from ..one_drive_object_base import OneDriveObjectBase


class HardwareInformation(OneDriveObjectBase):

    def __init__(self, prop_dict={}):
        self._prop_dict = prop_dict

    @property
    def serial_number(self):
        """Gets and sets the serialNumber
        
        Returns: 
            str:
                The serialNumber
        """
        if "serialNumber" in self._prop_dict:
            return self._prop_dict["serialNumber"]
        else:
            return None

    @serial_number.setter
    def serial_number(self, val):
        self._prop_dict["serialNumber"] = val

    @property
    def total_storage_space(self):
        """Gets and sets the totalStorageSpace
        
        Returns: 
            int:
                The totalStorageSpace
        """
        if "totalStorageSpace" in self._prop_dict:
            return self._prop_dict["totalStorageSpace"]
        else:
            return None

    @total_storage_space.setter
    def total_storage_space(self, val):
        self._prop_dict["totalStorageSpace"] = val

    @property
    def free_storage_space(self):
        """Gets and sets the freeStorageSpace
        
        Returns: 
            int:
                The freeStorageSpace
        """
        if "freeStorageSpace" in self._prop_dict:
            return self._prop_dict["freeStorageSpace"]
        else:
            return None

    @free_storage_space.setter
    def free_storage_space(self, val):
        self._prop_dict["freeStorageSpace"] = val

    @property
    def imei(self):
        """Gets and sets the imei
        
        Returns: 
            str:
                The imei
        """
        if "imei" in self._prop_dict:
            return self._prop_dict["imei"]
        else:
            return None

    @imei.setter
    def imei(self, val):
        self._prop_dict["imei"] = val

    @property
    def meid(self):
        """Gets and sets the meid
        
        Returns: 
            str:
                The meid
        """
        if "meid" in self._prop_dict:
            return self._prop_dict["meid"]
        else:
            return None

    @meid.setter
    def meid(self, val):
        self._prop_dict["meid"] = val

    @property
    def manufacturer(self):
        """Gets and sets the manufacturer
        
        Returns: 
            str:
                The manufacturer
        """
        if "manufacturer" in self._prop_dict:
            return self._prop_dict["manufacturer"]
        else:
            return None

    @manufacturer.setter
    def manufacturer(self, val):
        self._prop_dict["manufacturer"] = val

    @property
    def model(self):
        """Gets and sets the model
        
        Returns: 
            str:
                The model
        """
        if "model" in self._prop_dict:
            return self._prop_dict["model"]
        else:
            return None

    @model.setter
    def model(self, val):
        self._prop_dict["model"] = val

    @property
    def phone_number(self):
        """Gets and sets the phoneNumber
        
        Returns: 
            str:
                The phoneNumber
        """
        if "phoneNumber" in self._prop_dict:
            return self._prop_dict["phoneNumber"]
        else:
            return None

    @phone_number.setter
    def phone_number(self, val):
        self._prop_dict["phoneNumber"] = val

    @property
    def subscriber_carrier(self):
        """Gets and sets the subscriberCarrier
        
        Returns: 
            str:
                The subscriberCarrier
        """
        if "subscriberCarrier" in self._prop_dict:
            return self._prop_dict["subscriberCarrier"]
        else:
            return None

    @subscriber_carrier.setter
    def subscriber_carrier(self, val):
        self._prop_dict["subscriberCarrier"] = val

    @property
    def cellular_technology(self):
        """Gets and sets the cellularTechnology
        
        Returns: 
            str:
                The cellularTechnology
        """
        if "cellularTechnology" in self._prop_dict:
            return self._prop_dict["cellularTechnology"]
        else:
            return None

    @cellular_technology.setter
    def cellular_technology(self, val):
        self._prop_dict["cellularTechnology"] = val

    @property
    def wifi_mac(self):
        """Gets and sets the wifiMac
        
        Returns: 
            str:
                The wifiMac
        """
        if "wifiMac" in self._prop_dict:
            return self._prop_dict["wifiMac"]
        else:
            return None

    @wifi_mac.setter
    def wifi_mac(self, val):
        self._prop_dict["wifiMac"] = val

    @property
    def operating_system_language(self):
        """Gets and sets the operatingSystemLanguage
        
        Returns: 
            str:
                The operatingSystemLanguage
        """
        if "operatingSystemLanguage" in self._prop_dict:
            return self._prop_dict["operatingSystemLanguage"]
        else:
            return None

    @operating_system_language.setter
    def operating_system_language(self, val):
        self._prop_dict["operatingSystemLanguage"] = val

    @property
    def is_supervised(self):
        """Gets and sets the isSupervised
        
        Returns: 
            bool:
                The isSupervised
        """
        if "isSupervised" in self._prop_dict:
            return self._prop_dict["isSupervised"]
        else:
            return None

    @is_supervised.setter
    def is_supervised(self, val):
        self._prop_dict["isSupervised"] = val

    @property
    def is_encrypted(self):
        """Gets and sets the isEncrypted
        
        Returns: 
            bool:
                The isEncrypted
        """
        if "isEncrypted" in self._prop_dict:
            return self._prop_dict["isEncrypted"]
        else:
            return None

    @is_encrypted.setter
    def is_encrypted(self, val):
        self._prop_dict["isEncrypted"] = val

    @property
    def is_shared_device(self):
        """Gets and sets the isSharedDevice
        
        Returns: 
            bool:
                The isSharedDevice
        """
        if "isSharedDevice" in self._prop_dict:
            return self._prop_dict["isSharedDevice"]
        else:
            return None

    @is_shared_device.setter
    def is_shared_device(self, val):
        self._prop_dict["isSharedDevice"] = val

    @property
    def shared_device_cached_users(self):
        """
        Gets and sets the sharedDeviceCachedUsers
        
        Returns: 
            :class:`SharedAppleDeviceUser<onedrivesdk.model.shared_apple_device_user.SharedAppleDeviceUser>`:
                The sharedDeviceCachedUsers
        """
        if "sharedDeviceCachedUsers" in self._prop_dict:
            if isinstance(self._prop_dict["sharedDeviceCachedUsers"], OneDriveObjectBase):
                return self._prop_dict["sharedDeviceCachedUsers"]
            else :
                self._prop_dict["sharedDeviceCachedUsers"] = SharedAppleDeviceUser(self._prop_dict["sharedDeviceCachedUsers"])
                return self._prop_dict["sharedDeviceCachedUsers"]

        return None

    @shared_device_cached_users.setter
    def shared_device_cached_users(self, val):
        self._prop_dict["sharedDeviceCachedUsers"] = val
    @property
    def tpm_specification_version(self):
        """Gets and sets the tpmSpecificationVersion
        
        Returns: 
            str:
                The tpmSpecificationVersion
        """
        if "tpmSpecificationVersion" in self._prop_dict:
            return self._prop_dict["tpmSpecificationVersion"]
        else:
            return None

    @tpm_specification_version.setter
    def tpm_specification_version(self, val):
        self._prop_dict["tpmSpecificationVersion"] = val

    @property
    def operating_system_edition(self):
        """Gets and sets the operatingSystemEdition
        
        Returns: 
            str:
                The operatingSystemEdition
        """
        if "operatingSystemEdition" in self._prop_dict:
            return self._prop_dict["operatingSystemEdition"]
        else:
            return None

    @operating_system_edition.setter
    def operating_system_edition(self, val):
        self._prop_dict["operatingSystemEdition"] = val

    @property
    def device_full_qualified_domain_name(self):
        """Gets and sets the deviceFullQualifiedDomainName
        
        Returns: 
            str:
                The deviceFullQualifiedDomainName
        """
        if "deviceFullQualifiedDomainName" in self._prop_dict:
            return self._prop_dict["deviceFullQualifiedDomainName"]
        else:
            return None

    @device_full_qualified_domain_name.setter
    def device_full_qualified_domain_name(self, val):
        self._prop_dict["deviceFullQualifiedDomainName"] = val

    @property
    def device_guard_virtualization_based_security_hardware_requirement_state(self):
        """
        Gets and sets the deviceGuardVirtualizationBasedSecurityHardwareRequirementState
        
        Returns: 
            :class:`DeviceGuardVirtualizationBasedSecurityHardwareRequirementState<onedrivesdk.model.device_guard_virtualization_based_security_hardware_requirement_state.DeviceGuardVirtualizationBasedSecurityHardwareRequirementState>`:
                The deviceGuardVirtualizationBasedSecurityHardwareRequirementState
        """
        if "deviceGuardVirtualizationBasedSecurityHardwareRequirementState" in self._prop_dict:
            if isinstance(self._prop_dict["deviceGuardVirtualizationBasedSecurityHardwareRequirementState"], OneDriveObjectBase):
                return self._prop_dict["deviceGuardVirtualizationBasedSecurityHardwareRequirementState"]
            else :
                self._prop_dict["deviceGuardVirtualizationBasedSecurityHardwareRequirementState"] = DeviceGuardVirtualizationBasedSecurityHardwareRequirementState(self._prop_dict["deviceGuardVirtualizationBasedSecurityHardwareRequirementState"])
                return self._prop_dict["deviceGuardVirtualizationBasedSecurityHardwareRequirementState"]

        return None

    @device_guard_virtualization_based_security_hardware_requirement_state.setter
    def device_guard_virtualization_based_security_hardware_requirement_state(self, val):
        self._prop_dict["deviceGuardVirtualizationBasedSecurityHardwareRequirementState"] = val
    @property
    def device_guard_virtualization_based_security_state(self):
        """
        Gets and sets the deviceGuardVirtualizationBasedSecurityState
        
        Returns: 
            :class:`DeviceGuardVirtualizationBasedSecurityState<onedrivesdk.model.device_guard_virtualization_based_security_state.DeviceGuardVirtualizationBasedSecurityState>`:
                The deviceGuardVirtualizationBasedSecurityState
        """
        if "deviceGuardVirtualizationBasedSecurityState" in self._prop_dict:
            if isinstance(self._prop_dict["deviceGuardVirtualizationBasedSecurityState"], OneDriveObjectBase):
                return self._prop_dict["deviceGuardVirtualizationBasedSecurityState"]
            else :
                self._prop_dict["deviceGuardVirtualizationBasedSecurityState"] = DeviceGuardVirtualizationBasedSecurityState(self._prop_dict["deviceGuardVirtualizationBasedSecurityState"])
                return self._prop_dict["deviceGuardVirtualizationBasedSecurityState"]

        return None

    @device_guard_virtualization_based_security_state.setter
    def device_guard_virtualization_based_security_state(self, val):
        self._prop_dict["deviceGuardVirtualizationBasedSecurityState"] = val
    @property
    def device_guard_local_system_authority_credential_guard_state(self):
        """
        Gets and sets the deviceGuardLocalSystemAuthorityCredentialGuardState
        
        Returns: 
            :class:`DeviceGuardLocalSystemAuthorityCredentialGuardState<onedrivesdk.model.device_guard_local_system_authority_credential_guard_state.DeviceGuardLocalSystemAuthorityCredentialGuardState>`:
                The deviceGuardLocalSystemAuthorityCredentialGuardState
        """
        if "deviceGuardLocalSystemAuthorityCredentialGuardState" in self._prop_dict:
            if isinstance(self._prop_dict["deviceGuardLocalSystemAuthorityCredentialGuardState"], OneDriveObjectBase):
                return self._prop_dict["deviceGuardLocalSystemAuthorityCredentialGuardState"]
            else :
                self._prop_dict["deviceGuardLocalSystemAuthorityCredentialGuardState"] = DeviceGuardLocalSystemAuthorityCredentialGuardState(self._prop_dict["deviceGuardLocalSystemAuthorityCredentialGuardState"])
                return self._prop_dict["deviceGuardLocalSystemAuthorityCredentialGuardState"]

        return None

    @device_guard_local_system_authority_credential_guard_state.setter
    def device_guard_local_system_authority_credential_guard_state(self, val):
        self._prop_dict["deviceGuardLocalSystemAuthorityCredentialGuardState"] = val
