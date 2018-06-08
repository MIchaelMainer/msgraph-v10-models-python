# -*- coding: utf-8 -*- 
'''
# Copyright (c) Microsoft Corporation.  All Rights Reserved.  Licensed under the MIT License.  See License in the project root for license information.
# 
#  This file was generated and any changes will be overwritten.
'''

from __future__ import unicode_literals
from ..model.conversation_thread import ConversationThread
from datetime import datetime
from ..one_drive_object_base import OneDriveObjectBase


class Conversation(OneDriveObjectBase):

    def __init__(self, prop_dict={}):
        self._prop_dict = prop_dict

    @property
    def topic(self):
        """
        Gets and sets the topic
        
        Returns:
            str:
                The topic
        """
        if "topic" in self._prop_dict:
            return self._prop_dict["topic"]
        else:
            return None

    @topic.setter
    def topic(self, val):
        self._prop_dict["topic"] = val

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
    def last_delivered_date_time(self):
        """
        Gets and sets the lastDeliveredDateTime
        
        Returns:
            datetime:
                The lastDeliveredDateTime
        """
        if "lastDeliveredDateTime" in self._prop_dict:
            return datetime.strptime(self._prop_dict["lastDeliveredDateTime"].replace("Z", ""), "%Y-%m-%dT%H:%M:%S.%f")
        else:
            return None

    @last_delivered_date_time.setter
    def last_delivered_date_time(self, val):
        self._prop_dict["lastDeliveredDateTime"] = val.isoformat()+"Z"

    @property
    def unique_senders(self):
        """
        Gets and sets the uniqueSenders
        
        Returns:
            str:
                The uniqueSenders
        """
        if "uniqueSenders" in self._prop_dict:
            return self._prop_dict["uniqueSenders"]
        else:
            return None

    @unique_senders.setter
    def unique_senders(self, val):
        self._prop_dict["uniqueSenders"] = val

    @property
    def preview(self):
        """
        Gets and sets the preview
        
        Returns:
            str:
                The preview
        """
        if "preview" in self._prop_dict:
            return self._prop_dict["preview"]
        else:
            return None

    @preview.setter
    def preview(self, val):
        self._prop_dict["preview"] = val

    @property
    def threads(self):
        """Gets and sets the threads
        
        Returns: 
            :class:`ThreadsCollectionPage<onedrivesdk.request.threads_collection.ThreadsCollectionPage>`:
                The threads
        """
        if "threads" in self._prop_dict:
            return ThreadsCollectionPage(self._prop_dict["threads"])
        else:
            return None

