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
from ..model.email_sync_schedule import EmailSyncSchedule
from ..model.android_username_source import AndroidUsernameSource
from ..model.domain_name_source import DomainNameSource
from ..model.android_certificate_profile_base import AndroidCertificateProfileBase
from ..one_drive_object_base import OneDriveObjectBase


class AndroidEasEmailProfileConfiguration(OneDriveObjectBase):

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
    def sync_calendar(self):
        """
        Gets and sets the syncCalendar
        
        Returns:
            bool:
                The syncCalendar
        """
        if "syncCalendar" in self._prop_dict:
            return self._prop_dict["syncCalendar"]
        else:
            return None

    @sync_calendar.setter
    def sync_calendar(self, val):
        self._prop_dict["syncCalendar"] = val

    @property
    def sync_contacts(self):
        """
        Gets and sets the syncContacts
        
        Returns:
            bool:
                The syncContacts
        """
        if "syncContacts" in self._prop_dict:
            return self._prop_dict["syncContacts"]
        else:
            return None

    @sync_contacts.setter
    def sync_contacts(self, val):
        self._prop_dict["syncContacts"] = val

    @property
    def sync_tasks(self):
        """
        Gets and sets the syncTasks
        
        Returns:
            bool:
                The syncTasks
        """
        if "syncTasks" in self._prop_dict:
            return self._prop_dict["syncTasks"]
        else:
            return None

    @sync_tasks.setter
    def sync_tasks(self, val):
        self._prop_dict["syncTasks"] = val

    @property
    def sync_notes(self):
        """
        Gets and sets the syncNotes
        
        Returns:
            bool:
                The syncNotes
        """
        if "syncNotes" in self._prop_dict:
            return self._prop_dict["syncNotes"]
        else:
            return None

    @sync_notes.setter
    def sync_notes(self, val):
        self._prop_dict["syncNotes"] = val

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
    def email_sync_schedule(self):
        """
        Gets and sets the emailSyncSchedule
        
        Returns: 
            :class:`EmailSyncSchedule<onedrivesdk.model.email_sync_schedule.EmailSyncSchedule>`:
                The emailSyncSchedule
        """
        if "emailSyncSchedule" in self._prop_dict:
            if isinstance(self._prop_dict["emailSyncSchedule"], OneDriveObjectBase):
                return self._prop_dict["emailSyncSchedule"]
            else :
                self._prop_dict["emailSyncSchedule"] = EmailSyncSchedule(self._prop_dict["emailSyncSchedule"])
                return self._prop_dict["emailSyncSchedule"]

        return None

    @email_sync_schedule.setter
    def email_sync_schedule(self, val):
        self._prop_dict["emailSyncSchedule"] = val

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
    def user_domain_name_source(self):
        """
        Gets and sets the userDomainNameSource
        
        Returns: 
            :class:`DomainNameSource<onedrivesdk.model.domain_name_source.DomainNameSource>`:
                The userDomainNameSource
        """
        if "userDomainNameSource" in self._prop_dict:
            if isinstance(self._prop_dict["userDomainNameSource"], OneDriveObjectBase):
                return self._prop_dict["userDomainNameSource"]
            else :
                self._prop_dict["userDomainNameSource"] = DomainNameSource(self._prop_dict["userDomainNameSource"])
                return self._prop_dict["userDomainNameSource"]

        return None

    @user_domain_name_source.setter
    def user_domain_name_source(self, val):
        self._prop_dict["userDomainNameSource"] = val

    @property
    def custom_domain_name(self):
        """
        Gets and sets the customDomainName
        
        Returns:
            str:
                The customDomainName
        """
        if "customDomainName" in self._prop_dict:
            return self._prop_dict["customDomainName"]
        else:
            return None

    @custom_domain_name.setter
    def custom_domain_name(self, val):
        self._prop_dict["customDomainName"] = val

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

    @property
    def smime_signing_certificate(self):
        """
        Gets and sets the smimeSigningCertificate
        
        Returns: 
            :class:`AndroidCertificateProfileBase<onedrivesdk.model.android_certificate_profile_base.AndroidCertificateProfileBase>`:
                The smimeSigningCertificate
        """
        if "smimeSigningCertificate" in self._prop_dict:
            if isinstance(self._prop_dict["smimeSigningCertificate"], OneDriveObjectBase):
                return self._prop_dict["smimeSigningCertificate"]
            else :
                self._prop_dict["smimeSigningCertificate"] = AndroidCertificateProfileBase(self._prop_dict["smimeSigningCertificate"])
                return self._prop_dict["smimeSigningCertificate"]

        return None

    @smime_signing_certificate.setter
    def smime_signing_certificate(self, val):
        self._prop_dict["smimeSigningCertificate"] = val

