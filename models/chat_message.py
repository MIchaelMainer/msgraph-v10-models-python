# -*- coding: utf-8 -*- 
'''
# Copyright (c) Microsoft Corporation.  All Rights Reserved.  Licensed under the MIT License.  See License in the project root for license information.
# 
#  This file was generated and any changes will be overwritten.
'''

from __future__ import unicode_literals
from ..model.item_body import ItemBody
from ..model.user import User
from ..one_drive_object_base import OneDriveObjectBase


class ChatMessage(OneDriveObjectBase):

    def __init__(self, prop_dict={}):
        self._prop_dict = prop_dict

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
    def in_reply_to(self):
        """
        Gets and sets the inReplyTo
        
        Returns: 
            :class:`ChatMessage<onedrivesdk.model.chat_message.ChatMessage>`:
                The inReplyTo
        """
        if "inReplyTo" in self._prop_dict:
            if isinstance(self._prop_dict["inReplyTo"], OneDriveObjectBase):
                return self._prop_dict["inReplyTo"]
            else :
                self._prop_dict["inReplyTo"] = ChatMessage(self._prop_dict["inReplyTo"])
                return self._prop_dict["inReplyTo"]

        return None

    @in_reply_to.setter
    def in_reply_to(self, val):
        self._prop_dict["inReplyTo"] = val

    @property
    def replies(self):
        """Gets and sets the replies
        
        Returns: 
            :class:`RepliesCollectionPage<onedrivesdk.request.replies_collection.RepliesCollectionPage>`:
                The replies
        """
        if "replies" in self._prop_dict:
            return RepliesCollectionPage(self._prop_dict["replies"])
        else:
            return None

    @property
    def from(self):
        """
        Gets and sets the from
        
        Returns: 
            :class:`User<onedrivesdk.model.user.User>`:
                The from
        """
        if "from" in self._prop_dict:
            if isinstance(self._prop_dict["from"], OneDriveObjectBase):
                return self._prop_dict["from"]
            else :
                self._prop_dict["from"] = User(self._prop_dict["from"])
                return self._prop_dict["from"]

        return None

    @from.setter
    def from(self, val):
        self._prop_dict["from"] = val

