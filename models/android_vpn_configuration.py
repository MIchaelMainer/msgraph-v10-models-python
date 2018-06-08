# -*- coding: utf-8 -*- 
'''
# Copyright (c) Microsoft Corporation.  All Rights Reserved.  Licensed under the MIT License.  See License in the project root for license information.
# 
#  This file was generated and any changes will be overwritten.
'''

from __future__ import unicode_literals
from ..model.android_vpn_connection_type import AndroidVpnConnectionType
from ..model.vpn_server import VpnServer
from ..model.key_value import KeyValue
from ..model.vpn_authentication_method import VpnAuthenticationMethod
from ..model.android_certificate_profile_base import AndroidCertificateProfileBase
from ..one_drive_object_base import OneDriveObjectBase


class AndroidVpnConfiguration(OneDriveObjectBase):

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
            :class:`AndroidVpnConnectionType<onedrivesdk.model.android_vpn_connection_type.AndroidVpnConnectionType>`:
                The connectionType
        """
        if "connectionType" in self._prop_dict:
            if isinstance(self._prop_dict["connectionType"], OneDriveObjectBase):
                return self._prop_dict["connectionType"]
            else :
                self._prop_dict["connectionType"] = AndroidVpnConnectionType(self._prop_dict["connectionType"])
                return self._prop_dict["connectionType"]

        return None

    @connection_type.setter
    def connection_type(self, val):
        self._prop_dict["connectionType"] = val

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

    @property
    def fingerprint(self):
        """
        Gets and sets the fingerprint
        
        Returns:
            str:
                The fingerprint
        """
        if "fingerprint" in self._prop_dict:
            return self._prop_dict["fingerprint"]
        else:
            return None

    @fingerprint.setter
    def fingerprint(self, val):
        self._prop_dict["fingerprint"] = val

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
    def identity_certificate(self):
        """
        Gets and sets the identityCertificate
        
        Returns: 
            :class:`AndroidCertificateProfileBase<onedrivesdk.model.android_certificate_profile_base.AndroidCertificateProfileBase>`:
                The identityCertificate
        """
        if "identityCertificate" in self._prop_dict:
            if isinstance(self._prop_dict["identityCertificate"], OneDriveObjectBase):
                return self._prop_dict["identityCertificate"]
            else :
                self._prop_dict["identityCertificate"] = AndroidCertificateProfileBase(self._prop_dict["identityCertificate"])
                return self._prop_dict["identityCertificate"]

        return None

    @identity_certificate.setter
    def identity_certificate(self, val):
        self._prop_dict["identityCertificate"] = val

