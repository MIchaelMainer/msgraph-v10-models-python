# -*- coding: utf-8 -*- 
'''
# Copyright (c) Microsoft Corporation.  All Rights Reserved.  Licensed under the MIT License.  See License in the project root for license information.
# 
#  This file was generated and any changes will be overwritten.
'''

from __future__ import unicode_literals
from ..model.device_management_subscription_state import DeviceManagementSubscriptionState
from ..model.device_management_subscriptions import DeviceManagementSubscriptions
from ..model.managed_device_cleanup_settings import ManagedDeviceCleanupSettings
from ..model.admin_consent import AdminConsent
from ..model.device_protection_overview import DeviceProtectionOverview
from ..model.device_management_settings import DeviceManagementSettings
from ..model.intune_brand import IntuneBrand
from ..model.terms_and_conditions import TermsAndConditions
from ..model.android_for_work_settings import AndroidForWorkSettings
from ..model.android_for_work_app_configuration_schema import AndroidForWorkAppConfigurationSchema
from ..model.android_for_work_enrollment_profile import AndroidForWorkEnrollmentProfile
from ..model.android_managed_store_account_enterprise_settings import AndroidManagedStoreAccountEnterpriseSettings
from ..model.android_managed_store_app_configuration_schema import AndroidManagedStoreAppConfigurationSchema
from ..model.android_device_owner_enrollment_profile import AndroidDeviceOwnerEnrollmentProfile
from ..model.remote_action_audit import RemoteActionAudit
from ..model.apple_push_notification_certificate import ApplePushNotificationCertificate
from ..model.device_management_script import DeviceManagementScript
from ..model.managed_device_overview import ManagedDeviceOverview
from ..model.detected_app import DetectedApp
from ..model.managed_device import ManagedDevice
from ..model.windows_malware_information import WindowsMalwareInformation
from ..model.data_sharing_consent import DataSharingConsent
from ..model.device_configuration import DeviceConfiguration
from ..model.device_compliance_policy import DeviceCompliancePolicy
from ..model.software_update_status_summary import SoftwareUpdateStatusSummary
from ..model.device_compliance_policy_device_state_summary import DeviceCompliancePolicyDeviceStateSummary
from ..model.device_compliance_policy_setting_state_summary import DeviceCompliancePolicySettingStateSummary
from ..model.device_configuration_device_state_summary import DeviceConfigurationDeviceStateSummary
from ..model.device_configuration_user_state_summary import DeviceConfigurationUserStateSummary
from ..model.cart_to_class_association import CartToClassAssociation
from ..model.ios_update_device_status import IosUpdateDeviceStatus
from ..model.ndes_connector import NdesConnector
from ..model.restricted_apps_violation import RestrictedAppsViolation
from ..model.device_category import DeviceCategory
from ..model.device_management_exchange_connector import DeviceManagementExchangeConnector
from ..model.device_enrollment_configuration import DeviceEnrollmentConfiguration
from ..model.device_management_exchange_on_premises_policy import DeviceManagementExchangeOnPremisesPolicy
from ..model.on_premises_conditional_access_settings import OnPremisesConditionalAccessSettings
from ..model.mobile_threat_defense_connector import MobileThreatDefenseConnector
from ..model.device_management_partner import DeviceManagementPartner
from ..model.dep_onboarding_setting import DepOnboardingSetting
from ..model.notification_message_template import NotificationMessageTemplate
from ..model.role_definition import RoleDefinition
from ..model.device_and_app_management_role_assignment import DeviceAndAppManagementRoleAssignment
from ..model.resource_operation import ResourceOperation
from ..model.telecom_expense_management_partner import TelecomExpenseManagementPartner
from ..model.windows_autopilot_settings import WindowsAutopilotSettings
from ..model.windows_autopilot_device_identity import WindowsAutopilotDeviceIdentity
from ..model.windows_autopilot_deployment_profile import WindowsAutopilotDeploymentProfile
from ..model.imported_device_identity import ImportedDeviceIdentity
from ..model.imported_windows_autopilot_device_identity import ImportedWindowsAutopilotDeviceIdentity
from ..model.remote_assistance_partner import RemoteAssistancePartner
from ..model.windows_information_protection_app_learning_summary import WindowsInformationProtectionAppLearningSummary
from ..model.windows_information_protection_network_learning_summary import WindowsInformationProtectionNetworkLearningSummary
from ..model.audit_event import AuditEvent
from ..model.device_management_troubleshooting_event import DeviceManagementTroubleshootingEvent
from datetime import datetime
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
    def subscriptions(self):
        """
        Gets and sets the subscriptions
        
        Returns: 
            :class:`DeviceManagementSubscriptions<onedrivesdk.model.device_management_subscriptions.DeviceManagementSubscriptions>`:
                The subscriptions
        """
        if "subscriptions" in self._prop_dict:
            if isinstance(self._prop_dict["subscriptions"], OneDriveObjectBase):
                return self._prop_dict["subscriptions"]
            else :
                self._prop_dict["subscriptions"] = DeviceManagementSubscriptions(self._prop_dict["subscriptions"])
                return self._prop_dict["subscriptions"]

        return None

    @subscriptions.setter
    def subscriptions(self, val):
        self._prop_dict["subscriptions"] = val

    @property
    def managed_device_cleanup_settings(self):
        """
        Gets and sets the managedDeviceCleanupSettings
        
        Returns: 
            :class:`ManagedDeviceCleanupSettings<onedrivesdk.model.managed_device_cleanup_settings.ManagedDeviceCleanupSettings>`:
                The managedDeviceCleanupSettings
        """
        if "managedDeviceCleanupSettings" in self._prop_dict:
            if isinstance(self._prop_dict["managedDeviceCleanupSettings"], OneDriveObjectBase):
                return self._prop_dict["managedDeviceCleanupSettings"]
            else :
                self._prop_dict["managedDeviceCleanupSettings"] = ManagedDeviceCleanupSettings(self._prop_dict["managedDeviceCleanupSettings"])
                return self._prop_dict["managedDeviceCleanupSettings"]

        return None

    @managed_device_cleanup_settings.setter
    def managed_device_cleanup_settings(self, val):
        self._prop_dict["managedDeviceCleanupSettings"] = val

    @property
    def admin_consent(self):
        """
        Gets and sets the adminConsent
        
        Returns: 
            :class:`AdminConsent<onedrivesdk.model.admin_consent.AdminConsent>`:
                The adminConsent
        """
        if "adminConsent" in self._prop_dict:
            if isinstance(self._prop_dict["adminConsent"], OneDriveObjectBase):
                return self._prop_dict["adminConsent"]
            else :
                self._prop_dict["adminConsent"] = AdminConsent(self._prop_dict["adminConsent"])
                return self._prop_dict["adminConsent"]

        return None

    @admin_consent.setter
    def admin_consent(self, val):
        self._prop_dict["adminConsent"] = val

    @property
    def device_protection_overview(self):
        """
        Gets and sets the deviceProtectionOverview
        
        Returns: 
            :class:`DeviceProtectionOverview<onedrivesdk.model.device_protection_overview.DeviceProtectionOverview>`:
                The deviceProtectionOverview
        """
        if "deviceProtectionOverview" in self._prop_dict:
            if isinstance(self._prop_dict["deviceProtectionOverview"], OneDriveObjectBase):
                return self._prop_dict["deviceProtectionOverview"]
            else :
                self._prop_dict["deviceProtectionOverview"] = DeviceProtectionOverview(self._prop_dict["deviceProtectionOverview"])
                return self._prop_dict["deviceProtectionOverview"]

        return None

    @device_protection_overview.setter
    def device_protection_overview(self, val):
        self._prop_dict["deviceProtectionOverview"] = val

    @property
    def account_move_completion_date_time(self):
        """
        Gets and sets the accountMoveCompletionDateTime
        
        Returns:
            datetime:
                The accountMoveCompletionDateTime
        """
        if "accountMoveCompletionDateTime" in self._prop_dict:
            return datetime.strptime(self._prop_dict["accountMoveCompletionDateTime"].replace("Z", ""), "%Y-%m-%dT%H:%M:%S.%f")
        else:
            return None

    @account_move_completion_date_time.setter
    def account_move_completion_date_time(self, val):
        self._prop_dict["accountMoveCompletionDateTime"] = val.isoformat()+"Z"

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
    def maximum_dep_tokens(self):
        """
        Gets and sets the maximumDepTokens
        
        Returns:
            int:
                The maximumDepTokens
        """
        if "maximumDepTokens" in self._prop_dict:
            return self._prop_dict["maximumDepTokens"]
        else:
            return None

    @maximum_dep_tokens.setter
    def maximum_dep_tokens(self, val):
        self._prop_dict["maximumDepTokens"] = val

    @property
    def intune_account_id(self):
        """
        Gets and sets the intuneAccountId
        
        Returns:
            UUID:
                The intuneAccountId
        """
        if "intuneAccountId" in self._prop_dict:
            return self._prop_dict["intuneAccountId"]
        else:
            return None

    @intune_account_id.setter
    def intune_account_id(self, val):
        self._prop_dict["intuneAccountId"] = val

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
    def android_for_work_settings(self):
        """
        Gets and sets the androidForWorkSettings
        
        Returns: 
            :class:`AndroidForWorkSettings<onedrivesdk.model.android_for_work_settings.AndroidForWorkSettings>`:
                The androidForWorkSettings
        """
        if "androidForWorkSettings" in self._prop_dict:
            if isinstance(self._prop_dict["androidForWorkSettings"], OneDriveObjectBase):
                return self._prop_dict["androidForWorkSettings"]
            else :
                self._prop_dict["androidForWorkSettings"] = AndroidForWorkSettings(self._prop_dict["androidForWorkSettings"])
                return self._prop_dict["androidForWorkSettings"]

        return None

    @android_for_work_settings.setter
    def android_for_work_settings(self, val):
        self._prop_dict["androidForWorkSettings"] = val

    @property
    def android_for_work_app_configuration_schemas(self):
        """Gets and sets the androidForWorkAppConfigurationSchemas
        
        Returns: 
            :class:`AndroidForWorkAppConfigurationSchemasCollectionPage<onedrivesdk.request.android_for_work_app_configuration_schemas_collection.AndroidForWorkAppConfigurationSchemasCollectionPage>`:
                The androidForWorkAppConfigurationSchemas
        """
        if "androidForWorkAppConfigurationSchemas" in self._prop_dict:
            return AndroidForWorkAppConfigurationSchemasCollectionPage(self._prop_dict["androidForWorkAppConfigurationSchemas"])
        else:
            return None

    @property
    def android_for_work_enrollment_profiles(self):
        """Gets and sets the androidForWorkEnrollmentProfiles
        
        Returns: 
            :class:`AndroidForWorkEnrollmentProfilesCollectionPage<onedrivesdk.request.android_for_work_enrollment_profiles_collection.AndroidForWorkEnrollmentProfilesCollectionPage>`:
                The androidForWorkEnrollmentProfiles
        """
        if "androidForWorkEnrollmentProfiles" in self._prop_dict:
            return AndroidForWorkEnrollmentProfilesCollectionPage(self._prop_dict["androidForWorkEnrollmentProfiles"])
        else:
            return None

    @property
    def android_managed_store_account_enterprise_settings(self):
        """
        Gets and sets the androidManagedStoreAccountEnterpriseSettings
        
        Returns: 
            :class:`AndroidManagedStoreAccountEnterpriseSettings<onedrivesdk.model.android_managed_store_account_enterprise_settings.AndroidManagedStoreAccountEnterpriseSettings>`:
                The androidManagedStoreAccountEnterpriseSettings
        """
        if "androidManagedStoreAccountEnterpriseSettings" in self._prop_dict:
            if isinstance(self._prop_dict["androidManagedStoreAccountEnterpriseSettings"], OneDriveObjectBase):
                return self._prop_dict["androidManagedStoreAccountEnterpriseSettings"]
            else :
                self._prop_dict["androidManagedStoreAccountEnterpriseSettings"] = AndroidManagedStoreAccountEnterpriseSettings(self._prop_dict["androidManagedStoreAccountEnterpriseSettings"])
                return self._prop_dict["androidManagedStoreAccountEnterpriseSettings"]

        return None

    @android_managed_store_account_enterprise_settings.setter
    def android_managed_store_account_enterprise_settings(self, val):
        self._prop_dict["androidManagedStoreAccountEnterpriseSettings"] = val

    @property
    def android_managed_store_app_configuration_schemas(self):
        """Gets and sets the androidManagedStoreAppConfigurationSchemas
        
        Returns: 
            :class:`AndroidManagedStoreAppConfigurationSchemasCollectionPage<onedrivesdk.request.android_managed_store_app_configuration_schemas_collection.AndroidManagedStoreAppConfigurationSchemasCollectionPage>`:
                The androidManagedStoreAppConfigurationSchemas
        """
        if "androidManagedStoreAppConfigurationSchemas" in self._prop_dict:
            return AndroidManagedStoreAppConfigurationSchemasCollectionPage(self._prop_dict["androidManagedStoreAppConfigurationSchemas"])
        else:
            return None

    @property
    def android_device_owner_enrollment_profiles(self):
        """Gets and sets the androidDeviceOwnerEnrollmentProfiles
        
        Returns: 
            :class:`AndroidDeviceOwnerEnrollmentProfilesCollectionPage<onedrivesdk.request.android_device_owner_enrollment_profiles_collection.AndroidDeviceOwnerEnrollmentProfilesCollectionPage>`:
                The androidDeviceOwnerEnrollmentProfiles
        """
        if "androidDeviceOwnerEnrollmentProfiles" in self._prop_dict:
            return AndroidDeviceOwnerEnrollmentProfilesCollectionPage(self._prop_dict["androidDeviceOwnerEnrollmentProfiles"])
        else:
            return None

    @property
    def remote_action_audits(self):
        """Gets and sets the remoteActionAudits
        
        Returns: 
            :class:`RemoteActionAuditsCollectionPage<onedrivesdk.request.remote_action_audits_collection.RemoteActionAuditsCollectionPage>`:
                The remoteActionAudits
        """
        if "remoteActionAudits" in self._prop_dict:
            return RemoteActionAuditsCollectionPage(self._prop_dict["remoteActionAudits"])
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
    def device_management_scripts(self):
        """Gets and sets the deviceManagementScripts
        
        Returns: 
            :class:`DeviceManagementScriptsCollectionPage<onedrivesdk.request.device_management_scripts_collection.DeviceManagementScriptsCollectionPage>`:
                The deviceManagementScripts
        """
        if "deviceManagementScripts" in self._prop_dict:
            return DeviceManagementScriptsCollectionPage(self._prop_dict["deviceManagementScripts"])
        else:
            return None

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
    def windows_malware_information(self):
        """Gets and sets the windowsMalwareInformation
        
        Returns: 
            :class:`WindowsMalwareInformationCollectionPage<onedrivesdk.request.windows_malware_information_collection.WindowsMalwareInformationCollectionPage>`:
                The windowsMalwareInformation
        """
        if "windowsMalwareInformation" in self._prop_dict:
            return WindowsMalwareInformationCollectionPage(self._prop_dict["windowsMalwareInformation"])
        else:
            return None

    @property
    def data_sharing_consents(self):
        """Gets and sets the dataSharingConsents
        
        Returns: 
            :class:`DataSharingConsentsCollectionPage<onedrivesdk.request.data_sharing_consents_collection.DataSharingConsentsCollectionPage>`:
                The dataSharingConsents
        """
        if "dataSharingConsents" in self._prop_dict:
            return DataSharingConsentsCollectionPage(self._prop_dict["dataSharingConsents"])
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
    def device_configuration_user_state_summaries(self):
        """
        Gets and sets the deviceConfigurationUserStateSummaries
        
        Returns: 
            :class:`DeviceConfigurationUserStateSummary<onedrivesdk.model.device_configuration_user_state_summary.DeviceConfigurationUserStateSummary>`:
                The deviceConfigurationUserStateSummaries
        """
        if "deviceConfigurationUserStateSummaries" in self._prop_dict:
            if isinstance(self._prop_dict["deviceConfigurationUserStateSummaries"], OneDriveObjectBase):
                return self._prop_dict["deviceConfigurationUserStateSummaries"]
            else :
                self._prop_dict["deviceConfigurationUserStateSummaries"] = DeviceConfigurationUserStateSummary(self._prop_dict["deviceConfigurationUserStateSummaries"])
                return self._prop_dict["deviceConfigurationUserStateSummaries"]

        return None

    @device_configuration_user_state_summaries.setter
    def device_configuration_user_state_summaries(self, val):
        self._prop_dict["deviceConfigurationUserStateSummaries"] = val

    @property
    def cart_to_class_associations(self):
        """Gets and sets the cartToClassAssociations
        
        Returns: 
            :class:`CartToClassAssociationsCollectionPage<onedrivesdk.request.cart_to_class_associations_collection.CartToClassAssociationsCollectionPage>`:
                The cartToClassAssociations
        """
        if "cartToClassAssociations" in self._prop_dict:
            return CartToClassAssociationsCollectionPage(self._prop_dict["cartToClassAssociations"])
        else:
            return None

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
    def ndes_connectors(self):
        """Gets and sets the ndesConnectors
        
        Returns: 
            :class:`NdesConnectorsCollectionPage<onedrivesdk.request.ndes_connectors_collection.NdesConnectorsCollectionPage>`:
                The ndesConnectors
        """
        if "ndesConnectors" in self._prop_dict:
            return NdesConnectorsCollectionPage(self._prop_dict["ndesConnectors"])
        else:
            return None

    @property
    def device_configuration_restricted_apps_violations(self):
        """Gets and sets the deviceConfigurationRestrictedAppsViolations
        
        Returns: 
            :class:`DeviceConfigurationRestrictedAppsViolationsCollectionPage<onedrivesdk.request.device_configuration_restricted_apps_violations_collection.DeviceConfigurationRestrictedAppsViolationsCollectionPage>`:
                The deviceConfigurationRestrictedAppsViolations
        """
        if "deviceConfigurationRestrictedAppsViolations" in self._prop_dict:
            return DeviceConfigurationRestrictedAppsViolationsCollectionPage(self._prop_dict["deviceConfigurationRestrictedAppsViolations"])
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
    def exchange_on_premises_policy(self):
        """
        Gets and sets the exchangeOnPremisesPolicy
        
        Returns: 
            :class:`DeviceManagementExchangeOnPremisesPolicy<onedrivesdk.model.device_management_exchange_on_premises_policy.DeviceManagementExchangeOnPremisesPolicy>`:
                The exchangeOnPremisesPolicy
        """
        if "exchangeOnPremisesPolicy" in self._prop_dict:
            if isinstance(self._prop_dict["exchangeOnPremisesPolicy"], OneDriveObjectBase):
                return self._prop_dict["exchangeOnPremisesPolicy"]
            else :
                self._prop_dict["exchangeOnPremisesPolicy"] = DeviceManagementExchangeOnPremisesPolicy(self._prop_dict["exchangeOnPremisesPolicy"])
                return self._prop_dict["exchangeOnPremisesPolicy"]

        return None

    @exchange_on_premises_policy.setter
    def exchange_on_premises_policy(self, val):
        self._prop_dict["exchangeOnPremisesPolicy"] = val

    @property
    def exchange_on_premises_policies(self):
        """Gets and sets the exchangeOnPremisesPolicies
        
        Returns: 
            :class:`ExchangeOnPremisesPoliciesCollectionPage<onedrivesdk.request.exchange_on_premises_policies_collection.ExchangeOnPremisesPoliciesCollectionPage>`:
                The exchangeOnPremisesPolicies
        """
        if "exchangeOnPremisesPolicies" in self._prop_dict:
            return ExchangeOnPremisesPoliciesCollectionPage(self._prop_dict["exchangeOnPremisesPolicies"])
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
    def dep_onboarding_settings(self):
        """Gets and sets the depOnboardingSettings
        
        Returns: 
            :class:`DepOnboardingSettingsCollectionPage<onedrivesdk.request.dep_onboarding_settings_collection.DepOnboardingSettingsCollectionPage>`:
                The depOnboardingSettings
        """
        if "depOnboardingSettings" in self._prop_dict:
            return DepOnboardingSettingsCollectionPage(self._prop_dict["depOnboardingSettings"])
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
    def windows_autopilot_settings(self):
        """
        Gets and sets the windowsAutopilotSettings
        
        Returns: 
            :class:`WindowsAutopilotSettings<onedrivesdk.model.windows_autopilot_settings.WindowsAutopilotSettings>`:
                The windowsAutopilotSettings
        """
        if "windowsAutopilotSettings" in self._prop_dict:
            if isinstance(self._prop_dict["windowsAutopilotSettings"], OneDriveObjectBase):
                return self._prop_dict["windowsAutopilotSettings"]
            else :
                self._prop_dict["windowsAutopilotSettings"] = WindowsAutopilotSettings(self._prop_dict["windowsAutopilotSettings"])
                return self._prop_dict["windowsAutopilotSettings"]

        return None

    @windows_autopilot_settings.setter
    def windows_autopilot_settings(self, val):
        self._prop_dict["windowsAutopilotSettings"] = val

    @property
    def windows_autopilot_device_identities(self):
        """Gets and sets the windowsAutopilotDeviceIdentities
        
        Returns: 
            :class:`WindowsAutopilotDeviceIdentitiesCollectionPage<onedrivesdk.request.windows_autopilot_device_identities_collection.WindowsAutopilotDeviceIdentitiesCollectionPage>`:
                The windowsAutopilotDeviceIdentities
        """
        if "windowsAutopilotDeviceIdentities" in self._prop_dict:
            return WindowsAutopilotDeviceIdentitiesCollectionPage(self._prop_dict["windowsAutopilotDeviceIdentities"])
        else:
            return None

    @property
    def windows_autopilot_deployment_profiles(self):
        """Gets and sets the windowsAutopilotDeploymentProfiles
        
        Returns: 
            :class:`WindowsAutopilotDeploymentProfilesCollectionPage<onedrivesdk.request.windows_autopilot_deployment_profiles_collection.WindowsAutopilotDeploymentProfilesCollectionPage>`:
                The windowsAutopilotDeploymentProfiles
        """
        if "windowsAutopilotDeploymentProfiles" in self._prop_dict:
            return WindowsAutopilotDeploymentProfilesCollectionPage(self._prop_dict["windowsAutopilotDeploymentProfiles"])
        else:
            return None

    @property
    def imported_device_identities(self):
        """Gets and sets the importedDeviceIdentities
        
        Returns: 
            :class:`ImportedDeviceIdentitiesCollectionPage<onedrivesdk.request.imported_device_identities_collection.ImportedDeviceIdentitiesCollectionPage>`:
                The importedDeviceIdentities
        """
        if "importedDeviceIdentities" in self._prop_dict:
            return ImportedDeviceIdentitiesCollectionPage(self._prop_dict["importedDeviceIdentities"])
        else:
            return None

    @property
    def imported_windows_autopilot_device_identities(self):
        """Gets and sets the importedWindowsAutopilotDeviceIdentities
        
        Returns: 
            :class:`ImportedWindowsAutopilotDeviceIdentitiesCollectionPage<onedrivesdk.request.imported_windows_autopilot_device_identities_collection.ImportedWindowsAutopilotDeviceIdentitiesCollectionPage>`:
                The importedWindowsAutopilotDeviceIdentities
        """
        if "importedWindowsAutopilotDeviceIdentities" in self._prop_dict:
            return ImportedWindowsAutopilotDeviceIdentitiesCollectionPage(self._prop_dict["importedWindowsAutopilotDeviceIdentities"])
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
    def audit_events(self):
        """Gets and sets the auditEvents
        
        Returns: 
            :class:`AuditEventsCollectionPage<onedrivesdk.request.audit_events_collection.AuditEventsCollectionPage>`:
                The auditEvents
        """
        if "auditEvents" in self._prop_dict:
            return AuditEventsCollectionPage(self._prop_dict["auditEvents"])
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

