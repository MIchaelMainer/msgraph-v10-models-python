# -*- coding: utf-8 -*- 
'''
# Copyright (c) Microsoft Corporation.  All Rights Reserved.  Licensed under the MIT License.  See License in the project root for license information.
# 
#  This file was generated and any changes will be overwritten.
'''

from __future__ import unicode_literals
from ..model.windows_vpn_connection_type import WindowsVpnConnectionType
from ..model.windows81_vpn_proxy_server import Windows81VpnProxyServer
from ..one_drive_object_base import OneDriveObjectBase


class Windows81VpnConfiguration(OneDriveObjectBase):

    def __init__(self, prop_dict={}):
        self._prop_dict = prop_dict

    @property
    def apply_only_to_windows81(self):
        """
        Gets and sets the applyOnlyToWindows81
        
        Returns:
            bool:
                The applyOnlyToWindows81
        """
        if "applyOnlyToWindows81" in self._prop_dict:
            return self._prop_dict["applyOnlyToWindows81"]
        else:
            return None

    @apply_only_to_windows81.setter
    def apply_only_to_windows81(self, val):
        self._prop_dict["applyOnlyToWindows81"] = val

    @property
    def connection_type(self):
        """
        Gets and sets the connectionType
        
        Returns: 
            :class:`WindowsVpnConnectionType<onedrivesdk.model.windows_vpn_connection_type.WindowsVpnConnectionType>`:
                The connectionType
        """
        if "connectionType" in self._prop_dict:
            if isinstance(self._prop_dict["connectionType"], OneDriveObjectBase):
                return self._prop_dict["connectionType"]
            else :
                self._prop_dict["connectionType"] = WindowsVpnConnectionType(self._prop_dict["connectionType"])
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
    def proxy_server(self):
        """
        Gets and sets the proxyServer
        
        Returns: 
            :class:`Windows81VpnProxyServer<onedrivesdk.model.windows81_vpn_proxy_server.Windows81VpnProxyServer>`:
                The proxyServer
        """
        if "proxyServer" in self._prop_dict:
            if isinstance(self._prop_dict["proxyServer"], OneDriveObjectBase):
                return self._prop_dict["proxyServer"]
            else :
                self._prop_dict["proxyServer"] = Windows81VpnProxyServer(self._prop_dict["proxyServer"])
                return self._prop_dict["proxyServer"]

        return None

    @proxy_server.setter
    def proxy_server(self, val):
        self._prop_dict["proxyServer"] = val

