# -*- coding: utf-8 -*- 
'''
# Copyright (c) Microsoft Corporation.  All Rights Reserved.  Licensed under the MIT License.  See License in the project root for license information.
# 
#  This file was generated and any changes will be overwritten.
'''

from __future__ import unicode_literals
from ..one_drive_object_base import OneDriveObjectBase


class MacOSFirewallApplication(OneDriveObjectBase):

    def __init__(self, prop_dict={}):
        self._prop_dict = prop_dict

    @property
    def bundle_id(self):
        """Gets and sets the bundleId
        
        Returns: 
            str:
                The bundleId
        """
        if "bundleId" in self._prop_dict:
            return self._prop_dict["bundleId"]
        else:
            return None

    @bundle_id.setter
    def bundle_id(self, val):
        self._prop_dict["bundleId"] = val

    @property
    def allows_incoming_connections(self):
        """Gets and sets the allowsIncomingConnections
        
        Returns: 
            bool:
                The allowsIncomingConnections
        """
        if "allowsIncomingConnections" in self._prop_dict:
            return self._prop_dict["allowsIncomingConnections"]
        else:
            return None

    @allows_incoming_connections.setter
    def allows_incoming_connections(self, val):
        self._prop_dict["allowsIncomingConnections"] = val

