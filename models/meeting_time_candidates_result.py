# -*- coding: utf-8 -*- 
'''
# Copyright (c) Microsoft Corporation.  All Rights Reserved.  Licensed under the MIT License.  See License in the project root for license information.
# 
#  This file was generated and any changes will be overwritten.
'''

from __future__ import unicode_literals
from ..model.meeting_time_candidate import MeetingTimeCandidate
from ..one_drive_object_base import OneDriveObjectBase


class MeetingTimeCandidatesResult(OneDriveObjectBase):

    def __init__(self, prop_dict={}):
        self._prop_dict = prop_dict

    @property
    def meeting_time_slots(self):
        """
        Gets and sets the meetingTimeSlots
        
        Returns: 
            :class:`MeetingTimeCandidate<onedrivesdk.model.meeting_time_candidate.MeetingTimeCandidate>`:
                The meetingTimeSlots
        """
        if "meetingTimeSlots" in self._prop_dict:
            if isinstance(self._prop_dict["meetingTimeSlots"], OneDriveObjectBase):
                return self._prop_dict["meetingTimeSlots"]
            else :
                self._prop_dict["meetingTimeSlots"] = MeetingTimeCandidate(self._prop_dict["meetingTimeSlots"])
                return self._prop_dict["meetingTimeSlots"]

        return None

    @meeting_time_slots.setter
    def meeting_time_slots(self, val):
        self._prop_dict["meetingTimeSlots"] = val
    @property
    def empty_suggestions_hint(self):
        """Gets and sets the emptySuggestionsHint
        
        Returns: 
            str:
                The emptySuggestionsHint
        """
        if "emptySuggestionsHint" in self._prop_dict:
            return self._prop_dict["emptySuggestionsHint"]
        else:
            return None

    @empty_suggestions_hint.setter
    def empty_suggestions_hint(self, val):
        self._prop_dict["emptySuggestionsHint"] = val

