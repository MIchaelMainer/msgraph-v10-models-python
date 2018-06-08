# -*- coding: utf-8 -*- 
'''
# Copyright (c) Microsoft Corporation.  All Rights Reserved.  Licensed under the MIT License.  See License in the project root for license information.
# 
#  This file was generated and any changes will be overwritten.
'''

from __future__ import unicode_literals
from ..model.planner_preview_type import PlannerPreviewType
from ..model.planner_external_references import PlannerExternalReferences
from ..model.planner_checklist_items import PlannerChecklistItems
from ..one_drive_object_base import OneDriveObjectBase


class PlannerTaskDetails(OneDriveObjectBase):

    def __init__(self, prop_dict={}):
        self._prop_dict = prop_dict

    @property
    def description(self):
        """
        Gets and sets the description
        
        Returns:
            str:
                The description
        """
        if "description" in self._prop_dict:
            return self._prop_dict["description"]
        else:
            return None

    @description.setter
    def description(self, val):
        self._prop_dict["description"] = val

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
    def references(self):
        """
        Gets and sets the references
        
        Returns: 
            :class:`PlannerExternalReferences<onedrivesdk.model.planner_external_references.PlannerExternalReferences>`:
                The references
        """
        if "references" in self._prop_dict:
            if isinstance(self._prop_dict["references"], OneDriveObjectBase):
                return self._prop_dict["references"]
            else :
                self._prop_dict["references"] = PlannerExternalReferences(self._prop_dict["references"])
                return self._prop_dict["references"]

        return None

    @references.setter
    def references(self, val):
        self._prop_dict["references"] = val

    @property
    def checklist(self):
        """
        Gets and sets the checklist
        
        Returns: 
            :class:`PlannerChecklistItems<onedrivesdk.model.planner_checklist_items.PlannerChecklistItems>`:
                The checklist
        """
        if "checklist" in self._prop_dict:
            if isinstance(self._prop_dict["checklist"], OneDriveObjectBase):
                return self._prop_dict["checklist"]
            else :
                self._prop_dict["checklist"] = PlannerChecklistItems(self._prop_dict["checklist"])
                return self._prop_dict["checklist"]

        return None

    @checklist.setter
    def checklist(self, val):
        self._prop_dict["checklist"] = val

