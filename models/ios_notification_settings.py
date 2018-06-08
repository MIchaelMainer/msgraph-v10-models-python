# -*- coding: utf-8 -*- 
'''
# Copyright (c) Microsoft Corporation.  All Rights Reserved.  Licensed under the MIT License.  See License in the project root for license information.
# 
#  This file was generated and any changes will be overwritten.
'''

from __future__ import unicode_literals
from ..model.ios_notification_alert_type import IosNotificationAlertType
from ..one_drive_object_base import OneDriveObjectBase


class IosNotificationSettings(OneDriveObjectBase):

    def __init__(self, prop_dict={}):
        self._prop_dict = prop_dict

    @property
    def bundle_id(self):
        """Gets and sets the bundleID
        
        Returns: 
            str:
                The bundleID
        """
        if "bundleID" in self._prop_dict:
            return self._prop_dict["bundleID"]
        else:
            return None

    @bundle_id.setter
    def bundle_id(self, val):
        self._prop_dict["bundleID"] = val

    @property
    def app_name(self):
        """Gets and sets the appName
        
        Returns: 
            str:
                The appName
        """
        if "appName" in self._prop_dict:
            return self._prop_dict["appName"]
        else:
            return None

    @app_name.setter
    def app_name(self, val):
        self._prop_dict["appName"] = val

    @property
    def publisher(self):
        """Gets and sets the publisher
        
        Returns: 
            str:
                The publisher
        """
        if "publisher" in self._prop_dict:
            return self._prop_dict["publisher"]
        else:
            return None

    @publisher.setter
    def publisher(self, val):
        self._prop_dict["publisher"] = val

    @property
    def enabled(self):
        """Gets and sets the enabled
        
        Returns: 
            bool:
                The enabled
        """
        if "enabled" in self._prop_dict:
            return self._prop_dict["enabled"]
        else:
            return None

    @enabled.setter
    def enabled(self, val):
        self._prop_dict["enabled"] = val

    @property
    def show_in_notification_center(self):
        """Gets and sets the showInNotificationCenter
        
        Returns: 
            bool:
                The showInNotificationCenter
        """
        if "showInNotificationCenter" in self._prop_dict:
            return self._prop_dict["showInNotificationCenter"]
        else:
            return None

    @show_in_notification_center.setter
    def show_in_notification_center(self, val):
        self._prop_dict["showInNotificationCenter"] = val

    @property
    def show_on_lock_screen(self):
        """Gets and sets the showOnLockScreen
        
        Returns: 
            bool:
                The showOnLockScreen
        """
        if "showOnLockScreen" in self._prop_dict:
            return self._prop_dict["showOnLockScreen"]
        else:
            return None

    @show_on_lock_screen.setter
    def show_on_lock_screen(self, val):
        self._prop_dict["showOnLockScreen"] = val

    @property
    def alert_type(self):
        """
        Gets and sets the alertType
        
        Returns: 
            :class:`IosNotificationAlertType<onedrivesdk.model.ios_notification_alert_type.IosNotificationAlertType>`:
                The alertType
        """
        if "alertType" in self._prop_dict:
            if isinstance(self._prop_dict["alertType"], OneDriveObjectBase):
                return self._prop_dict["alertType"]
            else :
                self._prop_dict["alertType"] = IosNotificationAlertType(self._prop_dict["alertType"])
                return self._prop_dict["alertType"]

        return None

    @alert_type.setter
    def alert_type(self, val):
        self._prop_dict["alertType"] = val
    @property
    def badges_enabled(self):
        """Gets and sets the badgesEnabled
        
        Returns: 
            bool:
                The badgesEnabled
        """
        if "badgesEnabled" in self._prop_dict:
            return self._prop_dict["badgesEnabled"]
        else:
            return None

    @badges_enabled.setter
    def badges_enabled(self, val):
        self._prop_dict["badgesEnabled"] = val

    @property
    def sounds_enabled(self):
        """Gets and sets the soundsEnabled
        
        Returns: 
            bool:
                The soundsEnabled
        """
        if "soundsEnabled" in self._prop_dict:
            return self._prop_dict["soundsEnabled"]
        else:
            return None

    @sounds_enabled.setter
    def sounds_enabled(self, val):
        self._prop_dict["soundsEnabled"] = val

