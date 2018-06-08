# -*- coding: utf-8 -*- 
'''
# Copyright (c) Microsoft Corporation.  All Rights Reserved.  Licensed under the MIT License.  See License in the project root for license information.
# 
#  This file was generated and any changes will be overwritten.
'''

from __future__ import unicode_literals
from ..model.targeted_managed_app_policy_assignment import TargetedManagedAppPolicyAssignment
from ..one_drive_object_base import OneDriveObjectBase


class TargetedManagedAppProtection(OneDriveObjectBase):

    def __init__(self, prop_dict={}):
        self._prop_dict = prop_dict

    @property
    def is_assigned(self):
        """
        Gets and sets the isAssigned
        
        Returns:
            bool:
                The isAssigned
        """
        if "isAssigned" in self._prop_dict:
            return self._prop_dict["isAssigned"]
        else:
            return None

    @is_assigned.setter
    def is_assigned(self, val):
        self._prop_dict["isAssigned"] = val

    @property
    def assignments(self):
        """Gets and sets the assignments
        
        Returns: 
            :class:`AssignmentsCollectionPage<onedrivesdk.request.assignments_collection.AssignmentsCollectionPage>`:
                The assignments
        """
        if "assignments" in self._prop_dict:
            return AssignmentsCollectionPage(self._prop_dict["assignments"])
        else:
            return None

