# -*- coding: utf-8 -*- 
'''
# Copyright (c) Microsoft Corporation.  All Rights Reserved.  Licensed under the MIT License.  See License in the project root for license information.
# 
#  This file was generated and any changes will be overwritten.
'''

from __future__ import unicode_literals
from ..model.remote_action import RemoteAction
from ..model.action_state import ActionState
from datetime import datetime
from ..one_drive_object_base import OneDriveObjectBase


class RemoteActionAudit(OneDriveObjectBase):

    def __init__(self, prop_dict={}):
        self._prop_dict = prop_dict

    @property
    def device_display_name(self):
        """
        Gets and sets the deviceDisplayName
        
        Returns:
            str:
                The deviceDisplayName
        """
        if "deviceDisplayName" in self._prop_dict:
            return self._prop_dict["deviceDisplayName"]
        else:
            return None

    @device_display_name.setter
    def device_display_name(self, val):
        self._prop_dict["deviceDisplayName"] = val

    @property
    def user_name(self):
        """
        Gets and sets the userName
        
        Returns:
            str:
                The userName
        """
        if "userName" in self._prop_dict:
            return self._prop_dict["userName"]
        else:
            return None

    @user_name.setter
    def user_name(self, val):
        self._prop_dict["userName"] = val

    @property
    def initiated_by_user_principal_name(self):
        """
        Gets and sets the initiatedByUserPrincipalName
        
        Returns:
            str:
                The initiatedByUserPrincipalName
        """
        if "initiatedByUserPrincipalName" in self._prop_dict:
            return self._prop_dict["initiatedByUserPrincipalName"]
        else:
            return None

    @initiated_by_user_principal_name.setter
    def initiated_by_user_principal_name(self, val):
        self._prop_dict["initiatedByUserPrincipalName"] = val

    @property
    def action(self):
        """
        Gets and sets the action
        
        Returns: 
            :class:`RemoteAction<onedrivesdk.model.remote_action.RemoteAction>`:
                The action
        """
        if "action" in self._prop_dict:
            if isinstance(self._prop_dict["action"], OneDriveObjectBase):
                return self._prop_dict["action"]
            else :
                self._prop_dict["action"] = RemoteAction(self._prop_dict["action"])
                return self._prop_dict["action"]

        return None

    @action.setter
    def action(self, val):
        self._prop_dict["action"] = val

    @property
    def request_date_time(self):
        """
        Gets and sets the requestDateTime
        
        Returns:
            datetime:
                The requestDateTime
        """
        if "requestDateTime" in self._prop_dict:
            return datetime.strptime(self._prop_dict["requestDateTime"].replace("Z", ""), "%Y-%m-%dT%H:%M:%S.%f")
        else:
            return None

    @request_date_time.setter
    def request_date_time(self, val):
        self._prop_dict["requestDateTime"] = val.isoformat()+"Z"

    @property
    def device_owner_user_principal_name(self):
        """
        Gets and sets the deviceOwnerUserPrincipalName
        
        Returns:
            str:
                The deviceOwnerUserPrincipalName
        """
        if "deviceOwnerUserPrincipalName" in self._prop_dict:
            return self._prop_dict["deviceOwnerUserPrincipalName"]
        else:
            return None

    @device_owner_user_principal_name.setter
    def device_owner_user_principal_name(self, val):
        self._prop_dict["deviceOwnerUserPrincipalName"] = val

    @property
    def device_imei(self):
        """
        Gets and sets the deviceIMEI
        
        Returns:
            str:
                The deviceIMEI
        """
        if "deviceIMEI" in self._prop_dict:
            return self._prop_dict["deviceIMEI"]
        else:
            return None

    @device_imei.setter
    def device_imei(self, val):
        self._prop_dict["deviceIMEI"] = val

    @property
    def action_state(self):
        """
        Gets and sets the actionState
        
        Returns: 
            :class:`ActionState<onedrivesdk.model.action_state.ActionState>`:
                The actionState
        """
        if "actionState" in self._prop_dict:
            if isinstance(self._prop_dict["actionState"], OneDriveObjectBase):
                return self._prop_dict["actionState"]
            else :
                self._prop_dict["actionState"] = ActionState(self._prop_dict["actionState"])
                return self._prop_dict["actionState"]

        return None

    @action_state.setter
    def action_state(self, val):
        self._prop_dict["actionState"] = val

