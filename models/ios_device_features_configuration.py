# -*- coding: utf-8 -*- 
'''
# Copyright (c) Microsoft Corporation.  All Rights Reserved.  Licensed under the MIT License.  See License in the project root for license information.
# 
#  This file was generated and any changes will be overwritten.
'''

from __future__ import unicode_literals
from ..model.ios_home_screen_item import IosHomeScreenItem
from ..model.ios_home_screen_page import IosHomeScreenPage
from ..model.ios_notification_settings import IosNotificationSettings
from ..one_drive_object_base import OneDriveObjectBase


class IosDeviceFeaturesConfiguration(OneDriveObjectBase):

    def __init__(self, prop_dict={}):
        self._prop_dict = prop_dict

    @property
    def asset_tag_template(self):
        """
        Gets and sets the assetTagTemplate
        
        Returns:
            str:
                The assetTagTemplate
        """
        if "assetTagTemplate" in self._prop_dict:
            return self._prop_dict["assetTagTemplate"]
        else:
            return None

    @asset_tag_template.setter
    def asset_tag_template(self, val):
        self._prop_dict["assetTagTemplate"] = val

    @property
    def lock_screen_footnote(self):
        """
        Gets and sets the lockScreenFootnote
        
        Returns:
            str:
                The lockScreenFootnote
        """
        if "lockScreenFootnote" in self._prop_dict:
            return self._prop_dict["lockScreenFootnote"]
        else:
            return None

    @lock_screen_footnote.setter
    def lock_screen_footnote(self, val):
        self._prop_dict["lockScreenFootnote"] = val

    @property
    def home_screen_dock_icons(self):
        """Gets and sets the homeScreenDockIcons
        
        Returns: 
            :class:`HomeScreenDockIconsCollectionPage<onedrivesdk.request.home_screen_dock_icons_collection.HomeScreenDockIconsCollectionPage>`:
                The homeScreenDockIcons
        """
        if "homeScreenDockIcons" in self._prop_dict:
            return HomeScreenDockIconsCollectionPage(self._prop_dict["homeScreenDockIcons"])
        else:
            return None

    @property
    def home_screen_pages(self):
        """Gets and sets the homeScreenPages
        
        Returns: 
            :class:`HomeScreenPagesCollectionPage<onedrivesdk.request.home_screen_pages_collection.HomeScreenPagesCollectionPage>`:
                The homeScreenPages
        """
        if "homeScreenPages" in self._prop_dict:
            return HomeScreenPagesCollectionPage(self._prop_dict["homeScreenPages"])
        else:
            return None

    @property
    def notification_settings(self):
        """Gets and sets the notificationSettings
        
        Returns: 
            :class:`NotificationSettingsCollectionPage<onedrivesdk.request.notification_settings_collection.NotificationSettingsCollectionPage>`:
                The notificationSettings
        """
        if "notificationSettings" in self._prop_dict:
            return NotificationSettingsCollectionPage(self._prop_dict["notificationSettings"])
        else:
            return None

