# -*- coding: utf-8 -*- 
'''
# Copyright (c) Microsoft Corporation.  All Rights Reserved.  Licensed under the MIT License.  See License in the project root for license information.
# 
#  This file was generated and any changes will be overwritten.
'''

from __future__ import unicode_literals
from ..model.duration import Duration
from ..model.booking_reminder_recipients import BookingReminderRecipients
from ..one_drive_object_base import OneDriveObjectBase


class BookingReminder(OneDriveObjectBase):

    def __init__(self, prop_dict={}):
        self._prop_dict = prop_dict

    @property
    def offset(self):
        """
        Gets and sets the offset
        
        Returns: 
            :class:`Duration<onedrivesdk.model.duration.Duration>`:
                The offset
        """
        if "offset" in self._prop_dict:
            if isinstance(self._prop_dict["offset"], OneDriveObjectBase):
                return self._prop_dict["offset"]
            else :
                self._prop_dict["offset"] = Duration(self._prop_dict["offset"])
                return self._prop_dict["offset"]

        return None

    @offset.setter
    def offset(self, val):
        self._prop_dict["offset"] = val
    @property
    def recipients(self):
        """
        Gets and sets the recipients
        
        Returns: 
            :class:`BookingReminderRecipients<onedrivesdk.model.booking_reminder_recipients.BookingReminderRecipients>`:
                The recipients
        """
        if "recipients" in self._prop_dict:
            if isinstance(self._prop_dict["recipients"], OneDriveObjectBase):
                return self._prop_dict["recipients"]
            else :
                self._prop_dict["recipients"] = BookingReminderRecipients(self._prop_dict["recipients"])
                return self._prop_dict["recipients"]

        return None

    @recipients.setter
    def recipients(self, val):
        self._prop_dict["recipients"] = val
    @property
    def message(self):
        """Gets and sets the message
        
        Returns: 
            str:
                The message
        """
        if "message" in self._prop_dict:
            return self._prop_dict["message"]
        else:
            return None

    @message.setter
    def message(self, val):
        self._prop_dict["message"] = val

