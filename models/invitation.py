# -*- coding: utf-8 -*- 
'''
# Copyright (c) Microsoft Corporation.  All Rights Reserved.  Licensed under the MIT License.  See License in the project root for license information.
# 
#  This file was generated and any changes will be overwritten.
'''

from __future__ import unicode_literals
from ..model.invited_user_message_info import InvitedUserMessageInfo
from ..model.user import User
from ..one_drive_object_base import OneDriveObjectBase


class Invitation(OneDriveObjectBase):

    def __init__(self, prop_dict={}):
        self._prop_dict = prop_dict

    @property
    def invited_user_display_name(self):
        """
        Gets and sets the invitedUserDisplayName
        
        Returns:
            str:
                The invitedUserDisplayName
        """
        if "invitedUserDisplayName" in self._prop_dict:
            return self._prop_dict["invitedUserDisplayName"]
        else:
            return None

    @invited_user_display_name.setter
    def invited_user_display_name(self, val):
        self._prop_dict["invitedUserDisplayName"] = val

    @property
    def invited_user_type(self):
        """
        Gets and sets the invitedUserType
        
        Returns:
            str:
                The invitedUserType
        """
        if "invitedUserType" in self._prop_dict:
            return self._prop_dict["invitedUserType"]
        else:
            return None

    @invited_user_type.setter
    def invited_user_type(self, val):
        self._prop_dict["invitedUserType"] = val

    @property
    def invited_user_email_address(self):
        """
        Gets and sets the invitedUserEmailAddress
        
        Returns:
            str:
                The invitedUserEmailAddress
        """
        if "invitedUserEmailAddress" in self._prop_dict:
            return self._prop_dict["invitedUserEmailAddress"]
        else:
            return None

    @invited_user_email_address.setter
    def invited_user_email_address(self, val):
        self._prop_dict["invitedUserEmailAddress"] = val

    @property
    def invited_user_message_info(self):
        """
        Gets and sets the invitedUserMessageInfo
        
        Returns: 
            :class:`InvitedUserMessageInfo<onedrivesdk.model.invited_user_message_info.InvitedUserMessageInfo>`:
                The invitedUserMessageInfo
        """
        if "invitedUserMessageInfo" in self._prop_dict:
            if isinstance(self._prop_dict["invitedUserMessageInfo"], OneDriveObjectBase):
                return self._prop_dict["invitedUserMessageInfo"]
            else :
                self._prop_dict["invitedUserMessageInfo"] = InvitedUserMessageInfo(self._prop_dict["invitedUserMessageInfo"])
                return self._prop_dict["invitedUserMessageInfo"]

        return None

    @invited_user_message_info.setter
    def invited_user_message_info(self, val):
        self._prop_dict["invitedUserMessageInfo"] = val

    @property
    def send_invitation_message(self):
        """
        Gets and sets the sendInvitationMessage
        
        Returns:
            bool:
                The sendInvitationMessage
        """
        if "sendInvitationMessage" in self._prop_dict:
            return self._prop_dict["sendInvitationMessage"]
        else:
            return None

    @send_invitation_message.setter
    def send_invitation_message(self, val):
        self._prop_dict["sendInvitationMessage"] = val

    @property
    def invite_redirect_url(self):
        """
        Gets and sets the inviteRedirectUrl
        
        Returns:
            str:
                The inviteRedirectUrl
        """
        if "inviteRedirectUrl" in self._prop_dict:
            return self._prop_dict["inviteRedirectUrl"]
        else:
            return None

    @invite_redirect_url.setter
    def invite_redirect_url(self, val):
        self._prop_dict["inviteRedirectUrl"] = val

    @property
    def invite_redeem_url(self):
        """
        Gets and sets the inviteRedeemUrl
        
        Returns:
            str:
                The inviteRedeemUrl
        """
        if "inviteRedeemUrl" in self._prop_dict:
            return self._prop_dict["inviteRedeemUrl"]
        else:
            return None

    @invite_redeem_url.setter
    def invite_redeem_url(self, val):
        self._prop_dict["inviteRedeemUrl"] = val

    @property
    def status(self):
        """
        Gets and sets the status
        
        Returns:
            str:
                The status
        """
        if "status" in self._prop_dict:
            return self._prop_dict["status"]
        else:
            return None

    @status.setter
    def status(self, val):
        self._prop_dict["status"] = val

    @property
    def invited_user(self):
        """
        Gets and sets the invitedUser
        
        Returns: 
            :class:`User<onedrivesdk.model.user.User>`:
                The invitedUser
        """
        if "invitedUser" in self._prop_dict:
            if isinstance(self._prop_dict["invitedUser"], OneDriveObjectBase):
                return self._prop_dict["invitedUser"]
            else :
                self._prop_dict["invitedUser"] = User(self._prop_dict["invitedUser"])
                return self._prop_dict["invitedUser"]

        return None

    @invited_user.setter
    def invited_user(self, val):
        self._prop_dict["invitedUser"] = val

