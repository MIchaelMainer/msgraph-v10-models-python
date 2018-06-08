# -*- coding: utf-8 -*- 
'''
# Copyright (c) Microsoft Corporation.  All Rights Reserved.  Licensed under the MIT License.  See License in the project root for license information.
# 
#  This file was generated and any changes will be overwritten.
'''

from __future__ import unicode_literals
from ..model.windows_kiosk_profile import WindowsKioskProfile
from ..one_drive_object_base import OneDriveObjectBase


class WindowsKioskConfiguration(OneDriveObjectBase):

    def __init__(self, prop_dict={}):
        self._prop_dict = prop_dict

    @property
    def kiosk_profiles(self):
        """Gets and sets the kioskProfiles
        
        Returns: 
            :class:`KioskProfilesCollectionPage<onedrivesdk.request.kiosk_profiles_collection.KioskProfilesCollectionPage>`:
                The kioskProfiles
        """
        if "kioskProfiles" in self._prop_dict:
            return KioskProfilesCollectionPage(self._prop_dict["kioskProfiles"])
        else:
            return None

    @property
    def kiosk_browser_default_url(self):
        """
        Gets and sets the kioskBrowserDefaultUrl
        
        Returns:
            str:
                The kioskBrowserDefaultUrl
        """
        if "kioskBrowserDefaultUrl" in self._prop_dict:
            return self._prop_dict["kioskBrowserDefaultUrl"]
        else:
            return None

    @kiosk_browser_default_url.setter
    def kiosk_browser_default_url(self, val):
        self._prop_dict["kioskBrowserDefaultUrl"] = val

    @property
    def kiosk_browser_enable_home_button(self):
        """
        Gets and sets the kioskBrowserEnableHomeButton
        
        Returns:
            bool:
                The kioskBrowserEnableHomeButton
        """
        if "kioskBrowserEnableHomeButton" in self._prop_dict:
            return self._prop_dict["kioskBrowserEnableHomeButton"]
        else:
            return None

    @kiosk_browser_enable_home_button.setter
    def kiosk_browser_enable_home_button(self, val):
        self._prop_dict["kioskBrowserEnableHomeButton"] = val

    @property
    def kiosk_browser_enable_navigation_buttons(self):
        """
        Gets and sets the kioskBrowserEnableNavigationButtons
        
        Returns:
            bool:
                The kioskBrowserEnableNavigationButtons
        """
        if "kioskBrowserEnableNavigationButtons" in self._prop_dict:
            return self._prop_dict["kioskBrowserEnableNavigationButtons"]
        else:
            return None

    @kiosk_browser_enable_navigation_buttons.setter
    def kiosk_browser_enable_navigation_buttons(self, val):
        self._prop_dict["kioskBrowserEnableNavigationButtons"] = val

    @property
    def kiosk_browser_restart_on_idle_time_in_minutes(self):
        """
        Gets and sets the kioskBrowserRestartOnIdleTimeInMinutes
        
        Returns:
            int:
                The kioskBrowserRestartOnIdleTimeInMinutes
        """
        if "kioskBrowserRestartOnIdleTimeInMinutes" in self._prop_dict:
            return self._prop_dict["kioskBrowserRestartOnIdleTimeInMinutes"]
        else:
            return None

    @kiosk_browser_restart_on_idle_time_in_minutes.setter
    def kiosk_browser_restart_on_idle_time_in_minutes(self, val):
        self._prop_dict["kioskBrowserRestartOnIdleTimeInMinutes"] = val

    @property
    def kiosk_browser_blocked_ur_ls(self):
        """
        Gets and sets the kioskBrowserBlockedURLs
        
        Returns:
            str:
                The kioskBrowserBlockedURLs
        """
        if "kioskBrowserBlockedURLs" in self._prop_dict:
            return self._prop_dict["kioskBrowserBlockedURLs"]
        else:
            return None

    @kiosk_browser_blocked_ur_ls.setter
    def kiosk_browser_blocked_ur_ls(self, val):
        self._prop_dict["kioskBrowserBlockedURLs"] = val

    @property
    def kiosk_browser_blocked_url_exceptions(self):
        """
        Gets and sets the kioskBrowserBlockedUrlExceptions
        
        Returns:
            str:
                The kioskBrowserBlockedUrlExceptions
        """
        if "kioskBrowserBlockedUrlExceptions" in self._prop_dict:
            return self._prop_dict["kioskBrowserBlockedUrlExceptions"]
        else:
            return None

    @kiosk_browser_blocked_url_exceptions.setter
    def kiosk_browser_blocked_url_exceptions(self, val):
        self._prop_dict["kioskBrowserBlockedUrlExceptions"] = val

