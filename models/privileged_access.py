# -*- coding: utf-8 -*- 
'''
# Copyright (c) Microsoft Corporation.  All Rights Reserved.  Licensed under the MIT License.  See License in the project root for license information.
# 
#  This file was generated and any changes will be overwritten.
'''

from __future__ import unicode_literals
from ..model.governance_resource import GovernanceResource
from ..model.governance_role_definition import GovernanceRoleDefinition
from ..model.governance_role_assignment import GovernanceRoleAssignment
from ..model.governance_role_assignment_request import GovernanceRoleAssignmentRequest
from ..model.governance_role_setting import GovernanceRoleSetting
from ..one_drive_object_base import OneDriveObjectBase


class PrivilegedAccess(OneDriveObjectBase):

    def __init__(self, prop_dict={}):
        self._prop_dict = prop_dict

    @property
    def display_name(self):
        """
        Gets and sets the displayName
        
        Returns:
            str:
                The displayName
        """
        if "displayName" in self._prop_dict:
            return self._prop_dict["displayName"]
        else:
            return None

    @display_name.setter
    def display_name(self, val):
        self._prop_dict["displayName"] = val

    @property
    def resources(self):
        """Gets and sets the resources
        
        Returns: 
            :class:`ResourcesCollectionPage<onedrivesdk.request.resources_collection.ResourcesCollectionPage>`:
                The resources
        """
        if "resources" in self._prop_dict:
            return ResourcesCollectionPage(self._prop_dict["resources"])
        else:
            return None

    @property
    def role_definitions(self):
        """Gets and sets the roleDefinitions
        
        Returns: 
            :class:`RoleDefinitionsCollectionPage<onedrivesdk.request.role_definitions_collection.RoleDefinitionsCollectionPage>`:
                The roleDefinitions
        """
        if "roleDefinitions" in self._prop_dict:
            return RoleDefinitionsCollectionPage(self._prop_dict["roleDefinitions"])
        else:
            return None

    @property
    def role_assignments(self):
        """Gets and sets the roleAssignments
        
        Returns: 
            :class:`RoleAssignmentsCollectionPage<onedrivesdk.request.role_assignments_collection.RoleAssignmentsCollectionPage>`:
                The roleAssignments
        """
        if "roleAssignments" in self._prop_dict:
            return RoleAssignmentsCollectionPage(self._prop_dict["roleAssignments"])
        else:
            return None

    @property
    def role_assignment_requests(self):
        """Gets and sets the roleAssignmentRequests
        
        Returns: 
            :class:`RoleAssignmentRequestsCollectionPage<onedrivesdk.request.role_assignment_requests_collection.RoleAssignmentRequestsCollectionPage>`:
                The roleAssignmentRequests
        """
        if "roleAssignmentRequests" in self._prop_dict:
            return RoleAssignmentRequestsCollectionPage(self._prop_dict["roleAssignmentRequests"])
        else:
            return None

    @property
    def role_settings(self):
        """Gets and sets the roleSettings
        
        Returns: 
            :class:`RoleSettingsCollectionPage<onedrivesdk.request.role_settings_collection.RoleSettingsCollectionPage>`:
                The roleSettings
        """
        if "roleSettings" in self._prop_dict:
            return RoleSettingsCollectionPage(self._prop_dict["roleSettings"])
        else:
            return None

