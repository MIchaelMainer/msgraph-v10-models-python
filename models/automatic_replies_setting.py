# -*- coding: utf-8 -*- 
'''
# Copyright (c) Microsoft Corporation.  All Rights Reserved.  Licensed under the MIT License.  See License in the project root for license information.
# 
#  This file was generated and any changes will be overwritten.
'''

from __future__ import unicode_literals
from ..model.automatic_replies_status import AutomaticRepliesStatus
from ..model.external_audience_scope import ExternalAudienceScope
from ..model.date_time_time_zone import DateTimeTimeZone
from ..one_drive_object_base import OneDriveObjectBase


class AutomaticRepliesSetting(OneDriveObjectBase):

    def __init__(self, prop_dict={}):
        self._prop_dict = prop_dict

    @property
    def status(self):
        """
        Gets and sets the status
        
        Returns: 
            :class:`AutomaticRepliesStatus<onedrivesdk.model.automatic_replies_status.AutomaticRepliesStatus>`:
                The status
        """
        if "status" in self._prop_dict:
            if isinstance(self._prop_dict["status"], OneDriveObjectBase):
                return self._prop_dict["status"]
            else :
                self._prop_dict["status"] = AutomaticRepliesStatus(self._prop_dict["status"])
                return self._prop_dict["status"]

        return None

    @status.setter
    def status(self, val):
        self._prop_dict["status"] = val
    @property
    def external_audience(self):
        """
        Gets and sets the externalAudience
        
        Returns: 
            :class:`ExternalAudienceScope<onedrivesdk.model.external_audience_scope.ExternalAudienceScope>`:
                The externalAudience
        """
        if "externalAudience" in self._prop_dict:
            if isinstance(self._prop_dict["externalAudience"], OneDriveObjectBase):
                return self._prop_dict["externalAudience"]
            else :
                self._prop_dict["externalAudience"] = ExternalAudienceScope(self._prop_dict["externalAudience"])
                return self._prop_dict["externalAudience"]

        return None

    @external_audience.setter
    def external_audience(self, val):
        self._prop_dict["externalAudience"] = val
    @property
    def scheduled_start_date_time(self):
        """
        Gets and sets the scheduledStartDateTime
        
        Returns: 
            :class:`DateTimeTimeZone<onedrivesdk.model.date_time_time_zone.DateTimeTimeZone>`:
                The scheduledStartDateTime
        """
        if "scheduledStartDateTime" in self._prop_dict:
            if isinstance(self._prop_dict["scheduledStartDateTime"], OneDriveObjectBase):
                return self._prop_dict["scheduledStartDateTime"]
            else :
                self._prop_dict["scheduledStartDateTime"] = DateTimeTimeZone(self._prop_dict["scheduledStartDateTime"])
                return self._prop_dict["scheduledStartDateTime"]

        return None

    @scheduled_start_date_time.setter
    def scheduled_start_date_time(self, val):
        self._prop_dict["scheduledStartDateTime"] = val
    @property
    def scheduled_end_date_time(self):
        """
        Gets and sets the scheduledEndDateTime
        
        Returns: 
            :class:`DateTimeTimeZone<onedrivesdk.model.date_time_time_zone.DateTimeTimeZone>`:
                The scheduledEndDateTime
        """
        if "scheduledEndDateTime" in self._prop_dict:
            if isinstance(self._prop_dict["scheduledEndDateTime"], OneDriveObjectBase):
                return self._prop_dict["scheduledEndDateTime"]
            else :
                self._prop_dict["scheduledEndDateTime"] = DateTimeTimeZone(self._prop_dict["scheduledEndDateTime"])
                return self._prop_dict["scheduledEndDateTime"]

        return None

    @scheduled_end_date_time.setter
    def scheduled_end_date_time(self, val):
        self._prop_dict["scheduledEndDateTime"] = val
    @property
    def internal_reply_message(self):
        """Gets and sets the internalReplyMessage
        
        Returns: 
            str:
                The internalReplyMessage
        """
        if "internalReplyMessage" in self._prop_dict:
            return self._prop_dict["internalReplyMessage"]
        else:
            return None

    @internal_reply_message.setter
    def internal_reply_message(self, val):
        self._prop_dict["internalReplyMessage"] = val

    @property
    def external_reply_message(self):
        """Gets and sets the externalReplyMessage
        
        Returns: 
            str:
                The externalReplyMessage
        """
        if "externalReplyMessage" in self._prop_dict:
            return self._prop_dict["externalReplyMessage"]
        else:
            return None

    @external_reply_message.setter
    def external_reply_message(self, val):
        self._prop_dict["externalReplyMessage"] = val

