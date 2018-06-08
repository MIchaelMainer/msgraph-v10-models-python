# -*- coding: utf-8 -*- 
'''
# Copyright (c) Microsoft Corporation.  All Rights Reserved.  Licensed under the MIT License.  See License in the project root for license information.
# 
#  This file was generated and any changes will be overwritten.
'''

from __future__ import unicode_literals
from ..model.onenote_patch_action_type import OnenotePatchActionType
from ..model.onenote_patch_insert_position import OnenotePatchInsertPosition
from ..one_drive_object_base import OneDriveObjectBase


class OnenotePatchContentCommand(OneDriveObjectBase):

    def __init__(self, prop_dict={}):
        self._prop_dict = prop_dict

    @property
    def action(self):
        """
        Gets and sets the action
        
        Returns: 
            :class:`OnenotePatchActionType<onedrivesdk.model.onenote_patch_action_type.OnenotePatchActionType>`:
                The action
        """
        if "action" in self._prop_dict:
            if isinstance(self._prop_dict["action"], OneDriveObjectBase):
                return self._prop_dict["action"]
            else :
                self._prop_dict["action"] = OnenotePatchActionType(self._prop_dict["action"])
                return self._prop_dict["action"]

        return None

    @action.setter
    def action(self, val):
        self._prop_dict["action"] = val
    @property
    def target(self):
        """Gets and sets the target
        
        Returns: 
            str:
                The target
        """
        if "target" in self._prop_dict:
            return self._prop_dict["target"]
        else:
            return None

    @target.setter
    def target(self, val):
        self._prop_dict["target"] = val

    @property
    def content(self):
        """Gets and sets the content
        
        Returns: 
            str:
                The content
        """
        if "content" in self._prop_dict:
            return self._prop_dict["content"]
        else:
            return None

    @content.setter
    def content(self, val):
        self._prop_dict["content"] = val

    @property
    def position(self):
        """
        Gets and sets the position
        
        Returns: 
            :class:`OnenotePatchInsertPosition<onedrivesdk.model.onenote_patch_insert_position.OnenotePatchInsertPosition>`:
                The position
        """
        if "position" in self._prop_dict:
            if isinstance(self._prop_dict["position"], OneDriveObjectBase):
                return self._prop_dict["position"]
            else :
                self._prop_dict["position"] = OnenotePatchInsertPosition(self._prop_dict["position"])
                return self._prop_dict["position"]

        return None

    @position.setter
    def position(self, val):
        self._prop_dict["position"] = val
