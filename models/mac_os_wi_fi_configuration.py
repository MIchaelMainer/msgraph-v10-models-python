# -*- coding: utf-8 -*- 
'''
# Copyright (c) Microsoft Corporation.  All Rights Reserved.  Licensed under the MIT License.  See License in the project root for license information.
# 
#  This file was generated and any changes will be overwritten.
'''

from __future__ import unicode_literals
from ..model.wi_fi_security_type import WiFiSecurityType
from ..model.wi_fi_proxy_setting import WiFiProxySetting
from ..one_drive_object_base import OneDriveObjectBase


class MacOSWiFiConfiguration(OneDriveObjectBase):

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
            :class:`WiFiSecurityType<onedrivesdk.model.wi_fi_security_type.WiFiSecurityType>`:
                The wiFiSecurityType
        """
        if "wiFiSecurityType" in self._prop_dict:
            if isinstance(self._prop_dict["wiFiSecurityType"], OneDriveObjectBase):
                return self._prop_dict["wiFiSecurityType"]
            else :
                self._prop_dict["wiFiSecurityType"] = WiFiSecurityType(self._prop_dict["wiFiSecurityType"])
                return self._prop_dict["wiFiSecurityType"]

        return None

    @wi_fi_security_type.setter
    def wi_fi_security_type(self, val):
        self._prop_dict["wiFiSecurityType"] = val

    @property
    def proxy_settings(self):
        """
        Gets and sets the proxySettings
        
        Returns: 
            :class:`WiFiProxySetting<onedrivesdk.model.wi_fi_proxy_setting.WiFiProxySetting>`:
                The proxySettings
        """
        if "proxySettings" in self._prop_dict:
            if isinstance(self._prop_dict["proxySettings"], OneDriveObjectBase):
                return self._prop_dict["proxySettings"]
            else :
                self._prop_dict["proxySettings"] = WiFiProxySetting(self._prop_dict["proxySettings"])
                return self._prop_dict["proxySettings"]

        return None

    @proxy_settings.setter
    def proxy_settings(self, val):
        self._prop_dict["proxySettings"] = val

    @property
    def proxy_manual_address(self):
        """
        Gets and sets the proxyManualAddress
        
        Returns:
            str:
                The proxyManualAddress
        """
        if "proxyManualAddress" in self._prop_dict:
            return self._prop_dict["proxyManualAddress"]
        else:
            return None

    @proxy_manual_address.setter
    def proxy_manual_address(self, val):
        self._prop_dict["proxyManualAddress"] = val

    @property
    def proxy_manual_port(self):
        """
        Gets and sets the proxyManualPort
        
        Returns:
            int:
                The proxyManualPort
        """
        if "proxyManualPort" in self._prop_dict:
            return self._prop_dict["proxyManualPort"]
        else:
            return None

    @proxy_manual_port.setter
    def proxy_manual_port(self, val):
        self._prop_dict["proxyManualPort"] = val

    @property
    def proxy_automatic_configuration_url(self):
        """
        Gets and sets the proxyAutomaticConfigurationUrl
        
        Returns:
            str:
                The proxyAutomaticConfigurationUrl
        """
        if "proxyAutomaticConfigurationUrl" in self._prop_dict:
            return self._prop_dict["proxyAutomaticConfigurationUrl"]
        else:
            return None

    @proxy_automatic_configuration_url.setter
    def proxy_automatic_configuration_url(self, val):
        self._prop_dict["proxyAutomaticConfigurationUrl"] = val

    @property
    def pre_shared_key(self):
        """
        Gets and sets the preSharedKey
        
        Returns:
            str:
                The preSharedKey
        """
        if "preSharedKey" in self._prop_dict:
            return self._prop_dict["preSharedKey"]
        else:
            return None

    @pre_shared_key.setter
    def pre_shared_key(self, val):
        self._prop_dict["preSharedKey"] = val

