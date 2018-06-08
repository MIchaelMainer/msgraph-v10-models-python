# -*- coding: utf-8 -*- 
'''
# Copyright (c) Microsoft Corporation.  All Rights Reserved.  Licensed under the MIT License.  See License in the project root for license information.
# 
#  This file was generated and any changes will be overwritten.
'''

from __future__ import unicode_literals
from ..model.windows_information_protection_enforcement_level import WindowsInformationProtectionEnforcementLevel
from ..model.windows_information_protection_resource_collection import WindowsInformationProtectionResourceCollection
from ..model.windows_information_protection_data_recovery_certificate import WindowsInformationProtectionDataRecoveryCertificate
from ..model.windows_information_protection_app import WindowsInformationProtectionApp
from ..model.windows_information_protection_proxied_domain_collection import WindowsInformationProtectionProxiedDomainCollection
from ..model.windows_information_protection_ip_range_collection import WindowsInformationProtectionIPRangeCollection
from ..model.windows_information_protection_app_locker_file import WindowsInformationProtectionAppLockerFile
from ..model.targeted_managed_app_policy_assignment import TargetedManagedAppPolicyAssignment
from ..one_drive_object_base import OneDriveObjectBase


class WindowsInformationProtection(OneDriveObjectBase):

    def __init__(self, prop_dict={}):
        self._prop_dict = prop_dict

    @property
    def enforcement_level(self):
        """
        Gets and sets the enforcementLevel
        
        Returns: 
            :class:`WindowsInformationProtectionEnforcementLevel<onedrivesdk.model.windows_information_protection_enforcement_level.WindowsInformationProtectionEnforcementLevel>`:
                The enforcementLevel
        """
        if "enforcementLevel" in self._prop_dict:
            if isinstance(self._prop_dict["enforcementLevel"], OneDriveObjectBase):
                return self._prop_dict["enforcementLevel"]
            else :
                self._prop_dict["enforcementLevel"] = WindowsInformationProtectionEnforcementLevel(self._prop_dict["enforcementLevel"])
                return self._prop_dict["enforcementLevel"]

        return None

    @enforcement_level.setter
    def enforcement_level(self, val):
        self._prop_dict["enforcementLevel"] = val

    @property
    def enterprise_domain(self):
        """
        Gets and sets the enterpriseDomain
        
        Returns:
            str:
                The enterpriseDomain
        """
        if "enterpriseDomain" in self._prop_dict:
            return self._prop_dict["enterpriseDomain"]
        else:
            return None

    @enterprise_domain.setter
    def enterprise_domain(self, val):
        self._prop_dict["enterpriseDomain"] = val

    @property
    def enterprise_protected_domain_names(self):
        """Gets and sets the enterpriseProtectedDomainNames
        
        Returns: 
            :class:`EnterpriseProtectedDomainNamesCollectionPage<onedrivesdk.request.enterprise_protected_domain_names_collection.EnterpriseProtectedDomainNamesCollectionPage>`:
                The enterpriseProtectedDomainNames
        """
        if "enterpriseProtectedDomainNames" in self._prop_dict:
            return EnterpriseProtectedDomainNamesCollectionPage(self._prop_dict["enterpriseProtectedDomainNames"])
        else:
            return None

    @property
    def protection_under_lock_config_required(self):
        """
        Gets and sets the protectionUnderLockConfigRequired
        
        Returns:
            bool:
                The protectionUnderLockConfigRequired
        """
        if "protectionUnderLockConfigRequired" in self._prop_dict:
            return self._prop_dict["protectionUnderLockConfigRequired"]
        else:
            return None

    @protection_under_lock_config_required.setter
    def protection_under_lock_config_required(self, val):
        self._prop_dict["protectionUnderLockConfigRequired"] = val

    @property
    def data_recovery_certificate(self):
        """
        Gets and sets the dataRecoveryCertificate
        
        Returns: 
            :class:`WindowsInformationProtectionDataRecoveryCertificate<onedrivesdk.model.windows_information_protection_data_recovery_certificate.WindowsInformationProtectionDataRecoveryCertificate>`:
                The dataRecoveryCertificate
        """
        if "dataRecoveryCertificate" in self._prop_dict:
            if isinstance(self._prop_dict["dataRecoveryCertificate"], OneDriveObjectBase):
                return self._prop_dict["dataRecoveryCertificate"]
            else :
                self._prop_dict["dataRecoveryCertificate"] = WindowsInformationProtectionDataRecoveryCertificate(self._prop_dict["dataRecoveryCertificate"])
                return self._prop_dict["dataRecoveryCertificate"]

        return None

    @data_recovery_certificate.setter
    def data_recovery_certificate(self, val):
        self._prop_dict["dataRecoveryCertificate"] = val

    @property
    def revoke_on_unenroll_disabled(self):
        """
        Gets and sets the revokeOnUnenrollDisabled
        
        Returns:
            bool:
                The revokeOnUnenrollDisabled
        """
        if "revokeOnUnenrollDisabled" in self._prop_dict:
            return self._prop_dict["revokeOnUnenrollDisabled"]
        else:
            return None

    @revoke_on_unenroll_disabled.setter
    def revoke_on_unenroll_disabled(self, val):
        self._prop_dict["revokeOnUnenrollDisabled"] = val

    @property
    def rights_management_services_template_id(self):
        """
        Gets and sets the rightsManagementServicesTemplateId
        
        Returns:
            UUID:
                The rightsManagementServicesTemplateId
        """
        if "rightsManagementServicesTemplateId" in self._prop_dict:
            return self._prop_dict["rightsManagementServicesTemplateId"]
        else:
            return None

    @rights_management_services_template_id.setter
    def rights_management_services_template_id(self, val):
        self._prop_dict["rightsManagementServicesTemplateId"] = val

    @property
    def azure_rights_management_services_allowed(self):
        """
        Gets and sets the azureRightsManagementServicesAllowed
        
        Returns:
            bool:
                The azureRightsManagementServicesAllowed
        """
        if "azureRightsManagementServicesAllowed" in self._prop_dict:
            return self._prop_dict["azureRightsManagementServicesAllowed"]
        else:
            return None

    @azure_rights_management_services_allowed.setter
    def azure_rights_management_services_allowed(self, val):
        self._prop_dict["azureRightsManagementServicesAllowed"] = val

    @property
    def icons_visible(self):
        """
        Gets and sets the iconsVisible
        
        Returns:
            bool:
                The iconsVisible
        """
        if "iconsVisible" in self._prop_dict:
            return self._prop_dict["iconsVisible"]
        else:
            return None

    @icons_visible.setter
    def icons_visible(self, val):
        self._prop_dict["iconsVisible"] = val

    @property
    def protected_apps(self):
        """Gets and sets the protectedApps
        
        Returns: 
            :class:`ProtectedAppsCollectionPage<onedrivesdk.request.protected_apps_collection.ProtectedAppsCollectionPage>`:
                The protectedApps
        """
        if "protectedApps" in self._prop_dict:
            return ProtectedAppsCollectionPage(self._prop_dict["protectedApps"])
        else:
            return None

    @property
    def exempt_apps(self):
        """Gets and sets the exemptApps
        
        Returns: 
            :class:`ExemptAppsCollectionPage<onedrivesdk.request.exempt_apps_collection.ExemptAppsCollectionPage>`:
                The exemptApps
        """
        if "exemptApps" in self._prop_dict:
            return ExemptAppsCollectionPage(self._prop_dict["exemptApps"])
        else:
            return None

    @property
    def enterprise_network_domain_names(self):
        """Gets and sets the enterpriseNetworkDomainNames
        
        Returns: 
            :class:`EnterpriseNetworkDomainNamesCollectionPage<onedrivesdk.request.enterprise_network_domain_names_collection.EnterpriseNetworkDomainNamesCollectionPage>`:
                The enterpriseNetworkDomainNames
        """
        if "enterpriseNetworkDomainNames" in self._prop_dict:
            return EnterpriseNetworkDomainNamesCollectionPage(self._prop_dict["enterpriseNetworkDomainNames"])
        else:
            return None

    @property
    def enterprise_proxied_domains(self):
        """Gets and sets the enterpriseProxiedDomains
        
        Returns: 
            :class:`EnterpriseProxiedDomainsCollectionPage<onedrivesdk.request.enterprise_proxied_domains_collection.EnterpriseProxiedDomainsCollectionPage>`:
                The enterpriseProxiedDomains
        """
        if "enterpriseProxiedDomains" in self._prop_dict:
            return EnterpriseProxiedDomainsCollectionPage(self._prop_dict["enterpriseProxiedDomains"])
        else:
            return None

    @property
    def enterprise_ip_ranges(self):
        """Gets and sets the enterpriseIPRanges
        
        Returns: 
            :class:`EnterpriseIPRangesCollectionPage<onedrivesdk.request.enterprise_ip_ranges_collection.EnterpriseIPRangesCollectionPage>`:
                The enterpriseIPRanges
        """
        if "enterpriseIPRanges" in self._prop_dict:
            return EnterpriseIPRangesCollectionPage(self._prop_dict["enterpriseIPRanges"])
        else:
            return None

    @property
    def enterprise_ip_ranges_are_authoritative(self):
        """
        Gets and sets the enterpriseIPRangesAreAuthoritative
        
        Returns:
            bool:
                The enterpriseIPRangesAreAuthoritative
        """
        if "enterpriseIPRangesAreAuthoritative" in self._prop_dict:
            return self._prop_dict["enterpriseIPRangesAreAuthoritative"]
        else:
            return None

    @enterprise_ip_ranges_are_authoritative.setter
    def enterprise_ip_ranges_are_authoritative(self, val):
        self._prop_dict["enterpriseIPRangesAreAuthoritative"] = val

    @property
    def enterprise_proxy_servers(self):
        """Gets and sets the enterpriseProxyServers
        
        Returns: 
            :class:`EnterpriseProxyServersCollectionPage<onedrivesdk.request.enterprise_proxy_servers_collection.EnterpriseProxyServersCollectionPage>`:
                The enterpriseProxyServers
        """
        if "enterpriseProxyServers" in self._prop_dict:
            return EnterpriseProxyServersCollectionPage(self._prop_dict["enterpriseProxyServers"])
        else:
            return None

    @property
    def enterprise_internal_proxy_servers(self):
        """Gets and sets the enterpriseInternalProxyServers
        
        Returns: 
            :class:`EnterpriseInternalProxyServersCollectionPage<onedrivesdk.request.enterprise_internal_proxy_servers_collection.EnterpriseInternalProxyServersCollectionPage>`:
                The enterpriseInternalProxyServers
        """
        if "enterpriseInternalProxyServers" in self._prop_dict:
            return EnterpriseInternalProxyServersCollectionPage(self._prop_dict["enterpriseInternalProxyServers"])
        else:
            return None

    @property
    def enterprise_proxy_servers_are_authoritative(self):
        """
        Gets and sets the enterpriseProxyServersAreAuthoritative
        
        Returns:
            bool:
                The enterpriseProxyServersAreAuthoritative
        """
        if "enterpriseProxyServersAreAuthoritative" in self._prop_dict:
            return self._prop_dict["enterpriseProxyServersAreAuthoritative"]
        else:
            return None

    @enterprise_proxy_servers_are_authoritative.setter
    def enterprise_proxy_servers_are_authoritative(self, val):
        self._prop_dict["enterpriseProxyServersAreAuthoritative"] = val

    @property
    def neutral_domain_resources(self):
        """Gets and sets the neutralDomainResources
        
        Returns: 
            :class:`NeutralDomainResourcesCollectionPage<onedrivesdk.request.neutral_domain_resources_collection.NeutralDomainResourcesCollectionPage>`:
                The neutralDomainResources
        """
        if "neutralDomainResources" in self._prop_dict:
            return NeutralDomainResourcesCollectionPage(self._prop_dict["neutralDomainResources"])
        else:
            return None

    @property
    def indexing_encrypted_stores_or_items_blocked(self):
        """
        Gets and sets the indexingEncryptedStoresOrItemsBlocked
        
        Returns:
            bool:
                The indexingEncryptedStoresOrItemsBlocked
        """
        if "indexingEncryptedStoresOrItemsBlocked" in self._prop_dict:
            return self._prop_dict["indexingEncryptedStoresOrItemsBlocked"]
        else:
            return None

    @indexing_encrypted_stores_or_items_blocked.setter
    def indexing_encrypted_stores_or_items_blocked(self, val):
        self._prop_dict["indexingEncryptedStoresOrItemsBlocked"] = val

    @property
    def smb_auto_encrypted_file_extensions(self):
        """Gets and sets the smbAutoEncryptedFileExtensions
        
        Returns: 
            :class:`SmbAutoEncryptedFileExtensionsCollectionPage<onedrivesdk.request.smb_auto_encrypted_file_extensions_collection.SmbAutoEncryptedFileExtensionsCollectionPage>`:
                The smbAutoEncryptedFileExtensions
        """
        if "smbAutoEncryptedFileExtensions" in self._prop_dict:
            return SmbAutoEncryptedFileExtensionsCollectionPage(self._prop_dict["smbAutoEncryptedFileExtensions"])
        else:
            return None

    @property
    def is_assigned(self):
        """
        Gets and sets the isAssigned
        
        Returns:
            bool:
                The isAssigned
        """
        if "isAssigned" in self._prop_dict:
            return self._prop_dict["isAssigned"]
        else:
            return None

    @is_assigned.setter
    def is_assigned(self, val):
        self._prop_dict["isAssigned"] = val

    @property
    def protected_app_locker_files(self):
        """Gets and sets the protectedAppLockerFiles
        
        Returns: 
            :class:`ProtectedAppLockerFilesCollectionPage<onedrivesdk.request.protected_app_locker_files_collection.ProtectedAppLockerFilesCollectionPage>`:
                The protectedAppLockerFiles
        """
        if "protectedAppLockerFiles" in self._prop_dict:
            return ProtectedAppLockerFilesCollectionPage(self._prop_dict["protectedAppLockerFiles"])
        else:
            return None

    @property
    def exempt_app_locker_files(self):
        """Gets and sets the exemptAppLockerFiles
        
        Returns: 
            :class:`ExemptAppLockerFilesCollectionPage<onedrivesdk.request.exempt_app_locker_files_collection.ExemptAppLockerFilesCollectionPage>`:
                The exemptAppLockerFiles
        """
        if "exemptAppLockerFiles" in self._prop_dict:
            return ExemptAppLockerFilesCollectionPage(self._prop_dict["exemptAppLockerFiles"])
        else:
            return None

    @property
    def assignments(self):
        """Gets and sets the assignments
        
        Returns: 
            :class:`AssignmentsCollectionPage<onedrivesdk.request.assignments_collection.AssignmentsCollectionPage>`:
                The assignments
        """
        if "assignments" in self._prop_dict:
            return AssignmentsCollectionPage(self._prop_dict["assignments"])
        else:
            return None

