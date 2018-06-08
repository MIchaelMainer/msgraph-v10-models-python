# -*- coding: utf-8 -*- 
'''
# Copyright (c) Microsoft Corporation.  All Rights Reserved.  Licensed under the MIT License.  See License in the project root for license information.
# 
#  This file was generated and any changes will be overwritten.
'''

from __future__ import unicode_literals
from ..model.time_slot_old import TimeSlotOLD
from ..model.free_busy_status import FreeBusyStatus
from ..model.attendee_availability import AttendeeAvailability
from ..model.location import Location
from ..one_drive_object_base import OneDriveObjectBase


class MeetingTimeCandidate(OneDriveObjectBase):

    def __init__(self, prop_dict={}):
        self._prop_dict = prop_dict

    @property
    def meeting_time_slot(self):
        """
        Gets and sets the meetingTimeSlot
        
        Returns: 
            :class:`TimeSlotOLD<onedrivesdk.model.time_slot_old.TimeSlotOLD>`:
                The meetingTimeSlot
        """
        if "meetingTimeSlot" in self._prop_dict:
            if isinstance(self._prop_dict["meetingTimeSlot"], OneDriveObjectBase):
                return self._prop_dict["meetingTimeSlot"]
            else :
                self._prop_dict["meetingTimeSlot"] = TimeSlotOLD(self._prop_dict["meetingTimeSlot"])
                return self._prop_dict["meetingTimeSlot"]

        return None

    @meeting_time_slot.setter
    def meeting_time_slot(self, val):
        self._prop_dict["meetingTimeSlot"] = val
    @property
    def confidence(self):
        """Gets and sets the confidence
        
        Returns: 
            float:
                The confidence
        """
        if "confidence" in self._prop_dict:
            return self._prop_dict["confidence"]
        else:
            return None

    @confidence.setter
    def confidence(self, val):
        self._prop_dict["confidence"] = val

    @property
    def organizer_availability(self):
        """
        Gets and sets the organizerAvailability
        
        Returns: 
            :class:`FreeBusyStatus<onedrivesdk.model.free_busy_status.FreeBusyStatus>`:
                The organizerAvailability
        """
        if "organizerAvailability" in self._prop_dict:
            if isinstance(self._prop_dict["organizerAvailability"], OneDriveObjectBase):
                return self._prop_dict["organizerAvailability"]
            else :
                self._prop_dict["organizerAvailability"] = FreeBusyStatus(self._prop_dict["organizerAvailability"])
                return self._prop_dict["organizerAvailability"]

        return None

    @organizer_availability.setter
    def organizer_availability(self, val):
        self._prop_dict["organizerAvailability"] = val
    @property
    def attendee_availability(self):
        """
        Gets and sets the attendeeAvailability
        
        Returns: 
            :class:`AttendeeAvailability<onedrivesdk.model.attendee_availability.AttendeeAvailability>`:
                The attendeeAvailability
        """
        if "attendeeAvailability" in self._prop_dict:
            if isinstance(self._prop_dict["attendeeAvailability"], OneDriveObjectBase):
                return self._prop_dict["attendeeAvailability"]
            else :
                self._prop_dict["attendeeAvailability"] = AttendeeAvailability(self._prop_dict["attendeeAvailability"])
                return self._prop_dict["attendeeAvailability"]

        return None

    @attendee_availability.setter
    def attendee_availability(self, val):
        self._prop_dict["attendeeAvailability"] = val
    @property
    def locations(self):
        """
        Gets and sets the locations
        
        Returns: 
            :class:`Location<onedrivesdk.model.location.Location>`:
                The locations
        """
        if "locations" in self._prop_dict:
            if isinstance(self._prop_dict["locations"], OneDriveObjectBase):
                return self._prop_dict["locations"]
            else :
                self._prop_dict["locations"] = Location(self._prop_dict["locations"])
                return self._prop_dict["locations"]

        return None

    @locations.setter
    def locations(self, val):
        self._prop_dict["locations"] = val
    @property
    def suggestion_hint(self):
        """Gets and sets the suggestionHint
        
        Returns: 
            str:
                The suggestionHint
        """
        if "suggestionHint" in self._prop_dict:
            return self._prop_dict["suggestionHint"]
        else:
            return None

    @suggestion_hint.setter
    def suggestion_hint(self, val):
        self._prop_dict["suggestionHint"] = val

