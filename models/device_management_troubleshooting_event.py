# -*- coding: utf-8 -*- 
'''
# Copyright (c) Microsoft Corporation.  All Rights Reserved.  Licensed under the MIT License.  See License in the project root for license information.
# 
#  This file was generated and any changes will be overwritten.
'''

from __future__ import unicode_literals
from datetime import datetime
from ..one_drive_object_base import OneDriveObjectBase


class DeviceManagementTroubleshootingEvent(OneDriveObjectBase):

    def __init__(self, prop_dict={}):
        self._prop_dict = prop_dict

    @property
    def event_date_time(self):
        """
        Gets and sets the eventDateTime
        
        Returns:
            datetime:
                The eventDateTime
        """
        if "eventDateTime" in self._prop_dict:
            return datetime.strptime(self._prop_dict["eventDateTime"].replace("Z", ""), "%Y-%m-%dT%H:%M:%S.%f")
        else:
            return None

    @event_date_time.setter
    def event_date_time(self, val):
        self._prop_dict["eventDateTime"] = val.isoformat()+"Z"

    @property
    def correlation_id(self):
        """
        Gets and sets the correlationId
        
        Returns:
            str:
                The correlationId
        """
        if "correlationId" in self._prop_dict:
            return self._prop_dict["correlationId"]
        else:
            return None

    @correlation_id.setter
    def correlation_id(self, val):
        self._prop_dict["correlationId"] = val

