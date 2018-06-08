# -*- coding: utf-8 -*- 
'''
# Copyright (c) Microsoft Corporation.  All Rights Reserved.  Licensed under the MIT License.  See License in the project root for license information.
# 
#  This file was generated and any changes will be overwritten.
'''

from __future__ import unicode_literals
from ..model.identity_set import IdentitySet
from ..model.planner_plan_context_collection import PlannerPlanContextCollection
from ..model.planner_task import PlannerTask
from ..model.planner_bucket import PlannerBucket
from ..model.planner_plan_details import PlannerPlanDetails
from datetime import datetime
from ..one_drive_object_base import OneDriveObjectBase


class PlannerPlan(OneDriveObjectBase):

    def __init__(self, prop_dict={}):
        self._prop_dict = prop_dict

    @property
    def created_by(self):
        """
        Gets and sets the createdBy
        
        Returns: 
            :class:`IdentitySet<onedrivesdk.model.identity_set.IdentitySet>`:
                The createdBy
        """
        if "createdBy" in self._prop_dict:
            if isinstance(self._prop_dict["createdBy"], OneDriveObjectBase):
                return self._prop_dict["createdBy"]
            else :
                self._prop_dict["createdBy"] = IdentitySet(self._prop_dict["createdBy"])
                return self._prop_dict["createdBy"]

        return None

    @created_by.setter
    def created_by(self, val):
        self._prop_dict["createdBy"] = val

    @property
    def created_date_time(self):
        """
        Gets and sets the createdDateTime
        
        Returns:
            datetime:
                The createdDateTime
        """
        if "createdDateTime" in self._prop_dict:
            return datetime.strptime(self._prop_dict["createdDateTime"].replace("Z", ""), "%Y-%m-%dT%H:%M:%S.%f")
        else:
            return None

    @created_date_time.setter
    def created_date_time(self, val):
        self._prop_dict["createdDateTime"] = val.isoformat()+"Z"

    @property
    def owner(self):
        """
        Gets and sets the owner
        
        Returns:
            str:
                The owner
        """
        if "owner" in self._prop_dict:
            return self._prop_dict["owner"]
        else:
            return None

    @owner.setter
    def owner(self, val):
        self._prop_dict["owner"] = val

    @property
    def title(self):
        """
        Gets and sets the title
        
        Returns:
            str:
                The title
        """
        if "title" in self._prop_dict:
            return self._prop_dict["title"]
        else:
            return None

    @title.setter
    def title(self, val):
        self._prop_dict["title"] = val

    @property
    def contexts(self):
        """
        Gets and sets the contexts
        
        Returns: 
            :class:`PlannerPlanContextCollection<onedrivesdk.model.planner_plan_context_collection.PlannerPlanContextCollection>`:
                The contexts
        """
        if "contexts" in self._prop_dict:
            if isinstance(self._prop_dict["contexts"], OneDriveObjectBase):
                return self._prop_dict["contexts"]
            else :
                self._prop_dict["contexts"] = PlannerPlanContextCollection(self._prop_dict["contexts"])
                return self._prop_dict["contexts"]

        return None

    @contexts.setter
    def contexts(self, val):
        self._prop_dict["contexts"] = val

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
    def buckets(self):
        """Gets and sets the buckets
        
        Returns: 
            :class:`BucketsCollectionPage<onedrivesdk.request.buckets_collection.BucketsCollectionPage>`:
                The buckets
        """
        if "buckets" in self._prop_dict:
            return BucketsCollectionPage(self._prop_dict["buckets"])
        else:
            return None

    @property
    def details(self):
        """
        Gets and sets the details
        
        Returns: 
            :class:`PlannerPlanDetails<onedrivesdk.model.planner_plan_details.PlannerPlanDetails>`:
                The details
        """
        if "details" in self._prop_dict:
            if isinstance(self._prop_dict["details"], OneDriveObjectBase):
                return self._prop_dict["details"]
            else :
                self._prop_dict["details"] = PlannerPlanDetails(self._prop_dict["details"])
                return self._prop_dict["details"]

        return None

    @details.setter
    def details(self, val):
        self._prop_dict["details"] = val

