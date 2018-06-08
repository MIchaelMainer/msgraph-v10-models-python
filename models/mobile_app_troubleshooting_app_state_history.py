# -*- coding: utf-8 -*- 
'''
# Copyright (c) Microsoft Corporation.  All Rights Reserved.  Licensed under the MIT License.  See License in the project root for license information.
# 
#  This file was generated and any changes will be overwritten.
'''

from __future__ import unicode_literals
from ..model.mobile_app_action_type import MobileAppActionType
from ..model.run_state import RunState
from ..one_drive_object_base import OneDriveObjectBase


class MobileAppTroubleshootingAppStateHistory(OneDriveObjectBase):

    def __init__(self, prop_dict={}):
        self._prop_dict = prop_dict

    @property
    def action_type(self):
        """
        Gets and sets the actionType
        
        Returns: 
            :class:`MobileAppActionType<onedrivesdk.model.mobile_app_action_type.MobileAppActionType>`:
                The actionType
        """
        if "actionType" in self._prop_dict:
            if isinstance(self._prop_dict["actionType"], OneDriveObjectBase):
                return self._prop_dict["actionType"]
            else :
                self._prop_dict["actionType"] = MobileAppActionType(self._prop_dict["actionType"])
                return self._prop_dict["actionType"]

        return None

    @action_type.setter
    def action_type(self, val):
        self._prop_dict["actionType"] = val
    @property
    def run_state(self):
        """
        Gets and sets the runState
        
        Returns: 
            :class:`RunState<onedrivesdk.model.run_state.RunState>`:
                The runState
        """
        if "runState" in self._prop_dict:
            if isinstance(self._prop_dict["runState"], OneDriveObjectBase):
                return self._prop_dict["runState"]
            else :
                self._prop_dict["runState"] = RunState(self._prop_dict["runState"])
                return self._prop_dict["runState"]

        return None

    @run_state.setter
    def run_state(self, val):
        self._prop_dict["runState"] = val
    @property
    def error_code(self):
        """Gets and sets the errorCode
        
        Returns: 
            str:
                The errorCode
        """
        if "errorCode" in self._prop_dict:
            return self._prop_dict["errorCode"]
        else:
            return None

    @error_code.setter
    def error_code(self, val):
        self._prop_dict["errorCode"] = val

