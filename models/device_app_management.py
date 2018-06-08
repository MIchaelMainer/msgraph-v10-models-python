# -*- coding: utf-8 -*- 
'''
# Copyright (c) Microsoft Corporation.  All Rights Reserved.  Licensed under the MIT License.  See License in the project root for license information.
# 
#  This file was generated and any changes will be overwritten.
'''

from __future__ import unicode_literals
from ..model.mobile_app import MobileApp
from ..model.mobile_app_category import MobileAppCategory
from ..model.managed_device_mobile_app_configuration import ManagedDeviceMobileAppConfiguration
from ..model.vpp_token import VppToken
from ..model.managed_app_policy import ManagedAppPolicy
from ..model.ios_managed_app_protection import IosManagedAppProtection
from ..model.android_managed_app_protection import AndroidManagedAppProtection
from ..model.default_managed_app_protection import DefaultManagedAppProtection
from ..model.targeted_managed_app_configuration import TargetedManagedAppConfiguration
from ..model.mdm_windows_information_protection_policy import MdmWindowsInformationProtectionPolicy
from ..model.windows_information_protection_policy import WindowsInformationProtectionPolicy
from ..model.managed_app_registration import ManagedAppRegistration
from ..model.managed_app_status import ManagedAppStatus
from ..model.managed_e_book import ManagedEBook
from datetime import datetime
from ..one_drive_object_base import OneDriveObjectBase


