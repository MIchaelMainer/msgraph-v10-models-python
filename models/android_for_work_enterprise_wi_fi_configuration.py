# -*- coding: utf-8 -*- 
'''
# Copyright (c) Microsoft Corporation.  All Rights Reserved.  Licensed under the MIT License.  See License in the project root for license information.
# 
#  This file was generated and any changes will be overwritten.
'''

from __future__ import unicode_literals
from ..model.android_eap_type import AndroidEapType
from ..model.wi_fi_authentication_method import WiFiAuthenticationMethod
from ..model.non_eap_authentication_method_for_eap_ttls_type import NonEapAuthenticationMethodForEapTtlsType
from ..model.non_eap_authentication_method_for_peap import NonEapAuthenticationMethodForPeap
from ..model.android_for_work_trusted_root_certificate import AndroidForWorkTrustedRootCertificate
from ..model.android_for_work_certificate_profile_base import AndroidForWorkCertificateProfileBase
from ..one_drive_object_base import OneDriveObjectBase


class AndroidForWorkEnterpriseWiFiConfiguration(OneDriveObjectBase):

    def __init__(self, prop_dict={}):
        self._prop_dict = prop_dict

    @property
    def eap_type(self):
        """
        Gets and sets the eapType
        
        Returns: 
            :class:`AndroidEapType<onedrivesdk.model.android_eap_type.AndroidEapType>`:
                The eapType
        """
        if "eapType" in self._prop_dict:
            if isinstance(self._prop_dict["eapType"], OneDriveObjectBase):
                return self._prop_dict["eapType"]
            else :
                self._prop_dict["eapType"] = AndroidEapType(self._prop_dict["eapType"])
                return self._prop_dict["eapType"]

        return None

    @eap_type.setter
    def eap_type(self, val):
        self._prop_dict["eapType"] = val

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
    def inner_authentication_protocol_for_peap(self):
        """
        Gets and sets the innerAuthenticationProtocolForPeap
        
        Returns: 
            :class:`NonEapAuthenticationMethodForPeap<onedrivesdk.model.non_eap_authentication_method_for_peap.NonEapAuthenticationMethodForPeap>`:
                The innerAuthenticationProtocolForPeap
        """
        if "innerAuthenticationProtocolForPeap" in self._prop_dict:
            if isinstance(self._prop_dict["innerAuthenticationProtocolForPeap"], OneDriveObjectBase):
                return self._prop_dict["innerAuthenticationProtocolForPeap"]
            else :
                self._prop_dict["innerAuthenticationProtocolForPeap"] = NonEapAuthenticationMethodForPeap(self._prop_dict["innerAuthenticationProtocolForPeap"])
                return self._prop_dict["innerAuthenticationProtocolForPeap"]

        return None

    @inner_authentication_protocol_for_peap.setter
    def inner_authentication_protocol_for_peap(self, val):
        self._prop_dict["innerAuthenticationProtocolForPeap"] = val

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
    def root_certificate_for_server_validation(self):
        """
        Gets and sets the rootCertificateForServerValidation
        
        Returns: 
            :class:`AndroidForWorkTrustedRootCertificate<onedrivesdk.model.android_for_work_trusted_root_certificate.AndroidForWorkTrustedRootCertificate>`:
                The rootCertificateForServerValidation
        """
        if "rootCertificateForServerValidation" in self._prop_dict:
            if isinstance(self._prop_dict["rootCertificateForServerValidation"], OneDriveObjectBase):
                return self._prop_dict["rootCertificateForServerValidation"]
            else :
                self._prop_dict["rootCertificateForServerValidation"] = AndroidForWorkTrustedRootCertificate(self._prop_dict["rootCertificateForServerValidation"])
                return self._prop_dict["rootCertificateForServerValidation"]

        return None

    @root_certificate_for_server_validation.setter
    def root_certificate_for_server_validation(self, val):
        self._prop_dict["rootCertificateForServerValidation"] = val

    @property
    def identity_certificate_for_client_authentication(self):
        """
        Gets and sets the identityCertificateForClientAuthentication
        
        Returns: 
            :class:`AndroidForWorkCertificateProfileBase<onedrivesdk.model.android_for_work_certificate_profile_base.AndroidForWorkCertificateProfileBase>`:
                The identityCertificateForClientAuthentication
        """
        if "identityCertificateForClientAuthentication" in self._prop_dict:
            if isinstance(self._prop_dict["identityCertificateForClientAuthentication"], OneDriveObjectBase):
                return self._prop_dict["identityCertificateForClientAuthentication"]
            else :
                self._prop_dict["identityCertificateForClientAuthentication"] = AndroidForWorkCertificateProfileBase(self._prop_dict["identityCertificateForClientAuthentication"])
                return self._prop_dict["identityCertificateForClientAuthentication"]

        return None

    @identity_certificate_for_client_authentication.setter
    def identity_certificate_for_client_authentication(self, val):
        self._prop_dict["identityCertificateForClientAuthentication"] = val

