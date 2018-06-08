# -*- coding: utf-8 -*- 
'''
# Copyright (c) Microsoft Corporation.  All Rights Reserved.  Licensed under the MIT License.  See License in the project root for license information.
# 
#  This file was generated and any changes will be overwritten.
'''

from __future__ import unicode_literals
from ..model.android_wi_fi_security_type import AndroidWiFiSecurityType
from ..one_drive_object_base import OneDriveObjectBase


class AndroidForWorkWiFiConfiguration(OneDriveObjectBase):

    def __init__(self, prop_dict={}):
        self._prop_dict = prop_dict

    @property
    def network_name(self):
        """
        Gets and sets the networkName
        
        Returns:
            str:
                The networkName
        """
        if "networkName" in self._prop_dict:
            return self._prop_dict["networkName"]
        else:
            return None

    @network_name.setter
    def network_name(self, val):
        self._prop_dict["networkName"] = val

    @property
    def ssid(self):
        """
        Gets and sets the ssid
        
        Returns:
            str:
                The ssid
        """
        if "ssid" in self._prop_dict:
            return self._prop_dict["ssid"]
        else:
            return None

    @ssid.setter
    def ssid(self, val):
        self._prop_dict["ssid"] = val

    @property
    def connect_automatically(self):
        """
        Gets and sets the connectAutomatically
        
        Returns:
            bool:
                The connectAutomatically
        """
        if "connectAutomatically" in self._prop_dict:
            return self._prop_dict["connectAutomatically"]
        else:
            return None

    @connect_automatically.setter
    def connect_automatically(self, val):
        self._prop_dict["connectAutomatically"] = val

    @property
    def connect_when_network_name_is_hidden(self):
        """
        Gets and sets the connectWhenNetworkNameIsHidden
        
        Returns:
            bool:
                The connectWhenNetworkNameIsHidden
        """
        if "connectWhenNetworkNameIsHidden" in self._prop_dict:
            return self._prop_dict["connectWhenNetworkNameIsHidden"]
        else:
            return None

    @connect_when_network_name_is_hidden.setter
    def connect_when_network_name_is_hidden(self, val):
        self._prop_dict["connectWhenNetworkNameIsHidden"] = val

    @property
    def wi_fi_security_type(self):
        """
        Gets and sets the wiFiSecurityType
        
        Returns: 
            :class:`AndroidWiFiSecurityType<onedrivesdk.model.android_wi_fi_security_type.AndroidWiFiSecurityType>`:
                The wiFiSecurityType
        """
        if "wiFiSecurityType" in self._prop_dict:
            if isinstance(self._prop_dict["wiFiSecurityType"], OneDriveObjectBase):
                return self._prop_dict["wiFiSecurityType"]
            else :
                self._prop_dict["wiFiSecurityType"] = AndroidWiFiSecurityType(self._prop_dict["wiFiSecurityType"])
                return self._prop_dict["wiFiSecurityType"]

        return None

    @wi_fi_security_type.setter
    def wi_fi_security_type(self, val):
        self._prop_dict["wiFiSecurityType"] = val

