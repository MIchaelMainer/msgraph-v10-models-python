# -*- coding: utf-8 -*- 
'''
# Copyright (c) Microsoft Corporation.  All Rights Reserved.  Licensed under the MIT License.  See License in the project root for license information.
# 
#  This file was generated and any changes will be overwritten.
'''

from __future__ import unicode_literals
from ..model.synchronization_schedule import SynchronizationSchedule
from ..model.synchronization_status import SynchronizationStatus
from ..model.synchronization_schema import SynchronizationSchema
from ..one_drive_object_base import OneDriveObjectBase


class SynchronizationJob(OneDriveObjectBase):

    def __init__(self, prop_dict={}):
        self._prop_dict = prop_dict

    @property
    def template_id(self):
        """
        Gets and sets the templateId
        
        Returns:
            str:
                The templateId
        """
        if "templateId" in self._prop_dict:
            return self._prop_dict["templateId"]
        else:
            return None

    @template_id.setter
    def template_id(self, val):
        self._prop_dict["templateId"] = val

    @property
    def schedule(self):
        """
        Gets and sets the schedule
        
        Returns: 
            :class:`SynchronizationSchedule<onedrivesdk.model.synchronization_schedule.SynchronizationSchedule>`:
                The schedule
        """
        if "schedule" in self._prop_dict:
            if isinstance(self._prop_dict["schedule"], OneDriveObjectBase):
                return self._prop_dict["schedule"]
            else :
                self._prop_dict["schedule"] = SynchronizationSchedule(self._prop_dict["schedule"])
                return self._prop_dict["schedule"]

        return None

    @schedule.setter
    def schedule(self, val):
        self._prop_dict["schedule"] = val

    @property
    def status(self):
        """
        Gets and sets the status
        
        Returns: 
            :class:`SynchronizationStatus<onedrivesdk.model.synchronization_status.SynchronizationStatus>`:
                The status
        """
        if "status" in self._prop_dict:
            if isinstance(self._prop_dict["status"], OneDriveObjectBase):
                return self._prop_dict["status"]
            else :
                self._prop_dict["status"] = SynchronizationStatus(self._prop_dict["status"])
                return self._prop_dict["status"]

        return None

    @status.setter
    def status(self, val):
        self._prop_dict["status"] = val

    @property
    def schema(self):
        """
        Gets and sets the schema
        
        Returns: 
            :class:`SynchronizationSchema<onedrivesdk.model.synchronization_schema.SynchronizationSchema>`:
                The schema
        """
        if "schema" in self._prop_dict:
            if isinstance(self._prop_dict["schema"], OneDriveObjectBase):
                return self._prop_dict["schema"]
            else :
                self._prop_dict["schema"] = SynchronizationSchema(self._prop_dict["schema"])
                return self._prop_dict["schema"]

        return None

    @schema.setter
    def schema(self, val):
        self._prop_dict["schema"] = val

