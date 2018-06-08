# -*- coding: utf-8 -*- 
'''
# Copyright (c) Microsoft Corporation.  All Rights Reserved.  Licensed under the MIT License.  See License in the project root for license information.
# 
#  This file was generated and any changes will be overwritten.
'''

from __future__ import unicode_literals
from ..model.locale_info import LocaleInfo
from ..model.date_time_time_zone import DateTimeTimeZone
from ..one_drive_object_base import OneDriveObjectBase


class AutomaticRepliesMailTips(OneDriveObjectBase):

    def __init__(self, prop_dict={}):
        self._prop_dict = prop_dict

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

    @property
    def message_language(self):
        """
        Gets and sets the messageLanguage
        
        Returns: 
            :class:`LocaleInfo<onedrivesdk.model.locale_info.LocaleInfo>`:
                The messageLanguage
        """
        if "messageLanguage" in self._prop_dict:
            if isinstance(self._prop_dict["messageLanguage"], OneDriveObjectBase):
                return self._prop_dict["messageLanguage"]
            else :
                self._prop_dict["messageLanguage"] = LocaleInfo(self._prop_dict["messageLanguage"])
                return self._prop_dict["messageLanguage"]

        return None

    @message_language.setter
    def message_language(self, val):
        self._prop_dict["messageLanguage"] = val
    @property
    def scheduled_start_time(self):
        """
        Gets and sets the scheduledStartTime
        
        Returns: 
            :class:`DateTimeTimeZone<onedrivesdk.model.date_time_time_zone.DateTimeTimeZone>`:
                The scheduledStartTime
        """
        if "scheduledStartTime" in self._prop_dict:
            if isinstance(self._prop_dict["scheduledStartTime"], OneDriveObjectBase):
                return self._prop_dict["scheduledStartTime"]
            else :
                self._prop_dict["scheduledStartTime"] = DateTimeTimeZone(self._prop_dict["scheduledStartTime"])
                return self._prop_dict["scheduledStartTime"]

        return None

    @scheduled_start_time.setter
    def scheduled_start_time(self, val):
        self._prop_dict["scheduledStartTime"] = val
    @property
    def scheduled_end_time(self):
        """
        Gets and sets the scheduledEndTime
        
        Returns: 
            :class:`DateTimeTimeZone<onedrivesdk.model.date_time_time_zone.DateTimeTimeZone>`:
                The scheduledEndTime
        """
        if "scheduledEndTime" in self._prop_dict:
            if isinstance(self._prop_dict["scheduledEndTime"], OneDriveObjectBase):
                return self._prop_dict["scheduledEndTime"]
            else :
                self._prop_dict["scheduledEndTime"] = DateTimeTimeZone(self._prop_dict["scheduledEndTime"])
                return self._prop_dict["scheduledEndTime"]

        return None

    @scheduled_end_time.setter
    def scheduled_end_time(self, val):
        self._prop_dict["scheduledEndTime"] = val
