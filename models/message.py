# -*- coding: utf-8 -*- 
'''
# Copyright (c) Microsoft Corporation.  All Rights Reserved.  Licensed under the MIT License.  See License in the project root for license information.
# 
#  This file was generated and any changes will be overwritten.
'''

from __future__ import unicode_literals
from ..model.internet_message_header import InternetMessageHeader
from ..model.item_body import ItemBody
from ..model.importance import Importance
from ..model.recipient import Recipient
from ..model.mentions_preview import MentionsPreview
from ..model.inference_classification_type import InferenceClassificationType
from ..model.followup_flag import FollowupFlag
from ..model.attachment import Attachment
from ..model.extension import Extension
from ..model.single_value_legacy_extended_property import SingleValueLegacyExtendedProperty
from ..model.multi_value_legacy_extended_property import MultiValueLegacyExtendedProperty
from ..model.mention import Mention
from datetime import datetime
from ..one_drive_object_base import OneDriveObjectBase


class Message(OneDriveObjectBase):

    def __init__(self, prop_dict={}):
        self._prop_dict = prop_dict

    @property
    def received_date_time(self):
        """
        Gets and sets the receivedDateTime
        
        Returns:
            datetime:
                The receivedDateTime
        """
        if "receivedDateTime" in self._prop_dict:
            return datetime.strptime(self._prop_dict["receivedDateTime"].replace("Z", ""), "%Y-%m-%dT%H:%M:%S.%f")
        else:
            return None

    @received_date_time.setter
    def received_date_time(self, val):
        self._prop_dict["receivedDateTime"] = val.isoformat()+"Z"

    @property
    def sent_date_time(self):
        """
        Gets and sets the sentDateTime
        
        Returns:
            datetime:
                The sentDateTime
        """
        if "sentDateTime" in self._prop_dict:
            return datetime.strptime(self._prop_dict["sentDateTime"].replace("Z", ""), "%Y-%m-%dT%H:%M:%S.%f")
        else:
            return None

    @sent_date_time.setter
    def sent_date_time(self, val):
        self._prop_dict["sentDateTime"] = val.isoformat()+"Z"

    @property
    def has_attachments(self):
        """
        Gets and sets the hasAttachments
        
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
    def internet_message_id(self):
        """
        Gets and sets the internetMessageId
        
        Returns:
            str:
                The internetMessageId
        """
        if "internetMessageId" in self._prop_dict:
            return self._prop_dict["internetMessageId"]
        else:
            return None

    @internet_message_id.setter
    def internet_message_id(self, val):
        self._prop_dict["internetMessageId"] = val

    @property
    def internet_message_headers(self):
        """Gets and sets the internetMessageHeaders
        
        Returns: 
            :class:`InternetMessageHeadersCollectionPage<onedrivesdk.request.internet_message_headers_collection.InternetMessageHeadersCollectionPage>`:
                The internetMessageHeaders
        """
        if "internetMessageHeaders" in self._prop_dict:
            return InternetMessageHeadersCollectionPage(self._prop_dict["internetMessageHeaders"])
        else:
            return None

    @property
    def subject(self):
        """
        Gets and sets the subject
        
        Returns:
            str:
                The subject
        """
        if "subject" in self._prop_dict:
            return self._prop_dict["subject"]
        else:
            return None

    @subject.setter
    def subject(self, val):
        self._prop_dict["subject"] = val

    @property
    def body(self):
        """
        Gets and sets the body
        
        Returns: 
            :class:`ItemBody<onedrivesdk.model.item_body.ItemBody>`:
                The body
        """
        if "body" in self._prop_dict:
            if isinstance(self._prop_dict["body"], OneDriveObjectBase):
                return self._prop_dict["body"]
            else :
                self._prop_dict["body"] = ItemBody(self._prop_dict["body"])
                return self._prop_dict["body"]

        return None

    @body.setter
    def body(self, val):
        self._prop_dict["body"] = val

    @property
    def body_preview(self):
        """
        Gets and sets the bodyPreview
        
        Returns:
            str:
                The bodyPreview
        """
        if "bodyPreview" in self._prop_dict:
            return self._prop_dict["bodyPreview"]
        else:
            return None

    @body_preview.setter
    def body_preview(self, val):
        self._prop_dict["bodyPreview"] = val

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
    def parent_folder_id(self):
        """
        Gets and sets the parentFolderId
        
        Returns:
            str:
                The parentFolderId
        """
        if "parentFolderId" in self._prop_dict:
            return self._prop_dict["parentFolderId"]
        else:
            return None

    @parent_folder_id.setter
    def parent_folder_id(self, val):
        self._prop_dict["parentFolderId"] = val

    @property
    def sender(self):
        """
        Gets and sets the sender
        
        Returns: 
            :class:`Recipient<onedrivesdk.model.recipient.Recipient>`:
                The sender
        """
        if "sender" in self._prop_dict:
            if isinstance(self._prop_dict["sender"], OneDriveObjectBase):
                return self._prop_dict["sender"]
            else :
                self._prop_dict["sender"] = Recipient(self._prop_dict["sender"])
                return self._prop_dict["sender"]

        return None

    @sender.setter
    def sender(self, val):
        self._prop_dict["sender"] = val

    @property
    def from(self):
        """
        Gets and sets the from
        
        Returns: 
            :class:`Recipient<onedrivesdk.model.recipient.Recipient>`:
                The from
        """
        if "from" in self._prop_dict:
            if isinstance(self._prop_dict["from"], OneDriveObjectBase):
                return self._prop_dict["from"]
            else :
                self._prop_dict["from"] = Recipient(self._prop_dict["from"])
                return self._prop_dict["from"]

        return None

    @from.setter
    def from(self, val):
        self._prop_dict["from"] = val

    @property
    def to_recipients(self):
        """Gets and sets the toRecipients
        
        Returns: 
            :class:`ToRecipientsCollectionPage<onedrivesdk.request.to_recipients_collection.ToRecipientsCollectionPage>`:
                The toRecipients
        """
        if "toRecipients" in self._prop_dict:
            return ToRecipientsCollectionPage(self._prop_dict["toRecipients"])
        else:
            return None

    @property
    def cc_recipients(self):
        """Gets and sets the ccRecipients
        
        Returns: 
            :class:`CcRecipientsCollectionPage<onedrivesdk.request.cc_recipients_collection.CcRecipientsCollectionPage>`:
                The ccRecipients
        """
        if "ccRecipients" in self._prop_dict:
            return CcRecipientsCollectionPage(self._prop_dict["ccRecipients"])
        else:
            return None

    @property
    def bcc_recipients(self):
        """Gets and sets the bccRecipients
        
        Returns: 
            :class:`BccRecipientsCollectionPage<onedrivesdk.request.bcc_recipients_collection.BccRecipientsCollectionPage>`:
                The bccRecipients
        """
        if "bccRecipients" in self._prop_dict:
            return BccRecipientsCollectionPage(self._prop_dict["bccRecipients"])
        else:
            return None

    @property
    def reply_to(self):
        """Gets and sets the replyTo
        
        Returns: 
            :class:`ReplyToCollectionPage<onedrivesdk.request.reply_to_collection.ReplyToCollectionPage>`:
                The replyTo
        """
        if "replyTo" in self._prop_dict:
            return ReplyToCollectionPage(self._prop_dict["replyTo"])
        else:
            return None

    @property
    def conversation_id(self):
        """
        Gets and sets the conversationId
        
        Returns:
            str:
                The conversationId
        """
        if "conversationId" in self._prop_dict:
            return self._prop_dict["conversationId"]
        else:
            return None

    @conversation_id.setter
    def conversation_id(self, val):
        self._prop_dict["conversationId"] = val

    @property
    def unique_body(self):
        """
        Gets and sets the uniqueBody
        
        Returns: 
            :class:`ItemBody<onedrivesdk.model.item_body.ItemBody>`:
                The uniqueBody
        """
        if "uniqueBody" in self._prop_dict:
            if isinstance(self._prop_dict["uniqueBody"], OneDriveObjectBase):
                return self._prop_dict["uniqueBody"]
            else :
                self._prop_dict["uniqueBody"] = ItemBody(self._prop_dict["uniqueBody"])
                return self._prop_dict["uniqueBody"]

        return None

    @unique_body.setter
    def unique_body(self, val):
        self._prop_dict["uniqueBody"] = val

    @property
    def is_delivery_receipt_requested(self):
        """
        Gets and sets the isDeliveryReceiptRequested
        
        Returns:
            bool:
                The isDeliveryReceiptRequested
        """
        if "isDeliveryReceiptRequested" in self._prop_dict:
            return self._prop_dict["isDeliveryReceiptRequested"]
        else:
            return None

    @is_delivery_receipt_requested.setter
    def is_delivery_receipt_requested(self, val):
        self._prop_dict["isDeliveryReceiptRequested"] = val

    @property
    def is_read_receipt_requested(self):
        """
        Gets and sets the isReadReceiptRequested
        
        Returns:
            bool:
                The isReadReceiptRequested
        """
        if "isReadReceiptRequested" in self._prop_dict:
            return self._prop_dict["isReadReceiptRequested"]
        else:
            return None

    @is_read_receipt_requested.setter
    def is_read_receipt_requested(self, val):
        self._prop_dict["isReadReceiptRequested"] = val

    @property
    def is_read(self):
        """
        Gets and sets the isRead
        
        Returns:
            bool:
                The isRead
        """
        if "isRead" in self._prop_dict:
            return self._prop_dict["isRead"]
        else:
            return None

    @is_read.setter
    def is_read(self, val):
        self._prop_dict["isRead"] = val

    @property
    def is_draft(self):
        """
        Gets and sets the isDraft
        
        Returns:
            bool:
                The isDraft
        """
        if "isDraft" in self._prop_dict:
            return self._prop_dict["isDraft"]
        else:
            return None

    @is_draft.setter
    def is_draft(self, val):
        self._prop_dict["isDraft"] = val

    @property
    def web_link(self):
        """
        Gets and sets the webLink
        
        Returns:
            str:
                The webLink
        """
        if "webLink" in self._prop_dict:
            return self._prop_dict["webLink"]
        else:
            return None

    @web_link.setter
    def web_link(self, val):
        self._prop_dict["webLink"] = val

    @property
    def mentions_preview(self):
        """
        Gets and sets the mentionsPreview
        
        Returns: 
            :class:`MentionsPreview<onedrivesdk.model.mentions_preview.MentionsPreview>`:
                The mentionsPreview
        """
        if "mentionsPreview" in self._prop_dict:
            if isinstance(self._prop_dict["mentionsPreview"], OneDriveObjectBase):
                return self._prop_dict["mentionsPreview"]
            else :
                self._prop_dict["mentionsPreview"] = MentionsPreview(self._prop_dict["mentionsPreview"])
                return self._prop_dict["mentionsPreview"]

        return None

    @mentions_preview.setter
    def mentions_preview(self, val):
        self._prop_dict["mentionsPreview"] = val

    @property
    def inference_classification(self):
        """
        Gets and sets the inferenceClassification
        
        Returns: 
            :class:`InferenceClassificationType<onedrivesdk.model.inference_classification_type.InferenceClassificationType>`:
                The inferenceClassification
        """
        if "inferenceClassification" in self._prop_dict:
            if isinstance(self._prop_dict["inferenceClassification"], OneDriveObjectBase):
                return self._prop_dict["inferenceClassification"]
            else :
                self._prop_dict["inferenceClassification"] = InferenceClassificationType(self._prop_dict["inferenceClassification"])
                return self._prop_dict["inferenceClassification"]

        return None

    @inference_classification.setter
    def inference_classification(self, val):
        self._prop_dict["inferenceClassification"] = val

    @property
    def unsubscribe_data(self):
        """
        Gets and sets the unsubscribeData
        
        Returns:
            str:
                The unsubscribeData
        """
        if "unsubscribeData" in self._prop_dict:
            return self._prop_dict["unsubscribeData"]
        else:
            return None

    @unsubscribe_data.setter
    def unsubscribe_data(self, val):
        self._prop_dict["unsubscribeData"] = val

    @property
    def unsubscribe_enabled(self):
        """
        Gets and sets the unsubscribeEnabled
        
        Returns:
            bool:
                The unsubscribeEnabled
        """
        if "unsubscribeEnabled" in self._prop_dict:
            return self._prop_dict["unsubscribeEnabled"]
        else:
            return None

    @unsubscribe_enabled.setter
    def unsubscribe_enabled(self, val):
        self._prop_dict["unsubscribeEnabled"] = val

    @property
    def flag(self):
        """
        Gets and sets the flag
        
        Returns: 
            :class:`FollowupFlag<onedrivesdk.model.followup_flag.FollowupFlag>`:
                The flag
        """
        if "flag" in self._prop_dict:
            if isinstance(self._prop_dict["flag"], OneDriveObjectBase):
                return self._prop_dict["flag"]
            else :
                self._prop_dict["flag"] = FollowupFlag(self._prop_dict["flag"])
                return self._prop_dict["flag"]

        return None

    @flag.setter
    def flag(self, val):
        self._prop_dict["flag"] = val

    @property
    def attachments(self):
        """Gets and sets the attachments
        
        Returns: 
            :class:`AttachmentsCollectionPage<onedrivesdk.request.attachments_collection.AttachmentsCollectionPage>`:
                The attachments
        """
        if "attachments" in self._prop_dict:
            return AttachmentsCollectionPage(self._prop_dict["attachments"])
        else:
            return None

    @property
    def extensions(self):
        """Gets and sets the extensions
        
        Returns: 
            :class:`ExtensionsCollectionPage<onedrivesdk.request.extensions_collection.ExtensionsCollectionPage>`:
                The extensions
        """
        if "extensions" in self._prop_dict:
            return ExtensionsCollectionPage(self._prop_dict["extensions"])
        else:
            return None

    @property
    def single_value_extended_properties(self):
        """Gets and sets the singleValueExtendedProperties
        
        Returns: 
            :class:`SingleValueExtendedPropertiesCollectionPage<onedrivesdk.request.single_value_extended_properties_collection.SingleValueExtendedPropertiesCollectionPage>`:
                The singleValueExtendedProperties
        """
        if "singleValueExtendedProperties" in self._prop_dict:
            return SingleValueExtendedPropertiesCollectionPage(self._prop_dict["singleValueExtendedProperties"])
        else:
            return None

    @property
    def multi_value_extended_properties(self):
        """Gets and sets the multiValueExtendedProperties
        
        Returns: 
            :class:`MultiValueExtendedPropertiesCollectionPage<onedrivesdk.request.multi_value_extended_properties_collection.MultiValueExtendedPropertiesCollectionPage>`:
                The multiValueExtendedProperties
        """
        if "multiValueExtendedProperties" in self._prop_dict:
            return MultiValueExtendedPropertiesCollectionPage(self._prop_dict["multiValueExtendedProperties"])
        else:
            return None

    @property
    def mentions(self):
        """Gets and sets the mentions
        
        Returns: 
            :class:`MentionsCollectionPage<onedrivesdk.request.mentions_collection.MentionsCollectionPage>`:
                The mentions
        """
        if "mentions" in self._prop_dict:
            return MentionsCollectionPage(self._prop_dict["mentions"])
        else:
            return None

