# -*- coding: utf-8 -*- 
'''
# Copyright (c) Microsoft Corporation.  All Rights Reserved.  Licensed under the MIT License.  See License in the project root for license information.
# 
#  This file was generated and any changes will be overwritten.
'''

from __future__ import unicode_literals
from ..model.email_address import EmailAddress
from ..model.automatic_replies_mail_tips import AutomaticRepliesMailTips
from ..model.recipient_scope_type import RecipientScopeType
from ..model.recipient import Recipient
from ..model.mail_tips_error import MailTipsError
from ..one_drive_object_base import OneDriveObjectBase


class MailTips(OneDriveObjectBase):

    def __init__(self, prop_dict={}):
        self._prop_dict = prop_dict

    @property
    def email_address(self):
        """
        Gets and sets the emailAddress
        
        Returns: 
            :class:`EmailAddress<onedrivesdk.model.email_address.EmailAddress>`:
                The emailAddress
        """
        if "emailAddress" in self._prop_dict:
            if isinstance(self._prop_dict["emailAddress"], OneDriveObjectBase):
                return self._prop_dict["emailAddress"]
            else :
                self._prop_dict["emailAddress"] = EmailAddress(self._prop_dict["emailAddress"])
                return self._prop_dict["emailAddress"]

        return None

    @email_address.setter
    def email_address(self, val):
        self._prop_dict["emailAddress"] = val
    @property
    def automatic_replies(self):
        """
        Gets and sets the automaticReplies
        
        Returns: 
            :class:`AutomaticRepliesMailTips<onedrivesdk.model.automatic_replies_mail_tips.AutomaticRepliesMailTips>`:
                The automaticReplies
        """
        if "automaticReplies" in self._prop_dict:
            if isinstance(self._prop_dict["automaticReplies"], OneDriveObjectBase):
                return self._prop_dict["automaticReplies"]
            else :
                self._prop_dict["automaticReplies"] = AutomaticRepliesMailTips(self._prop_dict["automaticReplies"])
                return self._prop_dict["automaticReplies"]

        return None

    @automatic_replies.setter
    def automatic_replies(self, val):
        self._prop_dict["automaticReplies"] = val
    @property
    def mailbox_full(self):
        """Gets and sets the mailboxFull
        
        Returns: 
            bool:
                The mailboxFull
        """
        if "mailboxFull" in self._prop_dict:
            return self._prop_dict["mailboxFull"]
        else:
            return None

    @mailbox_full.setter
    def mailbox_full(self, val):
        self._prop_dict["mailboxFull"] = val

    @property
    def custom_mail_tip(self):
        """Gets and sets the customMailTip
        
        Returns: 
            str:
                The customMailTip
        """
        if "customMailTip" in self._prop_dict:
            return self._prop_dict["customMailTip"]
        else:
            return None

    @custom_mail_tip.setter
    def custom_mail_tip(self, val):
        self._prop_dict["customMailTip"] = val

    @property
    def external_member_count(self):
        """Gets and sets the externalMemberCount
        
        Returns: 
            int:
                The externalMemberCount
        """
        if "externalMemberCount" in self._prop_dict:
            return self._prop_dict["externalMemberCount"]
        else:
            return None

    @external_member_count.setter
    def external_member_count(self, val):
        self._prop_dict["externalMemberCount"] = val

    @property
    def total_member_count(self):
        """Gets and sets the totalMemberCount
        
        Returns: 
            int:
                The totalMemberCount
        """
        if "totalMemberCount" in self._prop_dict:
            return self._prop_dict["totalMemberCount"]
        else:
            return None

    @total_member_count.setter
    def total_member_count(self, val):
        self._prop_dict["totalMemberCount"] = val

    @property
    def delivery_restricted(self):
        """Gets and sets the deliveryRestricted
        
        Returns: 
            bool:
                The deliveryRestricted
        """
        if "deliveryRestricted" in self._prop_dict:
            return self._prop_dict["deliveryRestricted"]
        else:
            return None

    @delivery_restricted.setter
    def delivery_restricted(self, val):
        self._prop_dict["deliveryRestricted"] = val

    @property
    def is_moderated(self):
        """Gets and sets the isModerated
        
        Returns: 
            bool:
                The isModerated
        """
        if "isModerated" in self._prop_dict:
            return self._prop_dict["isModerated"]
        else:
            return None

    @is_moderated.setter
    def is_moderated(self, val):
        self._prop_dict["isModerated"] = val

    @property
    def recipient_scope(self):
        """
        Gets and sets the recipientScope
        
        Returns: 
            :class:`RecipientScopeType<onedrivesdk.model.recipient_scope_type.RecipientScopeType>`:
                The recipientScope
        """
        if "recipientScope" in self._prop_dict:
            if isinstance(self._prop_dict["recipientScope"], OneDriveObjectBase):
                return self._prop_dict["recipientScope"]
            else :
                self._prop_dict["recipientScope"] = RecipientScopeType(self._prop_dict["recipientScope"])
                return self._prop_dict["recipientScope"]

        return None

    @recipient_scope.setter
    def recipient_scope(self, val):
        self._prop_dict["recipientScope"] = val
    @property
    def recipient_suggestions(self):
        """
        Gets and sets the recipientSuggestions
        
        Returns: 
            :class:`Recipient<onedrivesdk.model.recipient.Recipient>`:
                The recipientSuggestions
        """
        if "recipientSuggestions" in self._prop_dict:
            if isinstance(self._prop_dict["recipientSuggestions"], OneDriveObjectBase):
                return self._prop_dict["recipientSuggestions"]
            else :
                self._prop_dict["recipientSuggestions"] = Recipient(self._prop_dict["recipientSuggestions"])
                return self._prop_dict["recipientSuggestions"]

        return None

    @recipient_suggestions.setter
    def recipient_suggestions(self, val):
        self._prop_dict["recipientSuggestions"] = val
    @property
    def max_message_size(self):
        """Gets and sets the maxMessageSize
        
        Returns: 
            int:
                The maxMessageSize
        """
        if "maxMessageSize" in self._prop_dict:
            return self._prop_dict["maxMessageSize"]
        else:
            return None

    @max_message_size.setter
    def max_message_size(self, val):
        self._prop_dict["maxMessageSize"] = val

    @property
    def error(self):
        """
        Gets and sets the error
        
        Returns: 
            :class:`MailTipsError<onedrivesdk.model.mail_tips_error.MailTipsError>`:
                The error
        """
        if "error" in self._prop_dict:
            if isinstance(self._prop_dict["error"], OneDriveObjectBase):
                return self._prop_dict["error"]
            else :
                self._prop_dict["error"] = MailTipsError(self._prop_dict["error"])
                return self._prop_dict["error"]

        return None

    @error.setter
    def error(self, val):
        self._prop_dict["error"] = val
