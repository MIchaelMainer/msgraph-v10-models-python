# -*- coding: utf-8 -*- 
'''
# Copyright (c) Microsoft Corporation.  All Rights Reserved.  Licensed under the MIT License.  See License in the project root for license information.
# 
#  This file was generated and any changes will be overwritten.
'''

from __future__ import unicode_literals
from ..model.windows10_vpn_profile_target import Windows10VpnProfileTarget
from ..model.windows10_vpn_connection_type import Windows10VpnConnectionType
from ..model.windows10_vpn_authentication_method import Windows10VpnAuthenticationMethod
from ..model.extended_key_usage import ExtendedKeyUsage
from ..model.windows10_vpn_proxy_server import Windows10VpnProxyServer
from ..model.windows10_associated_apps import Windows10AssociatedApps
from ..model.vpn_traffic_rule import VpnTrafficRule
from ..model.vpn_route import VpnRoute
from ..model.vpn_dns_rule import VpnDnsRule
from ..model.windows_certificate_profile_base import WindowsCertificateProfileBase
from ..one_drive_object_base import OneDriveObjectBase


class Windows10VpnConfiguration(OneDriveObjectBase):

    def __init__(self, prop_dict={}):
        self._prop_dict = prop_dict

    @property
    def profile_target(self):
        """
        Gets and sets the profileTarget
        
        Returns: 
            :class:`Windows10VpnProfileTarget<onedrivesdk.model.windows10_vpn_profile_target.Windows10VpnProfileTarget>`:
                The profileTarget
        """
        if "profileTarget" in self._prop_dict:
            if isinstance(self._prop_dict["profileTarget"], OneDriveObjectBase):
                return self._prop_dict["profileTarget"]
            else :
                self._prop_dict["profileTarget"] = Windows10VpnProfileTarget(self._prop_dict["profileTarget"])
                return self._prop_dict["profileTarget"]

        return None

    @profile_target.setter
    def profile_target(self, val):
        self._prop_dict["profileTarget"] = val

    @property
    def connection_type(self):
        """
        Gets and sets the connectionType
        
        Returns: 
            :class:`Windows10VpnConnectionType<onedrivesdk.model.windows10_vpn_connection_type.Windows10VpnConnectionType>`:
                The connectionType
        """
        if "connectionType" in self._prop_dict:
            if isinstance(self._prop_dict["connectionType"], OneDriveObjectBase):
                return self._prop_dict["connectionType"]
            else :
                self._prop_dict["connectionType"] = Windows10VpnConnectionType(self._prop_dict["connectionType"])
                return self._prop_dict["connectionType"]

        return None

    @connection_type.setter
    def connection_type(self, val):
        self._prop_dict["connectionType"] = val

    @property
    def enable_split_tunneling(self):
        """
        Gets and sets the enableSplitTunneling
        
        Returns:
            bool:
                The enableSplitTunneling
        """
        if "enableSplitTunneling" in self._prop_dict:
            return self._prop_dict["enableSplitTunneling"]
        else:
            return None

    @enable_split_tunneling.setter
    def enable_split_tunneling(self, val):
        self._prop_dict["enableSplitTunneling"] = val

    @property
    def enable_always_on(self):
        """
        Gets and sets the enableAlwaysOn
        
        Returns:
            bool:
                The enableAlwaysOn
        """
        if "enableAlwaysOn" in self._prop_dict:
            return self._prop_dict["enableAlwaysOn"]
        else:
            return None

    @enable_always_on.setter
    def enable_always_on(self, val):
        self._prop_dict["enableAlwaysOn"] = val

    @property
    def enable_device_tunnel(self):
        """
        Gets and sets the enableDeviceTunnel
        
        Returns:
            bool:
                The enableDeviceTunnel
        """
        if "enableDeviceTunnel" in self._prop_dict:
            return self._prop_dict["enableDeviceTunnel"]
        else:
            return None

    @enable_device_tunnel.setter
    def enable_device_tunnel(self, val):
        self._prop_dict["enableDeviceTunnel"] = val

    @property
    def authentication_method(self):
        """
        Gets and sets the authenticationMethod
        
        Returns: 
            :class:`Windows10VpnAuthenticationMethod<onedrivesdk.model.windows10_vpn_authentication_method.Windows10VpnAuthenticationMethod>`:
                The authenticationMethod
        """
        if "authenticationMethod" in self._prop_dict:
            if isinstance(self._prop_dict["authenticationMethod"], OneDriveObjectBase):
                return self._prop_dict["authenticationMethod"]
            else :
                self._prop_dict["authenticationMethod"] = Windows10VpnAuthenticationMethod(self._prop_dict["authenticationMethod"])
                return self._prop_dict["authenticationMethod"]

        return None

    @authentication_method.setter
    def authentication_method(self, val):
        self._prop_dict["authenticationMethod"] = val

    @property
    def remember_user_credentials(self):
        """
        Gets and sets the rememberUserCredentials
        
        Returns:
            bool:
                The rememberUserCredentials
        """
        if "rememberUserCredentials" in self._prop_dict:
            return self._prop_dict["rememberUserCredentials"]
        else:
            return None

    @remember_user_credentials.setter
    def remember_user_credentials(self, val):
        self._prop_dict["rememberUserCredentials"] = val

    @property
    def enable_conditional_access(self):
        """
        Gets and sets the enableConditionalAccess
        
        Returns:
            bool:
                The enableConditionalAccess
        """
        if "enableConditionalAccess" in self._prop_dict:
            return self._prop_dict["enableConditionalAccess"]
        else:
            return None

    @enable_conditional_access.setter
    def enable_conditional_access(self, val):
        self._prop_dict["enableConditionalAccess"] = val

    @property
    def enable_single_sign_on_with_alternate_certificate(self):
        """
        Gets and sets the enableSingleSignOnWithAlternateCertificate
        
        Returns:
            bool:
                The enableSingleSignOnWithAlternateCertificate
        """
        if "enableSingleSignOnWithAlternateCertificate" in self._prop_dict:
            return self._prop_dict["enableSingleSignOnWithAlternateCertificate"]
        else:
            return None

    @enable_single_sign_on_with_alternate_certificate.setter
    def enable_single_sign_on_with_alternate_certificate(self, val):
        self._prop_dict["enableSingleSignOnWithAlternateCertificate"] = val

    @property
    def single_sign_on_eku(self):
        """
        Gets and sets the singleSignOnEku
        
        Returns: 
            :class:`ExtendedKeyUsage<onedrivesdk.model.extended_key_usage.ExtendedKeyUsage>`:
                The singleSignOnEku
        """
        if "singleSignOnEku" in self._prop_dict:
            if isinstance(self._prop_dict["singleSignOnEku"], OneDriveObjectBase):
                return self._prop_dict["singleSignOnEku"]
            else :
                self._prop_dict["singleSignOnEku"] = ExtendedKeyUsage(self._prop_dict["singleSignOnEku"])
                return self._prop_dict["singleSignOnEku"]

        return None

    @single_sign_on_eku.setter
    def single_sign_on_eku(self, val):
        self._prop_dict["singleSignOnEku"] = val

    @property
    def single_sign_on_issuer_hash(self):
        """
        Gets and sets the singleSignOnIssuerHash
        
        Returns:
            str:
                The singleSignOnIssuerHash
        """
        if "singleSignOnIssuerHash" in self._prop_dict:
            return self._prop_dict["singleSignOnIssuerHash"]
        else:
            return None

    @single_sign_on_issuer_hash.setter
    def single_sign_on_issuer_hash(self, val):
        self._prop_dict["singleSignOnIssuerHash"] = val

    @property
    def proxy_server(self):
        """
        Gets and sets the proxyServer
        
        Returns: 
            :class:`Windows10VpnProxyServer<onedrivesdk.model.windows10_vpn_proxy_server.Windows10VpnProxyServer>`:
                The proxyServer
        """
        if "proxyServer" in self._prop_dict:
            if isinstance(self._prop_dict["proxyServer"], OneDriveObjectBase):
                return self._prop_dict["proxyServer"]
            else :
                self._prop_dict["proxyServer"] = Windows10VpnProxyServer(self._prop_dict["proxyServer"])
                return self._prop_dict["proxyServer"]

        return None

    @proxy_server.setter
    def proxy_server(self, val):
        self._prop_dict["proxyServer"] = val

    @property
    def associated_apps(self):
        """Gets and sets the associatedApps
        
        Returns: 
            :class:`AssociatedAppsCollectionPage<onedrivesdk.request.associated_apps_collection.AssociatedAppsCollectionPage>`:
                The associatedApps
        """
        if "associatedApps" in self._prop_dict:
            return AssociatedAppsCollectionPage(self._prop_dict["associatedApps"])
        else:
            return None

    @property
    def only_associated_apps_can_use_connection(self):
        """
        Gets and sets the onlyAssociatedAppsCanUseConnection
        
        Returns:
            bool:
                The onlyAssociatedAppsCanUseConnection
        """
        if "onlyAssociatedAppsCanUseConnection" in self._prop_dict:
            return self._prop_dict["onlyAssociatedAppsCanUseConnection"]
        else:
            return None

    @only_associated_apps_can_use_connection.setter
    def only_associated_apps_can_use_connection(self, val):
        self._prop_dict["onlyAssociatedAppsCanUseConnection"] = val

    @property
    def windows_information_protection_domain(self):
        """
        Gets and sets the windowsInformationProtectionDomain
        
        Returns:
            str:
                The windowsInformationProtectionDomain
        """
        if "windowsInformationProtectionDomain" in self._prop_dict:
            return self._prop_dict["windowsInformationProtectionDomain"]
        else:
            return None

    @windows_information_protection_domain.setter
    def windows_information_protection_domain(self, val):
        self._prop_dict["windowsInformationProtectionDomain"] = val

    @property
    def traffic_rules(self):
        """Gets and sets the trafficRules
        
        Returns: 
            :class:`TrafficRulesCollectionPage<onedrivesdk.request.traffic_rules_collection.TrafficRulesCollectionPage>`:
                The trafficRules
        """
        if "trafficRules" in self._prop_dict:
            return TrafficRulesCollectionPage(self._prop_dict["trafficRules"])
        else:
            return None

    @property
    def routes(self):
        """Gets and sets the routes
        
        Returns: 
            :class:`RoutesCollectionPage<onedrivesdk.request.routes_collection.RoutesCollectionPage>`:
                The routes
        """
        if "routes" in self._prop_dict:
            return RoutesCollectionPage(self._prop_dict["routes"])
        else:
            return None

    @property
    def dns_rules(self):
        """Gets and sets the dnsRules
        
        Returns: 
            :class:`DnsRulesCollectionPage<onedrivesdk.request.dns_rules_collection.DnsRulesCollectionPage>`:
                The dnsRules
        """
        if "dnsRules" in self._prop_dict:
            return DnsRulesCollectionPage(self._prop_dict["dnsRules"])
        else:
            return None

    @property
    def identity_certificate(self):
        """
        Gets and sets the identityCertificate
        
        Returns: 
            :class:`WindowsCertificateProfileBase<onedrivesdk.model.windows_certificate_profile_base.WindowsCertificateProfileBase>`:
                The identityCertificate
        """
        if "identityCertificate" in self._prop_dict:
            if isinstance(self._prop_dict["identityCertificate"], OneDriveObjectBase):
                return self._prop_dict["identityCertificate"]
            else :
                self._prop_dict["identityCertificate"] = WindowsCertificateProfileBase(self._prop_dict["identityCertificate"])
                return self._prop_dict["identityCertificate"]

        return None

    @identity_certificate.setter
    def identity_certificate(self, val):
        self._prop_dict["identityCertificate"] = val

