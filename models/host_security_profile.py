# -*- coding: utf-8 -*- 
'''
# Copyright (c) Microsoft Corporation.  All Rights Reserved.  Licensed under the MIT License.  See License in the project root for license information.
# 
#  This file was generated and any changes will be overwritten.
'''

from __future__ import unicode_literals
from ..model.logon_user import LogonUser
from ..model.network_interface import NetworkInterface
from ..model.security_vendor_information import SecurityVendorInformation
from datetime import datetime
from ..one_drive_object_base import OneDriveObjectBase


class HostSecurityProfile(OneDriveObjectBase):

    def __init__(self, prop_dict={}):
        self._prop_dict = prop_dict

    @property
    def azure_subscription_id(self):
        """
        Gets and sets the azureSubscriptionId
        
        Returns:
            str:
                The azureSubscriptionId
        """
        if "azureSubscriptionId" in self._prop_dict:
            return self._prop_dict["azureSubscriptionId"]
        else:
            return None

    @azure_subscription_id.setter
    def azure_subscription_id(self, val):
        self._prop_dict["azureSubscriptionId"] = val

    @property
    def azure_tenant_id(self):
        """
        Gets and sets the azureTenantId
        
        Returns:
            str:
                The azureTenantId
        """
        if "azureTenantId" in self._prop_dict:
            return self._prop_dict["azureTenantId"]
        else:
            return None

    @azure_tenant_id.setter
    def azure_tenant_id(self, val):
        self._prop_dict["azureTenantId"] = val

    @property
    def created_date_time(self):
        """
        Gets and sets the createdDateTime
        
        Returns:
            datetime:
                The createdDateTime
        """
        if "createdDateTime" in self._prop_dict:
            return datetime.strptime(self._prop_dict["createdDateTime"].replace("Z", ""), "%Y-%m-%dT%H:%M:%S.%f")
        else:
            return None

    @created_date_time.setter
    def created_date_time(self, val):
        self._prop_dict["createdDateTime"] = val.isoformat()+"Z"

    @property
    def fqdn(self):
        """
        Gets and sets the fqdn
        
        Returns:
            str:
                The fqdn
        """
        if "fqdn" in self._prop_dict:
            return self._prop_dict["fqdn"]
        else:
            return None

    @fqdn.setter
    def fqdn(self, val):
        self._prop_dict["fqdn"] = val

    @property
    def is_azure_ad_joined(self):
        """
        Gets and sets the isAzureAdJoined
        
        Returns:
            bool:
                The isAzureAdJoined
        """
        if "isAzureAdJoined" in self._prop_dict:
            return self._prop_dict["isAzureAdJoined"]
        else:
            return None

    @is_azure_ad_joined.setter
    def is_azure_ad_joined(self, val):
        self._prop_dict["isAzureAdJoined"] = val

    @property
    def is_azure_ad_registered(self):
        """
        Gets and sets the isAzureAdRegistered
        
        Returns:
            bool:
                The isAzureAdRegistered
        """
        if "isAzureAdRegistered" in self._prop_dict:
            return self._prop_dict["isAzureAdRegistered"]
        else:
            return None

    @is_azure_ad_registered.setter
    def is_azure_ad_registered(self, val):
        self._prop_dict["isAzureAdRegistered"] = val

    @property
    def is_hybrid_azure_domain_joined(self):
        """
        Gets and sets the isHybridAzureDomainJoined
        
        Returns:
            bool:
                The isHybridAzureDomainJoined
        """
        if "isHybridAzureDomainJoined" in self._prop_dict:
            return self._prop_dict["isHybridAzureDomainJoined"]
        else:
            return None

    @is_hybrid_azure_domain_joined.setter
    def is_hybrid_azure_domain_joined(self, val):
        self._prop_dict["isHybridAzureDomainJoined"] = val

    @property
    def last_modified_date_time(self):
        """
        Gets and sets the lastModifiedDateTime
        
        Returns:
            datetime:
                The lastModifiedDateTime
        """
        if "lastModifiedDateTime" in self._prop_dict:
            return datetime.strptime(self._prop_dict["lastModifiedDateTime"].replace("Z", ""), "%Y-%m-%dT%H:%M:%S.%f")
        else:
            return None

    @last_modified_date_time.setter
    def last_modified_date_time(self, val):
        self._prop_dict["lastModifiedDateTime"] = val.isoformat()+"Z"

    @property
    def logical_name(self):
        """
        Gets and sets the logicalName
        
        Returns:
            str:
                The logicalName
        """
        if "logicalName" in self._prop_dict:
            return self._prop_dict["logicalName"]
        else:
            return None

    @logical_name.setter
    def logical_name(self, val):
        self._prop_dict["logicalName"] = val

    @property
    def logon_users(self):
        """Gets and sets the logonUsers
        
        Returns: 
            :class:`LogonUsersCollectionPage<onedrivesdk.request.logon_users_collection.LogonUsersCollectionPage>`:
                The logonUsers
        """
        if "logonUsers" in self._prop_dict:
            return LogonUsersCollectionPage(self._prop_dict["logonUsers"])
        else:
            return None

    @property
    def net_bios_name(self):
        """
        Gets and sets the netBiosName
        
        Returns:
            str:
                The netBiosName
        """
        if "netBiosName" in self._prop_dict:
            return self._prop_dict["netBiosName"]
        else:
            return None

    @net_bios_name.setter
    def net_bios_name(self, val):
        self._prop_dict["netBiosName"] = val

    @property
    def network_interfaces(self):
        """Gets and sets the networkInterfaces
        
        Returns: 
            :class:`NetworkInterfacesCollectionPage<onedrivesdk.request.network_interfaces_collection.NetworkInterfacesCollectionPage>`:
                The networkInterfaces
        """
        if "networkInterfaces" in self._prop_dict:
            return NetworkInterfacesCollectionPage(self._prop_dict["networkInterfaces"])
        else:
            return None

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
    def parent_host(self):
        """
        Gets and sets the parentHost
        
        Returns:
            str:
                The parentHost
        """
        if "parentHost" in self._prop_dict:
            return self._prop_dict["parentHost"]
        else:
            return None

    @parent_host.setter
    def parent_host(self, val):
        self._prop_dict["parentHost"] = val

    @property
    def platform(self):
        """
        Gets and sets the platform
        
        Returns:
            str:
                The platform
        """
        if "platform" in self._prop_dict:
            return self._prop_dict["platform"]
        else:
            return None

    @platform.setter
    def platform(self, val):
        self._prop_dict["platform"] = val

    @property
    def risk_score(self):
        """
        Gets and sets the riskScore
        
        Returns:
            str:
                The riskScore
        """
        if "riskScore" in self._prop_dict:
            return self._prop_dict["riskScore"]
        else:
            return None

    @risk_score.setter
    def risk_score(self, val):
        self._prop_dict["riskScore"] = val

    @property
    def tags(self):
        """
        Gets and sets the tags
        
        Returns:
            str:
                The tags
        """
        if "tags" in self._prop_dict:
            return self._prop_dict["tags"]
        else:
            return None

    @tags.setter
    def tags(self, val):
        self._prop_dict["tags"] = val

    @property
    def vendor_information(self):
        """
        Gets and sets the vendorInformation
        
        Returns: 
            :class:`SecurityVendorInformation<onedrivesdk.model.security_vendor_information.SecurityVendorInformation>`:
                The vendorInformation
        """
        if "vendorInformation" in self._prop_dict:
            if isinstance(self._prop_dict["vendorInformation"], OneDriveObjectBase):
                return self._prop_dict["vendorInformation"]
            else :
                self._prop_dict["vendorInformation"] = SecurityVendorInformation(self._prop_dict["vendorInformation"])
                return self._prop_dict["vendorInformation"]

        return None

    @vendor_information.setter
    def vendor_information(self, val):
        self._prop_dict["vendorInformation"] = val

