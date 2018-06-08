# -*- coding: utf-8 -*- 
'''
# Copyright (c) Microsoft Corporation.  All Rights Reserved.  Licensed under the MIT License.  See License in the project root for license information.
# 
#  This file was generated and any changes will be overwritten.
'''

from __future__ import unicode_literals
from ..model.proxied_domain import ProxiedDomain
from ..model.ip_range import IpRange
from ..one_drive_object_base import OneDriveObjectBase


class WindowsNetworkIsolationPolicy(OneDriveObjectBase):

    def __init__(self, prop_dict={}):
        self._prop_dict = prop_dict

    @property
    def enterprise_network_domain_names(self):
        """Gets and sets the enterpriseNetworkDomainNames
        
        Returns: 
            str:
                The enterpriseNetworkDomainNames
        """
        if "enterpriseNetworkDomainNames" in self._prop_dict:
            return self._prop_dict["enterpriseNetworkDomainNames"]
        else:
            return None

    @enterprise_network_domain_names.setter
    def enterprise_network_domain_names(self, val):
        self._prop_dict["enterpriseNetworkDomainNames"] = val

    @property
    def enterprise_cloud_resources(self):
        """
        Gets and sets the enterpriseCloudResources
        
        Returns: 
            :class:`ProxiedDomain<onedrivesdk.model.proxied_domain.ProxiedDomain>`:
                The enterpriseCloudResources
        """
        if "enterpriseCloudResources" in self._prop_dict:
            if isinstance(self._prop_dict["enterpriseCloudResources"], OneDriveObjectBase):
                return self._prop_dict["enterpriseCloudResources"]
            else :
                self._prop_dict["enterpriseCloudResources"] = ProxiedDomain(self._prop_dict["enterpriseCloudResources"])
                return self._prop_dict["enterpriseCloudResources"]

        return None

    @enterprise_cloud_resources.setter
    def enterprise_cloud_resources(self, val):
        self._prop_dict["enterpriseCloudResources"] = val
    @property
    def enterprise_ip_ranges(self):
        """
        Gets and sets the enterpriseIPRanges
        
        Returns: 
            :class:`IpRange<onedrivesdk.model.ip_range.IpRange>`:
                The enterpriseIPRanges
        """
        if "enterpriseIPRanges" in self._prop_dict:
            if isinstance(self._prop_dict["enterpriseIPRanges"], OneDriveObjectBase):
                return self._prop_dict["enterpriseIPRanges"]
            else :
                self._prop_dict["enterpriseIPRanges"] = IpRange(self._prop_dict["enterpriseIPRanges"])
                return self._prop_dict["enterpriseIPRanges"]

        return None

    @enterprise_ip_ranges.setter
    def enterprise_ip_ranges(self, val):
        self._prop_dict["enterpriseIPRanges"] = val
    @property
    def enterprise_internal_proxy_servers(self):
        """Gets and sets the enterpriseInternalProxyServers
        
        Returns: 
            str:
                The enterpriseInternalProxyServers
        """
        if "enterpriseInternalProxyServers" in self._prop_dict:
            return self._prop_dict["enterpriseInternalProxyServers"]
        else:
            return None

    @enterprise_internal_proxy_servers.setter
    def enterprise_internal_proxy_servers(self, val):
        self._prop_dict["enterpriseInternalProxyServers"] = val

    @property
    def enterprise_ip_ranges_are_authoritative(self):
        """Gets and sets the enterpriseIPRangesAreAuthoritative
        
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
            str:
                The enterpriseProxyServers
        """
        if "enterpriseProxyServers" in self._prop_dict:
            return self._prop_dict["enterpriseProxyServers"]
        else:
            return None

    @enterprise_proxy_servers.setter
    def enterprise_proxy_servers(self, val):
        self._prop_dict["enterpriseProxyServers"] = val

    @property
    def enterprise_proxy_servers_are_authoritative(self):
        """Gets and sets the enterpriseProxyServersAreAuthoritative
        
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
            str:
                The neutralDomainResources
        """
        if "neutralDomainResources" in self._prop_dict:
            return self._prop_dict["neutralDomainResources"]
        else:
            return None

    @neutral_domain_resources.setter
    def neutral_domain_resources(self, val):
        self._prop_dict["neutralDomainResources"] = val

