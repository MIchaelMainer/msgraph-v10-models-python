# -*- coding: utf-8 -*- 
'''
# Copyright (c) Microsoft Corporation.  All Rights Reserved.  Licensed under the MIT License.  See License in the project root for license information.
# 
#  This file was generated and any changes will be overwritten.
'''

from __future__ import unicode_literals
from ..model.security_network_protocol import SecurityNetworkProtocol
from ..one_drive_object_base import OneDriveObjectBase


class NetworkConnection(OneDriveObjectBase):

    def __init__(self, prop_dict={}):
        self._prop_dict = prop_dict

    @property
    def destination_address(self):
        """Gets and sets the destinationAddress
        
        Returns: 
            str:
                The destinationAddress
        """
        if "destinationAddress" in self._prop_dict:
            return self._prop_dict["destinationAddress"]
        else:
            return None

    @destination_address.setter
    def destination_address(self, val):
        self._prop_dict["destinationAddress"] = val

    @property
    def destination_port(self):
        """Gets and sets the destinationPort
        
        Returns: 
            str:
                The destinationPort
        """
        if "destinationPort" in self._prop_dict:
            return self._prop_dict["destinationPort"]
        else:
            return None

    @destination_port.setter
    def destination_port(self, val):
        self._prop_dict["destinationPort"] = val

    @property
    def protocol(self):
        """
        Gets and sets the protocol
        
        Returns: 
            :class:`SecurityNetworkProtocol<onedrivesdk.model.security_network_protocol.SecurityNetworkProtocol>`:
                The protocol
        """
        if "protocol" in self._prop_dict:
            if isinstance(self._prop_dict["protocol"], OneDriveObjectBase):
                return self._prop_dict["protocol"]
            else :
                self._prop_dict["protocol"] = SecurityNetworkProtocol(self._prop_dict["protocol"])
                return self._prop_dict["protocol"]

        return None

    @protocol.setter
    def protocol(self, val):
        self._prop_dict["protocol"] = val
    @property
    def source_address(self):
        """Gets and sets the sourceAddress
        
        Returns: 
            str:
                The sourceAddress
        """
        if "sourceAddress" in self._prop_dict:
            return self._prop_dict["sourceAddress"]
        else:
            return None

    @source_address.setter
    def source_address(self, val):
        self._prop_dict["sourceAddress"] = val

    @property
    def source_port(self):
        """Gets and sets the sourcePort
        
        Returns: 
            str:
                The sourcePort
        """
        if "sourcePort" in self._prop_dict:
            return self._prop_dict["sourcePort"]
        else:
            return None

    @source_port.setter
    def source_port(self, val):
        self._prop_dict["sourcePort"] = val

    @property
    def uri(self):
        """Gets and sets the uri
        
        Returns: 
            str:
                The uri
        """
        if "uri" in self._prop_dict:
            return self._prop_dict["uri"]
        else:
            return None

    @uri.setter
    def uri(self, val):
        self._prop_dict["uri"] = val

