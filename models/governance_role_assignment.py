# -*- coding: utf-8 -*- 
'''
# Copyright (c) Microsoft Corporation.  All Rights Reserved.  Licensed under the MIT License.  See License in the project root for license information.
# 
#  This file was generated and any changes will be overwritten.
'''

from __future__ import unicode_literals
from ..model.governance_resource import GovernanceResource
from ..model.governance_role_definition import GovernanceRoleDefinition
from ..model.governance_subject import GovernanceSubject
from datetime import datetime
from ..one_drive_object_base import OneDriveObjectBase


class GovernanceRoleAssignment(OneDriveObjectBase):

    def __init__(self, prop_dict={}):
        self._prop_dict = prop_dict

    @property
    def resource_id(self):
        """
        Gets and sets the resourceId
        
        Returns:
            str:
                The resourceId
        """
        if "resourceId" in self._prop_dict:
            return self._prop_dict["resourceId"]
        else:
            return None

    @resource_id.setter
    def resource_id(self, val):
        self._prop_dict["resourceId"] = val

    @property
    def role_definition_id(self):
        """
        Gets and sets the roleDefinitionId
        
        Returns:
            str:
                The roleDefinitionId
        """
        if "roleDefinitionId" in self._prop_dict:
            return self._prop_dict["roleDefinitionId"]
        else:
            return None

    @role_definition_id.setter
    def role_definition_id(self, val):
        self._prop_dict["roleDefinitionId"] = val

    @property
    def subject_id(self):
        """
        Gets and sets the subjectId
        
        Returns:
            str:
                The subjectId
        """
        if "subjectId" in self._prop_dict:
            return self._prop_dict["subjectId"]
        else:
            return None

    @subject_id.setter
    def subject_id(self, val):
        self._prop_dict["subjectId"] = val

    @property
    def linked_eligible_role_assignment_id(self):
        """
        Gets and sets the linkedEligibleRoleAssignmentId
        
        Returns:
            str:
                The linkedEligibleRoleAssignmentId
        """
        if "linkedEligibleRoleAssignmentId" in self._prop_dict:
            return self._prop_dict["linkedEligibleRoleAssignmentId"]
        else:
            return None

    @linked_eligible_role_assignment_id.setter
    def linked_eligible_role_assignment_id(self, val):
        self._prop_dict["linkedEligibleRoleAssignmentId"] = val

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
    def is_permanent(self):
        """
        Gets and sets the isPermanent
        
        Returns:
            bool:
                The isPermanent
        """
        if "isPermanent" in self._prop_dict:
            return self._prop_dict["isPermanent"]
        else:
            return None

    @is_permanent.setter
    def is_permanent(self, val):
        self._prop_dict["isPermanent"] = val

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
    def end_date_time(self):
        """
        Gets and sets the endDateTime
        
        Returns:
            datetime:
                The endDateTime
        """
        if "endDateTime" in self._prop_dict:
            return datetime.strptime(self._prop_dict["endDateTime"].replace("Z", ""), "%Y-%m-%dT%H:%M:%S.%f")
        else:
            return None

    @end_date_time.setter
    def end_date_time(self, val):
        self._prop_dict["endDateTime"] = val.isoformat()+"Z"

    @property
    def member_type(self):
        """
        Gets and sets the memberType
        
        Returns:
            str:
                The memberType
        """
        if "memberType" in self._prop_dict:
            return self._prop_dict["memberType"]
        else:
            return None

    @member_type.setter
    def member_type(self, val):
        self._prop_dict["memberType"] = val

    @property
    def assignment_state(self):
        """
        Gets and sets the assignmentState
        
        Returns:
            str:
                The assignmentState
        """
        if "assignmentState" in self._prop_dict:
            return self._prop_dict["assignmentState"]
        else:
            return None

    @assignment_state.setter
    def assignment_state(self, val):
        self._prop_dict["assignmentState"] = val

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
    def resource(self):
        """
        Gets and sets the resource
        
        Returns: 
            :class:`GovernanceResource<onedrivesdk.model.governance_resource.GovernanceResource>`:
                The resource
        """
        if "resource" in self._prop_dict:
            if isinstance(self._prop_dict["resource"], OneDriveObjectBase):
                return self._prop_dict["resource"]
            else :
                self._prop_dict["resource"] = GovernanceResource(self._prop_dict["resource"])
                return self._prop_dict["resource"]

        return None

    @resource.setter
    def resource(self, val):
        self._prop_dict["resource"] = val

    @property
    def role_definition(self):
        """
        Gets and sets the roleDefinition
        
        Returns: 
            :class:`GovernanceRoleDefinition<onedrivesdk.model.governance_role_definition.GovernanceRoleDefinition>`:
                The roleDefinition
        """
        if "roleDefinition" in self._prop_dict:
            if isinstance(self._prop_dict["roleDefinition"], OneDriveObjectBase):
                return self._prop_dict["roleDefinition"]
            else :
                self._prop_dict["roleDefinition"] = GovernanceRoleDefinition(self._prop_dict["roleDefinition"])
                return self._prop_dict["roleDefinition"]

        return None

    @role_definition.setter
    def role_definition(self, val):
        self._prop_dict["roleDefinition"] = val

    @property
    def subject(self):
        """
        Gets and sets the subject
        
        Returns: 
            :class:`GovernanceSubject<onedrivesdk.model.governance_subject.GovernanceSubject>`:
                The subject
        """
        if "subject" in self._prop_dict:
            if isinstance(self._prop_dict["subject"], OneDriveObjectBase):
                return self._prop_dict["subject"]
            else :
                self._prop_dict["subject"] = GovernanceSubject(self._prop_dict["subject"])
                return self._prop_dict["subject"]

        return None

    @subject.setter
    def subject(self, val):
        self._prop_dict["subject"] = val

    @property
    def linked_eligible_role_assignment(self):
        """
        Gets and sets the linkedEligibleRoleAssignment
        
        Returns: 
            :class:`GovernanceRoleAssignment<onedrivesdk.model.governance_role_assignment.GovernanceRoleAssignment>`:
                The linkedEligibleRoleAssignment
        """
        if "linkedEligibleRoleAssignment" in self._prop_dict:
            if isinstance(self._prop_dict["linkedEligibleRoleAssignment"], OneDriveObjectBase):
                return self._prop_dict["linkedEligibleRoleAssignment"]
            else :
                self._prop_dict["linkedEligibleRoleAssignment"] = GovernanceRoleAssignment(self._prop_dict["linkedEligibleRoleAssignment"])
                return self._prop_dict["linkedEligibleRoleAssignment"]

        return None

    @linked_eligible_role_assignment.setter
    def linked_eligible_role_assignment(self, val):
        self._prop_dict["linkedEligibleRoleAssignment"] = val

