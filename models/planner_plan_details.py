# -*- coding: utf-8 -*- 
'''
# Copyright (c) Microsoft Corporation.  All Rights Reserved.  Licensed under the MIT License.  See License in the project root for license information.
# 
#  This file was generated and any changes will be overwritten.
'''

from __future__ import unicode_literals
from ..model.planner_user_ids import PlannerUserIds
from ..model.planner_category_descriptions import PlannerCategoryDescriptions
from ..one_drive_object_base import OneDriveObjectBase


class PlannerPlanDetails(OneDriveObjectBase):

    def __init__(self, prop_dict={}):
        self._prop_dict = prop_dict

    @property
    def shared_with(self):
        """
        Gets and sets the sharedWith
        
        Returns: 
            :class:`PlannerUserIds<onedrivesdk.model.planner_user_ids.PlannerUserIds>`:
                The sharedWith
        """
        if "sharedWith" in self._prop_dict:
            if isinstance(self._prop_dict["sharedWith"], OneDriveObjectBase):
                return self._prop_dict["sharedWith"]
            else :
                self._prop_dict["sharedWith"] = PlannerUserIds(self._prop_dict["sharedWith"])
                return self._prop_dict["sharedWith"]

        return None

    @shared_with.setter
    def shared_with(self, val):
        self._prop_dict["sharedWith"] = val

    @property
    def category_descriptions(self):
        """
        Gets and sets the categoryDescriptions
        
        Returns: 
            :class:`PlannerCategoryDescriptions<onedrivesdk.model.planner_category_descriptions.PlannerCategoryDescriptions>`:
                The categoryDescriptions
        """
        if "categoryDescriptions" in self._prop_dict:
            if isinstance(self._prop_dict["categoryDescriptions"], OneDriveObjectBase):
                return self._prop_dict["categoryDescriptions"]
            else :
                self._prop_dict["categoryDescriptions"] = PlannerCategoryDescriptions(self._prop_dict["categoryDescriptions"])
                return self._prop_dict["categoryDescriptions"]

        return None

    @category_descriptions.setter
    def category_descriptions(self, val):
        self._prop_dict["categoryDescriptions"] = val

