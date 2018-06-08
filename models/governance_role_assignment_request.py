# -*- coding: utf-8 -*- 
'''
# Copyright (c) Microsoft Corporation.  All Rights Reserved.  Licensed under the MIT License.  See License in the project root for license information.
# 
#  This file was generated and any changes will be overwritten.
'''

from __future__ import unicode_literals
from ..model.governance_role_assignment_request_status import GovernanceRoleAssignmentRequestStatus
from ..model.governance_schedule import GovernanceSchedule
from ..model.governance_resource import GovernanceResource
from ..model.governance_role_definition import GovernanceRoleDefinition
from ..model.governance_subject import GovernanceSubject
from datetime import datetime
from ..one_drive_object_base import OneDriveObjectBase


class GovernanceRoleAssignmentRequest(OneDriveObjectBase):

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
    def requested_date_time(self):
        """
        Gets and sets the requestedDateTime
        
        Returns:
            datetime:
                The requestedDateTime
        """
        if "requestedDateTime" in self._prop_dict:
            return datetime.strptime(self._prop_dict["requestedDateTime"].replace("Z", ""), "%Y-%m-%dT%H:%M:%S.%f")
        else:
            return None

    @requested_date_time.setter
    def requested_date_time(self, val):
        self._prop_dict["requestedDateTime"] = val.isoformat()+"Z"

    @property
    def role_assignment_start_date_time(self):
        """
        Gets and sets the roleAssignmentStartDateTime
        
        Returns:
            datetime:
                The roleAssignmentStartDateTime
        """
        if "roleAssignmentStartDateTime" in self._prop_dict:
            return datetime.strptime(self._prop_dict["roleAssignmentStartDateTime"].replace("Z", ""), "%Y-%m-%dT%H:%M:%S.%f")
        else:
            return None

    @role_assignment_start_date_time.setter
    def role_assignment_start_date_time(self, val):
        self._prop_dict["roleAssignmentStartDateTime"] = val.isoformat()+"Z"

    @property
    def role_assignment_end_date_time(self):
        """
        Gets and sets the roleAssignmentEndDateTime
        
        Returns:
            datetime:
                The roleAssignmentEndDateTime
        """
        if "roleAssignmentEndDateTime" in self._prop_dict:
            return datetime.strptime(self._prop_dict["roleAssignmentEndDateTime"].replace("Z", ""), "%Y-%m-%dT%H:%M:%S.%f")
        else:
            return None

    @role_assignment_end_date_time.setter
    def role_assignment_end_date_time(self, val):
        self._prop_dict["roleAssignmentEndDateTime"] = val.isoformat()+"Z"

    @property
    def reason(self):
        """
        Gets and sets the reason
        
        Returns:
            str:
                The reason
        """
        if "reason" in self._prop_dict:
            return self._prop_dict["reason"]
        else:
            return None

    @reason.setter
    def reason(self, val):
        self._prop_dict["reason"] = val

    @property
    def status(self):
        """
        Gets and sets the status
        
        Returns: 
            :class:`GovernanceRoleAssignmentRequestStatus<onedrivesdk.model.governance_role_assignment_request_status.GovernanceRoleAssignmentRequestStatus>`:
                The status
        """
        if "status" in self._prop_dict:
            if isinstance(self._prop_dict["status"], OneDriveObjectBase):
                return self._prop_dict["status"]
            else :
                self._prop_dict["status"] = GovernanceRoleAssignmentRequestStatus(self._prop_dict["status"])
                return self._prop_dict["status"]

        return None

    @status.setter
    def status(self, val):
        self._prop_dict["status"] = val

    @property
    def schedule(self):
        """
        Gets and sets the schedule
        
        Returns: 
            :class:`GovernanceSchedule<onedrivesdk.model.governance_schedule.GovernanceSchedule>`:
                The schedule
        """
        if "schedule" in self._prop_dict:
            if isinstance(self._prop_dict["schedule"], OneDriveObjectBase):
                return self._prop_dict["schedule"]
            else :
                self._prop_dict["schedule"] = GovernanceSchedule(self._prop_dict["schedule"])
                return self._prop_dict["schedule"]

        return None

    @schedule.setter
    def schedule(self, val):
        self._prop_dict["schedule"] = val

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

