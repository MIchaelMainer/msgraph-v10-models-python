# -*- coding: utf-8 -*- 
'''
# Copyright (c) Microsoft Corporation.  All Rights Reserved.  Licensed under the MIT License.  See License in the project root for license information.
# 
#  This file was generated and any changes will be overwritten.
'''

from __future__ import unicode_literals
from ..model.vpn_authentication_method import VpnAuthenticationMethod
from ..model.windows_phone81_certificate_profile_base import WindowsPhone81CertificateProfileBase
from ..one_drive_object_base import OneDriveObjectBase


class WindowsPhone81VpnConfiguration(OneDriveObjectBase):

    def __init__(self, prop_dict={}):
        self._prop_dict = prop_dict

    @property
    def bypass_vpn_on_company_wifi(self):
        """
        Gets and sets the bypassVpnOnCompanyWifi
        
        Returns:
            bool:
                The bypassVpnOnCompanyWifi
        """
        if "bypassVpnOnCompanyWifi" in self._prop_dict:
            return self._prop_dict["bypassVpnOnCompanyWifi"]
        else:
            return None

    @bypass_vpn_on_company_wifi.setter
    def bypass_vpn_on_company_wifi(self, val):
        self._prop_dict["bypassVpnOnCompanyWifi"] = val

    @property
    def bypass_vpn_on_home_wifi(self):
        """
        Gets and sets the bypassVpnOnHomeWifi
        
        Returns:
            bool:
                The bypassVpnOnHomeWifi
        """
        if "bypassVpnOnHomeWifi" in self._prop_dict:
            return self._prop_dict["bypassVpnOnHomeWifi"]
        else:
            return None

    @bypass_vpn_on_home_wifi.setter
    def bypass_vpn_on_home_wifi(self, val):
        self._prop_dict["bypassVpnOnHomeWifi"] = val

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
    def remember_user_credentials(self):
        """
        Gets and sets the rememberUserCredentials
        
        Returns:
            bool:
                The rememberUserCredentials
        """
        if "rememberUserCredentials" in self._prop_dict:
            return self._prop_dict["rememberUserCredentials"]
        else:
            return None

    @remember_user_credentials.setter
    def remember_user_credentials(self, val):
        self._prop_dict["rememberUserCredentials"] = val

    @property
    def dns_suffix_search_list(self):
        """
        Gets and sets the dnsSuffixSearchList
        
        Returns:
            str:
                The dnsSuffixSearchList
        """
        if "dnsSuffixSearchList" in self._prop_dict:
            return self._prop_dict["dnsSuffixSearchList"]
        else:
            return None

    @dns_suffix_search_list.setter
    def dns_suffix_search_list(self, val):
        self._prop_dict["dnsSuffixSearchList"] = val

    @property
    def identity_certificate(self):
        """
        Gets and sets the identityCertificate
        
        Returns: 
            :class:`WindowsPhone81CertificateProfileBase<onedrivesdk.model.windows_phone81_certificate_profile_base.WindowsPhone81CertificateProfileBase>`:
                The identityCertificate
        """
        if "identityCertificate" in self._prop_dict:
            if isinstance(self._prop_dict["identityCertificate"], OneDriveObjectBase):
                return self._prop_dict["identityCertificate"]
            else :
                self._prop_dict["identityCertificate"] = WindowsPhone81CertificateProfileBase(self._prop_dict["identityCertificate"])
                return self._prop_dict["identityCertificate"]

        return None

    @identity_certificate.setter
    def identity_certificate(self, val):
        self._prop_dict["identityCertificate"] = val

