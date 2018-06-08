# -*- coding: utf-8 -*- 
'''
# Copyright (c) Microsoft Corporation.  All Rights Reserved.  Licensed under the MIT License.  See License in the project root for license information.
# 
#  This file was generated and any changes will be overwritten.
'''

from __future__ import unicode_literals
from ..model.team_member_settings import TeamMemberSettings
from ..model.team_messaging_settings import TeamMessagingSettings
from ..model.team_fun_settings import TeamFunSettings
from ..model.team_guest_settings import TeamGuestSettings
from ..model.channel import Channel
from ..one_drive_object_base import OneDriveObjectBase


class Team(OneDriveObjectBase):

    def __init__(self, prop_dict={}):
        self._prop_dict = prop_dict

    @property
    def member_settings(self):
        """
        Gets and sets the memberSettings
        
        Returns: 
            :class:`TeamMemberSettings<onedrivesdk.model.team_member_settings.TeamMemberSettings>`:
                The memberSettings
        """
        if "memberSettings" in self._prop_dict:
            if isinstance(self._prop_dict["memberSettings"], OneDriveObjectBase):
                return self._prop_dict["memberSettings"]
            else :
                self._prop_dict["memberSettings"] = TeamMemberSettings(self._prop_dict["memberSettings"])
                return self._prop_dict["memberSettings"]

        return None

    @member_settings.setter
    def member_settings(self, val):
        self._prop_dict["memberSettings"] = val

    @property
    def messaging_settings(self):
        """
        Gets and sets the messagingSettings
        
        Returns: 
            :class:`TeamMessagingSettings<onedrivesdk.model.team_messaging_settings.TeamMessagingSettings>`:
                The messagingSettings
        """
        if "messagingSettings" in self._prop_dict:
            if isinstance(self._prop_dict["messagingSettings"], OneDriveObjectBase):
                return self._prop_dict["messagingSettings"]
            else :
                self._prop_dict["messagingSettings"] = TeamMessagingSettings(self._prop_dict["messagingSettings"])
                return self._prop_dict["messagingSettings"]

        return None

    @messaging_settings.setter
    def messaging_settings(self, val):
        self._prop_dict["messagingSettings"] = val

    @property
    def fun_settings(self):
        """
        Gets and sets the funSettings
        
        Returns: 
            :class:`TeamFunSettings<onedrivesdk.model.team_fun_settings.TeamFunSettings>`:
                The funSettings
        """
        if "funSettings" in self._prop_dict:
            if isinstance(self._prop_dict["funSettings"], OneDriveObjectBase):
                return self._prop_dict["funSettings"]
            else :
                self._prop_dict["funSettings"] = TeamFunSettings(self._prop_dict["funSettings"])
                return self._prop_dict["funSettings"]

        return None

    @fun_settings.setter
    def fun_settings(self, val):
        self._prop_dict["funSettings"] = val

    @property
    def guest_settings(self):
        """
        Gets and sets the guestSettings
        
        Returns: 
            :class:`TeamGuestSettings<onedrivesdk.model.team_guest_settings.TeamGuestSettings>`:
                The guestSettings
        """
        if "guestSettings" in self._prop_dict:
            if isinstance(self._prop_dict["guestSettings"], OneDriveObjectBase):
                return self._prop_dict["guestSettings"]
            else :
                self._prop_dict["guestSettings"] = TeamGuestSettings(self._prop_dict["guestSettings"])
                return self._prop_dict["guestSettings"]

        return None

    @guest_settings.setter
    def guest_settings(self, val):
        self._prop_dict["guestSettings"] = val

    @property
    def web_url(self):
        """
        Gets and sets the webUrl
        
        Returns:
            str:
                The webUrl
        """
        if "webUrl" in self._prop_dict:
            return self._prop_dict["webUrl"]
        else:
            return None

    @web_url.setter
    def web_url(self, val):
        self._prop_dict["webUrl"] = val

    @property
    def channels(self):
        """Gets and sets the channels
        
        Returns: 
            :class:`ChannelsCollectionPage<onedrivesdk.request.channels_collection.ChannelsCollectionPage>`:
                The channels
        """
        if "channels" in self._prop_dict:
            return ChannelsCollectionPage(self._prop_dict["channels"])
        else:
            return None

