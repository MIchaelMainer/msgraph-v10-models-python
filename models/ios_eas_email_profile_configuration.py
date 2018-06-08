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
from ..model.ios_certificate_profile_base import IosCertificateProfileBase
from ..model.ios_certificate_profile import IosCertificateProfile
from ..one_drive_object_base import OneDriveObjectBase


class IosEasEmailProfileConfiguration(OneDriveObjectBase):

    def __init__(self, prop_dict={}):
        self._prop_dict = prop_dict

    @property
    def account_name(self):
        """
        Gets and sets the accountName
        
        Returns:
            str:
                The accountName
        """
        if "accountName" in self._prop_dict:
            return self._prop_dict["accountName"]
        else:
            return None

    @account_name.setter
    def account_name(self, val):
        self._prop_dict["accountName"] = val

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
    def block_moving_messages_to_other_email_accounts(self):
        """
        Gets and sets the blockMovingMessagesToOtherEmailAccounts
        
        Returns:
            bool:
                The blockMovingMessagesToOtherEmailAccounts
        """
        if "blockMovingMessagesToOtherEmailAccounts" in self._prop_dict:
            return self._prop_dict["blockMovingMessagesToOtherEmailAccounts"]
        else:
            return None

    @block_moving_messages_to_other_email_accounts.setter
    def block_moving_messages_to_other_email_accounts(self, val):
        self._prop_dict["blockMovingMessagesToOtherEmailAccounts"] = val

    @property
    def block_sending_email_from_third_party_apps(self):
        """
        Gets and sets the blockSendingEmailFromThirdPartyApps
        
        Returns:
            bool:
                The blockSendingEmailFromThirdPartyApps
        """
        if "blockSendingEmailFromThirdPartyApps" in self._prop_dict:
            return self._prop_dict["blockSendingEmailFromThirdPartyApps"]
        else:
            return None

    @block_sending_email_from_third_party_apps.setter
    def block_sending_email_from_third_party_apps(self, val):
        self._prop_dict["blockSendingEmailFromThirdPartyApps"] = val

    @property
    def block_syncing_recently_used_email_addresses(self):
        """
        Gets and sets the blockSyncingRecentlyUsedEmailAddresses
        
        Returns:
            bool:
                The blockSyncingRecentlyUsedEmailAddresses
        """
        if "blockSyncingRecentlyUsedEmailAddresses" in self._prop_dict:
            return self._prop_dict["blockSyncingRecentlyUsedEmailAddresses"]
        else:
            return None

    @block_syncing_recently_used_email_addresses.setter
    def block_syncing_recently_used_email_addresses(self, val):
        self._prop_dict["blockSyncingRecentlyUsedEmailAddresses"] = val

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
    def require_smime(self):
        """
        Gets and sets the requireSmime
        
        Returns:
            bool:
                The requireSmime
        """
        if "requireSmime" in self._prop_dict:
            return self._prop_dict["requireSmime"]
        else:
            return None

    @require_smime.setter
    def require_smime(self, val):
        self._prop_dict["requireSmime"] = val

    @property
    def smime_enable_per_message_switch(self):
        """
        Gets and sets the smimeEnablePerMessageSwitch
        
        Returns:
            bool:
                The smimeEnablePerMessageSwitch
        """
        if "smimeEnablePerMessageSwitch" in self._prop_dict:
            return self._prop_dict["smimeEnablePerMessageSwitch"]
        else:
            return None

    @smime_enable_per_message_switch.setter
    def smime_enable_per_message_switch(self, val):
        self._prop_dict["smimeEnablePerMessageSwitch"] = val

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
    def identity_certificate(self):
        """
        Gets and sets the identityCertificate
        
        Returns: 
            :class:`IosCertificateProfileBase<onedrivesdk.model.ios_certificate_profile_base.IosCertificateProfileBase>`:
                The identityCertificate
        """
        if "identityCertificate" in self._prop_dict:
            if isinstance(self._prop_dict["identityCertificate"], OneDriveObjectBase):
                return self._prop_dict["identityCertificate"]
            else :
                self._prop_dict["identityCertificate"] = IosCertificateProfileBase(self._prop_dict["identityCertificate"])
                return self._prop_dict["identityCertificate"]

        return None

    @identity_certificate.setter
    def identity_certificate(self, val):
        self._prop_dict["identityCertificate"] = val

    @property
    def smime_signing_certificate(self):
        """
        Gets and sets the smimeSigningCertificate
        
        Returns: 
            :class:`IosCertificateProfile<onedrivesdk.model.ios_certificate_profile.IosCertificateProfile>`:
                The smimeSigningCertificate
        """
        if "smimeSigningCertificate" in self._prop_dict:
            if isinstance(self._prop_dict["smimeSigningCertificate"], OneDriveObjectBase):
                return self._prop_dict["smimeSigningCertificate"]
            else :
                self._prop_dict["smimeSigningCertificate"] = IosCertificateProfile(self._prop_dict["smimeSigningCertificate"])
                return self._prop_dict["smimeSigningCertificate"]

        return None

    @smime_signing_certificate.setter
    def smime_signing_certificate(self, val):
        self._prop_dict["smimeSigningCertificate"] = val

    @property
    def smime_encryption_certificate(self):
        """
        Gets and sets the smimeEncryptionCertificate
        
        Returns: 
            :class:`IosCertificateProfile<onedrivesdk.model.ios_certificate_profile.IosCertificateProfile>`:
                The smimeEncryptionCertificate
        """
        if "smimeEncryptionCertificate" in self._prop_dict:
            if isinstance(self._prop_dict["smimeEncryptionCertificate"], OneDriveObjectBase):
                return self._prop_dict["smimeEncryptionCertificate"]
            else :
                self._prop_dict["smimeEncryptionCertificate"] = IosCertificateProfile(self._prop_dict["smimeEncryptionCertificate"])
                return self._prop_dict["smimeEncryptionCertificate"]

        return None

    @smime_encryption_certificate.setter
    def smime_encryption_certificate(self, val):
        self._prop_dict["smimeEncryptionCertificate"] = val

