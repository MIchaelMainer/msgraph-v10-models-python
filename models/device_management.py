# -*- coding: utf-8 -*- 
'''
# Copyright (c) Microsoft Corporation.  All Rights Reserved.  Licensed under the MIT License.  See License in the project root for license information.
# 
#  This file was generated and any changes will be overwritten.
'''

from __future__ import unicode_literals
from ..model.device_management_subscription_state import DeviceManagementSubscriptionState
from ..model.device_management_settings import DeviceManagementSettings
from ..model.intune_brand import IntuneBrand
from ..model.terms_and_conditions import TermsAndConditions
from ..model.apple_push_notification_certificate import ApplePushNotificationCertificate
from ..model.managed_device_overview import ManagedDeviceOverview
from ..model.detected_app import DetectedApp
from ..model.managed_device import ManagedDevice
from ..model.device_configuration import DeviceConfiguration
from ..model.device_compliance_policy import DeviceCompliancePolicy
from ..model.software_update_status_summary import SoftwareUpdateStatusSummary
from ..model.device_compliance_policy_device_state_summary import DeviceCompliancePolicyDeviceStateSummary
from ..model.device_compliance_policy_setting_state_summary import DeviceCompliancePolicySettingStateSummary
from ..model.device_configuration_device_state_summary import DeviceConfigurationDeviceStateSummary
from ..model.ios_update_device_status import IosUpdateDeviceStatus
from ..model.device_category import DeviceCategory
from ..model.device_management_exchange_connector import DeviceManagementExchangeConnector
from ..model.device_enrollment_configuration import DeviceEnrollmentConfiguration
from ..model.on_premises_conditional_access_settings import OnPremisesConditionalAccessSettings
from ..model.mobile_threat_defense_connector import MobileThreatDefenseConnector
from ..model.device_management_partner import DeviceManagementPartner
from ..model.notification_message_template import NotificationMessageTemplate
from ..model.role_definition import RoleDefinition
from ..model.device_and_app_management_role_assignment import DeviceAndAppManagementRoleAssignment
from ..model.resource_operation import ResourceOperation
from ..model.telecom_expense_management_partner import TelecomExpenseManagementPartner
from ..model.remote_assistance_partner import RemoteAssistancePartner
from ..model.windows_information_protection_app_learning_summary import WindowsInformationProtectionAppLearningSummary
from ..model.windows_information_protection_network_learning_summary import WindowsInformationProtectionNetworkLearningSummary
from ..model.device_management_troubleshooting_event import DeviceManagementTroubleshootingEvent
from ..one_drive_object_base import OneDriveObjectBase


