# -*- coding: utf-8 -*- 
'''
# Copyright (c) Microsoft Corporation.  All Rights Reserved.  Licensed under the MIT License.  See License in the project root for license information.
# 
#  This file was generated and any changes will be overwritten.
'''

from __future__ import unicode_literals
from ..model.education_item_body import EducationItemBody
from ..model.education_assignment_grade_type import EducationAssignmentGradeType
from ..model.education_assignment_recipient import EducationAssignmentRecipient
from ..model.identity_set import IdentitySet
from ..model.education_assignment_status import EducationAssignmentStatus
from ..model.education_assignment_resource import EducationAssignmentResource
from ..model.education_submission import EducationSubmission
from datetime import datetime
from ..one_drive_object_base import OneDriveObjectBase


class EducationAssignment(OneDriveObjectBase):

    def __init__(self, prop_dict={}):
        self._prop_dict = prop_dict

    @property
    def class_id(self):
        """
        Gets and sets the classId
        
        Returns:
            str:
                The classId
        """
        if "classId" in self._prop_dict:
            return self._prop_dict["classId"]
        else:
            return None

    @class_id.setter
    def class_id(self, val):
        self._prop_dict["classId"] = val

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
    def instructions(self):
        """
        Gets and sets the instructions
        
        Returns: 
            :class:`EducationItemBody<onedrivesdk.model.education_item_body.EducationItemBody>`:
                The instructions
        """
        if "instructions" in self._prop_dict:
            if isinstance(self._prop_dict["instructions"], OneDriveObjectBase):
                return self._prop_dict["instructions"]
            else :
                self._prop_dict["instructions"] = EducationItemBody(self._prop_dict["instructions"])
                return self._prop_dict["instructions"]

        return None

    @instructions.setter
    def instructions(self, val):
        self._prop_dict["instructions"] = val

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
    def assign_date_time(self):
        """
        Gets and sets the assignDateTime
        
        Returns:
            datetime:
                The assignDateTime
        """
        if "assignDateTime" in self._prop_dict:
            return datetime.strptime(self._prop_dict["assignDateTime"].replace("Z", ""), "%Y-%m-%dT%H:%M:%S.%f")
        else:
            return None

    @assign_date_time.setter
    def assign_date_time(self, val):
        self._prop_dict["assignDateTime"] = val.isoformat()+"Z"

    @property
    def assigned_date_time(self):
        """
        Gets and sets the assignedDateTime
        
        Returns:
            datetime:
                The assignedDateTime
        """
        if "assignedDateTime" in self._prop_dict:
            return datetime.strptime(self._prop_dict["assignedDateTime"].replace("Z", ""), "%Y-%m-%dT%H:%M:%S.%f")
        else:
            return None

    @assigned_date_time.setter
    def assigned_date_time(self, val):
        self._prop_dict["assignedDateTime"] = val.isoformat()+"Z"

    @property
    def grading(self):
        """
        Gets and sets the grading
        
        Returns: 
            :class:`EducationAssignmentGradeType<onedrivesdk.model.education_assignment_grade_type.EducationAssignmentGradeType>`:
                The grading
        """
        if "grading" in self._prop_dict:
            if isinstance(self._prop_dict["grading"], OneDriveObjectBase):
                return self._prop_dict["grading"]
            else :
                self._prop_dict["grading"] = EducationAssignmentGradeType(self._prop_dict["grading"])
                return self._prop_dict["grading"]

        return None

    @grading.setter
    def grading(self, val):
        self._prop_dict["grading"] = val

    @property
    def assign_to(self):
        """
        Gets and sets the assignTo
        
        Returns: 
            :class:`EducationAssignmentRecipient<onedrivesdk.model.education_assignment_recipient.EducationAssignmentRecipient>`:
                The assignTo
        """
        if "assignTo" in self._prop_dict:
            if isinstance(self._prop_dict["assignTo"], OneDriveObjectBase):
                return self._prop_dict["assignTo"]
            else :
                self._prop_dict["assignTo"] = EducationAssignmentRecipient(self._prop_dict["assignTo"])
                return self._prop_dict["assignTo"]

        return None

    @assign_to.setter
    def assign_to(self, val):
        self._prop_dict["assignTo"] = val

    @property
    def allow_late_submissions(self):
        """
        Gets and sets the allowLateSubmissions
        
        Returns:
            bool:
                The allowLateSubmissions
        """
        if "allowLateSubmissions" in self._prop_dict:
            return self._prop_dict["allowLateSubmissions"]
        else:
            return None

    @allow_late_submissions.setter
    def allow_late_submissions(self, val):
        self._prop_dict["allowLateSubmissions"] = val

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
    def last_modified_date_time(self):
        """
        Gets and sets the lastModifiedDateTime
        
        Returns:
            datetime:
                The lastModifiedDateTime
        """
        if "lastModifiedDateTime" in self._prop_dict:
            return datetime.strptime(self._prop_dict["lastModifiedDateTime"].replace("Z", ""), "%Y-%m-%dT%H:%M:%S.%f")
        else:
            return None

    @last_modified_date_time.setter
    def last_modified_date_time(self, val):
        self._prop_dict["lastModifiedDateTime"] = val.isoformat()+"Z"

    @property
    def last_modified_by(self):
        """
        Gets and sets the lastModifiedBy
        
        Returns: 
            :class:`IdentitySet<onedrivesdk.model.identity_set.IdentitySet>`:
                The lastModifiedBy
        """
        if "lastModifiedBy" in self._prop_dict:
            if isinstance(self._prop_dict["lastModifiedBy"], OneDriveObjectBase):
                return self._prop_dict["lastModifiedBy"]
            else :
                self._prop_dict["lastModifiedBy"] = IdentitySet(self._prop_dict["lastModifiedBy"])
                return self._prop_dict["lastModifiedBy"]

        return None

    @last_modified_by.setter
    def last_modified_by(self, val):
        self._prop_dict["lastModifiedBy"] = val

    @property
    def allow_students_to_add_resources_to_submission(self):
        """
        Gets and sets the allowStudentsToAddResourcesToSubmission
        
        Returns:
            bool:
                The allowStudentsToAddResourcesToSubmission
        """
        if "allowStudentsToAddResourcesToSubmission" in self._prop_dict:
            return self._prop_dict["allowStudentsToAddResourcesToSubmission"]
        else:
            return None

    @allow_students_to_add_resources_to_submission.setter
    def allow_students_to_add_resources_to_submission(self, val):
        self._prop_dict["allowStudentsToAddResourcesToSubmission"] = val

    @property
    def status(self):
        """
        Gets and sets the status
        
        Returns: 
            :class:`EducationAssignmentStatus<onedrivesdk.model.education_assignment_status.EducationAssignmentStatus>`:
                The status
        """
        if "status" in self._prop_dict:
            if isinstance(self._prop_dict["status"], OneDriveObjectBase):
                return self._prop_dict["status"]
            else :
                self._prop_dict["status"] = EducationAssignmentStatus(self._prop_dict["status"])
                return self._prop_dict["status"]

        return None

    @status.setter
    def status(self, val):
        self._prop_dict["status"] = val

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
    def submissions(self):
        """Gets and sets the submissions
        
        Returns: 
            :class:`SubmissionsCollectionPage<onedrivesdk.request.submissions_collection.SubmissionsCollectionPage>`:
                The submissions
        """
        if "submissions" in self._prop_dict:
            return SubmissionsCollectionPage(self._prop_dict["submissions"])
        else:
            return None

