# -*- coding: utf-8 -*- 
'''
# Copyright (c) Microsoft Corporation.  All Rights Reserved.  Licensed under the MIT License.  See License in the project root for license information.
# 
#  This file was generated and any changes will be overwritten.
'''

from __future__ import unicode_literals
from ..model.chat_message import ChatMessage
from ..one_drive_object_base import OneDriveObjectBase


class ChatThread(OneDriveObjectBase):

    def __init__(self, prop_dict={}):
        self._prop_dict = prop_dict

    @property
    def chat_messages(self):
        """Gets and sets the chatMessages
        
        Returns: 
            :class:`ChatMessagesCollectionPage<onedrivesdk.request.chat_messages_collection.ChatMessagesCollectionPage>`:
                The chatMessages
        """
        if "chatMessages" in self._prop_dict:
            return ChatMessagesCollectionPage(self._prop_dict["chatMessages"])
        else:
            return None

    @property
    def root_message(self):
        """
        Gets and sets the rootMessage
        
        Returns: 
            :class:`ChatMessage<onedrivesdk.model.chat_message.ChatMessage>`:
                The rootMessage
        """
        if "rootMessage" in self._prop_dict:
            if isinstance(self._prop_dict["rootMessage"], OneDriveObjectBase):
                return self._prop_dict["rootMessage"]
            else :
                self._prop_dict["rootMessage"] = ChatMessage(self._prop_dict["rootMessage"])
                return self._prop_dict["rootMessage"]

        return None

    @root_message.setter
    def root_message(self, val):
        self._prop_dict["rootMessage"] = val

