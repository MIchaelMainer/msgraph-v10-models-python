# -*- coding: utf-8 -*- 
'''
# Copyright (c) Microsoft Corporation.  All Rights Reserved.  Licensed under the MIT License.  See License in the project root for license information.
# 
#  This file was generated and any changes will be overwritten.
'''

from __future__ import unicode_literals
from ..model.meeting_message_type import MeetingMessageType
from ..model.event import Event
from ..one_drive_object_base import OneDriveObjectBase


class EventMessage(OneDriveObjectBase):

    def __init__(self, prop_dict={}):
        self._prop_dict = prop_dict

    @property
    def meeting_message_type(self):
        """
        Gets and sets the meetingMessageType
        
        Returns: 
            :class:`MeetingMessageType<onedrivesdk.model.meeting_message_type.MeetingMessageType>`:
                The meetingMessageType
        """
        if "meetingMessageType" in self._prop_dict:
            if isinstance(self._prop_dict["meetingMessageType"], OneDriveObjectBase):
                return self._prop_dict["meetingMessageType"]
            else :
                self._prop_dict["meetingMessageType"] = MeetingMessageType(self._prop_dict["meetingMessageType"])
                return self._prop_dict["meetingMessageType"]

        return None

    @meeting_message_type.setter
    def meeting_message_type(self, val):
        self._prop_dict["meetingMessageType"] = val

    @property
    def event(self):
        """
        Gets and sets the event
        
        Returns: 
            :class:`Event<onedrivesdk.model.event.Event>`:
                The event
        """
        if "event" in self._prop_dict:
            if isinstance(self._prop_dict["event"], OneDriveObjectBase):
                return self._prop_dict["event"]
            else :
                self._prop_dict["event"] = Event(self._prop_dict["event"])
                return self._prop_dict["event"]

        return None

    @event.setter
    def event(self, val):
        self._prop_dict["event"] = val

