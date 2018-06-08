# -*- coding: utf-8 -*- 
'''
# Copyright (c) Microsoft Corporation.  All Rights Reserved.  Licensed under the MIT License.  See License in the project root for license information.
# 
#  This file was generated and any changes will be overwritten.
'''

from __future__ import unicode_literals
from ..one_drive_object_base import OneDriveObjectBase


class HostSecurityState(OneDriveObjectBase):

    def __init__(self, prop_dict={}):
        self._prop_dict = prop_dict

    @property
    def fqdn(self):
        """Gets and sets the fqdn
        
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
    def is_azure_aad_joined(self):
        """Gets and sets the isAzureAadJoined
        
        Returns: 
            bool:
                The isAzureAadJoined
        """
        if "isAzureAadJoined" in self._prop_dict:
            return self._prop_dict["isAzureAadJoined"]
        else:
            return None

    @is_azure_aad_joined.setter
    def is_azure_aad_joined(self, val):
        self._prop_dict["isAzureAadJoined"] = val

    @property
    def is_azure_aad_registered(self):
        """Gets and sets the isAzureAadRegistered
        
        Returns: 
            bool:
                The isAzureAadRegistered
        """
        if "isAzureAadRegistered" in self._prop_dict:
            return self._prop_dict["isAzureAadRegistered"]
        else:
            return None

    @is_azure_aad_registered.setter
    def is_azure_aad_registered(self, val):
        self._prop_dict["isAzureAadRegistered"] = val

    @property
    def is_hybrid_azure_domain_joined(self):
        """Gets and sets the isHybridAzureDomainJoined
        
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
    def net_bios_name(self):
        """Gets and sets the netBiosName
        
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
    def private_ip_address(self):
        """Gets and sets the privateIpAddress
        
        Returns: 
            str:
                The privateIpAddress
        """
        if "privateIpAddress" in self._prop_dict:
            return self._prop_dict["privateIpAddress"]
        else:
            return None

    @private_ip_address.setter
    def private_ip_address(self, val):
        self._prop_dict["privateIpAddress"] = val

    @property
    def public_ip_address(self):
        """Gets and sets the publicIpAddress
        
        Returns: 
            str:
                The publicIpAddress
        """
        if "publicIpAddress" in self._prop_dict:
            return self._prop_dict["publicIpAddress"]
        else:
            return None

    @public_ip_address.setter
    def public_ip_address(self, val):
        self._prop_dict["publicIpAddress"] = val

    @property
    def risk_score(self):
        """Gets and sets the riskScore
        
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

