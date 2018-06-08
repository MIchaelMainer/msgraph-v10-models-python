# -*- coding: utf-8 -*- 
'''
# Copyright (c) Microsoft Corporation.  All Rights Reserved.  Licensed under the MIT License.  See License in the project root for license information.
# 
#  This file was generated and any changes will be overwritten.
'''

from __future__ import unicode_literals
from datetime import datetime
from ..one_drive_object_base import OneDriveObjectBase


class DeviceHealthAttestationState(OneDriveObjectBase):

    def __init__(self, prop_dict={}):
        self._prop_dict = prop_dict

    @property
    def last_update_date_time(self):
        """Gets and sets the lastUpdateDateTime
        
        Returns: 
            str:
                The lastUpdateDateTime
        """
        if "lastUpdateDateTime" in self._prop_dict:
            return self._prop_dict["lastUpdateDateTime"]
        else:
            return None

    @last_update_date_time.setter
    def last_update_date_time(self, val):
        self._prop_dict["lastUpdateDateTime"] = val

    @property
    def content_namespace_url(self):
        """Gets and sets the contentNamespaceUrl
        
        Returns: 
            str:
                The contentNamespaceUrl
        """
        if "contentNamespaceUrl" in self._prop_dict:
            return self._prop_dict["contentNamespaceUrl"]
        else:
            return None

    @content_namespace_url.setter
    def content_namespace_url(self, val):
        self._prop_dict["contentNamespaceUrl"] = val

    @property
    def device_health_attestation_status(self):
        """Gets and sets the deviceHealthAttestationStatus
        
        Returns: 
            str:
                The deviceHealthAttestationStatus
        """
        if "deviceHealthAttestationStatus" in self._prop_dict:
            return self._prop_dict["deviceHealthAttestationStatus"]
        else:
            return None

    @device_health_attestation_status.setter
    def device_health_attestation_status(self, val):
        self._prop_dict["deviceHealthAttestationStatus"] = val

    @property
    def content_version(self):
        """Gets and sets the contentVersion
        
        Returns: 
            str:
                The contentVersion
        """
        if "contentVersion" in self._prop_dict:
            return self._prop_dict["contentVersion"]
        else:
            return None

    @content_version.setter
    def content_version(self, val):
        self._prop_dict["contentVersion"] = val

    @property
    def issued_date_time(self):
        """Gets and sets the issuedDateTime
        
        Returns: 
            datetime:
                The issuedDateTime
        """
        if "issuedDateTime" in self._prop_dict:
            return datetime.strptime(self._prop_dict["issuedDateTime"].replace("Z", ""), "%Y-%m-%dT%H:%M:%S.%f")
        else:
            return None

    @issued_date_time.setter
    def issued_date_time(self, val):
        self._prop_dict["issuedDateTime"] = val.isoformat()+"Z"

    @property
    def attestation_identity_key(self):
        """Gets and sets the attestationIdentityKey
        
        Returns: 
            str:
                The attestationIdentityKey
        """
        if "attestationIdentityKey" in self._prop_dict:
            return self._prop_dict["attestationIdentityKey"]
        else:
            return None

    @attestation_identity_key.setter
    def attestation_identity_key(self, val):
        self._prop_dict["attestationIdentityKey"] = val

    @property
    def reset_count(self):
        """Gets and sets the resetCount
        
        Returns: 
            int:
                The resetCount
        """
        if "resetCount" in self._prop_dict:
            return self._prop_dict["resetCount"]
        else:
            return None

    @reset_count.setter
    def reset_count(self, val):
        self._prop_dict["resetCount"] = val

    @property
    def restart_count(self):
        """Gets and sets the restartCount
        
        Returns: 
            int:
                The restartCount
        """
        if "restartCount" in self._prop_dict:
            return self._prop_dict["restartCount"]
        else:
            return None

    @restart_count.setter
    def restart_count(self, val):
        self._prop_dict["restartCount"] = val

    @property
    def data_excution_policy(self):
        """Gets and sets the dataExcutionPolicy
        
        Returns: 
            str:
                The dataExcutionPolicy
        """
        if "dataExcutionPolicy" in self._prop_dict:
            return self._prop_dict["dataExcutionPolicy"]
        else:
            return None

    @data_excution_policy.setter
    def data_excution_policy(self, val):
        self._prop_dict["dataExcutionPolicy"] = val

    @property
    def bit_locker_status(self):
        """Gets and sets the bitLockerStatus
        
        Returns: 
            str:
                The bitLockerStatus
        """
        if "bitLockerStatus" in self._prop_dict:
            return self._prop_dict["bitLockerStatus"]
        else:
            return None

    @bit_locker_status.setter
    def bit_locker_status(self, val):
        self._prop_dict["bitLockerStatus"] = val

    @property
    def boot_manager_version(self):
        """Gets and sets the bootManagerVersion
        
        Returns: 
            str:
                The bootManagerVersion
        """
        if "bootManagerVersion" in self._prop_dict:
            return self._prop_dict["bootManagerVersion"]
        else:
            return None

    @boot_manager_version.setter
    def boot_manager_version(self, val):
        self._prop_dict["bootManagerVersion"] = val

    @property
    def code_integrity_check_version(self):
        """Gets and sets the codeIntegrityCheckVersion
        
        Returns: 
            str:
                The codeIntegrityCheckVersion
        """
        if "codeIntegrityCheckVersion" in self._prop_dict:
            return self._prop_dict["codeIntegrityCheckVersion"]
        else:
            return None

    @code_integrity_check_version.setter
    def code_integrity_check_version(self, val):
        self._prop_dict["codeIntegrityCheckVersion"] = val

    @property
    def secure_boot(self):
        """Gets and sets the secureBoot
        
        Returns: 
            str:
                The secureBoot
        """
        if "secureBoot" in self._prop_dict:
            return self._prop_dict["secureBoot"]
        else:
            return None

    @secure_boot.setter
    def secure_boot(self, val):
        self._prop_dict["secureBoot"] = val

    @property
    def boot_debugging(self):
        """Gets and sets the bootDebugging
        
        Returns: 
            str:
                The bootDebugging
        """
        if "bootDebugging" in self._prop_dict:
            return self._prop_dict["bootDebugging"]
        else:
            return None

    @boot_debugging.setter
    def boot_debugging(self, val):
        self._prop_dict["bootDebugging"] = val

    @property
    def operating_system_kernel_debugging(self):
        """Gets and sets the operatingSystemKernelDebugging
        
        Returns: 
            str:
                The operatingSystemKernelDebugging
        """
        if "operatingSystemKernelDebugging" in self._prop_dict:
            return self._prop_dict["operatingSystemKernelDebugging"]
        else:
            return None

    @operating_system_kernel_debugging.setter
    def operating_system_kernel_debugging(self, val):
        self._prop_dict["operatingSystemKernelDebugging"] = val

    @property
    def code_integrity(self):
        """Gets and sets the codeIntegrity
        
        Returns: 
            str:
                The codeIntegrity
        """
        if "codeIntegrity" in self._prop_dict:
            return self._prop_dict["codeIntegrity"]
        else:
            return None

    @code_integrity.setter
    def code_integrity(self, val):
        self._prop_dict["codeIntegrity"] = val

    @property
    def test_signing(self):
        """Gets and sets the testSigning
        
        Returns: 
            str:
                The testSigning
        """
        if "testSigning" in self._prop_dict:
            return self._prop_dict["testSigning"]
        else:
            return None

    @test_signing.setter
    def test_signing(self, val):
        self._prop_dict["testSigning"] = val

    @property
    def safe_mode(self):
        """Gets and sets the safeMode
        
        Returns: 
            str:
                The safeMode
        """
        if "safeMode" in self._prop_dict:
            return self._prop_dict["safeMode"]
        else:
            return None

    @safe_mode.setter
    def safe_mode(self, val):
        self._prop_dict["safeMode"] = val

    @property
    def windows_pe(self):
        """Gets and sets the windowsPE
        
        Returns: 
            str:
                The windowsPE
        """
        if "windowsPE" in self._prop_dict:
            return self._prop_dict["windowsPE"]
        else:
            return None

    @windows_pe.setter
    def windows_pe(self, val):
        self._prop_dict["windowsPE"] = val

    @property
    def early_launch_anti_malware_driver_protection(self):
        """Gets and sets the earlyLaunchAntiMalwareDriverProtection
        
        Returns: 
            str:
                The earlyLaunchAntiMalwareDriverProtection
        """
        if "earlyLaunchAntiMalwareDriverProtection" in self._prop_dict:
            return self._prop_dict["earlyLaunchAntiMalwareDriverProtection"]
        else:
            return None

    @early_launch_anti_malware_driver_protection.setter
    def early_launch_anti_malware_driver_protection(self, val):
        self._prop_dict["earlyLaunchAntiMalwareDriverProtection"] = val

    @property
    def virtual_secure_mode(self):
        """Gets and sets the virtualSecureMode
        
        Returns: 
            str:
                The virtualSecureMode
        """
        if "virtualSecureMode" in self._prop_dict:
            return self._prop_dict["virtualSecureMode"]
        else:
            return None

    @virtual_secure_mode.setter
    def virtual_secure_mode(self, val):
        self._prop_dict["virtualSecureMode"] = val

    @property
    def pcr_hash_algorithm(self):
        """Gets and sets the pcrHashAlgorithm
        
        Returns: 
            str:
                The pcrHashAlgorithm
        """
        if "pcrHashAlgorithm" in self._prop_dict:
            return self._prop_dict["pcrHashAlgorithm"]
        else:
            return None

    @pcr_hash_algorithm.setter
    def pcr_hash_algorithm(self, val):
        self._prop_dict["pcrHashAlgorithm"] = val

    @property
    def boot_app_security_version(self):
        """Gets and sets the bootAppSecurityVersion
        
        Returns: 
            str:
                The bootAppSecurityVersion
        """
        if "bootAppSecurityVersion" in self._prop_dict:
            return self._prop_dict["bootAppSecurityVersion"]
        else:
            return None

    @boot_app_security_version.setter
    def boot_app_security_version(self, val):
        self._prop_dict["bootAppSecurityVersion"] = val

    @property
    def boot_manager_security_version(self):
        """Gets and sets the bootManagerSecurityVersion
        
        Returns: 
            str:
                The bootManagerSecurityVersion
        """
        if "bootManagerSecurityVersion" in self._prop_dict:
            return self._prop_dict["bootManagerSecurityVersion"]
        else:
            return None

    @boot_manager_security_version.setter
    def boot_manager_security_version(self, val):
        self._prop_dict["bootManagerSecurityVersion"] = val

    @property
    def tpm_version(self):
        """Gets and sets the tpmVersion
        
        Returns: 
            str:
                The tpmVersion
        """
        if "tpmVersion" in self._prop_dict:
            return self._prop_dict["tpmVersion"]
        else:
            return None

    @tpm_version.setter
    def tpm_version(self, val):
        self._prop_dict["tpmVersion"] = val

    @property
    def pcr0(self):
        """Gets and sets the pcr0
        
        Returns: 
            str:
                The pcr0
        """
        if "pcr0" in self._prop_dict:
            return self._prop_dict["pcr0"]
        else:
            return None

    @pcr0.setter
    def pcr0(self, val):
        self._prop_dict["pcr0"] = val

    @property
    def secure_boot_configuration_policy_finger_print(self):
        """Gets and sets the secureBootConfigurationPolicyFingerPrint
        
        Returns: 
            str:
                The secureBootConfigurationPolicyFingerPrint
        """
        if "secureBootConfigurationPolicyFingerPrint" in self._prop_dict:
            return self._prop_dict["secureBootConfigurationPolicyFingerPrint"]
        else:
            return None

    @secure_boot_configuration_policy_finger_print.setter
    def secure_boot_configuration_policy_finger_print(self, val):
        self._prop_dict["secureBootConfigurationPolicyFingerPrint"] = val

    @property
    def code_integrity_policy(self):
        """Gets and sets the codeIntegrityPolicy
        
        Returns: 
            str:
                The codeIntegrityPolicy
        """
        if "codeIntegrityPolicy" in self._prop_dict:
            return self._prop_dict["codeIntegrityPolicy"]
        else:
            return None

    @code_integrity_policy.setter
    def code_integrity_policy(self, val):
        self._prop_dict["codeIntegrityPolicy"] = val

    @property
    def boot_revision_list_info(self):
        """Gets and sets the bootRevisionListInfo
        
        Returns: 
            str:
                The bootRevisionListInfo
        """
        if "bootRevisionListInfo" in self._prop_dict:
            return self._prop_dict["bootRevisionListInfo"]
        else:
            return None

    @boot_revision_list_info.setter
    def boot_revision_list_info(self, val):
        self._prop_dict["bootRevisionListInfo"] = val

    @property
    def operating_system_rev_list_info(self):
        """Gets and sets the operatingSystemRevListInfo
        
        Returns: 
            str:
                The operatingSystemRevListInfo
        """
        if "operatingSystemRevListInfo" in self._prop_dict:
            return self._prop_dict["operatingSystemRevListInfo"]
        else:
            return None

    @operating_system_rev_list_info.setter
    def operating_system_rev_list_info(self, val):
        self._prop_dict["operatingSystemRevListInfo"] = val

    @property
    def health_status_mismatch_info(self):
        """Gets and sets the healthStatusMismatchInfo
        
        Returns: 
            str:
                The healthStatusMismatchInfo
        """
        if "healthStatusMismatchInfo" in self._prop_dict:
            return self._prop_dict["healthStatusMismatchInfo"]
        else:
            return None

    @health_status_mismatch_info.setter
    def health_status_mismatch_info(self, val):
        self._prop_dict["healthStatusMismatchInfo"] = val

    @property
    def health_attestation_supported_status(self):
        """Gets and sets the healthAttestationSupportedStatus
        
        Returns: 
            str:
                The healthAttestationSupportedStatus
        """
        if "healthAttestationSupportedStatus" in self._prop_dict:
            return self._prop_dict["healthAttestationSupportedStatus"]
        else:
            return None

    @health_attestation_supported_status.setter
    def health_attestation_supported_status(self, val):
        self._prop_dict["healthAttestationSupportedStatus"] = val

