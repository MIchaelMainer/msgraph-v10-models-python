# -*- coding: utf-8 -*- 
'''
# Copyright (c) Microsoft Corporation.  All Rights Reserved.  Licensed under the MIT License.  See License in the project root for license information.
# 
#  This file was generated and any changes will be overwritten.
'''

from __future__ import unicode_literals
from ..model.recipient import Recipient
from ..one_drive_object_base import OneDriveObjectBase


class InvitedUserMessageInfo(OneDriveObjectBase):

    def __init__(self, prop_dict={}):
        self._prop_dict = prop_dict

    @property
    def cc_recipients(self):
        """
        Gets and sets the ccRecipients
        
        Returns: 
            :class:`Recipient<onedrivesdk.model.recipient.Recipient>`:
                The ccRecipients
        """
        if "ccRecipients" in self._prop_dict:
            if isinstance(self._prop_dict["ccRecipients"], OneDriveObjectBase):
                return self._prop_dict["ccRecipients"]
            else :
                self._prop_dict["ccRecipients"] = Recipient(self._prop_dict["ccRecipients"])
                return self._prop_dict["ccRecipients"]

        return None

    @cc_recipients.setter
    def cc_recipients(self, val):
        self._prop_dict["ccRecipients"] = val
    @property
    def message_language(self):
        """Gets and sets the messageLanguage
        
        Returns: 
            str:
                The messageLanguage
        """
        if "messageLanguage" in self._prop_dict:
            return self._prop_dict["messageLanguage"]
        else:
            return None

    @message_language.setter
    def message_language(self, val):
        self._prop_dict["messageLanguage"] = val

    @property
    def customized_message_body(self):
        """Gets and sets the customizedMessageBody
        
        Returns: 
            str:
                The customizedMessageBody
        """
        if "customizedMessageBody" in self._prop_dict:
            return self._prop_dict["customizedMessageBody"]
        else:
            return None

    @customized_message_body.setter
    def customized_message_body(self, val):
        self._prop_dict["customizedMessageBody"] = val

