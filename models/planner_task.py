# -*- coding: utf-8 -*- 
'''
# Copyright (c) Microsoft Corporation.  All Rights Reserved.  Licensed under the MIT License.  See License in the project root for license information.
# 
#  This file was generated and any changes will be overwritten.
'''

from __future__ import unicode_literals
from ..model.identity_set import IdentitySet
from ..model.planner_preview_type import PlannerPreviewType
from ..model.planner_applied_categories import PlannerAppliedCategories
from ..model.planner_assignments import PlannerAssignments
from ..model.planner_task_details import PlannerTaskDetails
from ..model.planner_assigned_to_task_board_task_format import PlannerAssignedToTaskBoardTaskFormat
from ..model.planner_progress_task_board_task_format import PlannerProgressTaskBoardTaskFormat
from ..model.planner_bucket_task_board_task_format import PlannerBucketTaskBoardTaskFormat
from datetime import datetime
from ..one_drive_object_base import OneDriveObjectBase


class PlannerTask(OneDriveObjectBase):

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
    def bucket_id(self):
        """
        Gets and sets the bucketId
        
        Returns:
            str:
                The bucketId
        """
        if "bucketId" in self._prop_dict:
            return self._prop_dict["bucketId"]
        else:
            return None

    @bucket_id.setter
    def bucket_id(self, val):
        self._prop_dict["bucketId"] = val

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
    def assignee_priority(self):
        """
        Gets and sets the assigneePriority
        
        Returns:
            str:
                The assigneePriority
        """
        if "assigneePriority" in self._prop_dict:
            return self._prop_dict["assigneePriority"]
        else:
            return None

    @assignee_priority.setter
    def assignee_priority(self, val):
        self._prop_dict["assigneePriority"] = val

    @property
    def percent_complete(self):
        """
        Gets and sets the percentComplete
        
        Returns:
            int:
                The percentComplete
        """
        if "percentComplete" in self._prop_dict:
            return self._prop_dict["percentComplete"]
        else:
            return None

    @percent_complete.setter
    def percent_complete(self, val):
        self._prop_dict["percentComplete"] = val

    @property
    def start_date_time(self):
        """
        Gets and sets the startDateTime
        
        Returns:
            datetime:
                The startDateTime
        """
        if "startDateTime" in self._prop_dict:
            return datetime.strptime(self._prop_dict["startDateTime"].replace("Z", ""), "%Y-%m-%dT%H:%M:%S.%f")
        else:
            return None

    @start_date_time.setter
    def start_date_time(self, val):
        self._prop_dict["startDateTime"] = val.isoformat()+"Z"

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
    def due_date_time(self):
        """
        Gets and sets the dueDateTime
        
        Returns:
            datetime:
                The dueDateTime
        """
        if "dueDateTime" in self._prop_dict:
            return datetime.strptime(self._prop_dict["dueDateTime"].replace("Z", ""), "%Y-%m-%dT%H:%M:%S.%f")
        else:
            return None

    @due_date_time.setter
    def due_date_time(self, val):
        self._prop_dict["dueDateTime"] = val.isoformat()+"Z"

    @property
    def has_description(self):
        """
        Gets and sets the hasDescription
        
        Returns:
            bool:
                The hasDescription
        """
        if "hasDescription" in self._prop_dict:
            return self._prop_dict["hasDescription"]
        else:
            return None

    @has_description.setter
    def has_description(self, val):
        self._prop_dict["hasDescription"] = val

    @property
    def preview_type(self):
        """
        Gets and sets the previewType
        
        Returns: 
            :class:`PlannerPreviewType<onedrivesdk.model.planner_preview_type.PlannerPreviewType>`:
                The previewType
        """
        if "previewType" in self._prop_dict:
            if isinstance(self._prop_dict["previewType"], OneDriveObjectBase):
                return self._prop_dict["previewType"]
            else :
                self._prop_dict["previewType"] = PlannerPreviewType(self._prop_dict["previewType"])
                return self._prop_dict["previewType"]

        return None

    @preview_type.setter
    def preview_type(self, val):
        self._prop_dict["previewType"] = val

    @property
    def completed_date_time(self):
        """
        Gets and sets the completedDateTime
        
        Returns:
            datetime:
                The completedDateTime
        """
        if "completedDateTime" in self._prop_dict:
            return datetime.strptime(self._prop_dict["completedDateTime"].replace("Z", ""), "%Y-%m-%dT%H:%M:%S.%f")
        else:
            return None

    @completed_date_time.setter
    def completed_date_time(self, val):
        self._prop_dict["completedDateTime"] = val.isoformat()+"Z"

    @property
    def completed_by(self):
        """
        Gets and sets the completedBy
        
        Returns: 
            :class:`IdentitySet<onedrivesdk.model.identity_set.IdentitySet>`:
                The completedBy
        """
        if "completedBy" in self._prop_dict:
            if isinstance(self._prop_dict["completedBy"], OneDriveObjectBase):
                return self._prop_dict["completedBy"]
            else :
                self._prop_dict["completedBy"] = IdentitySet(self._prop_dict["completedBy"])
                return self._prop_dict["completedBy"]

        return None

    @completed_by.setter
    def completed_by(self, val):
        self._prop_dict["completedBy"] = val

    @property
    def reference_count(self):
        """
        Gets and sets the referenceCount
        
        Returns:
            int:
                The referenceCount
        """
        if "referenceCount" in self._prop_dict:
            return self._prop_dict["referenceCount"]
        else:
            return None

    @reference_count.setter
    def reference_count(self, val):
        self._prop_dict["referenceCount"] = val

    @property
    def checklist_item_count(self):
        """
        Gets and sets the checklistItemCount
        
        Returns:
            int:
                The checklistItemCount
        """
        if "checklistItemCount" in self._prop_dict:
            return self._prop_dict["checklistItemCount"]
        else:
            return None

    @checklist_item_count.setter
    def checklist_item_count(self, val):
        self._prop_dict["checklistItemCount"] = val

    @property
    def active_checklist_item_count(self):
        """
        Gets and sets the activeChecklistItemCount
        
        Returns:
            int:
                The activeChecklistItemCount
        """
        if "activeChecklistItemCount" in self._prop_dict:
            return self._prop_dict["activeChecklistItemCount"]
        else:
            return None

    @active_checklist_item_count.setter
    def active_checklist_item_count(self, val):
        self._prop_dict["activeChecklistItemCount"] = val

    @property
    def applied_categories(self):
        """
        Gets and sets the appliedCategories
        
        Returns: 
            :class:`PlannerAppliedCategories<onedrivesdk.model.planner_applied_categories.PlannerAppliedCategories>`:
                The appliedCategories
        """
        if "appliedCategories" in self._prop_dict:
            if isinstance(self._prop_dict["appliedCategories"], OneDriveObjectBase):
                return self._prop_dict["appliedCategories"]
            else :
                self._prop_dict["appliedCategories"] = PlannerAppliedCategories(self._prop_dict["appliedCategories"])
                return self._prop_dict["appliedCategories"]

        return None

    @applied_categories.setter
    def applied_categories(self, val):
        self._prop_dict["appliedCategories"] = val

    @property
    def assignments(self):
        """
        Gets and sets the assignments
        
        Returns: 
            :class:`PlannerAssignments<onedrivesdk.model.planner_assignments.PlannerAssignments>`:
                The assignments
        """
        if "assignments" in self._prop_dict:
            if isinstance(self._prop_dict["assignments"], OneDriveObjectBase):
                return self._prop_dict["assignments"]
            else :
                self._prop_dict["assignments"] = PlannerAssignments(self._prop_dict["assignments"])
                return self._prop_dict["assignments"]

        return None

    @assignments.setter
    def assignments(self, val):
        self._prop_dict["assignments"] = val

    @property
    def conversation_thread_id(self):
        """
        Gets and sets the conversationThreadId
        
        Returns:
            str:
                The conversationThreadId
        """
        if "conversationThreadId" in self._prop_dict:
            return self._prop_dict["conversationThreadId"]
        else:
            return None

    @conversation_thread_id.setter
    def conversation_thread_id(self, val):
        self._prop_dict["conversationThreadId"] = val

    @property
    def details(self):
        """
        Gets and sets the details
        
        Returns: 
            :class:`PlannerTaskDetails<onedrivesdk.model.planner_task_details.PlannerTaskDetails>`:
                The details
        """
        if "details" in self._prop_dict:
            if isinstance(self._prop_dict["details"], OneDriveObjectBase):
                return self._prop_dict["details"]
            else :
                self._prop_dict["details"] = PlannerTaskDetails(self._prop_dict["details"])
                return self._prop_dict["details"]

        return None

    @details.setter
    def details(self, val):
        self._prop_dict["details"] = val

    @property
    def assigned_to_task_board_format(self):
        """
        Gets and sets the assignedToTaskBoardFormat
        
        Returns: 
            :class:`PlannerAssignedToTaskBoardTaskFormat<onedrivesdk.model.planner_assigned_to_task_board_task_format.PlannerAssignedToTaskBoardTaskFormat>`:
                The assignedToTaskBoardFormat
        """
        if "assignedToTaskBoardFormat" in self._prop_dict:
            if isinstance(self._prop_dict["assignedToTaskBoardFormat"], OneDriveObjectBase):
                return self._prop_dict["assignedToTaskBoardFormat"]
            else :
                self._prop_dict["assignedToTaskBoardFormat"] = PlannerAssignedToTaskBoardTaskFormat(self._prop_dict["assignedToTaskBoardFormat"])
                return self._prop_dict["assignedToTaskBoardFormat"]

        return None

    @assigned_to_task_board_format.setter
    def assigned_to_task_board_format(self, val):
        self._prop_dict["assignedToTaskBoardFormat"] = val

    @property
    def progress_task_board_format(self):
        """
        Gets and sets the progressTaskBoardFormat
        
        Returns: 
            :class:`PlannerProgressTaskBoardTaskFormat<onedrivesdk.model.planner_progress_task_board_task_format.PlannerProgressTaskBoardTaskFormat>`:
                The progressTaskBoardFormat
        """
        if "progressTaskBoardFormat" in self._prop_dict:
            if isinstance(self._prop_dict["progressTaskBoardFormat"], OneDriveObjectBase):
                return self._prop_dict["progressTaskBoardFormat"]
            else :
                self._prop_dict["progressTaskBoardFormat"] = PlannerProgressTaskBoardTaskFormat(self._prop_dict["progressTaskBoardFormat"])
                return self._prop_dict["progressTaskBoardFormat"]

        return None

    @progress_task_board_format.setter
    def progress_task_board_format(self, val):
        self._prop_dict["progressTaskBoardFormat"] = val

    @property
    def bucket_task_board_format(self):
        """
        Gets and sets the bucketTaskBoardFormat
        
        Returns: 
            :class:`PlannerBucketTaskBoardTaskFormat<onedrivesdk.model.planner_bucket_task_board_task_format.PlannerBucketTaskBoardTaskFormat>`:
                The bucketTaskBoardFormat
        """
        if "bucketTaskBoardFormat" in self._prop_dict:
            if isinstance(self._prop_dict["bucketTaskBoardFormat"], OneDriveObjectBase):
                return self._prop_dict["bucketTaskBoardFormat"]
            else :
                self._prop_dict["bucketTaskBoardFormat"] = PlannerBucketTaskBoardTaskFormat(self._prop_dict["bucketTaskBoardFormat"])
                return self._prop_dict["bucketTaskBoardFormat"]

        return None

    @bucket_task_board_format.setter
    def bucket_task_board_format(self, val):
        self._prop_dict["bucketTaskBoardFormat"] = val

