# -*- coding: utf-8 -*- 
'''
# Copyright (c) Microsoft Corporation.  All Rights Reserved.  Licensed under the MIT License.  See License in the project root for license information.
# 
#  This file was generated and any changes will be overwritten.
'''

from __future__ import unicode_literals
from ..model.ndes_connector_state import NdesConnectorState
from datetime import datetime
from ..one_drive_object_base import OneDriveObjectBase


class NdesConnector(OneDriveObjectBase):

    def __init__(self, prop_dict={}):
        self._prop_dict = prop_dict

    @property
    def last_connection_date_time(self):
        """
        Gets and sets the lastConnectionDateTime
        
        Returns:
            datetime:
                The lastConnectionDateTime
        """
        if "lastConnectionDateTime" in self._prop_dict:
            return datetime.strptime(self._prop_dict["lastConnectionDateTime"].replace("Z", ""), "%Y-%m-%dT%H:%M:%S.%f")
        else:
            return None

    @last_connection_date_time.setter
    def last_connection_date_time(self, val):
        self._prop_dict["lastConnectionDateTime"] = val.isoformat()+"Z"

    @property
    def state(self):
        """
        Gets and sets the state
        
        Returns: 
            :class:`NdesConnectorState<onedrivesdk.model.ndes_connector_state.NdesConnectorState>`:
                The state
        """
        if "state" in self._prop_dict:
            if isinstance(self._prop_dict["state"], OneDriveObjectBase):
                return self._prop_dict["state"]
            else :
                self._prop_dict["state"] = NdesConnectorState(self._prop_dict["state"])
                return self._prop_dict["state"]

        return None

    @state.setter
    def state(self, val):
        self._prop_dict["state"] = val

    @property
    def display_name(self):
        """
        Gets and sets the displayName
        
        Returns:
            str:
                The displayName
        """
        if "displayName" in self._prop_dict:
            return self._prop_dict["displayName"]
        else:
            return None

    @display_name.setter
    def display_name(self, val):
        self._prop_dict["displayName"] = val

