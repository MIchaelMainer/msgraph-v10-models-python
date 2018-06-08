# -*- coding: utf-8 -*- 
'''
# Copyright (c) Microsoft Corporation.  All Rights Reserved.  Licensed under the MIT License.  See License in the project root for license information.
# 
#  This file was generated and any changes will be overwritten.
'''

from __future__ import unicode_literals
from ..model.eap_type import EapType
from ..model.eap_fast_configuration import EapFastConfiguration
from ..model.wi_fi_authentication_method import WiFiAuthenticationMethod
from ..model.non_eap_authentication_method_for_eap_ttls_type import NonEapAuthenticationMethodForEapTtlsType
from ..model.ios_trusted_root_certificate import IosTrustedRootCertificate
from ..model.ios_certificate_profile_base import IosCertificateProfileBase
from ..one_drive_object_base import OneDriveObjectBase


class IosEnterpriseWiFiConfiguration(OneDriveObjectBase):

    def __init__(self, prop_dict={}):
        self._prop_dict = prop_dict

    @property
    def eap_type(self):
        """
        Gets and sets the eapType
        
        Returns: 
            :class:`EapType<onedrivesdk.model.eap_type.EapType>`:
                The eapType
        """
        if "eapType" in self._prop_dict:
            if isinstance(self._prop_dict["eapType"], OneDriveObjectBase):
                return self._prop_dict["eapType"]
            else :
                self._prop_dict["eapType"] = EapType(self._prop_dict["eapType"])
                return self._prop_dict["eapType"]

        return None

    @eap_type.setter
    def eap_type(self, val):
        self._prop_dict["eapType"] = val

    @property
    def eap_fast_configuration(self):
        """
        Gets and sets the eapFastConfiguration
        
        Returns: 
            :class:`EapFastConfiguration<onedrivesdk.model.eap_fast_configuration.EapFastConfiguration>`:
                The eapFastConfiguration
        """
        if "eapFastConfiguration" in self._prop_dict:
            if isinstance(self._prop_dict["eapFastConfiguration"], OneDriveObjectBase):
                return self._prop_dict["eapFastConfiguration"]
            else :
                self._prop_dict["eapFastConfiguration"] = EapFastConfiguration(self._prop_dict["eapFastConfiguration"])
                return self._prop_dict["eapFastConfiguration"]

        return None

    @eap_fast_configuration.setter
    def eap_fast_configuration(self, val):
        self._prop_dict["eapFastConfiguration"] = val

    @property
    def trusted_server_certificate_names(self):
        """
        Gets and sets the trustedServerCertificateNames
        
        Returns:
            str:
                The trustedServerCertificateNames
        """
        if "trustedServerCertificateNames" in self._prop_dict:
            return self._prop_dict["trustedServerCertificateNames"]
        else:
            return None

    @trusted_server_certificate_names.setter
    def trusted_server_certificate_names(self, val):
        self._prop_dict["trustedServerCertificateNames"] = val

    @property
    def authentication_method(self):
        """
        Gets and sets the authenticationMethod
        
        Returns: 
            :class:`WiFiAuthenticationMethod<onedrivesdk.model.wi_fi_authentication_method.WiFiAuthenticationMethod>`:
                The authenticationMethod
        """
        if "authenticationMethod" in self._prop_dict:
            if isinstance(self._prop_dict["authenticationMethod"], OneDriveObjectBase):
                return self._prop_dict["authenticationMethod"]
            else :
                self._prop_dict["authenticationMethod"] = WiFiAuthenticationMethod(self._prop_dict["authenticationMethod"])
                return self._prop_dict["authenticationMethod"]

        return None

    @authentication_method.setter
    def authentication_method(self, val):
        self._prop_dict["authenticationMethod"] = val

    @property
    def inner_authentication_protocol_for_eap_ttls(self):
        """
        Gets and sets the innerAuthenticationProtocolForEapTtls
        
        Returns: 
            :class:`NonEapAuthenticationMethodForEapTtlsType<onedrivesdk.model.non_eap_authentication_method_for_eap_ttls_type.NonEapAuthenticationMethodForEapTtlsType>`:
                The innerAuthenticationProtocolForEapTtls
        """
        if "innerAuthenticationProtocolForEapTtls" in self._prop_dict:
            if isinstance(self._prop_dict["innerAuthenticationProtocolForEapTtls"], OneDriveObjectBase):
                return self._prop_dict["innerAuthenticationProtocolForEapTtls"]
            else :
                self._prop_dict["innerAuthenticationProtocolForEapTtls"] = NonEapAuthenticationMethodForEapTtlsType(self._prop_dict["innerAuthenticationProtocolForEapTtls"])
                return self._prop_dict["innerAuthenticationProtocolForEapTtls"]

        return None

    @inner_authentication_protocol_for_eap_ttls.setter
    def inner_authentication_protocol_for_eap_ttls(self, val):
        self._prop_dict["innerAuthenticationProtocolForEapTtls"] = val

    @property
    def outer_identity_privacy_temporary_value(self):
        """
        Gets and sets the outerIdentityPrivacyTemporaryValue
        
        Returns:
            str:
                The outerIdentityPrivacyTemporaryValue
        """
        if "outerIdentityPrivacyTemporaryValue" in self._prop_dict:
            return self._prop_dict["outerIdentityPrivacyTemporaryValue"]
        else:
            return None

    @outer_identity_privacy_temporary_value.setter
    def outer_identity_privacy_temporary_value(self, val):
        self._prop_dict["outerIdentityPrivacyTemporaryValue"] = val

    @property
    def root_certificates_for_server_validation(self):
        """Gets and sets the rootCertificatesForServerValidation
        
        Returns: 
            :class:`RootCertificatesForServerValidationCollectionPage<onedrivesdk.request.root_certificates_for_server_validation_collection.RootCertificatesForServerValidationCollectionPage>`:
                The rootCertificatesForServerValidation
        """
        if "rootCertificatesForServerValidation" in self._prop_dict:
            return RootCertificatesForServerValidationCollectionPage(self._prop_dict["rootCertificatesForServerValidation"])
        else:
            return None

    @property
    def identity_certificate_for_client_authentication(self):
        """
        Gets and sets the identityCertificateForClientAuthentication
        
        Returns: 
            :class:`IosCertificateProfileBase<onedrivesdk.model.ios_certificate_profile_base.IosCertificateProfileBase>`:
                The identityCertificateForClientAuthentication
        """
        if "identityCertificateForClientAuthentication" in self._prop_dict:
            if isinstance(self._prop_dict["identityCertificateForClientAuthentication"], OneDriveObjectBase):
                return self._prop_dict["identityCertificateForClientAuthentication"]
            else :
                self._prop_dict["identityCertificateForClientAuthentication"] = IosCertificateProfileBase(self._prop_dict["identityCertificateForClientAuthentication"])
                return self._prop_dict["identityCertificateForClientAuthentication"]

        return None

    @identity_certificate_for_client_authentication.setter
    def identity_certificate_for_client_authentication(self, val):
        self._prop_dict["identityCertificateForClientAuthentication"] = val

