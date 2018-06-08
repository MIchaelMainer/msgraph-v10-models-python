# -*- coding: utf-8 -*- 
'''
# Copyright (c) Microsoft Corporation.  All Rights Reserved.  Licensed under the MIT License.  See License in the project root for license information.
# 
#  This file was generated and any changes will be overwritten.
'''

from __future__ import unicode_literals
from ..model.planner_plan import PlannerPlan
from ..one_drive_object_base import OneDriveObjectBase


class PlannerGroup(OneDriveObjectBase):

    def __init__(self, prop_dict={}):
        self._prop_dict = prop_dict

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

