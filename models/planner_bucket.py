# -*- coding: utf-8 -*- 
'''
# Copyright (c) Microsoft Corporation.  All Rights Reserved.  Licensed under the MIT License.  See License in the project root for license information.
# 
#  This file was generated and any changes will be overwritten.
'''

from __future__ import unicode_literals
from ..model.planner_task import PlannerTask
from ..one_drive_object_base import OneDriveObjectBase


class PlannerBucket(OneDriveObjectBase):

    def __init__(self, prop_dict={}):
        self._prop_dict = prop_dict

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
    def plan_id(self):
        """
        Gets and sets the planId
        
        Returns:
            str:
                The planId
        """
        if "planId" in self._prop_dict:
            return self._prop_dict["planId"]
        else:
            return None

    @plan_id.setter
    def plan_id(self, val):
        self._prop_dict["planId"] = val

    @property
    def order_hint(self):
        """
        Gets and sets the orderHint
        
        Returns:
            str:
                The orderHint
        """
        if "orderHint" in self._prop_dict:
            return self._prop_dict["orderHint"]
        else:
            return None

    @order_hint.setter
    def order_hint(self, val):
        self._prop_dict["orderHint"] = val

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

