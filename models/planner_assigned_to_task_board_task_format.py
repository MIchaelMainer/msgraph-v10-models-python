# -*- coding: utf-8 -*- 
'''
# Copyright (c) Microsoft Corporation.  All Rights Reserved.  Licensed under the MIT License.  See License in the project root for license information.
# 
#  This file was generated and any changes will be overwritten.
'''

from __future__ import unicode_literals
from ..model.planner_order_hints_by_assignee import PlannerOrderHintsByAssignee
from ..one_drive_object_base import OneDriveObjectBase


class PlannerAssignedToTaskBoardTaskFormat(OneDriveObjectBase):

    def __init__(self, prop_dict={}):
        self._prop_dict = prop_dict

    @property
    def unassigned_order_hint(self):
        """
        Gets and sets the unassignedOrderHint
        
        Returns:
            str:
                The unassignedOrderHint
        """
        if "unassignedOrderHint" in self._prop_dict:
            return self._prop_dict["unassignedOrderHint"]
        else:
            return None

    @unassigned_order_hint.setter
    def unassigned_order_hint(self, val):
        self._prop_dict["unassignedOrderHint"] = val

    @property
    def order_hints_by_assignee(self):
        """
        Gets and sets the orderHintsByAssignee
        
        Returns: 
            :class:`PlannerOrderHintsByAssignee<onedrivesdk.model.planner_order_hints_by_assignee.PlannerOrderHintsByAssignee>`:
                The orderHintsByAssignee
        """
        if "orderHintsByAssignee" in self._prop_dict:
            if isinstance(self._prop_dict["orderHintsByAssignee"], OneDriveObjectBase):
                return self._prop_dict["orderHintsByAssignee"]
            else :
                self._prop_dict["orderHintsByAssignee"] = PlannerOrderHintsByAssignee(self._prop_dict["orderHintsByAssignee"])
                return self._prop_dict["orderHintsByAssignee"]

        return None

    @order_hints_by_assignee.setter
    def order_hints_by_assignee(self, val):
        self._prop_dict["orderHintsByAssignee"] = val

