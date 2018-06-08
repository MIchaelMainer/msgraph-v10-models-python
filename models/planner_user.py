# -*- coding: utf-8 -*- 
'''
# Copyright (c) Microsoft Corporation.  All Rights Reserved.  Licensed under the MIT License.  See License in the project root for license information.
# 
#  This file was generated and any changes will be overwritten.
'''

from __future__ import unicode_literals
from ..model.planner_favorite_plan_reference_collection import PlannerFavoritePlanReferenceCollection
from ..model.planner_recent_plan_reference_collection import PlannerRecentPlanReferenceCollection
from ..model.planner_task import PlannerTask
from ..model.planner_plan import PlannerPlan
from ..model.planner_delta import PlannerDelta
from ..one_drive_object_base import OneDriveObjectBase


class PlannerUser(OneDriveObjectBase):

    def __init__(self, prop_dict={}):
        self._prop_dict = prop_dict

    @property
    def favorite_plan_references(self):
        """
        Gets and sets the favoritePlanReferences
        
        Returns: 
            :class:`PlannerFavoritePlanReferenceCollection<onedrivesdk.model.planner_favorite_plan_reference_collection.PlannerFavoritePlanReferenceCollection>`:
                The favoritePlanReferences
        """
        if "favoritePlanReferences" in self._prop_dict:
            if isinstance(self._prop_dict["favoritePlanReferences"], OneDriveObjectBase):
                return self._prop_dict["favoritePlanReferences"]
            else :
                self._prop_dict["favoritePlanReferences"] = PlannerFavoritePlanReferenceCollection(self._prop_dict["favoritePlanReferences"])
                return self._prop_dict["favoritePlanReferences"]

        return None

    @favorite_plan_references.setter
    def favorite_plan_references(self, val):
        self._prop_dict["favoritePlanReferences"] = val

    @property
    def recent_plan_references(self):
        """
        Gets and sets the recentPlanReferences
        
        Returns: 
            :class:`PlannerRecentPlanReferenceCollection<onedrivesdk.model.planner_recent_plan_reference_collection.PlannerRecentPlanReferenceCollection>`:
                The recentPlanReferences
        """
        if "recentPlanReferences" in self._prop_dict:
            if isinstance(self._prop_dict["recentPlanReferences"], OneDriveObjectBase):
                return self._prop_dict["recentPlanReferences"]
            else :
                self._prop_dict["recentPlanReferences"] = PlannerRecentPlanReferenceCollection(self._prop_dict["recentPlanReferences"])
                return self._prop_dict["recentPlanReferences"]

        return None

    @recent_plan_references.setter
    def recent_plan_references(self, val):
        self._prop_dict["recentPlanReferences"] = val

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
    def plans(self):
        """Gets and sets the plans
        
        Returns: 
            :class:`PlansCollectionPage<onedrivesdk.request.plans_collection.PlansCollectionPage>`:
                The plans
        """
        if "plans" in self._prop_dict:
            return PlansCollectionPage(self._prop_dict["plans"])
        else:
            return None

    @property
    def favorite_plans(self):
        """Gets and sets the favoritePlans
        
        Returns: 
            :class:`FavoritePlansCollectionPage<onedrivesdk.request.favorite_plans_collection.FavoritePlansCollectionPage>`:
                The favoritePlans
        """
        if "favoritePlans" in self._prop_dict:
            return FavoritePlansCollectionPage(self._prop_dict["favoritePlans"])
        else:
            return None

    @property
    def recent_plans(self):
        """Gets and sets the recentPlans
        
        Returns: 
            :class:`RecentPlansCollectionPage<onedrivesdk.request.recent_plans_collection.RecentPlansCollectionPage>`:
                The recentPlans
        """
        if "recentPlans" in self._prop_dict:
            return RecentPlansCollectionPage(self._prop_dict["recentPlans"])
        else:
            return None

    @property
    def all(self):
        """Gets and sets the all
        
        Returns: 
            :class:`AllCollectionPage<onedrivesdk.request.all_collection.AllCollectionPage>`:
                The all
        """
        if "all" in self._prop_dict:
            return AllCollectionPage(self._prop_dict["all"])
        else:
            return None

