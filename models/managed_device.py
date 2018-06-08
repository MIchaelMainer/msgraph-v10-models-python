# -*- coding: utf-8 -*- 
'''
# Copyright (c) Microsoft Corporation.  All Rights Reserved.  Licensed under the MIT License.  See License in the project root for license information.
# 
#  This file was generated and any changes will be overwritten.
'''

from __future__ import unicode_literals
from ..model.hardware_information import HardwareInformation
from ..model.owner_type import OwnerType
from ..model.managed_device_owner_type import ManagedDeviceOwnerType
from ..model.device_action_result import DeviceActionResult
from ..model.management_state import ManagementState
from ..model.chassis_type import ChassisType
from ..model.device_type import DeviceType
from ..model.compliance_state import ComplianceState
from ..model.management_agent_type import ManagementAgentType
from ..model.device_enrollment_type import DeviceEnrollmentType
from ..model.lost_mode_state import LostModeState
from ..model.device_registration_state import DeviceRegistrationState
from ..model.device_management_exchange_access_state import DeviceManagementExchangeAccessState
from ..model.device_management_exchange_access_state_reason import DeviceManagementExchangeAccessStateReason
from ..model.configuration_manager_client_enabled_features import ConfigurationManagerClientEnabledFeatures
from ..model.device_health_attestation_state import DeviceHealthAttestationState
from ..model.managed_device_partner_reported_health_state import ManagedDevicePartnerReportedHealthState
from ..model.logged_on_user import LoggedOnUser
from ..model.device_configuration_state import DeviceConfigurationState
from ..model.detected_app import DetectedApp
from ..model.device_category import DeviceCategory
from ..model.windows_protection_state import WindowsProtectionState
from ..model.device_compliance_policy_state import DeviceCompliancePolicyState
from datetime import datetime
from ..one_drive_object_base import OneDriveObjectBase