class DeviceManagement(OneDriveObjectBase):

    def __init__(self, prop_dict={}):
        self._prop_dict = prop_dict

    @property
    def subscription_state(self):
        """
        Gets and sets the subscriptionState
        
        Returns: 
            :class:`DeviceManagementSubscriptionState<onedrivesdk.model.device_management_subscription_state.DeviceManagementSubscriptionState>`:
                The subscriptionState
        """
        if "subscriptionState" in self._prop_dict:
            if isinstance(self._prop_dict["subscriptionState"], OneDriveObjectBase):
                return self._prop_dict["subscriptionState"]
            else :
                self._prop_dict["subscriptionState"] = DeviceManagementSubscriptionState(self._prop_dict["subscriptionState"])
                return self._prop_dict["subscriptionState"]

        return None

    @subscription_state.setter
    def subscription_state(self, val):
        self._prop_dict["subscriptionState"] = val

    @property
    def settings(self):
        """
        Gets and sets the settings
        
        Returns: 
            :class:`DeviceManagementSettings<onedrivesdk.model.device_management_settings.DeviceManagementSettings>`:
                The settings
        """
        if "settings" in self._prop_dict:
            if isinstance(self._prop_dict["settings"], OneDriveObjectBase):
                return self._prop_dict["settings"]
            else :
                self._prop_dict["settings"] = DeviceManagementSettings(self._prop_dict["settings"])
                return self._prop_dict["settings"]

        return None

    @settings.setter
    def settings(self, val):
        self._prop_dict["settings"] = val

    @property
    def intune_brand(self):
        """
        Gets and sets the intuneBrand
        
        Returns: 
            :class:`IntuneBrand<onedrivesdk.model.intune_brand.IntuneBrand>`:
                The intuneBrand
        """
        if "intuneBrand" in self._prop_dict:
            if isinstance(self._prop_dict["intuneBrand"], OneDriveObjectBase):
                return self._prop_dict["intuneBrand"]
            else :
                self._prop_dict["intuneBrand"] = IntuneBrand(self._prop_dict["intuneBrand"])
                return self._prop_dict["intuneBrand"]

        return None

    @intune_brand.setter
    def intune_brand(self, val):
        self._prop_dict["intuneBrand"] = val

    @property
    def terms_and_conditions(self):
        """Gets and sets the termsAndConditions
        
        Returns: 
            :class:`TermsAndConditionsCollectionPage<onedrivesdk.request.terms_and_conditions_collection.TermsAndConditionsCollectionPage>`:
                The termsAndConditions
        """
        if "termsAndConditions" in self._prop_dict:
            return TermsAndConditionsCollectionPage(self._prop_dict["termsAndConditions"])
        else:
            return None

    @property
    def apple_push_notification_certificate(self):
        """
        Gets and sets the applePushNotificationCertificate
        
        Returns: 
            :class:`ApplePushNotificationCertificate<onedrivesdk.model.apple_push_notification_certificate.ApplePushNotificationCertificate>`:
                The applePushNotificationCertificate
        """
        if "applePushNotificationCertificate" in self._prop_dict:
            if isinstance(self._prop_dict["applePushNotificationCertificate"], OneDriveObjectBase):
                return self._prop_dict["applePushNotificationCertificate"]
            else :
                self._prop_dict["applePushNotificationCertificate"] = ApplePushNotificationCertificate(self._prop_dict["applePushNotificationCertificate"])
                return self._prop_dict["applePushNotificationCertificate"]

        return None

    @apple_push_notification_certificate.setter
    def apple_push_notification_certificate(self, val):
        self._prop_dict["applePushNotificationCertificate"] = val

    @property
    def managed_device_overview(self):
        """
        Gets and sets the managedDeviceOverview
        
        Returns: 
            :class:`ManagedDeviceOverview<onedrivesdk.model.managed_device_overview.ManagedDeviceOverview>`:
                The managedDeviceOverview
        """
        if "managedDeviceOverview" in self._prop_dict:
            if isinstance(self._prop_dict["managedDeviceOverview"], OneDriveObjectBase):
                return self._prop_dict["managedDeviceOverview"]
            else :
                self._prop_dict["managedDeviceOverview"] = ManagedDeviceOverview(self._prop_dict["managedDeviceOverview"])
                return self._prop_dict["managedDeviceOverview"]

        return None

    @managed_device_overview.setter
    def managed_device_overview(self, val):
        self._prop_dict["managedDeviceOverview"] = val

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
    def managed_devices(self):
        """Gets and sets the managedDevices
        
        Returns: 
            :class:`ManagedDevicesCollectionPage<onedrivesdk.request.managed_devices_collection.ManagedDevicesCollectionPage>`:
                The managedDevices
        """
        if "managedDevices" in self._prop_dict:
            return ManagedDevicesCollectionPage(self._prop_dict["managedDevices"])
        else:
            return None

    @property
    def device_configurations(self):
        """Gets and sets the deviceConfigurations
        
        Returns: 
            :class:`DeviceConfigurationsCollectionPage<onedrivesdk.request.device_configurations_collection.DeviceConfigurationsCollectionPage>`:
                The deviceConfigurations
        """
        if "deviceConfigurations" in self._prop_dict:
            return DeviceConfigurationsCollectionPage(self._prop_dict["deviceConfigurations"])
        else:
            return None

    @property
    def device_compliance_policies(self):
        """Gets and sets the deviceCompliancePolicies
        
        Returns: 
            :class:`DeviceCompliancePoliciesCollectionPage<onedrivesdk.request.device_compliance_policies_collection.DeviceCompliancePoliciesCollectionPage>`:
                The deviceCompliancePolicies
        """
        if "deviceCompliancePolicies" in self._prop_dict:
            return DeviceCompliancePoliciesCollectionPage(self._prop_dict["deviceCompliancePolicies"])
        else:
            return None

    @property
    def software_update_status_summary(self):
        """
        Gets and sets the softwareUpdateStatusSummary
        
        Returns: 
            :class:`SoftwareUpdateStatusSummary<onedrivesdk.model.software_update_status_summary.SoftwareUpdateStatusSummary>`:
                The softwareUpdateStatusSummary
        """
        if "softwareUpdateStatusSummary" in self._prop_dict:
            if isinstance(self._prop_dict["softwareUpdateStatusSummary"], OneDriveObjectBase):
                return self._prop_dict["softwareUpdateStatusSummary"]
            else :
                self._prop_dict["softwareUpdateStatusSummary"] = SoftwareUpdateStatusSummary(self._prop_dict["softwareUpdateStatusSummary"])
                return self._prop_dict["softwareUpdateStatusSummary"]

        return None

    @software_update_status_summary.setter
    def software_update_status_summary(self, val):
        self._prop_dict["softwareUpdateStatusSummary"] = val

    @property
    def device_compliance_policy_device_state_summary(self):
        """
        Gets and sets the deviceCompliancePolicyDeviceStateSummary
        
        Returns: 
            :class:`DeviceCompliancePolicyDeviceStateSummary<onedrivesdk.model.device_compliance_policy_device_state_summary.DeviceCompliancePolicyDeviceStateSummary>`:
                The deviceCompliancePolicyDeviceStateSummary
        """
        if "deviceCompliancePolicyDeviceStateSummary" in self._prop_dict:
            if isinstance(self._prop_dict["deviceCompliancePolicyDeviceStateSummary"], OneDriveObjectBase):
                return self._prop_dict["deviceCompliancePolicyDeviceStateSummary"]
            else :
                self._prop_dict["deviceCompliancePolicyDeviceStateSummary"] = DeviceCompliancePolicyDeviceStateSummary(self._prop_dict["deviceCompliancePolicyDeviceStateSummary"])
                return self._prop_dict["deviceCompliancePolicyDeviceStateSummary"]

        return None

    @device_compliance_policy_device_state_summary.setter
    def device_compliance_policy_device_state_summary(self, val):
        self._prop_dict["deviceCompliancePolicyDeviceStateSummary"] = val

    @property
    def device_compliance_policy_setting_state_summaries(self):
        """Gets and sets the deviceCompliancePolicySettingStateSummaries
        
        Returns: 
            :class:`DeviceCompliancePolicySettingStateSummariesCollectionPage<onedrivesdk.request.device_compliance_policy_setting_state_summaries_collection.DeviceCompliancePolicySettingStateSummariesCollectionPage>`:
                The deviceCompliancePolicySettingStateSummaries
        """
        if "deviceCompliancePolicySettingStateSummaries" in self._prop_dict:
            return DeviceCompliancePolicySettingStateSummariesCollectionPage(self._prop_dict["deviceCompliancePolicySettingStateSummaries"])
        else:
            return None

    @property
    def device_configuration_device_state_summaries(self):
        """
        Gets and sets the deviceConfigurationDeviceStateSummaries
        
        Returns: 
            :class:`DeviceConfigurationDeviceStateSummary<onedrivesdk.model.device_configuration_device_state_summary.DeviceConfigurationDeviceStateSummary>`:
                The deviceConfigurationDeviceStateSummaries
        """
        if "deviceConfigurationDeviceStateSummaries" in self._prop_dict:
            if isinstance(self._prop_dict["deviceConfigurationDeviceStateSummaries"], OneDriveObjectBase):
                return self._prop_dict["deviceConfigurationDeviceStateSummaries"]
            else :
                self._prop_dict["deviceConfigurationDeviceStateSummaries"] = DeviceConfigurationDeviceStateSummary(self._prop_dict["deviceConfigurationDeviceStateSummaries"])
                return self._prop_dict["deviceConfigurationDeviceStateSummaries"]

        return None

    @device_configuration_device_state_summaries.setter
    def device_configuration_device_state_summaries(self, val):
        self._prop_dict["deviceConfigurationDeviceStateSummaries"] = val

    @property
    def ios_update_statuses(self):
        """Gets and sets the iosUpdateStatuses
        
        Returns: 
            :class:`IosUpdateStatusesCollectionPage<onedrivesdk.request.ios_update_statuses_collection.IosUpdateStatusesCollectionPage>`:
                The iosUpdateStatuses
        """
        if "iosUpdateStatuses" in self._prop_dict:
            return IosUpdateStatusesCollectionPage(self._prop_dict["iosUpdateStatuses"])
        else:
            return None

    @property
    def device_categories(self):
        """Gets and sets the deviceCategories
        
        Returns: 
            :class:`DeviceCategoriesCollectionPage<onedrivesdk.request.device_categories_collection.DeviceCategoriesCollectionPage>`:
                The deviceCategories
        """
        if "deviceCategories" in self._prop_dict:
            return DeviceCategoriesCollectionPage(self._prop_dict["deviceCategories"])
        else:
            return None

    @property
    def exchange_connectors(self):
        """Gets and sets the exchangeConnectors
        
        Returns: 
            :class:`ExchangeConnectorsCollectionPage<onedrivesdk.request.exchange_connectors_collection.ExchangeConnectorsCollectionPage>`:
                The exchangeConnectors
        """
        if "exchangeConnectors" in self._prop_dict:
            return ExchangeConnectorsCollectionPage(self._prop_dict["exchangeConnectors"])
        else:
            return None

    @property
    def device_enrollment_configurations(self):
        """Gets and sets the deviceEnrollmentConfigurations
        
        Returns: 
            :class:`DeviceEnrollmentConfigurationsCollectionPage<onedrivesdk.request.device_enrollment_configurations_collection.DeviceEnrollmentConfigurationsCollectionPage>`:
                The deviceEnrollmentConfigurations
        """
        if "deviceEnrollmentConfigurations" in self._prop_dict:
            return DeviceEnrollmentConfigurationsCollectionPage(self._prop_dict["deviceEnrollmentConfigurations"])
        else:
            return None

    @property
    def conditional_access_settings(self):
        """
        Gets and sets the conditionalAccessSettings
        
        Returns: 
            :class:`OnPremisesConditionalAccessSettings<onedrivesdk.model.on_premises_conditional_access_settings.OnPremisesConditionalAccessSettings>`:
                The conditionalAccessSettings
        """
        if "conditionalAccessSettings" in self._prop_dict:
            if isinstance(self._prop_dict["conditionalAccessSettings"], OneDriveObjectBase):
                return self._prop_dict["conditionalAccessSettings"]
            else :
                self._prop_dict["conditionalAccessSettings"] = OnPremisesConditionalAccessSettings(self._prop_dict["conditionalAccessSettings"])
                return self._prop_dict["conditionalAccessSettings"]

        return None

    @conditional_access_settings.setter
    def conditional_access_settings(self, val):
        self._prop_dict["conditionalAccessSettings"] = val

    @property
    def mobile_threat_defense_connectors(self):
        """Gets and sets the mobileThreatDefenseConnectors
        
        Returns: 
            :class:`MobileThreatDefenseConnectorsCollectionPage<onedrivesdk.request.mobile_threat_defense_connectors_collection.MobileThreatDefenseConnectorsCollectionPage>`:
                The mobileThreatDefenseConnectors
        """
        if "mobileThreatDefenseConnectors" in self._prop_dict:
            return MobileThreatDefenseConnectorsCollectionPage(self._prop_dict["mobileThreatDefenseConnectors"])
        else:
            return None

    @property
    def device_management_partners(self):
        """Gets and sets the deviceManagementPartners
        
        Returns: 
            :class:`DeviceManagementPartnersCollectionPage<onedrivesdk.request.device_management_partners_collection.DeviceManagementPartnersCollectionPage>`:
                The deviceManagementPartners
        """
        if "deviceManagementPartners" in self._prop_dict:
            return DeviceManagementPartnersCollectionPage(self._prop_dict["deviceManagementPartners"])
        else:
            return None

    @property
    def notification_message_templates(self):
        """Gets and sets the notificationMessageTemplates
        
        Returns: 
            :class:`NotificationMessageTemplatesCollectionPage<onedrivesdk.request.notification_message_templates_collection.NotificationMessageTemplatesCollectionPage>`:
                The notificationMessageTemplates
        """
        if "notificationMessageTemplates" in self._prop_dict:
            return NotificationMessageTemplatesCollectionPage(self._prop_dict["notificationMessageTemplates"])
        else:
            return None

    @property
    def role_definitions(self):
        """Gets and sets the roleDefinitions
        
        Returns: 
            :class:`RoleDefinitionsCollectionPage<onedrivesdk.request.role_definitions_collection.RoleDefinitionsCollectionPage>`:
                The roleDefinitions
        """
        if "roleDefinitions" in self._prop_dict:
            return RoleDefinitionsCollectionPage(self._prop_dict["roleDefinitions"])
        else:
            return None

    @property
    def role_assignments(self):
        """Gets and sets the roleAssignments
        
        Returns: 
            :class:`RoleAssignmentsCollectionPage<onedrivesdk.request.role_assignments_collection.RoleAssignmentsCollectionPage>`:
                The roleAssignments
        """
        if "roleAssignments" in self._prop_dict:
            return RoleAssignmentsCollectionPage(self._prop_dict["roleAssignments"])
        else:
            return None

    @property
    def resource_operations(self):
        """Gets and sets the resourceOperations
        
        Returns: 
            :class:`ResourceOperationsCollectionPage<onedrivesdk.request.resource_operations_collection.ResourceOperationsCollectionPage>`:
                The resourceOperations
        """
        if "resourceOperations" in self._prop_dict:
            return ResourceOperationsCollectionPage(self._prop_dict["resourceOperations"])
        else:
            return None

    @property
    def telecom_expense_management_partners(self):
        """Gets and sets the telecomExpenseManagementPartners
        
        Returns: 
            :class:`TelecomExpenseManagementPartnersCollectionPage<onedrivesdk.request.telecom_expense_management_partners_collection.TelecomExpenseManagementPartnersCollectionPage>`:
                The telecomExpenseManagementPartners
        """
        if "telecomExpenseManagementPartners" in self._prop_dict:
            return TelecomExpenseManagementPartnersCollectionPage(self._prop_dict["telecomExpenseManagementPartners"])
        else:
            return None

    @property
    def remote_assistance_partners(self):
        """Gets and sets the remoteAssistancePartners
        
        Returns: 
            :class:`RemoteAssistancePartnersCollectionPage<onedrivesdk.request.remote_assistance_partners_collection.RemoteAssistancePartnersCollectionPage>`:
                The remoteAssistancePartners
        """
        if "remoteAssistancePartners" in self._prop_dict:
            return RemoteAssistancePartnersCollectionPage(self._prop_dict["remoteAssistancePartners"])
        else:
            return None

    @property
    def windows_information_protection_app_learning_summaries(self):
        """Gets and sets the windowsInformationProtectionAppLearningSummaries
        
        Returns: 
            :class:`WindowsInformationProtectionAppLearningSummariesCollectionPage<onedrivesdk.request.windows_information_protection_app_learning_summaries_collection.WindowsInformationProtectionAppLearningSummariesCollectionPage>`:
                The windowsInformationProtectionAppLearningSummaries
        """
        if "windowsInformationProtectionAppLearningSummaries" in self._prop_dict:
            return WindowsInformationProtectionAppLearningSummariesCollectionPage(self._prop_dict["windowsInformationProtectionAppLearningSummaries"])
        else:
            return None

    @property
    def windows_information_protection_network_learning_summaries(self):
        """Gets and sets the windowsInformationProtectionNetworkLearningSummaries
        
        Returns: 
            :class:`WindowsInformationProtectionNetworkLearningSummariesCollectionPage<onedrivesdk.request.windows_information_protection_network_learning_summaries_collection.WindowsInformationProtectionNetworkLearningSummariesCollectionPage>`:
                The windowsInformationProtectionNetworkLearningSummaries
        """
        if "windowsInformationProtectionNetworkLearningSummaries" in self._prop_dict:
            return WindowsInformationProtectionNetworkLearningSummariesCollectionPage(self._prop_dict["windowsInformationProtectionNetworkLearningSummaries"])
        else:
            return None

    @property
    def troubleshooting_events(self):
        """Gets and sets the troubleshootingEvents
        
        Returns: 
            :class:`TroubleshootingEventsCollectionPage<onedrivesdk.request.troubleshooting_events_collection.TroubleshootingEventsCollectionPage>`:
                The troubleshootingEvents
        """
        if "troubleshootingEvents" in self._prop_dict:
            return TroubleshootingEventsCollectionPage(self._prop_dict["troubleshootingEvents"])
        else:
            return None

