# -*- coding: utf-8 -*- 
'''
# Copyright (c) Microsoft Corporation.  All Rights Reserved.  Licensed under the MIT License.  See License in the project root for license information.
# 
#  This file was generated and any changes will be overwritten.
'''

from __future__ import unicode_literals
from ..model.outlook_category import OutlookCategory
from ..model.outlook_task_group import OutlookTaskGroup
from ..model.outlook_task_folder import OutlookTaskFolder
from ..model.outlook_task import OutlookTask
from ..one_drive_object_base import OneDriveObjectBase


class OutlookUser(OneDriveObjectBase):

    def __init__(self, prop_dict={}):
        self._prop_dict = prop_dict

    @property
    def master_categories(self):
        """Gets and sets the masterCategories
        
        Returns: 
            :class:`MasterCategoriesCollectionPage<onedrivesdk.request.master_categories_collection.MasterCategoriesCollectionPage>`:
                The masterCategories
        """
        if "masterCategories" in self._prop_dict:
            return MasterCategoriesCollectionPage(self._prop_dict["masterCategories"])
        else:
            return None

    @property
    def task_groups(self):
        """Gets and sets the taskGroups
        
        Returns: 
            :class:`TaskGroupsCollectionPage<onedrivesdk.request.task_groups_collection.TaskGroupsCollectionPage>`:
                The taskGroups
        """
        if "taskGroups" in self._prop_dict:
            return TaskGroupsCollectionPage(self._prop_dict["taskGroups"])
        else:
            return None

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

