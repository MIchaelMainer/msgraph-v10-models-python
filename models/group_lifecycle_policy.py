# -*- coding: utf-8 -*- 
'''
# Copyright (c) Microsoft Corporation.  All Rights Reserved.  Licensed under the MIT License.  See License in the project root for license information.
# 
#  This file was generated and any changes will be overwritten.
'''

from __future__ import unicode_literals
from ..one_drive_object_base import OneDriveObjectBase


class GroupLifecyclePolicy(OneDriveObjectBase):

    def __init__(self, prop_dict={}):
        self._prop_dict = prop_dict

    @property
    def group_lifetime_in_days(self):
        """
        Gets and sets the groupLifetimeInDays
        
        Returns:
            int:
                The groupLifetimeInDays
        """
        if "groupLifetimeInDays" in self._prop_dict:
            return self._prop_dict["groupLifetimeInDays"]
        else:
            return None

    @group_lifetime_in_days.setter
    def group_lifetime_in_days(self, val):
        self._prop_dict["groupLifetimeInDays"] = val

    @property
    def managed_group_types(self):
        """
        Gets and sets the managedGroupTypes
        
        Returns:
            str:
                The managedGroupTypes
        """
        if "managedGroupTypes" in self._prop_dict:
            return self._prop_dict["managedGroupTypes"]
        else:
            return None

    @managed_group_types.setter
    def managed_group_types(self, val):
        self._prop_dict["managedGroupTypes"] = val

    @property
    def alternate_notification_emails(self):
        """
        Gets and sets the alternateNotificationEmails
        
        Returns:
            str:
                The alternateNotificationEmails
        """
        if "alternateNotificationEmails" in self._prop_dict:
            return self._prop_dict["alternateNotificationEmails"]
        else:
            return None

    @alternate_notification_emails.setter
    def alternate_notification_emails(self, val):
        self._prop_dict["alternateNotificationEmails"] = val

