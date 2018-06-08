# -*- coding: utf-8 -*- 
'''
# Copyright (c) Microsoft Corporation.  All Rights Reserved.  Licensed under the MIT License.  See License in the project root for license information.
# 
#  This file was generated and any changes will be overwritten.
'''

from __future__ import unicode_literals
from ..model.eas_authentication_method import EasAuthenticationMethod
from ..model.email_sync_duration import EmailSyncDuration
from ..model.user_email_source import UserEmailSource
from ..model.android_username_source import AndroidUsernameSource
from ..model.android_for_work_certificate_profile_base import AndroidForWorkCertificateProfileBase
from ..one_drive_object_base import OneDriveObjectBase


class AndroidForWorkEasEmailProfileBase(OneDriveObjectBase):

    def __init__(self, prop_dict={}):
        self._prop_dict = prop_dict

    @property
    def authentication_method(self):
        """
        Gets and sets the authenticationMethod
        
        Returns: 
            :class:`EasAuthenticationMethod<onedrivesdk.model.eas_authentication_method.EasAuthenticationMethod>`:
                The authenticationMethod
        """
        if "authenticationMethod" in self._prop_dict:
            if isinstance(self._prop_dict["authenticationMethod"], OneDriveObjectBase):
                return self._prop_dict["authenticationMethod"]
            else :
                self._prop_dict["authenticationMethod"] = EasAuthenticationMethod(self._prop_dict["authenticationMethod"])
                return self._prop_dict["authenticationMethod"]

        return None

    @authentication_method.setter
    def authentication_method(self, val):
        self._prop_dict["authenticationMethod"] = val

    @property
    def duration_of_email_to_sync(self):
        """
        Gets and sets the durationOfEmailToSync
        
        Returns: 
            :class:`EmailSyncDuration<onedrivesdk.model.email_sync_duration.EmailSyncDuration>`:
                The durationOfEmailToSync
        """
        if "durationOfEmailToSync" in self._prop_dict:
            if isinstance(self._prop_dict["durationOfEmailToSync"], OneDriveObjectBase):
                return self._prop_dict["durationOfEmailToSync"]
            else :
                self._prop_dict["durationOfEmailToSync"] = EmailSyncDuration(self._prop_dict["durationOfEmailToSync"])
                return self._prop_dict["durationOfEmailToSync"]

        return None

    @duration_of_email_to_sync.setter
    def duration_of_email_to_sync(self, val):
        self._prop_dict["durationOfEmailToSync"] = val

    @property
    def email_address_source(self):
        """
        Gets and sets the emailAddressSource
        
        Returns: 
            :class:`UserEmailSource<onedrivesdk.model.user_email_source.UserEmailSource>`:
                The emailAddressSource
        """
        if "emailAddressSource" in self._prop_dict:
            if isinstance(self._prop_dict["emailAddressSource"], OneDriveObjectBase):
                return self._prop_dict["emailAddressSource"]
            else :
                self._prop_dict["emailAddressSource"] = UserEmailSource(self._prop_dict["emailAddressSource"])
                return self._prop_dict["emailAddressSource"]

        return None

    @email_address_source.setter
    def email_address_source(self, val):
        self._prop_dict["emailAddressSource"] = val

    @property
    def host_name(self):
        """
        Gets and sets the hostName
        
        Returns:
            str:
                The hostName
        """
        if "hostName" in self._prop_dict:
            return self._prop_dict["hostName"]
        else:
            return None

    @host_name.setter
    def host_name(self, val):
        self._prop_dict["hostName"] = val

    @property
    def require_ssl(self):
        """
        Gets and sets the requireSsl
        
        Returns:
            bool:
                The requireSsl
        """
        if "requireSsl" in self._prop_dict:
            return self._prop_dict["requireSsl"]
        else:
            return None

    @require_ssl.setter
    def require_ssl(self, val):
        self._prop_dict["requireSsl"] = val

    @property
    def username_source(self):
        """
        Gets and sets the usernameSource
        
        Returns: 
            :class:`AndroidUsernameSource<onedrivesdk.model.android_username_source.AndroidUsernameSource>`:
                The usernameSource
        """
        if "usernameSource" in self._prop_dict:
            if isinstance(self._prop_dict["usernameSource"], OneDriveObjectBase):
                return self._prop_dict["usernameSource"]
            else :
                self._prop_dict["usernameSource"] = AndroidUsernameSource(self._prop_dict["usernameSource"])
                return self._prop_dict["usernameSource"]

        return None

    @username_source.setter
    def username_source(self, val):
        self._prop_dict["usernameSource"] = val

    @property
    def identity_certificate(self):
        """
        Gets and sets the identityCertificate
        
        Returns: 
            :class:`AndroidForWorkCertificateProfileBase<onedrivesdk.model.android_for_work_certificate_profile_base.AndroidForWorkCertificateProfileBase>`:
                The identityCertificate
        """
        if "identityCertificate" in self._prop_dict:
            if isinstance(self._prop_dict["identityCertificate"], OneDriveObjectBase):
                return self._prop_dict["identityCertificate"]
            else :
                self._prop_dict["identityCertificate"] = AndroidForWorkCertificateProfileBase(self._prop_dict["identityCertificate"])
                return self._prop_dict["identityCertificate"]

        return None

    @identity_certificate.setter
    def identity_certificate(self, val):
        self._prop_dict["identityCertificate"] = val

