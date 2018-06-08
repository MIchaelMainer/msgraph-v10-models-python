# -*- coding: utf-8 -*- 
'''
# Copyright (c) Microsoft Corporation.  All Rights Reserved.  Licensed under the MIT License.  See License in the project root for license information.
# 
#  This file was generated and any changes will be overwritten.
'''

from __future__ import unicode_literals
from ..model.message_action_flag import MessageActionFlag
from ..model.importance import Importance
from ..model.sensitivity import Sensitivity
from ..model.recipient import Recipient
from ..model.size_range import SizeRange
from ..one_drive_object_base import OneDriveObjectBase


class MessageRulePredicates(OneDriveObjectBase):

    def __init__(self, prop_dict={}):
        self._prop_dict = prop_dict

    @property
    def categories(self):
        """Gets and sets the categories
        
        Returns: 
            str:
                The categories
        """
        if "categories" in self._prop_dict:
            return self._prop_dict["categories"]
        else:
            return None

    @categories.setter
    def categories(self, val):
        self._prop_dict["categories"] = val

    @property
    def subject_contains(self):
        """Gets and sets the subjectContains
        
        Returns: 
            str:
                The subjectContains
        """
        if "subjectContains" in self._prop_dict:
            return self._prop_dict["subjectContains"]
        else:
            return None

    @subject_contains.setter
    def subject_contains(self, val):
        self._prop_dict["subjectContains"] = val

    @property
    def body_contains(self):
        """Gets and sets the bodyContains
        
        Returns: 
            str:
                The bodyContains
        """
        if "bodyContains" in self._prop_dict:
            return self._prop_dict["bodyContains"]
        else:
            return None

    @body_contains.setter
    def body_contains(self, val):
        self._prop_dict["bodyContains"] = val

    @property
    def body_or_subject_contains(self):
        """Gets and sets the bodyOrSubjectContains
        
        Returns: 
            str:
                The bodyOrSubjectContains
        """
        if "bodyOrSubjectContains" in self._prop_dict:
            return self._prop_dict["bodyOrSubjectContains"]
        else:
            return None

    @body_or_subject_contains.setter
    def body_or_subject_contains(self, val):
        self._prop_dict["bodyOrSubjectContains"] = val

    @property
    def sender_contains(self):
        """Gets and sets the senderContains
        
        Returns: 
            str:
                The senderContains
        """
        if "senderContains" in self._prop_dict:
            return self._prop_dict["senderContains"]
        else:
            return None

    @sender_contains.setter
    def sender_contains(self, val):
        self._prop_dict["senderContains"] = val

    @property
    def recipient_contains(self):
        """Gets and sets the recipientContains
        
        Returns: 
            str:
                The recipientContains
        """
        if "recipientContains" in self._prop_dict:
            return self._prop_dict["recipientContains"]
        else:
            return None

    @recipient_contains.setter
    def recipient_contains(self, val):
        self._prop_dict["recipientContains"] = val

    @property
    def header_contains(self):
        """Gets and sets the headerContains
        
        Returns: 
            str:
                The headerContains
        """
        if "headerContains" in self._prop_dict:
            return self._prop_dict["headerContains"]
        else:
            return None

    @header_contains.setter
    def header_contains(self, val):
        self._prop_dict["headerContains"] = val

    @property
    def message_action_flag(self):
        """
        Gets and sets the messageActionFlag
        
        Returns: 
            :class:`MessageActionFlag<onedrivesdk.model.message_action_flag.MessageActionFlag>`:
                The messageActionFlag
        """
        if "messageActionFlag" in self._prop_dict:
            if isinstance(self._prop_dict["messageActionFlag"], OneDriveObjectBase):
                return self._prop_dict["messageActionFlag"]
            else :
                self._prop_dict["messageActionFlag"] = MessageActionFlag(self._prop_dict["messageActionFlag"])
                return self._prop_dict["messageActionFlag"]

        return None

    @message_action_flag.setter
    def message_action_flag(self, val):
        self._prop_dict["messageActionFlag"] = val
    @property
    def importance(self):
        """
        Gets and sets the importance
        
        Returns: 
            :class:`Importance<onedrivesdk.model.importance.Importance>`:
                The importance
        """
        if "importance" in self._prop_dict:
            if isinstance(self._prop_dict["importance"], OneDriveObjectBase):
                return self._prop_dict["importance"]
            else :
                self._prop_dict["importance"] = Importance(self._prop_dict["importance"])
                return self._prop_dict["importance"]

        return None

    @importance.setter
    def importance(self, val):
        self._prop_dict["importance"] = val
    @property
    def sensitivity(self):
        """
        Gets and sets the sensitivity
        
        Returns: 
            :class:`Sensitivity<onedrivesdk.model.sensitivity.Sensitivity>`:
                The sensitivity
        """
        if "sensitivity" in self._prop_dict:
            if isinstance(self._prop_dict["sensitivity"], OneDriveObjectBase):
                return self._prop_dict["sensitivity"]
            else :
                self._prop_dict["sensitivity"] = Sensitivity(self._prop_dict["sensitivity"])
                return self._prop_dict["sensitivity"]

        return None

    @sensitivity.setter
    def sensitivity(self, val):
        self._prop_dict["sensitivity"] = val
    @property
    def from_addresses(self):
        """
        Gets and sets the fromAddresses
        
        Returns: 
            :class:`Recipient<onedrivesdk.model.recipient.Recipient>`:
                The fromAddresses
        """
        if "fromAddresses" in self._prop_dict:
            if isinstance(self._prop_dict["fromAddresses"], OneDriveObjectBase):
                return self._prop_dict["fromAddresses"]
            else :
                self._prop_dict["fromAddresses"] = Recipient(self._prop_dict["fromAddresses"])
                return self._prop_dict["fromAddresses"]

        return None

    @from_addresses.setter
    def from_addresses(self, val):
        self._prop_dict["fromAddresses"] = val
    @property
    def sent_to_addresses(self):
        """
        Gets and sets the sentToAddresses
        
        Returns: 
            :class:`Recipient<onedrivesdk.model.recipient.Recipient>`:
                The sentToAddresses
        """
        if "sentToAddresses" in self._prop_dict:
            if isinstance(self._prop_dict["sentToAddresses"], OneDriveObjectBase):
                return self._prop_dict["sentToAddresses"]
            else :
                self._prop_dict["sentToAddresses"] = Recipient(self._prop_dict["sentToAddresses"])
                return self._prop_dict["sentToAddresses"]

        return None

    @sent_to_addresses.setter
    def sent_to_addresses(self, val):
        self._prop_dict["sentToAddresses"] = val
    @property
    def sent_to_me(self):
        """Gets and sets the sentToMe
        
        Returns: 
            bool:
                The sentToMe
        """
        if "sentToMe" in self._prop_dict:
            return self._prop_dict["sentToMe"]
        else:
            return None

    @sent_to_me.setter
    def sent_to_me(self, val):
        self._prop_dict["sentToMe"] = val

    @property
    def sent_only_to_me(self):
        """Gets and sets the sentOnlyToMe
        
        Returns: 
            bool:
                The sentOnlyToMe
        """
        if "sentOnlyToMe" in self._prop_dict:
            return self._prop_dict["sentOnlyToMe"]
        else:
            return None

    @sent_only_to_me.setter
    def sent_only_to_me(self, val):
        self._prop_dict["sentOnlyToMe"] = val

    @property
    def sent_cc_me(self):
        """Gets and sets the sentCcMe
        
        Returns: 
            bool:
                The sentCcMe
        """
        if "sentCcMe" in self._prop_dict:
            return self._prop_dict["sentCcMe"]
        else:
            return None

    @sent_cc_me.setter
    def sent_cc_me(self, val):
        self._prop_dict["sentCcMe"] = val

    @property
    def sent_to_or_cc_me(self):
        """Gets and sets the sentToOrCcMe
        
        Returns: 
            bool:
                The sentToOrCcMe
        """
        if "sentToOrCcMe" in self._prop_dict:
            return self._prop_dict["sentToOrCcMe"]
        else:
            return None

    @sent_to_or_cc_me.setter
    def sent_to_or_cc_me(self, val):
        self._prop_dict["sentToOrCcMe"] = val

    @property
    def not_sent_to_me(self):
        """Gets and sets the notSentToMe
        
        Returns: 
            bool:
                The notSentToMe
        """
        if "notSentToMe" in self._prop_dict:
            return self._prop_dict["notSentToMe"]
        else:
            return None

    @not_sent_to_me.setter
    def not_sent_to_me(self, val):
        self._prop_dict["notSentToMe"] = val

    @property
    def has_attachments(self):
        """Gets and sets the hasAttachments
        
        Returns: 
            bool:
                The hasAttachments
        """
        if "hasAttachments" in self._prop_dict:
            return self._prop_dict["hasAttachments"]
        else:
            return None

    @has_attachments.setter
    def has_attachments(self, val):
        self._prop_dict["hasAttachments"] = val

    @property
    def is_approval_request(self):
        """Gets and sets the isApprovalRequest
        
        Returns: 
            bool:
                The isApprovalRequest
        """
        if "isApprovalRequest" in self._prop_dict:
            return self._prop_dict["isApprovalRequest"]
        else:
            return None

    @is_approval_request.setter
    def is_approval_request(self, val):
        self._prop_dict["isApprovalRequest"] = val

    @property
    def is_automatic_forward(self):
        """Gets and sets the isAutomaticForward
        
        Returns: 
            bool:
                The isAutomaticForward
        """
        if "isAutomaticForward" in self._prop_dict:
            return self._prop_dict["isAutomaticForward"]
        else:
            return None

    @is_automatic_forward.setter
    def is_automatic_forward(self, val):
        self._prop_dict["isAutomaticForward"] = val

    @property
    def is_automatic_reply(self):
        """Gets and sets the isAutomaticReply
        
        Returns: 
            bool:
                The isAutomaticReply
        """
        if "isAutomaticReply" in self._prop_dict:
            return self._prop_dict["isAutomaticReply"]
        else:
            return None

    @is_automatic_reply.setter
    def is_automatic_reply(self, val):
        self._prop_dict["isAutomaticReply"] = val

    @property
    def is_encrypted(self):
        """Gets and sets the isEncrypted
        
        Returns: 
            bool:
                The isEncrypted
        """
        if "isEncrypted" in self._prop_dict:
            return self._prop_dict["isEncrypted"]
        else:
            return None

    @is_encrypted.setter
    def is_encrypted(self, val):
        self._prop_dict["isEncrypted"] = val

    @property
    def is_meeting_request(self):
        """Gets and sets the isMeetingRequest
        
        Returns: 
            bool:
                The isMeetingRequest
        """
        if "isMeetingRequest" in self._prop_dict:
            return self._prop_dict["isMeetingRequest"]
        else:
            return None

    @is_meeting_request.setter
    def is_meeting_request(self, val):
        self._prop_dict["isMeetingRequest"] = val

    @property
    def is_meeting_response(self):
        """Gets and sets the isMeetingResponse
        
        Returns: 
            bool:
                The isMeetingResponse
        """
        if "isMeetingResponse" in self._prop_dict:
            return self._prop_dict["isMeetingResponse"]
        else:
            return None

    @is_meeting_response.setter
    def is_meeting_response(self, val):
        self._prop_dict["isMeetingResponse"] = val

    @property
    def is_non_delivery_report(self):
        """Gets and sets the isNonDeliveryReport
        
        Returns: 
            bool:
                The isNonDeliveryReport
        """
        if "isNonDeliveryReport" in self._prop_dict:
            return self._prop_dict["isNonDeliveryReport"]
        else:
            return None

    @is_non_delivery_report.setter
    def is_non_delivery_report(self, val):
        self._prop_dict["isNonDeliveryReport"] = val

    @property
    def is_permission_controlled(self):
        """Gets and sets the isPermissionControlled
        
        Returns: 
            bool:
                The isPermissionControlled
        """
        if "isPermissionControlled" in self._prop_dict:
            return self._prop_dict["isPermissionControlled"]
        else:
            return None

    @is_permission_controlled.setter
    def is_permission_controlled(self, val):
        self._prop_dict["isPermissionControlled"] = val

    @property
    def is_read_receipt(self):
        """Gets and sets the isReadReceipt
        
        Returns: 
            bool:
                The isReadReceipt
        """
        if "isReadReceipt" in self._prop_dict:
            return self._prop_dict["isReadReceipt"]
        else:
            return None

    @is_read_receipt.setter
    def is_read_receipt(self, val):
        self._prop_dict["isReadReceipt"] = val

    @property
    def is_signed(self):
        """Gets and sets the isSigned
        
        Returns: 
            bool:
                The isSigned
        """
        if "isSigned" in self._prop_dict:
            return self._prop_dict["isSigned"]
        else:
            return None

    @is_signed.setter
    def is_signed(self, val):
        self._prop_dict["isSigned"] = val

    @property
    def is_voicemail(self):
        """Gets and sets the isVoicemail
        
        Returns: 
            bool:
                The isVoicemail
        """
        if "isVoicemail" in self._prop_dict:
            return self._prop_dict["isVoicemail"]
        else:
            return None

    @is_voicemail.setter
    def is_voicemail(self, val):
        self._prop_dict["isVoicemail"] = val

    @property
    def within_size_range(self):
        """
        Gets and sets the withinSizeRange
        
        Returns: 
            :class:`SizeRange<onedrivesdk.model.size_range.SizeRange>`:
                The withinSizeRange
        """
        if "withinSizeRange" in self._prop_dict:
            if isinstance(self._prop_dict["withinSizeRange"], OneDriveObjectBase):
                return self._prop_dict["withinSizeRange"]
            else :
                self._prop_dict["withinSizeRange"] = SizeRange(self._prop_dict["withinSizeRange"])
                return self._prop_dict["withinSizeRange"]

        return None

    @within_size_range.setter
    def within_size_range(self, val):
        self._prop_dict["withinSizeRange"] = val
