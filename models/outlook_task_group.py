# -*- coding: utf-8 -*- 
'''
# Copyright (c) Microsoft Corporation.  All Rights Reserved.  Licensed under the MIT License.  See License in the project root for license information.
# 
#  This file was generated and any changes will be overwritten.
'''

from __future__ import unicode_literals
from ..model.outlook_task_folder import OutlookTaskFolder
from ..one_drive_object_base import OneDriveObjectBase


class OutlookTaskGroup(OneDriveObjectBase):

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
    def is_default_group(self):
        """
        Gets and sets the isDefaultGroup
        
        Returns:
            bool:
                The isDefaultGroup
        """
        if "isDefaultGroup" in self._prop_dict:
            return self._prop_dict["isDefaultGroup"]
        else:
            return None

    @is_default_group.setter
    def is_default_group(self, val):
        self._prop_dict["isDefaultGroup"] = val

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
    def group_key(self):
        """
        Gets and sets the groupKey
        
        Returns:
            UUID:
                The groupKey
        """
        if "groupKey" in self._prop_dict:
            return self._prop_dict["groupKey"]
        else:
            return None

    @group_key.setter
    def group_key(self, val):
        self._prop_dict["groupKey"] = val

    @property
    def task_folders(self):
        """Gets and sets the taskFolders
        
        Returns: 
            :class:`TaskFoldersCollectionPage<onedrivesdk.request.task_folders_collection.TaskFoldersCollectionPage>`:
                The taskFolders
        """
        if "taskFolders" in self._prop_dict:
            return TaskFoldersCollectionPage(self._prop_dict["taskFolders"])
        else:
            return None

