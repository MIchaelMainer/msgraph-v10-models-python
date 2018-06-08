# -*- coding: utf-8 -*- 
'''
# Copyright (c) Microsoft Corporation.  All Rights Reserved.  Licensed under the MIT License.  See License in the project root for license information.
# 
#  This file was generated and any changes will be overwritten.
'''

from __future__ import unicode_literals
from ..model.mdm_app_config_key_type import MdmAppConfigKeyType
from ..one_drive_object_base import OneDriveObjectBase


class AppConfigurationSettingItem(OneDriveObjectBase):

    def __init__(self, prop_dict={}):
        self._prop_dict = prop_dict

    @property
    def app_config_key(self):
        """Gets and sets the appConfigKey
        
        Returns: 
            str:
                The appConfigKey
        """
        if "appConfigKey" in self._prop_dict:
            return self._prop_dict["appConfigKey"]
        else:
            return None

    @app_config_key.setter
    def app_config_key(self, val):
        self._prop_dict["appConfigKey"] = val

    @property
    def app_config_key_type(self):
        """
        Gets and sets the appConfigKeyType
        
        Returns: 
            :class:`MdmAppConfigKeyType<onedrivesdk.model.mdm_app_config_key_type.MdmAppConfigKeyType>`:
                The appConfigKeyType
        """
        if "appConfigKeyType" in self._prop_dict:
            if isinstance(self._prop_dict["appConfigKeyType"], OneDriveObjectBase):
                return self._prop_dict["appConfigKeyType"]
            else :
                self._prop_dict["appConfigKeyType"] = MdmAppConfigKeyType(self._prop_dict["appConfigKeyType"])
                return self._prop_dict["appConfigKeyType"]

        return None

    @app_config_key_type.setter
    def app_config_key_type(self, val):
        self._prop_dict["appConfigKeyType"] = val
    @property
    def app_config_key_value(self):
        """Gets and sets the appConfigKeyValue
        
        Returns: 
            str:
                The appConfigKeyValue
        """
        if "appConfigKeyValue" in self._prop_dict:
            return self._prop_dict["appConfigKeyValue"]
        else:
            return None

    @app_config_key_value.setter
    def app_config_key_value(self, val):
        self._prop_dict["appConfigKeyValue"] = val

