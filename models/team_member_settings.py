# -*- coding: utf-8 -*- 
'''
# Copyright (c) Microsoft Corporation.  All Rights Reserved.  Licensed under the MIT License.  See License in the project root for license information.
# 
#  This file was generated and any changes will be overwritten.
'''

from __future__ import unicode_literals
from ..one_drive_object_base import OneDriveObjectBase


class TeamMemberSettings(OneDriveObjectBase):

    def __init__(self, prop_dict={}):
        self._prop_dict = prop_dict

    @property
    def allow_create_update_channels(self):
        """Gets and sets the allowCreateUpdateChannels
        
        Returns: 
            bool:
                The allowCreateUpdateChannels
        """
        if "allowCreateUpdateChannels" in self._prop_dict:
            return self._prop_dict["allowCreateUpdateChannels"]
        else:
            return None

    @allow_create_update_channels.setter
    def allow_create_update_channels(self, val):
        self._prop_dict["allowCreateUpdateChannels"] = val

    @property
    def allow_delete_channels(self):
        """Gets and sets the allowDeleteChannels
        
        Returns: 
            bool:
                The allowDeleteChannels
        """
        if "allowDeleteChannels" in self._prop_dict:
            return self._prop_dict["allowDeleteChannels"]
        else:
            return None

    @allow_delete_channels.setter
    def allow_delete_channels(self, val):
        self._prop_dict["allowDeleteChannels"] = val

    @property
    def allow_add_remove_apps(self):
        """Gets and sets the allowAddRemoveApps
        
        Returns: 
            bool:
                The allowAddRemoveApps
        """
        if "allowAddRemoveApps" in self._prop_dict:
            return self._prop_dict["allowAddRemoveApps"]
        else:
            return None

    @allow_add_remove_apps.setter
    def allow_add_remove_apps(self, val):
        self._prop_dict["allowAddRemoveApps"] = val

    @property
    def allow_create_update_remove_tabs(self):
        """Gets and sets the allowCreateUpdateRemoveTabs
        
        Returns: 
            bool:
                The allowCreateUpdateRemoveTabs
        """
        if "allowCreateUpdateRemoveTabs" in self._prop_dict:
            return self._prop_dict["allowCreateUpdateRemoveTabs"]
        else:
            return None

    @allow_create_update_remove_tabs.setter
    def allow_create_update_remove_tabs(self, val):
        self._prop_dict["allowCreateUpdateRemoveTabs"] = val

    @property
    def allow_create_update_remove_connectors(self):
        """Gets and sets the allowCreateUpdateRemoveConnectors
        
        Returns: 
            bool:
                The allowCreateUpdateRemoveConnectors
        """
        if "allowCreateUpdateRemoveConnectors" in self._prop_dict:
            return self._prop_dict["allowCreateUpdateRemoveConnectors"]
        else:
            return None

    @allow_create_update_remove_connectors.setter
    def allow_create_update_remove_connectors(self, val):
        self._prop_dict["allowCreateUpdateRemoveConnectors"] = val
