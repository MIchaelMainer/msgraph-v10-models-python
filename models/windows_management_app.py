# -*- coding: utf-8 -*- 
'''
# Copyright (c) Microsoft Corporation.  All Rights Reserved.  Licensed under the MIT License.  See License in the project root for license information.
# 
#  This file was generated and any changes will be overwritten.
'''

from __future__ import unicode_literals
from ..model.windows_management_app_health_summary import WindowsManagementAppHealthSummary
from ..model.windows_management_app_health_state import WindowsManagementAppHealthState
from ..one_drive_object_base import OneDriveObjectBase


class WindowsManagementApp(OneDriveObjectBase):

    def __init__(self, prop_dict={}):
        self._prop_dict = prop_dict

    @property
    def available_version(self):
        """
        Gets and sets the availableVersion
        
        Returns:
            str:
                The availableVersion
        """
        if "availableVersion" in self._prop_dict:
            return self._prop_dict["availableVersion"]
        else:
            return None

    @available_version.setter
    def available_version(self, val):
        self._prop_dict["availableVersion"] = val

    @property
    def health_summary(self):
        """
        Gets and sets the healthSummary
        
        Returns: 
            :class:`WindowsManagementAppHealthSummary<onedrivesdk.model.windows_management_app_health_summary.WindowsManagementAppHealthSummary>`:
                The healthSummary
        """
        if "healthSummary" in self._prop_dict:
            if isinstance(self._prop_dict["healthSummary"], OneDriveObjectBase):
                return self._prop_dict["healthSummary"]
            else :
                self._prop_dict["healthSummary"] = WindowsManagementAppHealthSummary(self._prop_dict["healthSummary"])
                return self._prop_dict["healthSummary"]

        return None

    @health_summary.setter
    def health_summary(self, val):
        self._prop_dict["healthSummary"] = val

    @property
    def health_states(self):
        """Gets and sets the healthStates
        
        Returns: 
            :class:`HealthStatesCollectionPage<onedrivesdk.request.health_states_collection.HealthStatesCollectionPage>`:
                The healthStates
        """
        if "healthStates" in self._prop_dict:
            return HealthStatesCollectionPage(self._prop_dict["healthStates"])
        else:
            return None

