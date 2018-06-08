# -*- coding: utf-8 -*- 
'''
# Copyright (c) Microsoft Corporation.  All Rights Reserved.  Licensed under the MIT License.  See License in the project root for license information.
# 
#  This file was generated and any changes will be overwritten.
'''

from __future__ import unicode_literals
from ..model.windows_device_account import WindowsDeviceAccount
from ..one_drive_object_base import OneDriveObjectBase


class UpdateWindowsDeviceAccountActionParameter(OneDriveObjectBase):

    def __init__(self, prop_dict={}):
        self._prop_dict = prop_dict

    @property
    def device_account(self):
        """
        Gets and sets the deviceAccount
        
        Returns: 
            :class:`WindowsDeviceAccount<onedrivesdk.model.windows_device_account.WindowsDeviceAccount>`:
                The deviceAccount
        """
        if "deviceAccount" in self._prop_dict:
            if isinstance(self._prop_dict["deviceAccount"], OneDriveObjectBase):
                return self._prop_dict["deviceAccount"]
            else :
                self._prop_dict["deviceAccount"] = WindowsDeviceAccount(self._prop_dict["deviceAccount"])
                return self._prop_dict["deviceAccount"]

        return None

    @device_account.setter
    def device_account(self, val):
        self._prop_dict["deviceAccount"] = val
    @property
    def password_rotation_enabled(self):
        """Gets and sets the passwordRotationEnabled
        
        Returns: 
            bool:
                The passwordRotationEnabled
        """
        if "passwordRotationEnabled" in self._prop_dict:
            return self._prop_dict["passwordRotationEnabled"]
        else:
            return None

    @password_rotation_enabled.setter
    def password_rotation_enabled(self, val):
        self._prop_dict["passwordRotationEnabled"] = val

    @property
    def calendar_sync_enabled(self):
        """Gets and sets the calendarSyncEnabled
        
        Returns: 
            bool:
                The calendarSyncEnabled
        """
        if "calendarSyncEnabled" in self._prop_dict:
            return self._prop_dict["calendarSyncEnabled"]
        else:
            return None

    @calendar_sync_enabled.setter
    def calendar_sync_enabled(self, val):
        self._prop_dict["calendarSyncEnabled"] = val

    @property
    def device_account_email(self):
        """Gets and sets the deviceAccountEmail
        
        Returns: 
            str:
                The deviceAccountEmail
        """
        if "deviceAccountEmail" in self._prop_dict:
            return self._prop_dict["deviceAccountEmail"]
        else:
            return None

    @device_account_email.setter
    def device_account_email(self, val):
        self._prop_dict["deviceAccountEmail"] = val

    @property
    def exchange_server(self):
        """Gets and sets the exchangeServer
        
        Returns: 
            str:
                The exchangeServer
        """
        if "exchangeServer" in self._prop_dict:
            return self._prop_dict["exchangeServer"]
        else:
            return None

    @exchange_server.setter
    def exchange_server(self, val):
        self._prop_dict["exchangeServer"] = val

    @property
    def session_initiation_protocal_address(self):
        """Gets and sets the sessionInitiationProtocalAddress
        
        Returns: 
            str:
                The sessionInitiationProtocalAddress
        """
        if "sessionInitiationProtocalAddress" in self._prop_dict:
            return self._prop_dict["sessionInitiationProtocalAddress"]
        else:
            return None

    @session_initiation_protocal_address.setter
    def session_initiation_protocal_address(self, val):
        self._prop_dict["sessionInitiationProtocalAddress"] = val

