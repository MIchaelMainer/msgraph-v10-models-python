# -*- coding: utf-8 -*- 
'''
# Copyright (c) Microsoft Corporation.  All Rights Reserved.  Licensed under the MIT License.  See License in the project root for license information.
# 
#  This file was generated and any changes will be overwritten.
'''

from __future__ import unicode_literals
from ..model.apple_vpn_connection_type import AppleVpnConnectionType
from ..model.vpn_server import VpnServer
from ..model.key_value import KeyValue
from ..model.vpn_authentication_method import VpnAuthenticationMethod
from ..model.vpn_on_demand_rule import VpnOnDemandRule
from ..model.vpn_proxy_server import VpnProxyServer
from ..one_drive_object_base import OneDriveObjectBase


class AppleVpnConfiguration(OneDriveObjectBase):

    def __init__(self, prop_dict={}):
        self._prop_dict = prop_dict

    @property
    def connection_name(self):
        """
        Gets and sets the connectionName
        
        Returns:
            str:
                The connectionName
        """
        if "connectionName" in self._prop_dict:
            return self._prop_dict["connectionName"]
        else:
            return None

    @connection_name.setter
    def connection_name(self, val):
        self._prop_dict["connectionName"] = val

    @property
    def connection_type(self):
        """
        Gets and sets the connectionType
        
        Returns: 
            :class:`AppleVpnConnectionType<onedrivesdk.model.apple_vpn_connection_type.AppleVpnConnectionType>`:
                The connectionType
        """
        if "connectionType" in self._prop_dict:
            if isinstance(self._prop_dict["connectionType"], OneDriveObjectBase):
                return self._prop_dict["connectionType"]
            else :
                self._prop_dict["connectionType"] = AppleVpnConnectionType(self._prop_dict["connectionType"])
                return self._prop_dict["connectionType"]

        return None

    @connection_type.setter
    def connection_type(self, val):
        self._prop_dict["connectionType"] = val

    @property
    def login_group_or_domain(self):
        """
        Gets and sets the loginGroupOrDomain
        
        Returns:
            str:
                The loginGroupOrDomain
        """
        if "loginGroupOrDomain" in self._prop_dict:
            return self._prop_dict["loginGroupOrDomain"]
        else:
            return None

    @login_group_or_domain.setter
    def login_group_or_domain(self, val):
        self._prop_dict["loginGroupOrDomain"] = val

    @property
    def role(self):
        """
        Gets and sets the role
        
        Returns:
            str:
                The role
        """
        if "role" in self._prop_dict:
            return self._prop_dict["role"]
        else:
            return None

    @role.setter
    def role(self, val):
        self._prop_dict["role"] = val

    @property
    def realm(self):
        """
        Gets and sets the realm
        
        Returns:
            str:
                The realm
        """
        if "realm" in self._prop_dict:
            return self._prop_dict["realm"]
        else:
            return None

    @realm.setter
    def realm(self, val):
        self._prop_dict["realm"] = val

    @property
    def server(self):
        """
        Gets and sets the server
        
        Returns: 
            :class:`VpnServer<onedrivesdk.model.vpn_server.VpnServer>`:
                The server
        """
        if "server" in self._prop_dict:
            if isinstance(self._prop_dict["server"], OneDriveObjectBase):
                return self._prop_dict["server"]
            else :
                self._prop_dict["server"] = VpnServer(self._prop_dict["server"])
                return self._prop_dict["server"]

        return None

    @server.setter
    def server(self, val):
        self._prop_dict["server"] = val

    @property
    def identifier(self):
        """
        Gets and sets the identifier
        
        Returns:
            str:
                The identifier
        """
        if "identifier" in self._prop_dict:
            return self._prop_dict["identifier"]
        else:
            return None

    @identifier.setter
    def identifier(self, val):
        self._prop_dict["identifier"] = val

    @property
    def custom_data(self):
        """Gets and sets the customData
        
        Returns: 
            :class:`CustomDataCollectionPage<onedrivesdk.request.custom_data_collection.CustomDataCollectionPage>`:
                The customData
        """
        if "customData" in self._prop_dict:
            return CustomDataCollectionPage(self._prop_dict["customData"])
        else:
            return None

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
    def authentication_method(self):
        """
        Gets and sets the authenticationMethod
        
        Returns: 
            :class:`VpnAuthenticationMethod<onedrivesdk.model.vpn_authentication_method.VpnAuthenticationMethod>`:
                The authenticationMethod
        """
        if "authenticationMethod" in self._prop_dict:
            if isinstance(self._prop_dict["authenticationMethod"], OneDriveObjectBase):
                return self._prop_dict["authenticationMethod"]
            else :
                self._prop_dict["authenticationMethod"] = VpnAuthenticationMethod(self._prop_dict["authenticationMethod"])
                return self._prop_dict["authenticationMethod"]

        return None

    @authentication_method.setter
    def authentication_method(self, val):
        self._prop_dict["authenticationMethod"] = val

    @property
    def enable_per_app(self):
        """
        Gets and sets the enablePerApp
        
        Returns:
            bool:
                The enablePerApp
        """
        if "enablePerApp" in self._prop_dict:
            return self._prop_dict["enablePerApp"]
        else:
            return None

    @enable_per_app.setter
    def enable_per_app(self, val):
        self._prop_dict["enablePerApp"] = val

    @property
    def safari_domains(self):
        """
        Gets and sets the safariDomains
        
        Returns:
            str:
                The safariDomains
        """
        if "safariDomains" in self._prop_dict:
            return self._prop_dict["safariDomains"]
        else:
            return None

    @safari_domains.setter
    def safari_domains(self, val):
        self._prop_dict["safariDomains"] = val

    @property
    def on_demand_rules(self):
        """Gets and sets the onDemandRules
        
        Returns: 
            :class:`OnDemandRulesCollectionPage<onedrivesdk.request.on_demand_rules_collection.OnDemandRulesCollectionPage>`:
                The onDemandRules
        """
        if "onDemandRules" in self._prop_dict:
            return OnDemandRulesCollectionPage(self._prop_dict["onDemandRules"])
        else:
            return None

    @property
    def proxy_server(self):
        """
        Gets and sets the proxyServer
        
        Returns: 
            :class:`VpnProxyServer<onedrivesdk.model.vpn_proxy_server.VpnProxyServer>`:
                The proxyServer
        """
        if "proxyServer" in self._prop_dict:
            if isinstance(self._prop_dict["proxyServer"], OneDriveObjectBase):
                return self._prop_dict["proxyServer"]
            else :
                self._prop_dict["proxyServer"] = VpnProxyServer(self._prop_dict["proxyServer"])
                return self._prop_dict["proxyServer"]

        return None

    @proxy_server.setter
    def proxy_server(self, val):
        self._prop_dict["proxyServer"] = val

