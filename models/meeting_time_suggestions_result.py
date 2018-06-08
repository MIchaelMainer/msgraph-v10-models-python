# -*- coding: utf-8 -*- 
'''
# Copyright (c) Microsoft Corporation.  All Rights Reserved.  Licensed under the MIT License.  See License in the project root for license information.
# 
#  This file was generated and any changes will be overwritten.
'''

from __future__ import unicode_literals
from ..model.meeting_time_suggestion import MeetingTimeSuggestion
from ..one_drive_object_base import OneDriveObjectBase


class MeetingTimeSuggestionsResult(OneDriveObjectBase):

    def __init__(self, prop_dict={}):
        self._prop_dict = prop_dict

    @property
    def meeting_time_suggestions(self):
        """
        Gets and sets the meetingTimeSuggestions
        
        Returns: 
            :class:`MeetingTimeSuggestion<onedrivesdk.model.meeting_time_suggestion.MeetingTimeSuggestion>`:
                The meetingTimeSuggestions
        """
        if "meetingTimeSuggestions" in self._prop_dict:
            if isinstance(self._prop_dict["meetingTimeSuggestions"], OneDriveObjectBase):
                return self._prop_dict["meetingTimeSuggestions"]
            else :
                self._prop_dict["meetingTimeSuggestions"] = MeetingTimeSuggestion(self._prop_dict["meetingTimeSuggestions"])
                return self._prop_dict["meetingTimeSuggestions"]

        return None

    @meeting_time_suggestions.setter
    def meeting_time_suggestions(self, val):
        self._prop_dict["meetingTimeSuggestions"] = val
    @property
    def empty_suggestions_reason(self):
        """Gets and sets the emptySuggestionsReason
        
        Returns: 
            str:
                The emptySuggestionsReason
        """
        if "emptySuggestionsReason" in self._prop_dict:
            return self._prop_dict["emptySuggestionsReason"]
        else:
            return None

    @empty_suggestions_reason.setter
    def empty_suggestions_reason(self, val):
        self._prop_dict["emptySuggestionsReason"] = val

