# -*- coding: utf-8 -*- 
'''
# Copyright (c) Microsoft Corporation.  All Rights Reserved.  Licensed under the MIT License.  See License in the project root for license information.
# 
#  This file was generated and any changes will be overwritten.
'''

from __future__ import unicode_literals
from ..model.education_submission_recipient import EducationSubmissionRecipient
from ..model.education_submission_status import EducationSubmissionStatus
from ..model.identity_set import IdentitySet
from ..model.education_assignment_grade import EducationAssignmentGrade
from ..model.education_feedback import EducationFeedback
from ..model.education_submission_resource import EducationSubmissionResource
from datetime import datetime
from ..one_drive_object_base import OneDriveObjectBase


class EducationSubmission(OneDriveObjectBase):

    def __init__(self, prop_dict={}):
        self._prop_dict = prop_dict

    @property
    def recipient(self):
        """
        Gets and sets the recipient
        
        Returns: 
            :class:`EducationSubmissionRecipient<onedrivesdk.model.education_submission_recipient.EducationSubmissionRecipient>`:
                The recipient
        """
        if "recipient" in self._prop_dict:
            if isinstance(self._prop_dict["recipient"], OneDriveObjectBase):
                return self._prop_dict["recipient"]
            else :
                self._prop_dict["recipient"] = EducationSubmissionRecipient(self._prop_dict["recipient"])
                return self._prop_dict["recipient"]

        return None

    @recipient.setter
    def recipient(self, val):
        self._prop_dict["recipient"] = val

    @property
    def status(self):
        """
        Gets and sets the status
        
        Returns: 
            :class:`EducationSubmissionStatus<onedrivesdk.model.education_submission_status.EducationSubmissionStatus>`:
                The status
        """
        if "status" in self._prop_dict:
            if isinstance(self._prop_dict["status"], OneDriveObjectBase):
                return self._prop_dict["status"]
            else :
                self._prop_dict["status"] = EducationSubmissionStatus(self._prop_dict["status"])
                return self._prop_dict["status"]

        return None

    @status.setter
    def status(self, val):
        self._prop_dict["status"] = val

    @property
    def submitted_by(self):
        """
        Gets and sets the submittedBy
        
        Returns: 
            :class:`IdentitySet<onedrivesdk.model.identity_set.IdentitySet>`:
                The submittedBy
        """
        if "submittedBy" in self._prop_dict:
            if isinstance(self._prop_dict["submittedBy"], OneDriveObjectBase):
                return self._prop_dict["submittedBy"]
            else :
                self._prop_dict["submittedBy"] = IdentitySet(self._prop_dict["submittedBy"])
                return self._prop_dict["submittedBy"]

        return None

    @submitted_by.setter
    def submitted_by(self, val):
        self._prop_dict["submittedBy"] = val

    @property
    def submitted_date_time(self):
        """
        Gets and sets the submittedDateTime
        
        Returns:
            datetime:
                The submittedDateTime
        """
        if "submittedDateTime" in self._prop_dict:
            return datetime.strptime(self._prop_dict["submittedDateTime"].replace("Z", ""), "%Y-%m-%dT%H:%M:%S.%f")
        else:
            return None

    @submitted_date_time.setter
    def submitted_date_time(self, val):
        self._prop_dict["submittedDateTime"] = val.isoformat()+"Z"

    @property
    def unsubmitted_by(self):
        """
        Gets and sets the unsubmittedBy
        
        Returns: 
            :class:`IdentitySet<onedrivesdk.model.identity_set.IdentitySet>`:
                The unsubmittedBy
        """
        if "unsubmittedBy" in self._prop_dict:
            if isinstance(self._prop_dict["unsubmittedBy"], OneDriveObjectBase):
                return self._prop_dict["unsubmittedBy"]
            else :
                self._prop_dict["unsubmittedBy"] = IdentitySet(self._prop_dict["unsubmittedBy"])
                return self._prop_dict["unsubmittedBy"]

        return None

    @unsubmitted_by.setter
    def unsubmitted_by(self, val):
        self._prop_dict["unsubmittedBy"] = val

    @property
    def unsubmitted_date_time(self):
        """
        Gets and sets the unsubmittedDateTime
        
        Returns:
            datetime:
                The unsubmittedDateTime
        """
        if "unsubmittedDateTime" in self._prop_dict:
            return datetime.strptime(self._prop_dict["unsubmittedDateTime"].replace("Z", ""), "%Y-%m-%dT%H:%M:%S.%f")
        else:
            return None

    @unsubmitted_date_time.setter
    def unsubmitted_date_time(self, val):
        self._prop_dict["unsubmittedDateTime"] = val.isoformat()+"Z"

    @property
    def released_by(self):
        """
        Gets and sets the releasedBy
        
        Returns: 
            :class:`IdentitySet<onedrivesdk.model.identity_set.IdentitySet>`:
                The releasedBy
        """
        if "releasedBy" in self._prop_dict:
            if isinstance(self._prop_dict["releasedBy"], OneDriveObjectBase):
                return self._prop_dict["releasedBy"]
            else :
                self._prop_dict["releasedBy"] = IdentitySet(self._prop_dict["releasedBy"])
                return self._prop_dict["releasedBy"]

        return None

    @released_by.setter
    def released_by(self, val):
        self._prop_dict["releasedBy"] = val

    @property
    def released_date_time(self):
        """
        Gets and sets the releasedDateTime
        
        Returns:
            datetime:
                The releasedDateTime
        """
        if "releasedDateTime" in self._prop_dict:
            return datetime.strptime(self._prop_dict["releasedDateTime"].replace("Z", ""), "%Y-%m-%dT%H:%M:%S.%f")
        else:
            return None

    @released_date_time.setter
    def released_date_time(self, val):
        self._prop_dict["releasedDateTime"] = val.isoformat()+"Z"

    @property
    def returned_by(self):
        """
        Gets and sets the returnedBy
        
        Returns: 
            :class:`IdentitySet<onedrivesdk.model.identity_set.IdentitySet>`:
                The returnedBy
        """
        if "returnedBy" in self._prop_dict:
            if isinstance(self._prop_dict["returnedBy"], OneDriveObjectBase):
                return self._prop_dict["returnedBy"]
            else :
                self._prop_dict["returnedBy"] = IdentitySet(self._prop_dict["returnedBy"])
                return self._prop_dict["returnedBy"]

        return None

    @returned_by.setter
    def returned_by(self, val):
        self._prop_dict["returnedBy"] = val

    @property
    def returned_date_time(self):
        """
        Gets and sets the returnedDateTime
        
        Returns:
            datetime:
                The returnedDateTime
        """
        if "returnedDateTime" in self._prop_dict:
            return datetime.strptime(self._prop_dict["returnedDateTime"].replace("Z", ""), "%Y-%m-%dT%H:%M:%S.%f")
        else:
            return None

    @returned_date_time.setter
    def returned_date_time(self, val):
        self._prop_dict["returnedDateTime"] = val.isoformat()+"Z"

    @property
    def grade(self):
        """
        Gets and sets the grade
        
        Returns: 
            :class:`EducationAssignmentGrade<onedrivesdk.model.education_assignment_grade.EducationAssignmentGrade>`:
                The grade
        """
        if "grade" in self._prop_dict:
            if isinstance(self._prop_dict["grade"], OneDriveObjectBase):
                return self._prop_dict["grade"]
            else :
                self._prop_dict["grade"] = EducationAssignmentGrade(self._prop_dict["grade"])
                return self._prop_dict["grade"]

        return None

    @grade.setter
    def grade(self, val):
        self._prop_dict["grade"] = val

    @property
    def feedback(self):
        """
        Gets and sets the feedback
        
        Returns: 
            :class:`EducationFeedback<onedrivesdk.model.education_feedback.EducationFeedback>`:
                The feedback
        """
        if "feedback" in self._prop_dict:
            if isinstance(self._prop_dict["feedback"], OneDriveObjectBase):
                return self._prop_dict["feedback"]
            else :
                self._prop_dict["feedback"] = EducationFeedback(self._prop_dict["feedback"])
                return self._prop_dict["feedback"]

        return None

    @feedback.setter
    def feedback(self, val):
        self._prop_dict["feedback"] = val

    @property
    def resources_folder_url(self):
        """
        Gets and sets the resourcesFolderUrl
        
        Returns:
            str:
                The resourcesFolderUrl
        """
        if "resourcesFolderUrl" in self._prop_dict:
            return self._prop_dict["resourcesFolderUrl"]
        else:
            return None

    @resources_folder_url.setter
    def resources_folder_url(self, val):
        self._prop_dict["resourcesFolderUrl"] = val

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
    def submitted_resources(self):
        """Gets and sets the submittedResources
        
        Returns: 
            :class:`SubmittedResourcesCollectionPage<onedrivesdk.request.submitted_resources_collection.SubmittedResourcesCollectionPage>`:
                The submittedResources
        """
        if "submittedResources" in self._prop_dict:
            return SubmittedResourcesCollectionPage(self._prop_dict["submittedResources"])
        else:
            return None