class ManagedDevice(OneDriveObjectBase):

    def __init__(self, prop_dict={}):
        self._prop_dict = prop_dict

    @property
    def user_id(self):
        """
        Gets and sets the userId
        
        Returns:
            str:
                The userId
        """
        if "userId" in self._prop_dict:
            return self._prop_dict["userId"]
        else:
            return None

    @user_id.setter
    def user_id(self, val):
        self._prop_dict["userId"] = val

    @property
    def device_name(self):
        """
        Gets and sets the deviceName
        
        Returns:
            str:
                The deviceName
        """
        if "deviceName" in self._prop_dict:
            return self._prop_dict["deviceName"]
        else:
            return None

    @device_name.setter
    def device_name(self, val):
        self._prop_dict["deviceName"] = val

    @property
    def hardware_information(self):
        """
        Gets and sets the hardwareInformation
        
        Returns: 
            :class:`HardwareInformation<onedrivesdk.model.hardware_information.HardwareInformation>`:
                The hardwareInformation
        """
        if "hardwareInformation" in self._prop_dict:
            if isinstance(self._prop_dict["hardwareInformation"], OneDriveObjectBase):
                return self._prop_dict["hardwareInformation"]
            else :
                self._prop_dict["hardwareInformation"] = HardwareInformation(self._prop_dict["hardwareInformation"])
                return self._prop_dict["hardwareInformation"]

        return None

    @hardware_information.setter
    def hardware_information(self, val):
        self._prop_dict["hardwareInformation"] = val

    @property
    def owner_type(self):
        """
        Gets and sets the ownerType
        
        Returns: 
            :class:`OwnerType<onedrivesdk.model.owner_type.OwnerType>`:
                The ownerType
        """
        if "ownerType" in self._prop_dict:
            if isinstance(self._prop_dict["ownerType"], OneDriveObjectBase):
                return self._prop_dict["ownerType"]
            else :
                self._prop_dict["ownerType"] = OwnerType(self._prop_dict["ownerType"])
                return self._prop_dict["ownerType"]

        return None

    @owner_type.setter
    def owner_type(self, val):
        self._prop_dict["ownerType"] = val

    @property
    def managed_device_owner_type(self):
        """
        Gets and sets the managedDeviceOwnerType
        
        Returns: 
            :class:`ManagedDeviceOwnerType<onedrivesdk.model.managed_device_owner_type.ManagedDeviceOwnerType>`:
                The managedDeviceOwnerType
        """
        if "managedDeviceOwnerType" in self._prop_dict:
            if isinstance(self._prop_dict["managedDeviceOwnerType"], OneDriveObjectBase):
                return self._prop_dict["managedDeviceOwnerType"]
            else :
                self._prop_dict["managedDeviceOwnerType"] = ManagedDeviceOwnerType(self._prop_dict["managedDeviceOwnerType"])
                return self._prop_dict["managedDeviceOwnerType"]

        return None

    @managed_device_owner_type.setter
    def managed_device_owner_type(self, val):
        self._prop_dict["managedDeviceOwnerType"] = val

    @property
    def device_action_results(self):
        """Gets and sets the deviceActionResults
        
        Returns: 
            :class:`DeviceActionResultsCollectionPage<onedrivesdk.request.device_action_results_collection.DeviceActionResultsCollectionPage>`:
                The deviceActionResults
        """
        if "deviceActionResults" in self._prop_dict:
            return DeviceActionResultsCollectionPage(self._prop_dict["deviceActionResults"])
        else:
            return None

    @property
    def management_state(self):
        """
        Gets and sets the managementState
        
        Returns: 
            :class:`ManagementState<onedrivesdk.model.management_state.ManagementState>`:
                The managementState
        """
        if "managementState" in self._prop_dict:
            if isinstance(self._prop_dict["managementState"], OneDriveObjectBase):
                return self._prop_dict["managementState"]
            else :
                self._prop_dict["managementState"] = ManagementState(self._prop_dict["managementState"])
                return self._prop_dict["managementState"]

        return None

    @management_state.setter
    def management_state(self, val):
        self._prop_dict["managementState"] = val

    @property
    def enrolled_date_time(self):
        """
        Gets and sets the enrolledDateTime
        
        Returns:
            datetime:
                The enrolledDateTime
        """
        if "enrolledDateTime" in self._prop_dict:
            return datetime.strptime(self._prop_dict["enrolledDateTime"].replace("Z", ""), "%Y-%m-%dT%H:%M:%S.%f")
        else:
            return None

    @enrolled_date_time.setter
    def enrolled_date_time(self, val):
        self._prop_dict["enrolledDateTime"] = val.isoformat()+"Z"

    @property
    def last_sync_date_time(self):
        """
        Gets and sets the lastSyncDateTime
        
        Returns:
            datetime:
                The lastSyncDateTime
        """
        if "lastSyncDateTime" in self._prop_dict:
            return datetime.strptime(self._prop_dict["lastSyncDateTime"].replace("Z", ""), "%Y-%m-%dT%H:%M:%S.%f")
        else:
            return None

    @last_sync_date_time.setter
    def last_sync_date_time(self, val):
        self._prop_dict["lastSyncDateTime"] = val.isoformat()+"Z"

    @property
    def chassis_type(self):
        """
        Gets and sets the chassisType
        
        Returns: 
            :class:`ChassisType<onedrivesdk.model.chassis_type.ChassisType>`:
                The chassisType
        """
        if "chassisType" in self._prop_dict:
            if isinstance(self._prop_dict["chassisType"], OneDriveObjectBase):
                return self._prop_dict["chassisType"]
            else :
                self._prop_dict["chassisType"] = ChassisType(self._prop_dict["chassisType"])
                return self._prop_dict["chassisType"]

        return None

    @chassis_type.setter
    def chassis_type(self, val):
        self._prop_dict["chassisType"] = val

    @property
    def operating_system(self):
        """
        Gets and sets the operatingSystem
        
        Returns:
            str:
                The operatingSystem
        """
        if "operatingSystem" in self._prop_dict:
            return self._prop_dict["operatingSystem"]
        else:
            return None

    @operating_system.setter
    def operating_system(self, val):
        self._prop_dict["operatingSystem"] = val

    @property
    def device_type(self):
        """
        Gets and sets the deviceType
        
        Returns: 
            :class:`DeviceType<onedrivesdk.model.device_type.DeviceType>`:
                The deviceType
        """
        if "deviceType" in self._prop_dict:
            if isinstance(self._prop_dict["deviceType"], OneDriveObjectBase):
                return self._prop_dict["deviceType"]
            else :
                self._prop_dict["deviceType"] = DeviceType(self._prop_dict["deviceType"])
                return self._prop_dict["deviceType"]

        return None

    @device_type.setter
    def device_type(self, val):
        self._prop_dict["deviceType"] = val

    @property
    def compliance_state(self):
        """
        Gets and sets the complianceState
        
        Returns: 
            :class:`ComplianceState<onedrivesdk.model.compliance_state.ComplianceState>`:
                The complianceState
        """
        if "complianceState" in self._prop_dict:
            if isinstance(self._prop_dict["complianceState"], OneDriveObjectBase):
                return self._prop_dict["complianceState"]
            else :
                self._prop_dict["complianceState"] = ComplianceState(self._prop_dict["complianceState"])
                return self._prop_dict["complianceState"]

        return None

    @compliance_state.setter
    def compliance_state(self, val):
        self._prop_dict["complianceState"] = val

    @property
    def jail_broken(self):
        """
        Gets and sets the jailBroken
        
        Returns:
            str:
                The jailBroken
        """
        if "jailBroken" in self._prop_dict:
            return self._prop_dict["jailBroken"]
        else:
            return None

    @jail_broken.setter
    def jail_broken(self, val):
        self._prop_dict["jailBroken"] = val

    @property
    def management_agent(self):
        """
        Gets and sets the managementAgent
        
        Returns: 
            :class:`ManagementAgentType<onedrivesdk.model.management_agent_type.ManagementAgentType>`:
                The managementAgent
        """
        if "managementAgent" in self._prop_dict:
            if isinstance(self._prop_dict["managementAgent"], OneDriveObjectBase):
                return self._prop_dict["managementAgent"]
            else :
                self._prop_dict["managementAgent"] = ManagementAgentType(self._prop_dict["managementAgent"])
                return self._prop_dict["managementAgent"]

        return None

    @management_agent.setter
    def management_agent(self, val):
        self._prop_dict["managementAgent"] = val

    @property
    def os_version(self):
        """
        Gets and sets the osVersion
        
        Returns:
            str:
                The osVersion
        """
        if "osVersion" in self._prop_dict:
            return self._prop_dict["osVersion"]
        else:
            return None

    @os_version.setter
    def os_version(self, val):
        self._prop_dict["osVersion"] = val

    @property
    def eas_activated(self):
        """
        Gets and sets the easActivated
        
        Returns:
            bool:
                The easActivated
        """
        if "easActivated" in self._prop_dict:
            return self._prop_dict["easActivated"]
        else:
            return None

    @eas_activated.setter
    def eas_activated(self, val):
        self._prop_dict["easActivated"] = val

    @property
    def eas_device_id(self):
        """
        Gets and sets the easDeviceId
        
        Returns:
            str:
                The easDeviceId
        """
        if "easDeviceId" in self._prop_dict:
            return self._prop_dict["easDeviceId"]
        else:
            return None

    @eas_device_id.setter
    def eas_device_id(self, val):
        self._prop_dict["easDeviceId"] = val

    @property
    def eas_activation_date_time(self):
        """
        Gets and sets the easActivationDateTime
        
        Returns:
            datetime:
                The easActivationDateTime
        """
        if "easActivationDateTime" in self._prop_dict:
            return datetime.strptime(self._prop_dict["easActivationDateTime"].replace("Z", ""), "%Y-%m-%dT%H:%M:%S.%f")
        else:
            return None

    @eas_activation_date_time.setter
    def eas_activation_date_time(self, val):
        self._prop_dict["easActivationDateTime"] = val.isoformat()+"Z"

    @property
    def aad_registered(self):
        """
        Gets and sets the aadRegistered
        
        Returns:
            bool:
                The aadRegistered
        """
        if "aadRegistered" in self._prop_dict:
            return self._prop_dict["aadRegistered"]
        else:
            return None

    @aad_registered.setter
    def aad_registered(self, val):
        self._prop_dict["aadRegistered"] = val

    @property
    def azure_ad_registered(self):
        """
        Gets and sets the azureADRegistered
        
        Returns:
            bool:
                The azureADRegistered
        """
        if "azureADRegistered" in self._prop_dict:
            return self._prop_dict["azureADRegistered"]
        else:
            return None

    @azure_ad_registered.setter
    def azure_ad_registered(self, val):
        self._prop_dict["azureADRegistered"] = val

    @property
    def device_enrollment_type(self):
        """
        Gets and sets the deviceEnrollmentType
        
        Returns: 
            :class:`DeviceEnrollmentType<onedrivesdk.model.device_enrollment_type.DeviceEnrollmentType>`:
                The deviceEnrollmentType
        """
        if "deviceEnrollmentType" in self._prop_dict:
            if isinstance(self._prop_dict["deviceEnrollmentType"], OneDriveObjectBase):
                return self._prop_dict["deviceEnrollmentType"]
            else :
                self._prop_dict["deviceEnrollmentType"] = DeviceEnrollmentType(self._prop_dict["deviceEnrollmentType"])
                return self._prop_dict["deviceEnrollmentType"]

        return None

    @device_enrollment_type.setter
    def device_enrollment_type(self, val):
        self._prop_dict["deviceEnrollmentType"] = val

    @property
    def lost_mode_state(self):
        """
        Gets and sets the lostModeState
        
        Returns: 
            :class:`LostModeState<onedrivesdk.model.lost_mode_state.LostModeState>`:
                The lostModeState
        """
        if "lostModeState" in self._prop_dict:
            if isinstance(self._prop_dict["lostModeState"], OneDriveObjectBase):
                return self._prop_dict["lostModeState"]
            else :
                self._prop_dict["lostModeState"] = LostModeState(self._prop_dict["lostModeState"])
                return self._prop_dict["lostModeState"]

        return None

    @lost_mode_state.setter
    def lost_mode_state(self, val):
        self._prop_dict["lostModeState"] = val

    @property
    def activation_lock_bypass_code(self):
        """
        Gets and sets the activationLockBypassCode
        
        Returns:
            str:
                The activationLockBypassCode
        """
        if "activationLockBypassCode" in self._prop_dict:
            return self._prop_dict["activationLockBypassCode"]
        else:
            return None

    @activation_lock_bypass_code.setter
    def activation_lock_bypass_code(self, val):
        self._prop_dict["activationLockBypassCode"] = val

    @property
    def email_address(self):
        """
        Gets and sets the emailAddress
        
        Returns:
            str:
                The emailAddress
        """
        if "emailAddress" in self._prop_dict:
            return self._prop_dict["emailAddress"]
        else:
            return None

    @email_address.setter
    def email_address(self, val):
        self._prop_dict["emailAddress"] = val

    @property
    def azure_active_directory_device_id(self):
        """
        Gets and sets the azureActiveDirectoryDeviceId
        
        Returns:
            str:
                The azureActiveDirectoryDeviceId
        """
        if "azureActiveDirectoryDeviceId" in self._prop_dict:
            return self._prop_dict["azureActiveDirectoryDeviceId"]
        else:
            return None

    @azure_active_directory_device_id.setter
    def azure_active_directory_device_id(self, val):
        self._prop_dict["azureActiveDirectoryDeviceId"] = val

    @property
    def azure_ad_device_id(self):
        """
        Gets and sets the azureADDeviceId
        
        Returns:
            str:
                The azureADDeviceId
        """
        if "azureADDeviceId" in self._prop_dict:
            return self._prop_dict["azureADDeviceId"]
        else:
            return None

    @azure_ad_device_id.setter
    def azure_ad_device_id(self, val):
        self._prop_dict["azureADDeviceId"] = val

    @property
    def device_registration_state(self):
        """
        Gets and sets the deviceRegistrationState
        
        Returns: 
            :class:`DeviceRegistrationState<onedrivesdk.model.device_registration_state.DeviceRegistrationState>`:
                The deviceRegistrationState
        """
        if "deviceRegistrationState" in self._prop_dict:
            if isinstance(self._prop_dict["deviceRegistrationState"], OneDriveObjectBase):
                return self._prop_dict["deviceRegistrationState"]
            else :
                self._prop_dict["deviceRegistrationState"] = DeviceRegistrationState(self._prop_dict["deviceRegistrationState"])
                return self._prop_dict["deviceRegistrationState"]

        return None

    @device_registration_state.setter
    def device_registration_state(self, val):
        self._prop_dict["deviceRegistrationState"] = val

    @property
    def device_category_display_name(self):
        """
        Gets and sets the deviceCategoryDisplayName
        
        Returns:
            str:
                The deviceCategoryDisplayName
        """
        if "deviceCategoryDisplayName" in self._prop_dict:
            return self._prop_dict["deviceCategoryDisplayName"]
        else:
            return None

    @device_category_display_name.setter
    def device_category_display_name(self, val):
        self._prop_dict["deviceCategoryDisplayName"] = val

    @property
    def is_supervised(self):
        """
        Gets and sets the isSupervised
        
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
    def exchange_last_successful_sync_date_time(self):
        """
        Gets and sets the exchangeLastSuccessfulSyncDateTime
        
        Returns:
            datetime:
                The exchangeLastSuccessfulSyncDateTime
        """
        if "exchangeLastSuccessfulSyncDateTime" in self._prop_dict:
            return datetime.strptime(self._prop_dict["exchangeLastSuccessfulSyncDateTime"].replace("Z", ""), "%Y-%m-%dT%H:%M:%S.%f")
        else:
            return None

    @exchange_last_successful_sync_date_time.setter
    def exchange_last_successful_sync_date_time(self, val):
        self._prop_dict["exchangeLastSuccessfulSyncDateTime"] = val.isoformat()+"Z"

    @property
    def exchange_access_state(self):
        """
        Gets and sets the exchangeAccessState
        
        Returns: 
            :class:`DeviceManagementExchangeAccessState<onedrivesdk.model.device_management_exchange_access_state.DeviceManagementExchangeAccessState>`:
                The exchangeAccessState
        """
        if "exchangeAccessState" in self._prop_dict:
            if isinstance(self._prop_dict["exchangeAccessState"], OneDriveObjectBase):
                return self._prop_dict["exchangeAccessState"]
            else :
                self._prop_dict["exchangeAccessState"] = DeviceManagementExchangeAccessState(self._prop_dict["exchangeAccessState"])
                return self._prop_dict["exchangeAccessState"]

        return None

    @exchange_access_state.setter
    def exchange_access_state(self, val):
        self._prop_dict["exchangeAccessState"] = val

    @property
    def exchange_access_state_reason(self):
        """
        Gets and sets the exchangeAccessStateReason
        
        Returns: 
            :class:`DeviceManagementExchangeAccessStateReason<onedrivesdk.model.device_management_exchange_access_state_reason.DeviceManagementExchangeAccessStateReason>`:
                The exchangeAccessStateReason
        """
        if "exchangeAccessStateReason" in self._prop_dict:
            if isinstance(self._prop_dict["exchangeAccessStateReason"], OneDriveObjectBase):
                return self._prop_dict["exchangeAccessStateReason"]
            else :
                self._prop_dict["exchangeAccessStateReason"] = DeviceManagementExchangeAccessStateReason(self._prop_dict["exchangeAccessStateReason"])
                return self._prop_dict["exchangeAccessStateReason"]

        return None

    @exchange_access_state_reason.setter
    def exchange_access_state_reason(self, val):
        self._prop_dict["exchangeAccessStateReason"] = val

    @property
    def remote_assistance_session_url(self):
        """
        Gets and sets the remoteAssistanceSessionUrl
        
        Returns:
            str:
                The remoteAssistanceSessionUrl
        """
        if "remoteAssistanceSessionUrl" in self._prop_dict:
            return self._prop_dict["remoteAssistanceSessionUrl"]
        else:
            return None

    @remote_assistance_session_url.setter
    def remote_assistance_session_url(self, val):
        self._prop_dict["remoteAssistanceSessionUrl"] = val

    @property
    def remote_assistance_session_error_string(self):
        """
        Gets and sets the remoteAssistanceSessionErrorString
        
        Returns:
            str:
                The remoteAssistanceSessionErrorString
        """
        if "remoteAssistanceSessionErrorString" in self._prop_dict:
            return self._prop_dict["remoteAssistanceSessionErrorString"]
        else:
            return None

    @remote_assistance_session_error_string.setter
    def remote_assistance_session_error_string(self, val):
        self._prop_dict["remoteAssistanceSessionErrorString"] = val

    @property
    def remote_assistance_session_error_details(self):
        """
        Gets and sets the remoteAssistanceSessionErrorDetails
        
        Returns:
            str:
                The remoteAssistanceSessionErrorDetails
        """
        if "remoteAssistanceSessionErrorDetails" in self._prop_dict:
            return self._prop_dict["remoteAssistanceSessionErrorDetails"]
        else:
            return None

    @remote_assistance_session_error_details.setter
    def remote_assistance_session_error_details(self, val):
        self._prop_dict["remoteAssistanceSessionErrorDetails"] = val

    @property
    def is_encrypted(self):
        """
        Gets and sets the isEncrypted
        
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
    def user_principal_name(self):
        """
        Gets and sets the userPrincipalName
        
        Returns:
            str:
                The userPrincipalName
        """
        if "userPrincipalName" in self._prop_dict:
            return self._prop_dict["userPrincipalName"]
        else:
            return None

    @user_principal_name.setter
    def user_principal_name(self, val):
        self._prop_dict["userPrincipalName"] = val

    @property
    def model(self):
        """
        Gets and sets the model
        
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
    def manufacturer(self):
        """
        Gets and sets the manufacturer
        
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
    def imei(self):
        """
        Gets and sets the imei
        
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
    def compliance_grace_period_expiration_date_time(self):
        """
        Gets and sets the complianceGracePeriodExpirationDateTime
        
        Returns:
            datetime:
                The complianceGracePeriodExpirationDateTime
        """
        if "complianceGracePeriodExpirationDateTime" in self._prop_dict:
            return datetime.strptime(self._prop_dict["complianceGracePeriodExpirationDateTime"].replace("Z", ""), "%Y-%m-%dT%H:%M:%S.%f")
        else:
            return None

    @compliance_grace_period_expiration_date_time.setter
    def compliance_grace_period_expiration_date_time(self, val):
        self._prop_dict["complianceGracePeriodExpirationDateTime"] = val.isoformat()+"Z"

    @property
    def serial_number(self):
        """
        Gets and sets the serialNumber
        
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
    def phone_number(self):
        """
        Gets and sets the phoneNumber
        
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
    def android_security_patch_level(self):
        """
        Gets and sets the androidSecurityPatchLevel
        
        Returns:
            str:
                The androidSecurityPatchLevel
        """
        if "androidSecurityPatchLevel" in self._prop_dict:
            return self._prop_dict["androidSecurityPatchLevel"]
        else:
            return None

    @android_security_patch_level.setter
    def android_security_patch_level(self, val):
        self._prop_dict["androidSecurityPatchLevel"] = val

    @property
    def user_display_name(self):
        """
        Gets and sets the userDisplayName
        
        Returns:
            str:
                The userDisplayName
        """
        if "userDisplayName" in self._prop_dict:
            return self._prop_dict["userDisplayName"]
        else:
            return None

    @user_display_name.setter
    def user_display_name(self, val):
        self._prop_dict["userDisplayName"] = val

    @property
    def configuration_manager_client_enabled_features(self):
        """
        Gets and sets the configurationManagerClientEnabledFeatures
        
        Returns: 
            :class:`ConfigurationManagerClientEnabledFeatures<onedrivesdk.model.configuration_manager_client_enabled_features.ConfigurationManagerClientEnabledFeatures>`:
                The configurationManagerClientEnabledFeatures
        """
        if "configurationManagerClientEnabledFeatures" in self._prop_dict:
            if isinstance(self._prop_dict["configurationManagerClientEnabledFeatures"], OneDriveObjectBase):
                return self._prop_dict["configurationManagerClientEnabledFeatures"]
            else :
                self._prop_dict["configurationManagerClientEnabledFeatures"] = ConfigurationManagerClientEnabledFeatures(self._prop_dict["configurationManagerClientEnabledFeatures"])
                return self._prop_dict["configurationManagerClientEnabledFeatures"]

        return None

    @configuration_manager_client_enabled_features.setter
    def configuration_manager_client_enabled_features(self, val):
        self._prop_dict["configurationManagerClientEnabledFeatures"] = val

    @property
    def wi_fi_mac_address(self):
        """
        Gets and sets the wiFiMacAddress
        
        Returns:
            str:
                The wiFiMacAddress
        """
        if "wiFiMacAddress" in self._prop_dict:
            return self._prop_dict["wiFiMacAddress"]
        else:
            return None

    @wi_fi_mac_address.setter
    def wi_fi_mac_address(self, val):
        self._prop_dict["wiFiMacAddress"] = val

    @property
    def device_health_attestation_state(self):
        """
        Gets and sets the deviceHealthAttestationState
        
        Returns: 
            :class:`DeviceHealthAttestationState<onedrivesdk.model.device_health_attestation_state.DeviceHealthAttestationState>`:
                The deviceHealthAttestationState
        """
        if "deviceHealthAttestationState" in self._prop_dict:
            if isinstance(self._prop_dict["deviceHealthAttestationState"], OneDriveObjectBase):
                return self._prop_dict["deviceHealthAttestationState"]
            else :
                self._prop_dict["deviceHealthAttestationState"] = DeviceHealthAttestationState(self._prop_dict["deviceHealthAttestationState"])
                return self._prop_dict["deviceHealthAttestationState"]

        return None

    @device_health_attestation_state.setter
    def device_health_attestation_state(self, val):
        self._prop_dict["deviceHealthAttestationState"] = val

    @property
    def subscriber_carrier(self):
        """
        Gets and sets the subscriberCarrier
        
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
    def meid(self):
        """
        Gets and sets the meid
        
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
    def total_storage_space_in_bytes(self):
        """
        Gets and sets the totalStorageSpaceInBytes
        
        Returns:
            int:
                The totalStorageSpaceInBytes
        """
        if "totalStorageSpaceInBytes" in self._prop_dict:
            return self._prop_dict["totalStorageSpaceInBytes"]
        else:
            return None

    @total_storage_space_in_bytes.setter
    def total_storage_space_in_bytes(self, val):
        self._prop_dict["totalStorageSpaceInBytes"] = val

    @property
    def free_storage_space_in_bytes(self):
        """
        Gets and sets the freeStorageSpaceInBytes
        
        Returns:
            int:
                The freeStorageSpaceInBytes
        """
        if "freeStorageSpaceInBytes" in self._prop_dict:
            return self._prop_dict["freeStorageSpaceInBytes"]
        else:
            return None

    @free_storage_space_in_bytes.setter
    def free_storage_space_in_bytes(self, val):
        self._prop_dict["freeStorageSpaceInBytes"] = val

    @property
    def managed_device_name(self):
        """
        Gets and sets the managedDeviceName
        
        Returns:
            str:
                The managedDeviceName
        """
        if "managedDeviceName" in self._prop_dict:
            return self._prop_dict["managedDeviceName"]
        else:
            return None

    @managed_device_name.setter
    def managed_device_name(self, val):
        self._prop_dict["managedDeviceName"] = val

    @property
    def partner_reported_threat_state(self):
        """
        Gets and sets the partnerReportedThreatState
        
        Returns: 
            :class:`ManagedDevicePartnerReportedHealthState<onedrivesdk.model.managed_device_partner_reported_health_state.ManagedDevicePartnerReportedHealthState>`:
                The partnerReportedThreatState
        """
        if "partnerReportedThreatState" in self._prop_dict:
            if isinstance(self._prop_dict["partnerReportedThreatState"], OneDriveObjectBase):
                return self._prop_dict["partnerReportedThreatState"]
            else :
                self._prop_dict["partnerReportedThreatState"] = ManagedDevicePartnerReportedHealthState(self._prop_dict["partnerReportedThreatState"])
                return self._prop_dict["partnerReportedThreatState"]

        return None

    @partner_reported_threat_state.setter
    def partner_reported_threat_state(self, val):
        self._prop_dict["partnerReportedThreatState"] = val

    @property
    def users_logged_on(self):
        """Gets and sets the usersLoggedOn
        
        Returns: 
            :class:`UsersLoggedOnCollectionPage<onedrivesdk.request.users_logged_on_collection.UsersLoggedOnCollectionPage>`:
                The usersLoggedOn
        """
        if "usersLoggedOn" in self._prop_dict:
            return UsersLoggedOnCollectionPage(self._prop_dict["usersLoggedOn"])
        else:
            return None

    @property
    def prefer_mdm_over_group_policy_applied_date_time(self):
        """
        Gets and sets the preferMdmOverGroupPolicyAppliedDateTime
        
        Returns:
            datetime:
                The preferMdmOverGroupPolicyAppliedDateTime
        """
        if "preferMdmOverGroupPolicyAppliedDateTime" in self._prop_dict:
            return datetime.strptime(self._prop_dict["preferMdmOverGroupPolicyAppliedDateTime"].replace("Z", ""), "%Y-%m-%dT%H:%M:%S.%f")
        else:
            return None

    @prefer_mdm_over_group_policy_applied_date_time.setter
    def prefer_mdm_over_group_policy_applied_date_time(self, val):
        self._prop_dict["preferMdmOverGroupPolicyAppliedDateTime"] = val.isoformat()+"Z"

    @property
    def autopilot_enrolled(self):
        """
        Gets and sets the autopilotEnrolled
        
        Returns:
            bool:
                The autopilotEnrolled
        """
        if "autopilotEnrolled" in self._prop_dict:
            return self._prop_dict["autopilotEnrolled"]
        else:
            return None

    @autopilot_enrolled.setter
    def autopilot_enrolled(self, val):
        self._prop_dict["autopilotEnrolled"] = val

    @property
    def require_user_enrollment_approval(self):
        """
        Gets and sets the requireUserEnrollmentApproval
        
        Returns:
            bool:
                The requireUserEnrollmentApproval
        """
        if "requireUserEnrollmentApproval" in self._prop_dict:
            return self._prop_dict["requireUserEnrollmentApproval"]
        else:
            return None

    @require_user_enrollment_approval.setter
    def require_user_enrollment_approval(self, val):
        self._prop_dict["requireUserEnrollmentApproval"] = val

    @property
    def management_certificate_expiration_date(self):
        """
        Gets and sets the managementCertificateExpirationDate
        
        Returns:
            datetime:
                The managementCertificateExpirationDate
        """
        if "managementCertificateExpirationDate" in self._prop_dict:
            return datetime.strptime(self._prop_dict["managementCertificateExpirationDate"].replace("Z", ""), "%Y-%m-%dT%H:%M:%S.%f")
        else:
            return None

    @management_certificate_expiration_date.setter
    def management_certificate_expiration_date(self, val):
        self._prop_dict["managementCertificateExpirationDate"] = val.isoformat()+"Z"

    @property
    def iccid(self):
        """
        Gets and sets the iccid
        
        Returns:
            str:
                The iccid
        """
        if "iccid" in self._prop_dict:
            return self._prop_dict["iccid"]
        else:
            return None

    @iccid.setter
    def iccid(self, val):
        self._prop_dict["iccid"] = val

    @property
    def udid(self):
        """
        Gets and sets the udid
        
        Returns:
            str:
                The udid
        """
        if "udid" in self._prop_dict:
            return self._prop_dict["udid"]
        else:
            return None

    @udid.setter
    def udid(self, val):
        self._prop_dict["udid"] = val

    @property
    def device_configuration_states(self):
        """Gets and sets the deviceConfigurationStates
        
        Returns: 
            :class:`DeviceConfigurationStatesCollectionPage<onedrivesdk.request.device_configuration_states_collection.DeviceConfigurationStatesCollectionPage>`:
                The deviceConfigurationStates
        """
        if "deviceConfigurationStates" in self._prop_dict:
            return DeviceConfigurationStatesCollectionPage(self._prop_dict["deviceConfigurationStates"])
        else:
            return None

    @property
    def detected_apps(self):
        """Gets and sets the detectedApps
        
        Returns: 
            :class:`DetectedAppsCollectionPage<onedrivesdk.request.detected_apps_collection.DetectedAppsCollectionPage>`:
                The detectedApps
        """
        if "detectedApps" in self._prop_dict:
            return DetectedAppsCollectionPage(self._prop_dict["detectedApps"])
        else:
            return None

    @property
    def device_category(self):
        """
        Gets and sets the deviceCategory
        
        Returns: 
            :class:`DeviceCategory<onedrivesdk.model.device_category.DeviceCategory>`:
                The deviceCategory
        """
        if "deviceCategory" in self._prop_dict:
            if isinstance(self._prop_dict["deviceCategory"], OneDriveObjectBase):
                return self._prop_dict["deviceCategory"]
            else :
                self._prop_dict["deviceCategory"] = DeviceCategory(self._prop_dict["deviceCategory"])
                return self._prop_dict["deviceCategory"]

        return None

    @device_category.setter
    def device_category(self, val):
        self._prop_dict["deviceCategory"] = val

    @property
    def windows_protection_state(self):
        """
        Gets and sets the windowsProtectionState
        
        Returns: 
            :class:`WindowsProtectionState<onedrivesdk.model.windows_protection_state.WindowsProtectionState>`:
                The windowsProtectionState
        """
        if "windowsProtectionState" in self._prop_dict:
            if isinstance(self._prop_dict["windowsProtectionState"], OneDriveObjectBase):
                return self._prop_dict["windowsProtectionState"]
            else :
                self._prop_dict["windowsProtectionState"] = WindowsProtectionState(self._prop_dict["windowsProtectionState"])
                return self._prop_dict["windowsProtectionState"]

        return None

    @windows_protection_state.setter
    def windows_protection_state(self, val):
        self._prop_dict["windowsProtectionState"] = val

    @property
    def device_compliance_policy_states(self):
        """Gets and sets the deviceCompliancePolicyStates
        
        Returns: 
            :class:`DeviceCompliancePolicyStatesCollectionPage<onedrivesdk.request.device_compliance_policy_states_collection.DeviceCompliancePolicyStatesCollectionPage>`:
                The deviceCompliancePolicyStates
        """
        if "deviceCompliancePolicyStates" in self._prop_dict:
            return DeviceCompliancePolicyStatesCollectionPage(self._prop_dict["deviceCompliancePolicyStates"])
        else:
            return None

