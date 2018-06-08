# -*- coding: utf-8 -*- 
'''
# Copyright (c) Microsoft Corporation.  All Rights Reserved.  Licensed under the MIT License.  See License in the project root for license information.
# 
#  This file was generated and any changes will be overwritten.
'''

from __future__ import unicode_literals
from ..model.firewall_pre_shared_key_encoding_method_type import FirewallPreSharedKeyEncodingMethodType
from ..model.firewall_certificate_revocation_list_check_method_type import FirewallCertificateRevocationListCheckMethodType
from ..model.firewall_packet_queueing_method_type import FirewallPacketQueueingMethodType
from ..model.windows_firewall_network_profile import WindowsFirewallNetworkProfile
from ..model.app_locker_application_control_type import AppLockerApplicationControlType
from ..model.application_guard_block_file_transfer_type import ApplicationGuardBlockFileTransferType
from ..model.application_guard_block_clipboard_sharing_type import ApplicationGuardBlockClipboardSharingType
from ..model.bit_locker_removable_drive_policy import BitLockerRemovableDrivePolicy
from ..one_drive_object_base import OneDriveObjectBase


class Windows10EndpointProtectionConfiguration(OneDriveObjectBase):

    def __init__(self, prop_dict={}):
        self._prop_dict = prop_dict

    @property
    def firewall_block_stateful_ftp(self):
        """
        Gets and sets the firewallBlockStatefulFTP
        
        Returns:
            bool:
                The firewallBlockStatefulFTP
        """
        if "firewallBlockStatefulFTP" in self._prop_dict:
            return self._prop_dict["firewallBlockStatefulFTP"]
        else:
            return None

    @firewall_block_stateful_ftp.setter
    def firewall_block_stateful_ftp(self, val):
        self._prop_dict["firewallBlockStatefulFTP"] = val

    @property
    def firewall_idle_timeout_for_security_association_in_seconds(self):
        """
        Gets and sets the firewallIdleTimeoutForSecurityAssociationInSeconds
        
        Returns:
            int:
                The firewallIdleTimeoutForSecurityAssociationInSeconds
        """
        if "firewallIdleTimeoutForSecurityAssociationInSeconds" in self._prop_dict:
            return self._prop_dict["firewallIdleTimeoutForSecurityAssociationInSeconds"]
        else:
            return None

    @firewall_idle_timeout_for_security_association_in_seconds.setter
    def firewall_idle_timeout_for_security_association_in_seconds(self, val):
        self._prop_dict["firewallIdleTimeoutForSecurityAssociationInSeconds"] = val

    @property
    def firewall_pre_shared_key_encoding_method(self):
        """
        Gets and sets the firewallPreSharedKeyEncodingMethod
        
        Returns: 
            :class:`FirewallPreSharedKeyEncodingMethodType<onedrivesdk.model.firewall_pre_shared_key_encoding_method_type.FirewallPreSharedKeyEncodingMethodType>`:
                The firewallPreSharedKeyEncodingMethod
        """
        if "firewallPreSharedKeyEncodingMethod" in self._prop_dict:
            if isinstance(self._prop_dict["firewallPreSharedKeyEncodingMethod"], OneDriveObjectBase):
                return self._prop_dict["firewallPreSharedKeyEncodingMethod"]
            else :
                self._prop_dict["firewallPreSharedKeyEncodingMethod"] = FirewallPreSharedKeyEncodingMethodType(self._prop_dict["firewallPreSharedKeyEncodingMethod"])
                return self._prop_dict["firewallPreSharedKeyEncodingMethod"]

        return None

    @firewall_pre_shared_key_encoding_method.setter
    def firewall_pre_shared_key_encoding_method(self, val):
        self._prop_dict["firewallPreSharedKeyEncodingMethod"] = val

    @property
    def firewall_ip_sec_exemptions_allow_neighbor_discovery(self):
        """
        Gets and sets the firewallIPSecExemptionsAllowNeighborDiscovery
        
        Returns:
            bool:
                The firewallIPSecExemptionsAllowNeighborDiscovery
        """
        if "firewallIPSecExemptionsAllowNeighborDiscovery" in self._prop_dict:
            return self._prop_dict["firewallIPSecExemptionsAllowNeighborDiscovery"]
        else:
            return None

    @firewall_ip_sec_exemptions_allow_neighbor_discovery.setter
    def firewall_ip_sec_exemptions_allow_neighbor_discovery(self, val):
        self._prop_dict["firewallIPSecExemptionsAllowNeighborDiscovery"] = val

    @property
    def firewall_ip_sec_exemptions_allow_icmp(self):
        """
        Gets and sets the firewallIPSecExemptionsAllowICMP
        
        Returns:
            bool:
                The firewallIPSecExemptionsAllowICMP
        """
        if "firewallIPSecExemptionsAllowICMP" in self._prop_dict:
            return self._prop_dict["firewallIPSecExemptionsAllowICMP"]
        else:
            return None

    @firewall_ip_sec_exemptions_allow_icmp.setter
    def firewall_ip_sec_exemptions_allow_icmp(self, val):
        self._prop_dict["firewallIPSecExemptionsAllowICMP"] = val

    @property
    def firewall_ip_sec_exemptions_allow_router_discovery(self):
        """
        Gets and sets the firewallIPSecExemptionsAllowRouterDiscovery
        
        Returns:
            bool:
                The firewallIPSecExemptionsAllowRouterDiscovery
        """
        if "firewallIPSecExemptionsAllowRouterDiscovery" in self._prop_dict:
            return self._prop_dict["firewallIPSecExemptionsAllowRouterDiscovery"]
        else:
            return None

    @firewall_ip_sec_exemptions_allow_router_discovery.setter
    def firewall_ip_sec_exemptions_allow_router_discovery(self, val):
        self._prop_dict["firewallIPSecExemptionsAllowRouterDiscovery"] = val

    @property
    def firewall_ip_sec_exemptions_allow_dhcp(self):
        """
        Gets and sets the firewallIPSecExemptionsAllowDHCP
        
        Returns:
            bool:
                The firewallIPSecExemptionsAllowDHCP
        """
        if "firewallIPSecExemptionsAllowDHCP" in self._prop_dict:
            return self._prop_dict["firewallIPSecExemptionsAllowDHCP"]
        else:
            return None

    @firewall_ip_sec_exemptions_allow_dhcp.setter
    def firewall_ip_sec_exemptions_allow_dhcp(self, val):
        self._prop_dict["firewallIPSecExemptionsAllowDHCP"] = val

    @property
    def firewall_certificate_revocation_list_check_method(self):
        """
        Gets and sets the firewallCertificateRevocationListCheckMethod
        
        Returns: 
            :class:`FirewallCertificateRevocationListCheckMethodType<onedrivesdk.model.firewall_certificate_revocation_list_check_method_type.FirewallCertificateRevocationListCheckMethodType>`:
                The firewallCertificateRevocationListCheckMethod
        """
        if "firewallCertificateRevocationListCheckMethod" in self._prop_dict:
            if isinstance(self._prop_dict["firewallCertificateRevocationListCheckMethod"], OneDriveObjectBase):
                return self._prop_dict["firewallCertificateRevocationListCheckMethod"]
            else :
                self._prop_dict["firewallCertificateRevocationListCheckMethod"] = FirewallCertificateRevocationListCheckMethodType(self._prop_dict["firewallCertificateRevocationListCheckMethod"])
                return self._prop_dict["firewallCertificateRevocationListCheckMethod"]

        return None

    @firewall_certificate_revocation_list_check_method.setter
    def firewall_certificate_revocation_list_check_method(self, val):
        self._prop_dict["firewallCertificateRevocationListCheckMethod"] = val

    @property
    def firewall_merge_keying_module_settings(self):
        """
        Gets and sets the firewallMergeKeyingModuleSettings
        
        Returns:
            bool:
                The firewallMergeKeyingModuleSettings
        """
        if "firewallMergeKeyingModuleSettings" in self._prop_dict:
            return self._prop_dict["firewallMergeKeyingModuleSettings"]
        else:
            return None

    @firewall_merge_keying_module_settings.setter
    def firewall_merge_keying_module_settings(self, val):
        self._prop_dict["firewallMergeKeyingModuleSettings"] = val

    @property
    def firewall_packet_queueing_method(self):
        """
        Gets and sets the firewallPacketQueueingMethod
        
        Returns: 
            :class:`FirewallPacketQueueingMethodType<onedrivesdk.model.firewall_packet_queueing_method_type.FirewallPacketQueueingMethodType>`:
                The firewallPacketQueueingMethod
        """
        if "firewallPacketQueueingMethod" in self._prop_dict:
            if isinstance(self._prop_dict["firewallPacketQueueingMethod"], OneDriveObjectBase):
                return self._prop_dict["firewallPacketQueueingMethod"]
            else :
                self._prop_dict["firewallPacketQueueingMethod"] = FirewallPacketQueueingMethodType(self._prop_dict["firewallPacketQueueingMethod"])
                return self._prop_dict["firewallPacketQueueingMethod"]

        return None

    @firewall_packet_queueing_method.setter
    def firewall_packet_queueing_method(self, val):
        self._prop_dict["firewallPacketQueueingMethod"] = val

    @property
    def firewall_profile_domain(self):
        """
        Gets and sets the firewallProfileDomain
        
        Returns: 
            :class:`WindowsFirewallNetworkProfile<onedrivesdk.model.windows_firewall_network_profile.WindowsFirewallNetworkProfile>`:
                The firewallProfileDomain
        """
        if "firewallProfileDomain" in self._prop_dict:
            if isinstance(self._prop_dict["firewallProfileDomain"], OneDriveObjectBase):
                return self._prop_dict["firewallProfileDomain"]
            else :
                self._prop_dict["firewallProfileDomain"] = WindowsFirewallNetworkProfile(self._prop_dict["firewallProfileDomain"])
                return self._prop_dict["firewallProfileDomain"]

        return None

    @firewall_profile_domain.setter
    def firewall_profile_domain(self, val):
        self._prop_dict["firewallProfileDomain"] = val

    @property
    def firewall_profile_public(self):
        """
        Gets and sets the firewallProfilePublic
        
        Returns: 
            :class:`WindowsFirewallNetworkProfile<onedrivesdk.model.windows_firewall_network_profile.WindowsFirewallNetworkProfile>`:
                The firewallProfilePublic
        """
        if "firewallProfilePublic" in self._prop_dict:
            if isinstance(self._prop_dict["firewallProfilePublic"], OneDriveObjectBase):
                return self._prop_dict["firewallProfilePublic"]
            else :
                self._prop_dict["firewallProfilePublic"] = WindowsFirewallNetworkProfile(self._prop_dict["firewallProfilePublic"])
                return self._prop_dict["firewallProfilePublic"]

        return None

    @firewall_profile_public.setter
    def firewall_profile_public(self, val):
        self._prop_dict["firewallProfilePublic"] = val

    @property
    def firewall_profile_private(self):
        """
        Gets and sets the firewallProfilePrivate
        
        Returns: 
            :class:`WindowsFirewallNetworkProfile<onedrivesdk.model.windows_firewall_network_profile.WindowsFirewallNetworkProfile>`:
                The firewallProfilePrivate
        """
        if "firewallProfilePrivate" in self._prop_dict:
            if isinstance(self._prop_dict["firewallProfilePrivate"], OneDriveObjectBase):
                return self._prop_dict["firewallProfilePrivate"]
            else :
                self._prop_dict["firewallProfilePrivate"] = WindowsFirewallNetworkProfile(self._prop_dict["firewallProfilePrivate"])
                return self._prop_dict["firewallProfilePrivate"]

        return None

    @firewall_profile_private.setter
    def firewall_profile_private(self, val):
        self._prop_dict["firewallProfilePrivate"] = val

    @property
    def defender_attack_surface_reduction_excluded_paths(self):
        """
        Gets and sets the defenderAttackSurfaceReductionExcludedPaths
        
        Returns:
            str:
                The defenderAttackSurfaceReductionExcludedPaths
        """
        if "defenderAttackSurfaceReductionExcludedPaths" in self._prop_dict:
            return self._prop_dict["defenderAttackSurfaceReductionExcludedPaths"]
        else:
            return None

    @defender_attack_surface_reduction_excluded_paths.setter
    def defender_attack_surface_reduction_excluded_paths(self, val):
        self._prop_dict["defenderAttackSurfaceReductionExcludedPaths"] = val

    @property
    def defender_guarded_folders_allowed_app_paths(self):
        """
        Gets and sets the defenderGuardedFoldersAllowedAppPaths
        
        Returns:
            str:
                The defenderGuardedFoldersAllowedAppPaths
        """
        if "defenderGuardedFoldersAllowedAppPaths" in self._prop_dict:
            return self._prop_dict["defenderGuardedFoldersAllowedAppPaths"]
        else:
            return None

    @defender_guarded_folders_allowed_app_paths.setter
    def defender_guarded_folders_allowed_app_paths(self, val):
        self._prop_dict["defenderGuardedFoldersAllowedAppPaths"] = val

    @property
    def defender_additional_guarded_folders(self):
        """
        Gets and sets the defenderAdditionalGuardedFolders
        
        Returns:
            str:
                The defenderAdditionalGuardedFolders
        """
        if "defenderAdditionalGuardedFolders" in self._prop_dict:
            return self._prop_dict["defenderAdditionalGuardedFolders"]
        else:
            return None

    @defender_additional_guarded_folders.setter
    def defender_additional_guarded_folders(self, val):
        self._prop_dict["defenderAdditionalGuardedFolders"] = val

    @property
    def defender_exploit_protection_xml_file_name(self):
        """
        Gets and sets the defenderExploitProtectionXmlFileName
        
        Returns:
            str:
                The defenderExploitProtectionXmlFileName
        """
        if "defenderExploitProtectionXmlFileName" in self._prop_dict:
            return self._prop_dict["defenderExploitProtectionXmlFileName"]
        else:
            return None

    @defender_exploit_protection_xml_file_name.setter
    def defender_exploit_protection_xml_file_name(self, val):
        self._prop_dict["defenderExploitProtectionXmlFileName"] = val

    @property
    def defender_security_center_block_exploit_protection_override(self):
        """
        Gets and sets the defenderSecurityCenterBlockExploitProtectionOverride
        
        Returns:
            bool:
                The defenderSecurityCenterBlockExploitProtectionOverride
        """
        if "defenderSecurityCenterBlockExploitProtectionOverride" in self._prop_dict:
            return self._prop_dict["defenderSecurityCenterBlockExploitProtectionOverride"]
        else:
            return None

    @defender_security_center_block_exploit_protection_override.setter
    def defender_security_center_block_exploit_protection_override(self, val):
        self._prop_dict["defenderSecurityCenterBlockExploitProtectionOverride"] = val

    @property
    def app_locker_application_control(self):
        """
        Gets and sets the appLockerApplicationControl
        
        Returns: 
            :class:`AppLockerApplicationControlType<onedrivesdk.model.app_locker_application_control_type.AppLockerApplicationControlType>`:
                The appLockerApplicationControl
        """
        if "appLockerApplicationControl" in self._prop_dict:
            if isinstance(self._prop_dict["appLockerApplicationControl"], OneDriveObjectBase):
                return self._prop_dict["appLockerApplicationControl"]
            else :
                self._prop_dict["appLockerApplicationControl"] = AppLockerApplicationControlType(self._prop_dict["appLockerApplicationControl"])
                return self._prop_dict["appLockerApplicationControl"]

        return None

    @app_locker_application_control.setter
    def app_locker_application_control(self, val):
        self._prop_dict["appLockerApplicationControl"] = val

    @property
    def smart_screen_enable_in_shell(self):
        """
        Gets and sets the smartScreenEnableInShell
        
        Returns:
            bool:
                The smartScreenEnableInShell
        """
        if "smartScreenEnableInShell" in self._prop_dict:
            return self._prop_dict["smartScreenEnableInShell"]
        else:
            return None

    @smart_screen_enable_in_shell.setter
    def smart_screen_enable_in_shell(self, val):
        self._prop_dict["smartScreenEnableInShell"] = val

    @property
    def smart_screen_block_override_for_files(self):
        """
        Gets and sets the smartScreenBlockOverrideForFiles
        
        Returns:
            bool:
                The smartScreenBlockOverrideForFiles
        """
        if "smartScreenBlockOverrideForFiles" in self._prop_dict:
            return self._prop_dict["smartScreenBlockOverrideForFiles"]
        else:
            return None

    @smart_screen_block_override_for_files.setter
    def smart_screen_block_override_for_files(self, val):
        self._prop_dict["smartScreenBlockOverrideForFiles"] = val

    @property
    def application_guard_enabled(self):
        """
        Gets and sets the applicationGuardEnabled
        
        Returns:
            bool:
                The applicationGuardEnabled
        """
        if "applicationGuardEnabled" in self._prop_dict:
            return self._prop_dict["applicationGuardEnabled"]
        else:
            return None

    @application_guard_enabled.setter
    def application_guard_enabled(self, val):
        self._prop_dict["applicationGuardEnabled"] = val

    @property
    def application_guard_block_file_transfer(self):
        """
        Gets and sets the applicationGuardBlockFileTransfer
        
        Returns: 
            :class:`ApplicationGuardBlockFileTransferType<onedrivesdk.model.application_guard_block_file_transfer_type.ApplicationGuardBlockFileTransferType>`:
                The applicationGuardBlockFileTransfer
        """
        if "applicationGuardBlockFileTransfer" in self._prop_dict:
            if isinstance(self._prop_dict["applicationGuardBlockFileTransfer"], OneDriveObjectBase):
                return self._prop_dict["applicationGuardBlockFileTransfer"]
            else :
                self._prop_dict["applicationGuardBlockFileTransfer"] = ApplicationGuardBlockFileTransferType(self._prop_dict["applicationGuardBlockFileTransfer"])
                return self._prop_dict["applicationGuardBlockFileTransfer"]

        return None

    @application_guard_block_file_transfer.setter
    def application_guard_block_file_transfer(self, val):
        self._prop_dict["applicationGuardBlockFileTransfer"] = val

    @property
    def application_guard_block_non_enterprise_content(self):
        """
        Gets and sets the applicationGuardBlockNonEnterpriseContent
        
        Returns:
            bool:
                The applicationGuardBlockNonEnterpriseContent
        """
        if "applicationGuardBlockNonEnterpriseContent" in self._prop_dict:
            return self._prop_dict["applicationGuardBlockNonEnterpriseContent"]
        else:
            return None

    @application_guard_block_non_enterprise_content.setter
    def application_guard_block_non_enterprise_content(self, val):
        self._prop_dict["applicationGuardBlockNonEnterpriseContent"] = val

    @property
    def application_guard_allow_persistence(self):
        """
        Gets and sets the applicationGuardAllowPersistence
        
        Returns:
            bool:
                The applicationGuardAllowPersistence
        """
        if "applicationGuardAllowPersistence" in self._prop_dict:
            return self._prop_dict["applicationGuardAllowPersistence"]
        else:
            return None

    @application_guard_allow_persistence.setter
    def application_guard_allow_persistence(self, val):
        self._prop_dict["applicationGuardAllowPersistence"] = val

    @property
    def application_guard_force_auditing(self):
        """
        Gets and sets the applicationGuardForceAuditing
        
        Returns:
            bool:
                The applicationGuardForceAuditing
        """
        if "applicationGuardForceAuditing" in self._prop_dict:
            return self._prop_dict["applicationGuardForceAuditing"]
        else:
            return None

    @application_guard_force_auditing.setter
    def application_guard_force_auditing(self, val):
        self._prop_dict["applicationGuardForceAuditing"] = val

    @property
    def application_guard_block_clipboard_sharing(self):
        """
        Gets and sets the applicationGuardBlockClipboardSharing
        
        Returns: 
            :class:`ApplicationGuardBlockClipboardSharingType<onedrivesdk.model.application_guard_block_clipboard_sharing_type.ApplicationGuardBlockClipboardSharingType>`:
                The applicationGuardBlockClipboardSharing
        """
        if "applicationGuardBlockClipboardSharing" in self._prop_dict:
            if isinstance(self._prop_dict["applicationGuardBlockClipboardSharing"], OneDriveObjectBase):
                return self._prop_dict["applicationGuardBlockClipboardSharing"]
            else :
                self._prop_dict["applicationGuardBlockClipboardSharing"] = ApplicationGuardBlockClipboardSharingType(self._prop_dict["applicationGuardBlockClipboardSharing"])
                return self._prop_dict["applicationGuardBlockClipboardSharing"]

        return None

    @application_guard_block_clipboard_sharing.setter
    def application_guard_block_clipboard_sharing(self, val):
        self._prop_dict["applicationGuardBlockClipboardSharing"] = val

    @property
    def application_guard_allow_print_to_pdf(self):
        """
        Gets and sets the applicationGuardAllowPrintToPDF
        
        Returns:
            bool:
                The applicationGuardAllowPrintToPDF
        """
        if "applicationGuardAllowPrintToPDF" in self._prop_dict:
            return self._prop_dict["applicationGuardAllowPrintToPDF"]
        else:
            return None

    @application_guard_allow_print_to_pdf.setter
    def application_guard_allow_print_to_pdf(self, val):
        self._prop_dict["applicationGuardAllowPrintToPDF"] = val

    @property
    def application_guard_allow_print_to_xps(self):
        """
        Gets and sets the applicationGuardAllowPrintToXPS
        
        Returns:
            bool:
                The applicationGuardAllowPrintToXPS
        """
        if "applicationGuardAllowPrintToXPS" in self._prop_dict:
            return self._prop_dict["applicationGuardAllowPrintToXPS"]
        else:
            return None

    @application_guard_allow_print_to_xps.setter
    def application_guard_allow_print_to_xps(self, val):
        self._prop_dict["applicationGuardAllowPrintToXPS"] = val

    @property
    def application_guard_allow_print_to_local_printers(self):
        """
        Gets and sets the applicationGuardAllowPrintToLocalPrinters
        
        Returns:
            bool:
                The applicationGuardAllowPrintToLocalPrinters
        """
        if "applicationGuardAllowPrintToLocalPrinters" in self._prop_dict:
            return self._prop_dict["applicationGuardAllowPrintToLocalPrinters"]
        else:
            return None

    @application_guard_allow_print_to_local_printers.setter
    def application_guard_allow_print_to_local_printers(self, val):
        self._prop_dict["applicationGuardAllowPrintToLocalPrinters"] = val

    @property
    def application_guard_allow_print_to_network_printers(self):
        """
        Gets and sets the applicationGuardAllowPrintToNetworkPrinters
        
        Returns:
            bool:
                The applicationGuardAllowPrintToNetworkPrinters
        """
        if "applicationGuardAllowPrintToNetworkPrinters" in self._prop_dict:
            return self._prop_dict["applicationGuardAllowPrintToNetworkPrinters"]
        else:
            return None

    @application_guard_allow_print_to_network_printers.setter
    def application_guard_allow_print_to_network_printers(self, val):
        self._prop_dict["applicationGuardAllowPrintToNetworkPrinters"] = val

    @property
    def bit_locker_disable_warning_for_other_disk_encryption(self):
        """
        Gets and sets the bitLockerDisableWarningForOtherDiskEncryption
        
        Returns:
            bool:
                The bitLockerDisableWarningForOtherDiskEncryption
        """
        if "bitLockerDisableWarningForOtherDiskEncryption" in self._prop_dict:
            return self._prop_dict["bitLockerDisableWarningForOtherDiskEncryption"]
        else:
            return None

    @bit_locker_disable_warning_for_other_disk_encryption.setter
    def bit_locker_disable_warning_for_other_disk_encryption(self, val):
        self._prop_dict["bitLockerDisableWarningForOtherDiskEncryption"] = val

    @property
    def bit_locker_enable_storage_card_encryption_on_mobile(self):
        """
        Gets and sets the bitLockerEnableStorageCardEncryptionOnMobile
        
        Returns:
            bool:
                The bitLockerEnableStorageCardEncryptionOnMobile
        """
        if "bitLockerEnableStorageCardEncryptionOnMobile" in self._prop_dict:
            return self._prop_dict["bitLockerEnableStorageCardEncryptionOnMobile"]
        else:
            return None

    @bit_locker_enable_storage_card_encryption_on_mobile.setter
    def bit_locker_enable_storage_card_encryption_on_mobile(self, val):
        self._prop_dict["bitLockerEnableStorageCardEncryptionOnMobile"] = val

    @property
    def bit_locker_encrypt_device(self):
        """
        Gets and sets the bitLockerEncryptDevice
        
        Returns:
            bool:
                The bitLockerEncryptDevice
        """
        if "bitLockerEncryptDevice" in self._prop_dict:
            return self._prop_dict["bitLockerEncryptDevice"]
        else:
            return None

    @bit_locker_encrypt_device.setter
    def bit_locker_encrypt_device(self, val):
        self._prop_dict["bitLockerEncryptDevice"] = val

    @property
    def bit_locker_removable_drive_policy(self):
        """
        Gets and sets the bitLockerRemovableDrivePolicy
        
        Returns: 
            :class:`BitLockerRemovableDrivePolicy<onedrivesdk.model.bit_locker_removable_drive_policy.BitLockerRemovableDrivePolicy>`:
                The bitLockerRemovableDrivePolicy
        """
        if "bitLockerRemovableDrivePolicy" in self._prop_dict:
            if isinstance(self._prop_dict["bitLockerRemovableDrivePolicy"], OneDriveObjectBase):
                return self._prop_dict["bitLockerRemovableDrivePolicy"]
            else :
                self._prop_dict["bitLockerRemovableDrivePolicy"] = BitLockerRemovableDrivePolicy(self._prop_dict["bitLockerRemovableDrivePolicy"])
                return self._prop_dict["bitLockerRemovableDrivePolicy"]

        return None

    @bit_locker_removable_drive_policy.setter
    def bit_locker_removable_drive_policy(self, val):
        self._prop_dict["bitLockerRemovableDrivePolicy"] = val

