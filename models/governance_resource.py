# -*- coding: utf-8 -*- 
'''
# Copyright (c) Microsoft Corporation.  All Rights Reserved.  Licensed under the MIT License.  See License in the project root for license information.
# 
#  This file was generated and any changes will be overwritten.
'''

from __future__ import unicode_literals
from ..model.governance_role_definition import GovernanceRoleDefinition
from ..model.governance_role_assignment import GovernanceRoleAssignment
from ..model.governance_role_assignment_request import GovernanceRoleAssignmentRequest
from ..model.governance_role_setting import GovernanceRoleSetting
from datetime import datetime
from ..one_drive_object_base import OneDriveObjectBase


class GovernanceResource(OneDriveObjectBase):

    def __init__(self, prop_dict={}):
        self._prop_dict = prop_dict

    @property
    def external_id(self):
        """
        Gets and sets the externalId
        
        Returns:
            str:
                The externalId
        """
        if "externalId" in self._prop_dict:
            return self._prop_dict["externalId"]
        else:
            return None

    @external_id.setter
    def external_id(self, val):
        self._prop_dict["externalId"] = val

    @property
    def type(self):
        """
        Gets and sets the type
        
        Returns:
            str:
                The type
        """
        if "type" in self._prop_dict:
            return self._prop_dict["type"]
        else:
            return None

    @type.setter
    def type(self, val):
        self._prop_dict["type"] = val

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
    def status(self):
        """
        Gets and sets the status
        
        Returns:
            str:
                The status
        """
        if "status" in self._prop_dict:
            return self._prop_dict["status"]
        else:
            return None

    @status.setter
    def status(self, val):
        self._prop_dict["status"] = val

    @property
    def onboard_date_time(self):
        """
        Gets and sets the onboardDateTime
        
        Returns:
            datetime:
                The onboardDateTime
        """
        if "onboardDateTime" in self._prop_dict:
            return datetime.strptime(self._prop_dict["onboardDateTime"].replace("Z", ""), "%Y-%m-%dT%H:%M:%S.%f")
        else:
            return None

    @onboard_date_time.setter
    def onboard_date_time(self, val):
        self._prop_dict["onboardDateTime"] = val.isoformat()+"Z"

    @property
    def parent(self):
        """
        Gets and sets the parent
        
        Returns: 
            :class:`GovernanceResource<onedrivesdk.model.governance_resource.GovernanceResource>`:
                The parent
        """
        if "parent" in self._prop_dict:
            if isinstance(self._prop_dict["parent"], OneDriveObjectBase):
                return self._prop_dict["parent"]
            else :
                self._prop_dict["parent"] = GovernanceResource(self._prop_dict["parent"])
                return self._prop_dict["parent"]

        return None

    @parent.setter
    def parent(self, val):
        self._prop_dict["parent"] = val

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

