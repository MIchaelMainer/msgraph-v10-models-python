# -*- coding: utf-8 -*- 
'''
# Copyright (c) Microsoft Corporation.  All Rights Reserved.  Licensed under the MIT License.  See License in the project root for license information.
# 
#  This file was generated and any changes will be overwritten.
'''

from __future__ import unicode_literals
from ..model.item_action_set import ItemActionSet
from ..model.identity_set import IdentitySet
from ..model.item_activity_time_set import ItemActivityTimeSet
from ..model.drive_item import DriveItem
from ..model.list_item import ListItem
from ..one_drive_object_base import OneDriveObjectBase


class ItemActivity(OneDriveObjectBase):

    def __init__(self, prop_dict={}):
        self._prop_dict = prop_dict

    @property
    def action(self):
        """
        Gets and sets the action
        
        Returns: 
            :class:`ItemActionSet<onedrivesdk.model.item_action_set.ItemActionSet>`:
                The action
        """
        if "action" in self._prop_dict:
            if isinstance(self._prop_dict["action"], OneDriveObjectBase):
                return self._prop_dict["action"]
            else :
                self._prop_dict["action"] = ItemActionSet(self._prop_dict["action"])
                return self._prop_dict["action"]

        return None

    @action.setter
    def action(self, val):
        self._prop_dict["action"] = val

    @property
    def actor(self):
        """
        Gets and sets the actor
        
        Returns: 
            :class:`IdentitySet<onedrivesdk.model.identity_set.IdentitySet>`:
                The actor
        """
        if "actor" in self._prop_dict:
            if isinstance(self._prop_dict["actor"], OneDriveObjectBase):
                return self._prop_dict["actor"]
            else :
                self._prop_dict["actor"] = IdentitySet(self._prop_dict["actor"])
                return self._prop_dict["actor"]

        return None

    @actor.setter
    def actor(self, val):
        self._prop_dict["actor"] = val

    @property
    def times(self):
        """
        Gets and sets the times
        
        Returns: 
            :class:`ItemActivityTimeSet<onedrivesdk.model.item_activity_time_set.ItemActivityTimeSet>`:
                The times
        """
        if "times" in self._prop_dict:
            if isinstance(self._prop_dict["times"], OneDriveObjectBase):
                return self._prop_dict["times"]
            else :
                self._prop_dict["times"] = ItemActivityTimeSet(self._prop_dict["times"])
                return self._prop_dict["times"]

        return None

    @times.setter
    def times(self, val):
        self._prop_dict["times"] = val

    @property
    def drive_item(self):
        """
        Gets and sets the driveItem
        
        Returns: 
            :class:`DriveItem<onedrivesdk.model.drive_item.DriveItem>`:
                The driveItem
        """
        if "driveItem" in self._prop_dict:
            if isinstance(self._prop_dict["driveItem"], OneDriveObjectBase):
                return self._prop_dict["driveItem"]
            else :
                self._prop_dict["driveItem"] = DriveItem(self._prop_dict["driveItem"])
                return self._prop_dict["driveItem"]

        return None

    @drive_item.setter
    def drive_item(self, val):
        self._prop_dict["driveItem"] = val

    @property
    def list_item(self):
        """
        Gets and sets the listItem
        
        Returns: 
            :class:`ListItem<onedrivesdk.model.list_item.ListItem>`:
                The listItem
        """
        if "listItem" in self._prop_dict:
            if isinstance(self._prop_dict["listItem"], OneDriveObjectBase):
                return self._prop_dict["listItem"]
            else :
                self._prop_dict["listItem"] = ListItem(self._prop_dict["listItem"])
                return self._prop_dict["listItem"]

        return None

    @list_item.setter
    def list_item(self, val):
        self._prop_dict["listItem"] = val

