# -*- coding: utf-8 -*- 
'''
# Copyright (c) Microsoft Corporation.  All Rights Reserved.  Licensed under the MIT License.  See License in the project root for license information.
# 
#  This file was generated and any changes will be overwritten.
'''

from __future__ import unicode_literals
from ..model.attendee_base import AttendeeBase
from ..model.free_busy_status import FreeBusyStatus
from ..one_drive_object_base import OneDriveObjectBase


class AttendeeAvailability(OneDriveObjectBase):

    def __init__(self, prop_dict={}):
        self._prop_dict = prop_dict

    @property
    def attendee(self):
        """
        Gets and sets the attendee
        
        Returns: 
            :class:`AttendeeBase<onedrivesdk.model.attendee_base.AttendeeBase>`:
                The attendee
        """
        if "attendee" in self._prop_dict:
            if isinstance(self._prop_dict["attendee"], OneDriveObjectBase):
                return self._prop_dict["attendee"]
            else :
                self._prop_dict["attendee"] = AttendeeBase(self._prop_dict["attendee"])
                return self._prop_dict["attendee"]

        return None

    @attendee.setter
    def attendee(self, val):
        self._prop_dict["attendee"] = val
    @property
    def availability(self):
        """
        Gets and sets the availability
        
        Returns: 
            :class:`FreeBusyStatus<onedrivesdk.model.free_busy_status.FreeBusyStatus>`:
                The availability
        """
        if "availability" in self._prop_dict:
            if isinstance(self._prop_dict["availability"], OneDriveObjectBase):
                return self._prop_dict["availability"]
            else :
                self._prop_dict["availability"] = FreeBusyStatus(self._prop_dict["availability"])
                return self._prop_dict["availability"]

        return None

    @availability.setter
    def availability(self, val):
        self._prop_dict["availability"] = val
