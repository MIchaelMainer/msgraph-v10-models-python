# -*- coding: utf-8 -*- 
'''
# Copyright (c) Microsoft Corporation.  All Rights Reserved.  Licensed under the MIT License.  See License in the project root for license information.
# 
#  This file was generated and any changes will be overwritten.
'''

from __future__ import unicode_literals
from ..one_drive_object_base import OneDriveObjectBase


class TeamMessagingSettings(OneDriveObjectBase):

    def __init__(self, prop_dict={}):
        self._prop_dict = prop_dict

    @property
    def allow_user_edit_messages(self):
        """Gets and sets the allowUserEditMessages
        
        Returns: 
            bool:
                The allowUserEditMessages
        """
        if "allowUserEditMessages" in self._prop_dict:
            return self._prop_dict["allowUserEditMessages"]
        else:
            return None

    @allow_user_edit_messages.setter
    def allow_user_edit_messages(self, val):
        self._prop_dict["allowUserEditMessages"] = val

    @property
    def allow_user_delete_messages(self):
        """Gets and sets the allowUserDeleteMessages
        
        Returns: 
            bool:
                The allowUserDeleteMessages
        """
        if "allowUserDeleteMessages" in self._prop_dict:
            return self._prop_dict["allowUserDeleteMessages"]
        else:
            return None

    @allow_user_delete_messages.setter
    def allow_user_delete_messages(self, val):
        self._prop_dict["allowUserDeleteMessages"] = val

    @property
    def allow_owner_delete_messages(self):
        """Gets and sets the allowOwnerDeleteMessages
        
        Returns: 
            bool:
                The allowOwnerDeleteMessages
        """
        if "allowOwnerDeleteMessages" in self._prop_dict:
            return self._prop_dict["allowOwnerDeleteMessages"]
        else:
            return None

    @allow_owner_delete_messages.setter
    def allow_owner_delete_messages(self, val):
        self._prop_dict["allowOwnerDeleteMessages"] = val

    @property
    def allow_team_mentions(self):
        """Gets and sets the allowTeamMentions
        
        Returns: 
            bool:
                The allowTeamMentions
        """
        if "allowTeamMentions" in self._prop_dict:
            return self._prop_dict["allowTeamMentions"]
        else:
            return None

    @allow_team_mentions.setter
    def allow_team_mentions(self, val):
        self._prop_dict["allowTeamMentions"] = val

    @property
    def allow_channel_mentions(self):
        """Gets and sets the allowChannelMentions
        
        Returns: 
            bool:
                The allowChannelMentions
        """
        if "allowChannelMentions" in self._prop_dict:
            return self._prop_dict["allowChannelMentions"]
        else:
            return None

    @allow_channel_mentions.setter
    def allow_channel_mentions(self, val):
        self._prop_dict["allowChannelMentions"] = val

