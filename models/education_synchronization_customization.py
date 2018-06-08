# -*- coding: utf-8 -*- 
'''
# Copyright (c) Microsoft Corporation.  All Rights Reserved.  Licensed under the MIT License.  See License in the project root for license information.
# 
#  This file was generated and any changes will be overwritten.
'''

from __future__ import unicode_literals
from datetime import datetime
from ..one_drive_object_base import OneDriveObjectBase


class EducationSynchronizationCustomization(OneDriveObjectBase):

    def __init__(self, prop_dict={}):
        self._prop_dict = prop_dict

    @property
    def optional_properties_to_sync(self):
        """Gets and sets the optionalPropertiesToSync
        
        Returns: 
            str:
                The optionalPropertiesToSync
        """
        if "optionalPropertiesToSync" in self._prop_dict:
            return self._prop_dict["optionalPropertiesToSync"]
        else:
            return None

    @optional_properties_to_sync.setter
    def optional_properties_to_sync(self, val):
        self._prop_dict["optionalPropertiesToSync"] = val

    @property
    def synchronization_start_date(self):
        """Gets and sets the synchronizationStartDate
        
        Returns: 
            datetime:
                The synchronizationStartDate
        """
        if "synchronizationStartDate" in self._prop_dict:
            return datetime.strptime(self._prop_dict["synchronizationStartDate"].replace("Z", ""), "%Y-%m-%dT%H:%M:%S.%f")
        else:
            return None

    @synchronization_start_date.setter
    def synchronization_start_date(self, val):
        self._prop_dict["synchronizationStartDate"] = val.isoformat()+"Z"

    @property
    def is_sync_deferred(self):
        """Gets and sets the isSyncDeferred
        
        Returns: 
            bool:
                The isSyncDeferred
        """
        if "isSyncDeferred" in self._prop_dict:
            return self._prop_dict["isSyncDeferred"]
        else:
            return None

    @is_sync_deferred.setter
    def is_sync_deferred(self, val):
        self._prop_dict["isSyncDeferred"] = val

    @property
    def allow_display_name_update(self):
        """Gets and sets the allowDisplayNameUpdate
        
        Returns: 
            bool:
                The allowDisplayNameUpdate
        """
        if "allowDisplayNameUpdate" in self._prop_dict:
            return self._prop_dict["allowDisplayNameUpdate"]
        else:
            return None

    @allow_display_name_update.setter
    def allow_display_name_update(self, val):
        self._prop_dict["allowDisplayNameUpdate"] = val

