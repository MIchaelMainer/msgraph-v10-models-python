# -*- coding: utf-8 -*- 
'''
# Copyright (c) Microsoft Corporation.  All Rights Reserved.  Licensed under the MIT License.  See License in the project root for license information.
# 
#  This file was generated and any changes will be overwritten.
'''

from __future__ import unicode_literals
from ..model.meeting_message_type import MeetingMessageType
from ..model.date_time_time_zone import DateTimeTimeZone
from ..model.location import Location
from ..model.event_type import EventType
from ..model.patterned_recurrence import PatternedRecurrence
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
    def start_date_time(self):
        """
        Gets and sets the startDateTime
        
        Returns: 
            :class:`DateTimeTimeZone<onedrivesdk.model.date_time_time_zone.DateTimeTimeZone>`:
                The startDateTime
        """
        if "startDateTime" in self._prop_dict:
            if isinstance(self._prop_dict["startDateTime"], OneDriveObjectBase):
                return self._prop_dict["startDateTime"]
            else :
                self._prop_dict["startDateTime"] = DateTimeTimeZone(self._prop_dict["startDateTime"])
                return self._prop_dict["startDateTime"]

        return None

    @start_date_time.setter
    def start_date_time(self, val):
        self._prop_dict["startDateTime"] = val

    @property
    def end_date_time(self):
        """
        Gets and sets the endDateTime
        
        Returns: 
            :class:`DateTimeTimeZone<onedrivesdk.model.date_time_time_zone.DateTimeTimeZone>`:
                The endDateTime
        """
        if "endDateTime" in self._prop_dict:
            if isinstance(self._prop_dict["endDateTime"], OneDriveObjectBase):
                return self._prop_dict["endDateTime"]
            else :
                self._prop_dict["endDateTime"] = DateTimeTimeZone(self._prop_dict["endDateTime"])
                return self._prop_dict["endDateTime"]

        return None

    @end_date_time.setter
    def end_date_time(self, val):
        self._prop_dict["endDateTime"] = val

    @property
    def location(self):
        """
        Gets and sets the location
        
        Returns: 
            :class:`Location<onedrivesdk.model.location.Location>`:
                The location
        """
        if "location" in self._prop_dict:
            if isinstance(self._prop_dict["location"], OneDriveObjectBase):
                return self._prop_dict["location"]
            else :
                self._prop_dict["location"] = Location(self._prop_dict["location"])
                return self._prop_dict["location"]

        return None

    @location.setter
    def location(self, val):
        self._prop_dict["location"] = val

    @property
    def type(self):
        """
        Gets and sets the type
        
        Returns: 
            :class:`EventType<onedrivesdk.model.event_type.EventType>`:
                The type
        """
        if "type" in self._prop_dict:
            if isinstance(self._prop_dict["type"], OneDriveObjectBase):
                return self._prop_dict["type"]
            else :
                self._prop_dict["type"] = EventType(self._prop_dict["type"])
                return self._prop_dict["type"]

        return None

    @type.setter
    def type(self, val):
        self._prop_dict["type"] = val

    @property
    def recurrence(self):
        """
        Gets and sets the recurrence
        
        Returns: 
            :class:`PatternedRecurrence<onedrivesdk.model.patterned_recurrence.PatternedRecurrence>`:
                The recurrence
        """
        if "recurrence" in self._prop_dict:
            if isinstance(self._prop_dict["recurrence"], OneDriveObjectBase):
                return self._prop_dict["recurrence"]
            else :
                self._prop_dict["recurrence"] = PatternedRecurrence(self._prop_dict["recurrence"])
                return self._prop_dict["recurrence"]

        return None

    @recurrence.setter
    def recurrence(self, val):
        self._prop_dict["recurrence"] = val

    @property
    def is_out_of_date(self):
        """
        Gets and sets the isOutOfDate
        
        Returns:
            bool:
                The isOutOfDate
        """
        if "isOutOfDate" in self._prop_dict:
            return self._prop_dict["isOutOfDate"]
        else:
            return None

    @is_out_of_date.setter
    def is_out_of_date(self, val):
        self._prop_dict["isOutOfDate"] = val

    @property
    def is_all_day(self):
        """
        Gets and sets the isAllDay
        
        Returns:
            bool:
                The isAllDay
        """
        if "isAllDay" in self._prop_dict:
            return self._prop_dict["isAllDay"]
        else:
            return None

    @is_all_day.setter
    def is_all_day(self, val):
        self._prop_dict["isAllDay"] = val

    @property
    def is_delegated(self):
        """
        Gets and sets the isDelegated
        
        Returns:
            bool:
                The isDelegated
        """
        if "isDelegated" in self._prop_dict:
            return self._prop_dict["isDelegated"]
        else:
            return None

    @is_delegated.setter
    def is_delegated(self, val):
        self._prop_dict["isDelegated"] = val

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

