# -*- coding: utf-8 -*- 
'''
# Copyright (c) Microsoft Corporation.  All Rights Reserved.  Licensed under the MIT License.  See License in the project root for license information.
# 
#  This file was generated and any changes will be overwritten.
'''

from __future__ import unicode_literals
from ..model.email_sync_duration import EmailSyncDuration
from ..model.user_email_source import UserEmailSource
from ..model.email_sync_schedule import EmailSyncSchedule
from ..one_drive_object_base import OneDriveObjectBase


class Windows10EasEmailProfileConfiguration(OneDriveObjectBase):

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

