# -*- coding: utf-8 -*- 
'''
# Copyright (c) Microsoft Corporation.  All Rights Reserved.  Licensed under the MIT License.  See License in the project root for license information.
# 
#  This file was generated and any changes will be overwritten.
'''

from __future__ import unicode_literals
from ..model.notification_template_branding_options import NotificationTemplateBrandingOptions
from ..model.localized_notification_message import LocalizedNotificationMessage
from datetime import datetime
from ..one_drive_object_base import OneDriveObjectBase


class NotificationMessageTemplate(OneDriveObjectBase):

    def __init__(self, prop_dict={}):
        self._prop_dict = prop_dict

    @property
    def last_modified_date_time(self):
        """
        Gets and sets the lastModifiedDateTime
        
        Returns:
            datetime:
                The lastModifiedDateTime
        """
        if "lastModifiedDateTime" in self._prop_dict:
            return datetime.strptime(self._prop_dict["lastModifiedDateTime"].replace("Z", ""), "%Y-%m-%dT%H:%M:%S.%f")
        else:
            return None

    @last_modified_date_time.setter
    def last_modified_date_time(self, val):
        self._prop_dict["lastModifiedDateTime"] = val.isoformat()+"Z"

    @property
    def display_name(self):
        """
        Gets and sets the displayName
        
        Returns:
            str:
                The displayName
        """
        if "displayName" in self._prop_dict:
            return self._prop_dict["displayName"]
        else:
            return None

    @display_name.setter
    def display_name(self, val):
        self._prop_dict["displayName"] = val

    @property
    def default_locale(self):
        """
        Gets and sets the defaultLocale
        
        Returns:
            str:
                The defaultLocale
        """
        if "defaultLocale" in self._prop_dict:
            return self._prop_dict["defaultLocale"]
        else:
            return None

    @default_locale.setter
    def default_locale(self, val):
        self._prop_dict["defaultLocale"] = val

    @property
    def branding_options(self):
        """
        Gets and sets the brandingOptions
        
        Returns: 
            :class:`NotificationTemplateBrandingOptions<onedrivesdk.model.notification_template_branding_options.NotificationTemplateBrandingOptions>`:
                The brandingOptions
        """
        if "brandingOptions" in self._prop_dict:
            if isinstance(self._prop_dict["brandingOptions"], OneDriveObjectBase):
                return self._prop_dict["brandingOptions"]
            else :
                self._prop_dict["brandingOptions"] = NotificationTemplateBrandingOptions(self._prop_dict["brandingOptions"])
                return self._prop_dict["brandingOptions"]

        return None

    @branding_options.setter
    def branding_options(self, val):
        self._prop_dict["brandingOptions"] = val

    @property
    def localized_notification_messages(self):
        """Gets and sets the localizedNotificationMessages
        
        Returns: 
            :class:`LocalizedNotificationMessagesCollectionPage<onedrivesdk.request.localized_notification_messages_collection.LocalizedNotificationMessagesCollectionPage>`:
                The localizedNotificationMessages
        """
        if "localizedNotificationMessages" in self._prop_dict:
            return LocalizedNotificationMessagesCollectionPage(self._prop_dict["localizedNotificationMessages"])
        else:
            return None

