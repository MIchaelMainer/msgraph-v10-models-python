# -*- coding: utf-8 -*- 
'''
# Copyright (c) Microsoft Corporation.  All Rights Reserved.  Licensed under the MIT License.  See License in the project root for license information.
# 
#  This file was generated and any changes will be overwritten.
'''

from __future__ import unicode_literals
from ..model.imported_windows_autopilot_device_identity_state import ImportedWindowsAutopilotDeviceIdentityState
from ..one_drive_object_base import OneDriveObjectBase


class ImportedWindowsAutopilotDeviceIdentity(OneDriveObjectBase):

    def __init__(self, prop_dict={}):
        self._prop_dict = prop_dict

    @property
    def order_identifier(self):
        """
        Gets and sets the orderIdentifier
        
        Returns:
            str:
                The orderIdentifier
        """
        if "orderIdentifier" in self._prop_dict:
            return self._prop_dict["orderIdentifier"]
        else:
            return None

    @order_identifier.setter
    def order_identifier(self, val):
        self._prop_dict["orderIdentifier"] = val

    @property
    def serial_number(self):
        """
        Gets and sets the serialNumber
        
        Returns:
            str:
                The serialNumber
        """
        if "serialNumber" in self._prop_dict:
            return self._prop_dict["serialNumber"]
        else:
            return None

    @serial_number.setter
    def serial_number(self, val):
        self._prop_dict["serialNumber"] = val

    @property
    def product_key(self):
        """
        Gets and sets the productKey
        
        Returns:
            str:
                The productKey
        """
        if "productKey" in self._prop_dict:
            return self._prop_dict["productKey"]
        else:
            return None

    @product_key.setter
    def product_key(self, val):
        self._prop_dict["productKey"] = val

    @property
    def state(self):
        """
        Gets and sets the state
        
        Returns: 
            :class:`ImportedWindowsAutopilotDeviceIdentityState<onedrivesdk.model.imported_windows_autopilot_device_identity_state.ImportedWindowsAutopilotDeviceIdentityState>`:
                The state
        """
        if "state" in self._prop_dict:
            if isinstance(self._prop_dict["state"], OneDriveObjectBase):
                return self._prop_dict["state"]
            else :
                self._prop_dict["state"] = ImportedWindowsAutopilotDeviceIdentityState(self._prop_dict["state"])
                return self._prop_dict["state"]

        return None

    @state.setter
    def state(self, val):
        self._prop_dict["state"] = val

