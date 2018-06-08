# -*- coding: utf-8 -*- 
'''
# Copyright (c) Microsoft Corporation.  All Rights Reserved.  Licensed under the MIT License.  See License in the project root for license information.
# 
#  This file was generated and any changes will be overwritten.
'''

from __future__ import unicode_literals
from ..model.outlook_task import OutlookTask
from ..model.single_value_legacy_extended_property import SingleValueLegacyExtendedProperty
from ..model.multi_value_legacy_extended_property import MultiValueLegacyExtendedProperty
from ..one_drive_object_base import OneDriveObjectBase


class OutlookTaskFolder(OneDriveObjectBase):

    def __init__(self, prop_dict={}):
        self._prop_dict = prop_dict

    @property
    def change_key(self):
        """
        Gets and sets the changeKey
        
        Returns:
            str:
                The changeKey
        """
        if "changeKey" in self._prop_dict:
            return self._prop_dict["changeKey"]
        else:
            return None

    @change_key.setter
    def change_key(self, val):
        self._prop_dict["changeKey"] = val

    @property
    def name(self):
        """
        Gets and sets the name
        
        Returns:
            str:
                The name
        """
        if "name" in self._prop_dict:
            return self._prop_dict["name"]
        else:
            return None

    @name.setter
    def name(self, val):
        self._prop_dict["name"] = val

    @property
    def is_default_folder(self):
        """
        Gets and sets the isDefaultFolder
        
        Returns:
            bool:
                The isDefaultFolder
        """
        if "isDefaultFolder" in self._prop_dict:
            return self._prop_dict["isDefaultFolder"]
        else:
            return None

    @is_default_folder.setter
    def is_default_folder(self, val):
        self._prop_dict["isDefaultFolder"] = val

    @property
    def parent_group_key(self):
        """
        Gets and sets the parentGroupKey
        
        Returns:
            UUID:
                The parentGroupKey
        """
        if "parentGroupKey" in self._prop_dict:
            return self._prop_dict["parentGroupKey"]
        else:
            return None

    @parent_group_key.setter
    def parent_group_key(self, val):
        self._prop_dict["parentGroupKey"] = val

    @property
    def tasks(self):
        """Gets and sets the tasks
        
        Returns: 
            :class:`TasksCollectionPage<onedrivesdk.request.tasks_collection.TasksCollectionPage>`:
                The tasks
        """
        if "tasks" in self._prop_dict:
            return TasksCollectionPage(self._prop_dict["tasks"])
        else:
            return None

    @property
    def single_value_extended_properties(self):
        """Gets and sets the singleValueExtendedProperties
        
        Returns: 
            :class:`SingleValueExtendedPropertiesCollectionPage<onedrivesdk.request.single_value_extended_properties_collection.SingleValueExtendedPropertiesCollectionPage>`:
                The singleValueExtendedProperties
        """
        if "singleValueExtendedProperties" in self._prop_dict:
            return SingleValueExtendedPropertiesCollectionPage(self._prop_dict["singleValueExtendedProperties"])
        else:
            return None

    @property
    def multi_value_extended_properties(self):
        """Gets and sets the multiValueExtendedProperties
        
        Returns: 
            :class:`MultiValueExtendedPropertiesCollectionPage<onedrivesdk.request.multi_value_extended_properties_collection.MultiValueExtendedPropertiesCollectionPage>`:
                The multiValueExtendedProperties
        """
        if "multiValueExtendedProperties" in self._prop_dict:
            return MultiValueExtendedPropertiesCollectionPage(self._prop_dict["multiValueExtendedProperties"])
        else:
            return None