class DeviceAppManagement(OneDriveObjectBase):

    def __init__(self, prop_dict={}):
        self._prop_dict = prop_dict

    @property
    def microsoft_store_for_business_last_successful_sync_date_time(self):
        """
        Gets and sets the microsoftStoreForBusinessLastSuccessfulSyncDateTime
        
        Returns:
            datetime:
                The microsoftStoreForBusinessLastSuccessfulSyncDateTime
        """
        if "microsoftStoreForBusinessLastSuccessfulSyncDateTime" in self._prop_dict:
            return datetime.strptime(self._prop_dict["microsoftStoreForBusinessLastSuccessfulSyncDateTime"].replace("Z", ""), "%Y-%m-%dT%H:%M:%S.%f")
        else:
            return None

    @microsoft_store_for_business_last_successful_sync_date_time.setter
    def microsoft_store_for_business_last_successful_sync_date_time(self, val):
        self._prop_dict["microsoftStoreForBusinessLastSuccessfulSyncDateTime"] = val.isoformat()+"Z"

    @property
    def is_enabled_for_microsoft_store_for_business(self):
        """
        Gets and sets the isEnabledForMicrosoftStoreForBusiness
        
        Returns:
            bool:
                The isEnabledForMicrosoftStoreForBusiness
        """
        if "isEnabledForMicrosoftStoreForBusiness" in self._prop_dict:
            return self._prop_dict["isEnabledForMicrosoftStoreForBusiness"]
        else:
            return None

    @is_enabled_for_microsoft_store_for_business.setter
    def is_enabled_for_microsoft_store_for_business(self, val):
        self._prop_dict["isEnabledForMicrosoftStoreForBusiness"] = val

    @property
    def microsoft_store_for_business_language(self):
        """
        Gets and sets the microsoftStoreForBusinessLanguage
        
        Returns:
            str:
                The microsoftStoreForBusinessLanguage
        """
        if "microsoftStoreForBusinessLanguage" in self._prop_dict:
            return self._prop_dict["microsoftStoreForBusinessLanguage"]
        else:
            return None

    @microsoft_store_for_business_language.setter
    def microsoft_store_for_business_language(self, val):
        self._prop_dict["microsoftStoreForBusinessLanguage"] = val

    @property
    def microsoft_store_for_business_last_completed_application_sync_time(self):
        """
        Gets and sets the microsoftStoreForBusinessLastCompletedApplicationSyncTime
        
        Returns:
            datetime:
                The microsoftStoreForBusinessLastCompletedApplicationSyncTime
        """
        if "microsoftStoreForBusinessLastCompletedApplicationSyncTime" in self._prop_dict:
            return datetime.strptime(self._prop_dict["microsoftStoreForBusinessLastCompletedApplicationSyncTime"].replace("Z", ""), "%Y-%m-%dT%H:%M:%S.%f")
        else:
            return None

    @microsoft_store_for_business_last_completed_application_sync_time.setter
    def microsoft_store_for_business_last_completed_application_sync_time(self, val):
        self._prop_dict["microsoftStoreForBusinessLastCompletedApplicationSyncTime"] = val.isoformat()+"Z"

    @property
    def mobile_apps(self):
        """Gets and sets the mobileApps
        
        Returns: 
            :class:`MobileAppsCollectionPage<onedrivesdk.request.mobile_apps_collection.MobileAppsCollectionPage>`:
                The mobileApps
        """
        if "mobileApps" in self._prop_dict:
            return MobileAppsCollectionPage(self._prop_dict["mobileApps"])
        else:
            return None

    @property
    def mobile_app_categories(self):
        """Gets and sets the mobileAppCategories
        
        Returns: 
            :class:`MobileAppCategoriesCollectionPage<onedrivesdk.request.mobile_app_categories_collection.MobileAppCategoriesCollectionPage>`:
                The mobileAppCategories
        """
        if "mobileAppCategories" in self._prop_dict:
            return MobileAppCategoriesCollectionPage(self._prop_dict["mobileAppCategories"])
        else:
            return None

    @property
    def mobile_app_configurations(self):
        """Gets and sets the mobileAppConfigurations
        
        Returns: 
            :class:`MobileAppConfigurationsCollectionPage<onedrivesdk.request.mobile_app_configurations_collection.MobileAppConfigurationsCollectionPage>`:
                The mobileAppConfigurations
        """
        if "mobileAppConfigurations" in self._prop_dict:
            return MobileAppConfigurationsCollectionPage(self._prop_dict["mobileAppConfigurations"])
        else:
            return None

    @property
    def vpp_tokens(self):
        """Gets and sets the vppTokens
        
        Returns: 
            :class:`VppTokensCollectionPage<onedrivesdk.request.vpp_tokens_collection.VppTokensCollectionPage>`:
                The vppTokens
        """
        if "vppTokens" in self._prop_dict:
            return VppTokensCollectionPage(self._prop_dict["vppTokens"])
        else:
            return None

    @property
    def managed_app_policies(self):
        """Gets and sets the managedAppPolicies
        
        Returns: 
            :class:`ManagedAppPoliciesCollectionPage<onedrivesdk.request.managed_app_policies_collection.ManagedAppPoliciesCollectionPage>`:
                The managedAppPolicies
        """
        if "managedAppPolicies" in self._prop_dict:
            return ManagedAppPoliciesCollectionPage(self._prop_dict["managedAppPolicies"])
        else:
            return None

    @property
    def ios_managed_app_protections(self):
        """Gets and sets the iosManagedAppProtections
        
        Returns: 
            :class:`IosManagedAppProtectionsCollectionPage<onedrivesdk.request.ios_managed_app_protections_collection.IosManagedAppProtectionsCollectionPage>`:
                The iosManagedAppProtections
        """
        if "iosManagedAppProtections" in self._prop_dict:
            return IosManagedAppProtectionsCollectionPage(self._prop_dict["iosManagedAppProtections"])
        else:
            return None

    @property
    def android_managed_app_protections(self):
        """Gets and sets the androidManagedAppProtections
        
        Returns: 
            :class:`AndroidManagedAppProtectionsCollectionPage<onedrivesdk.request.android_managed_app_protections_collection.AndroidManagedAppProtectionsCollectionPage>`:
                The androidManagedAppProtections
        """
        if "androidManagedAppProtections" in self._prop_dict:
            return AndroidManagedAppProtectionsCollectionPage(self._prop_dict["androidManagedAppProtections"])
        else:
            return None

    @property
    def default_managed_app_protections(self):
        """Gets and sets the defaultManagedAppProtections
        
        Returns: 
            :class:`DefaultManagedAppProtectionsCollectionPage<onedrivesdk.request.default_managed_app_protections_collection.DefaultManagedAppProtectionsCollectionPage>`:
                The defaultManagedAppProtections
        """
        if "defaultManagedAppProtections" in self._prop_dict:
            return DefaultManagedAppProtectionsCollectionPage(self._prop_dict["defaultManagedAppProtections"])
        else:
            return None

    @property
    def targeted_managed_app_configurations(self):
        """Gets and sets the targetedManagedAppConfigurations
        
        Returns: 
            :class:`TargetedManagedAppConfigurationsCollectionPage<onedrivesdk.request.targeted_managed_app_configurations_collection.TargetedManagedAppConfigurationsCollectionPage>`:
                The targetedManagedAppConfigurations
        """
        if "targetedManagedAppConfigurations" in self._prop_dict:
            return TargetedManagedAppConfigurationsCollectionPage(self._prop_dict["targetedManagedAppConfigurations"])
        else:
            return None

    @property
    def mdm_windows_information_protection_policies(self):
        """Gets and sets the mdmWindowsInformationProtectionPolicies
        
        Returns: 
            :class:`MdmWindowsInformationProtectionPoliciesCollectionPage<onedrivesdk.request.mdm_windows_information_protection_policies_collection.MdmWindowsInformationProtectionPoliciesCollectionPage>`:
                The mdmWindowsInformationProtectionPolicies
        """
        if "mdmWindowsInformationProtectionPolicies" in self._prop_dict:
            return MdmWindowsInformationProtectionPoliciesCollectionPage(self._prop_dict["mdmWindowsInformationProtectionPolicies"])
        else:
            return None

    @property
    def windows_information_protection_policies(self):
        """Gets and sets the windowsInformationProtectionPolicies
        
        Returns: 
            :class:`WindowsInformationProtectionPoliciesCollectionPage<onedrivesdk.request.windows_information_protection_policies_collection.WindowsInformationProtectionPoliciesCollectionPage>`:
                The windowsInformationProtectionPolicies
        """
        if "windowsInformationProtectionPolicies" in self._prop_dict:
            return WindowsInformationProtectionPoliciesCollectionPage(self._prop_dict["windowsInformationProtectionPolicies"])
        else:
            return None

    @property
    def managed_app_registrations(self):
        """Gets and sets the managedAppRegistrations
        
        Returns: 
            :class:`ManagedAppRegistrationsCollectionPage<onedrivesdk.request.managed_app_registrations_collection.ManagedAppRegistrationsCollectionPage>`:
                The managedAppRegistrations
        """
        if "managedAppRegistrations" in self._prop_dict:
            return ManagedAppRegistrationsCollectionPage(self._prop_dict["managedAppRegistrations"])
        else:
            return None

    @property
    def managed_app_statuses(self):
        """Gets and sets the managedAppStatuses
        
        Returns: 
            :class:`ManagedAppStatusesCollectionPage<onedrivesdk.request.managed_app_statuses_collection.ManagedAppStatusesCollectionPage>`:
                The managedAppStatuses
        """
        if "managedAppStatuses" in self._prop_dict:
            return ManagedAppStatusesCollectionPage(self._prop_dict["managedAppStatuses"])
        else:
            return None

    @property
    def managed_e_books(self):
        """Gets and sets the managedEBooks
        
        Returns: 
            :class:`ManagedEBooksCollectionPage<onedrivesdk.request.managed_e_books_collection.ManagedEBooksCollectionPage>`:
                The managedEBooks
        """
        if "managedEBooks" in self._prop_dict:
            return ManagedEBooksCollectionPage(self._prop_dict["managedEBooks"])
        else:
            return None

