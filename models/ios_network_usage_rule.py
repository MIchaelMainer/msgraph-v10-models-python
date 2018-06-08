# -*- coding: utf-8 -*- 
'''
# Copyright (c) Microsoft Corporation.  All Rights Reserved.  Licensed under the MIT License.  See License in the project root for license information.
# 
#  This file was generated and any changes will be overwritten.
'''

from __future__ import unicode_literals
from ..model.app_list_item import AppListItem
from ..one_drive_object_base import OneDriveObjectBase


class IosNetworkUsageRule(OneDriveObjectBase):

    def __init__(self, prop_dict={}):
        self._prop_dict = prop_dict

    @property
    def managed_apps(self):
        """
        Gets and sets the managedApps
        
        Returns: 
            :class:`AppListItem<onedrivesdk.model.app_list_item.AppListItem>`:
                The managedApps
        """
        if "managedApps" in self._prop_dict:
            if isinstance(self._prop_dict["managedApps"], OneDriveObjectBase):
                return self._prop_dict["managedApps"]
            else :
                self._prop_dict["managedApps"] = AppListItem(self._prop_dict["managedApps"])
                return self._prop_dict["managedApps"]

        return None

    @managed_apps.setter
    def managed_apps(self, val):
        self._prop_dict["managedApps"] = val
    @property
    def cellular_data_block_when_roaming(self):
        """Gets and sets the cellularDataBlockWhenRoaming
        
        Returns: 
            bool:
                The cellularDataBlockWhenRoaming
        """
        if "cellularDataBlockWhenRoaming" in self._prop_dict:
            return self._prop_dict["cellularDataBlockWhenRoaming"]
        else:
            return None

    @cellular_data_block_when_roaming.setter
    def cellular_data_block_when_roaming(self, val):
        self._prop_dict["cellularDataBlockWhenRoaming"] = val

    @property
    def cellular_data_blocked(self):
        """Gets and sets the cellularDataBlocked
        
        Returns: 
            bool:
                The cellularDataBlocked
        """
        if "cellularDataBlocked" in self._prop_dict:
            return self._prop_dict["cellularDataBlocked"]
        else:
            return None

    @cellular_data_blocked.setter
    def cellular_data_blocked(self, val):
        self._prop_dict["cellularDataBlocked"] = val

