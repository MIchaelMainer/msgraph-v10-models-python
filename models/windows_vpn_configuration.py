# -*- coding: utf-8 -*- 
'''
# Copyright (c) Microsoft Corporation.  All Rights Reserved.  Licensed under the MIT License.  See License in the project root for license information.
# 
#  This file was generated and any changes will be overwritten.
'''

from __future__ import unicode_literals
from ..model.vpn_server import VpnServer
from ..one_drive_object_base import OneDriveObjectBase


class WindowsVpnConfiguration(OneDriveObjectBase):

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
    def servers(self):
        """Gets and sets the servers
        
        Returns: 
            :class:`ServersCollectionPage<onedrivesdk.request.servers_collection.ServersCollectionPage>`:
                The servers
        """
        if "servers" in self._prop_dict:
            return ServersCollectionPage(self._prop_dict["servers"])
        else:
            return None

