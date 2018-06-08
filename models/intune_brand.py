# -*- coding: utf-8 -*- 
'''
# Copyright (c) Microsoft Corporation.  All Rights Reserved.  Licensed under the MIT License.  See License in the project root for license information.
# 
#  This file was generated and any changes will be overwritten.
'''

from __future__ import unicode_literals
from ..model.rgb_color import RgbColor
from ..model.mime_content import MimeContent
from ..one_drive_object_base import OneDriveObjectBase


class IntuneBrand(OneDriveObjectBase):

    def __init__(self, prop_dict={}):
        self._prop_dict = prop_dict

    @property
    def display_name(self):
        """Gets and sets the displayName
        
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
    def contact_it_name(self):
        """Gets and sets the contactITName
        
        Returns: 
            str:
                The contactITName
        """
        if "contactITName" in self._prop_dict:
            return self._prop_dict["contactITName"]
        else:
            return None

    @contact_it_name.setter
    def contact_it_name(self, val):
        self._prop_dict["contactITName"] = val

    @property
    def contact_it_phone_number(self):
        """Gets and sets the contactITPhoneNumber
        
        Returns: 
            str:
                The contactITPhoneNumber
        """
        if "contactITPhoneNumber" in self._prop_dict:
            return self._prop_dict["contactITPhoneNumber"]
        else:
            return None

    @contact_it_phone_number.setter
    def contact_it_phone_number(self, val):
        self._prop_dict["contactITPhoneNumber"] = val

    @property
    def contact_it_email_address(self):
        """Gets and sets the contactITEmailAddress
        
        Returns: 
            str:
                The contactITEmailAddress
        """
        if "contactITEmailAddress" in self._prop_dict:
            return self._prop_dict["contactITEmailAddress"]
        else:
            return None

    @contact_it_email_address.setter
    def contact_it_email_address(self, val):
        self._prop_dict["contactITEmailAddress"] = val

    @property
    def contact_it_notes(self):
        """Gets and sets the contactITNotes
        
        Returns: 
            str:
                The contactITNotes
        """
        if "contactITNotes" in self._prop_dict:
            return self._prop_dict["contactITNotes"]
        else:
            return None

    @contact_it_notes.setter
    def contact_it_notes(self, val):
        self._prop_dict["contactITNotes"] = val

    @property
    def privacy_url(self):
        """Gets and sets the privacyUrl
        
        Returns: 
            str:
                The privacyUrl
        """
        if "privacyUrl" in self._prop_dict:
            return self._prop_dict["privacyUrl"]
        else:
            return None

    @privacy_url.setter
    def privacy_url(self, val):
        self._prop_dict["privacyUrl"] = val

    @property
    def online_support_site_url(self):
        """Gets and sets the onlineSupportSiteUrl
        
        Returns: 
            str:
                The onlineSupportSiteUrl
        """
        if "onlineSupportSiteUrl" in self._prop_dict:
            return self._prop_dict["onlineSupportSiteUrl"]
        else:
            return None

    @online_support_site_url.setter
    def online_support_site_url(self, val):
        self._prop_dict["onlineSupportSiteUrl"] = val

    @property
    def online_support_site_name(self):
        """Gets and sets the onlineSupportSiteName
        
        Returns: 
            str:
                The onlineSupportSiteName
        """
        if "onlineSupportSiteName" in self._prop_dict:
            return self._prop_dict["onlineSupportSiteName"]
        else:
            return None

    @online_support_site_name.setter
    def online_support_site_name(self, val):
        self._prop_dict["onlineSupportSiteName"] = val

    @property
    def theme_color(self):
        """
        Gets and sets the themeColor
        
        Returns: 
            :class:`RgbColor<onedrivesdk.model.rgb_color.RgbColor>`:
                The themeColor
        """
        if "themeColor" in self._prop_dict:
            if isinstance(self._prop_dict["themeColor"], OneDriveObjectBase):
                return self._prop_dict["themeColor"]
            else :
                self._prop_dict["themeColor"] = RgbColor(self._prop_dict["themeColor"])
                return self._prop_dict["themeColor"]

        return None

    @theme_color.setter
    def theme_color(self, val):
        self._prop_dict["themeColor"] = val
    @property
    def show_logo(self):
        """Gets and sets the showLogo
        
        Returns: 
            bool:
                The showLogo
        """
        if "showLogo" in self._prop_dict:
            return self._prop_dict["showLogo"]
        else:
            return None

    @show_logo.setter
    def show_logo(self, val):
        self._prop_dict["showLogo"] = val

    @property
    def light_background_logo(self):
        """
        Gets and sets the lightBackgroundLogo
        
        Returns: 
            :class:`MimeContent<onedrivesdk.model.mime_content.MimeContent>`:
                The lightBackgroundLogo
        """
        if "lightBackgroundLogo" in self._prop_dict:
            if isinstance(self._prop_dict["lightBackgroundLogo"], OneDriveObjectBase):
                return self._prop_dict["lightBackgroundLogo"]
            else :
                self._prop_dict["lightBackgroundLogo"] = MimeContent(self._prop_dict["lightBackgroundLogo"])
                return self._prop_dict["lightBackgroundLogo"]

        return None

    @light_background_logo.setter
    def light_background_logo(self, val):
        self._prop_dict["lightBackgroundLogo"] = val
    @property
    def dark_background_logo(self):
        """
        Gets and sets the darkBackgroundLogo
        
        Returns: 
            :class:`MimeContent<onedrivesdk.model.mime_content.MimeContent>`:
                The darkBackgroundLogo
        """
        if "darkBackgroundLogo" in self._prop_dict:
            if isinstance(self._prop_dict["darkBackgroundLogo"], OneDriveObjectBase):
                return self._prop_dict["darkBackgroundLogo"]
            else :
                self._prop_dict["darkBackgroundLogo"] = MimeContent(self._prop_dict["darkBackgroundLogo"])
                return self._prop_dict["darkBackgroundLogo"]

        return None

    @dark_background_logo.setter
    def dark_background_logo(self, val):
        self._prop_dict["darkBackgroundLogo"] = val
    @property
    def show_name_next_to_logo(self):
        """Gets and sets the showNameNextToLogo
        
        Returns: 
            bool:
                The showNameNextToLogo
        """
        if "showNameNextToLogo" in self._prop_dict:
            return self._prop_dict["showNameNextToLogo"]
        else:
            return None

    @show_name_next_to_logo.setter
    def show_name_next_to_logo(self, val):
        self._prop_dict["showNameNextToLogo"] = val

    @property
    def show_display_name_next_to_logo(self):
        """Gets and sets the showDisplayNameNextToLogo
        
        Returns: 
            bool:
                The showDisplayNameNextToLogo
        """
        if "showDisplayNameNextToLogo" in self._prop_dict:
            return self._prop_dict["showDisplayNameNextToLogo"]
        else:
            return None

    @show_display_name_next_to_logo.setter
    def show_display_name_next_to_logo(self, val):
        self._prop_dict["showDisplayNameNextToLogo"] = val

