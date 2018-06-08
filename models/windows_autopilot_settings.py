# -*- coding: utf-8 -*- 
'''
# Copyright (c) Microsoft Corporation.  All Rights Reserved.  Licensed under the MIT License.  See License in the project root for license information.
# 
#  This file was generated and any changes will be overwritten.
'''

from __future__ import unicode_literals
from ..model.windows_autopilot_sync_status import WindowsAutopilotSyncStatus
from datetime import datetime
from ..one_drive_object_base import OneDriveObjectBase


class WindowsAutopilotSettings(OneDriveObjectBase):

    def __init__(self, prop_dict={}):
        self._prop_dict = prop_dict

    @property
    def last_sync_date_time(self):
        """
        Gets and sets the lastSyncDateTime
        
        Returns:
            datetime:
                The lastSyncDateTime
        """
        if "lastSyncDateTime" in self._prop_dict:
            return datetime.strptime(self._prop_dict["lastSyncDateTime"].replace("Z", ""), "%Y-%m-%dT%H:%M:%S.%f")
        else:
            return None

    @last_sync_date_time.setter
    def last_sync_date_time(self, val):
        self._prop_dict["lastSyncDateTime"] = val.isoformat()+"Z"

    @property
    def last_manual_sync_trigger_date_time(self):
        """
        Gets and sets the lastManualSyncTriggerDateTime
        
        Returns:
            datetime:
                The lastManualSyncTriggerDateTime
        """
        if "lastManualSyncTriggerDateTime" in self._prop_dict:
            return datetime.strptime(self._prop_dict["lastManualSyncTriggerDateTime"].replace("Z", ""), "%Y-%m-%dT%H:%M:%S.%f")
        else:
            return None

    @last_manual_sync_trigger_date_time.setter
    def last_manual_sync_trigger_date_time(self, val):
        self._prop_dict["lastManualSyncTriggerDateTime"] = val.isoformat()+"Z"

    @property
    def sync_status(self):
        """
        Gets and sets the syncStatus
        
        Returns: 
            :class:`WindowsAutopilotSyncStatus<onedrivesdk.model.windows_autopilot_sync_status.WindowsAutopilotSyncStatus>`:
                The syncStatus
        """
        if "syncStatus" in self._prop_dict:
            if isinstance(self._prop_dict["syncStatus"], OneDriveObjectBase):
                return self._prop_dict["syncStatus"]
            else :
                self._prop_dict["syncStatus"] = WindowsAutopilotSyncStatus(self._prop_dict["syncStatus"])
                return self._prop_dict["syncStatus"]

        return None

    @sync_status.setter
    def sync_status(self, val):
        self._prop_dict["syncStatus"] = val

