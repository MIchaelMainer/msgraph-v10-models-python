# -*- coding: utf-8 -*- 
'''
# Copyright (c) Microsoft Corporation.  All Rights Reserved.  Licensed under the MIT License.  See License in the project root for license information.
# 
#  This file was generated and any changes will be overwritten.
'''

from __future__ import unicode_literals
from ..model.android_managed_store_app_configuration_schema_item_data_type import AndroidManagedStoreAppConfigurationSchemaItemDataType
from ..model.key_value_pair import KeyValuePair
from ..one_drive_object_base import OneDriveObjectBase


class AndroidManagedStoreAppConfigurationSchemaItem(OneDriveObjectBase):

    def __init__(self, prop_dict={}):
        self._prop_dict = prop_dict

    @property
    def schema_item_key(self):
        """Gets and sets the schemaItemKey
        
        Returns: 
            str:
                The schemaItemKey
        """
        if "schemaItemKey" in self._prop_dict:
            return self._prop_dict["schemaItemKey"]
        else:
            return None

    @schema_item_key.setter
    def schema_item_key(self, val):
        self._prop_dict["schemaItemKey"] = val

    @property
    def display_name(self):
        """Gets and sets the displayName
        
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

    @property
    def description(self):
        """Gets and sets the description
        
        Returns: 
            str:
                The description
        """
        if "description" in self._prop_dict:
            return self._prop_dict["description"]
        else:
            return None

    @description.setter
    def description(self, val):
        self._prop_dict["description"] = val

    @property
    def default_bool_value(self):
        """Gets and sets the defaultBoolValue
        
        Returns: 
            bool:
                The defaultBoolValue
        """
        if "defaultBoolValue" in self._prop_dict:
            return self._prop_dict["defaultBoolValue"]
        else:
            return None

    @default_bool_value.setter
    def default_bool_value(self, val):
        self._prop_dict["defaultBoolValue"] = val

    @property
    def default_int_value(self):
        """Gets and sets the defaultIntValue
        
        Returns: 
            int:
                The defaultIntValue
        """
        if "defaultIntValue" in self._prop_dict:
            return self._prop_dict["defaultIntValue"]
        else:
            return None

    @default_int_value.setter
    def default_int_value(self, val):
        self._prop_dict["defaultIntValue"] = val

    @property
    def default_string_value(self):
        """Gets and sets the defaultStringValue
        
        Returns: 
            str:
                The defaultStringValue
        """
        if "defaultStringValue" in self._prop_dict:
            return self._prop_dict["defaultStringValue"]
        else:
            return None

    @default_string_value.setter
    def default_string_value(self, val):
        self._prop_dict["defaultStringValue"] = val

    @property
    def default_string_array_value(self):
        """Gets and sets the defaultStringArrayValue
        
        Returns: 
            str:
                The defaultStringArrayValue
        """
        if "defaultStringArrayValue" in self._prop_dict:
            return self._prop_dict["defaultStringArrayValue"]
        else:
            return None

    @default_string_array_value.setter
    def default_string_array_value(self, val):
        self._prop_dict["defaultStringArrayValue"] = val

    @property
    def data_type(self):
        """
        Gets and sets the dataType
        
        Returns: 
            :class:`AndroidManagedStoreAppConfigurationSchemaItemDataType<onedrivesdk.model.android_managed_store_app_configuration_schema_item_data_type.AndroidManagedStoreAppConfigurationSchemaItemDataType>`:
                The dataType
        """
        if "dataType" in self._prop_dict:
            if isinstance(self._prop_dict["dataType"], OneDriveObjectBase):
                return self._prop_dict["dataType"]
            else :
                self._prop_dict["dataType"] = AndroidManagedStoreAppConfigurationSchemaItemDataType(self._prop_dict["dataType"])
                return self._prop_dict["dataType"]

        return None

    @data_type.setter
    def data_type(self, val):
        self._prop_dict["dataType"] = val
    @property
    def selections(self):
        """
        Gets and sets the selections
        
        Returns: 
            :class:`KeyValuePair<onedrivesdk.model.key_value_pair.KeyValuePair>`:
                The selections
        """
        if "selections" in self._prop_dict:
            if isinstance(self._prop_dict["selections"], OneDriveObjectBase):
                return self._prop_dict["selections"]
            else :
                self._prop_dict["selections"] = KeyValuePair(self._prop_dict["selections"])
                return self._prop_dict["selections"]

        return None

    @selections.setter
    def selections(self, val):
        self._prop_dict["selections"] = val
