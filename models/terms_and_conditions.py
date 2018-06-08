# -*- coding: utf-8 -*- 
'''
# Copyright (c) Microsoft Corporation.  All Rights Reserved.  Licensed under the MIT License.  See License in the project root for license information.
# 
#  This file was generated and any changes will be overwritten.
'''

from __future__ import unicode_literals
from ..model.terms_and_conditions_group_assignment import TermsAndConditionsGroupAssignment
from ..model.terms_and_conditions_assignment import TermsAndConditionsAssignment
from ..model.terms_and_conditions_acceptance_status import TermsAndConditionsAcceptanceStatus
from datetime import datetime
from ..one_drive_object_base import OneDriveObjectBase


class TermsAndConditions(OneDriveObjectBase):

    def __init__(self, prop_dict={}):
        self._prop_dict = prop_dict

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
    def modified_date_time(self):
        """
        Gets and sets the modifiedDateTime
        
        Returns:
            datetime:
                The modifiedDateTime
        """
        if "modifiedDateTime" in self._prop_dict:
            return datetime.strptime(self._prop_dict["modifiedDateTime"].replace("Z", ""), "%Y-%m-%dT%H:%M:%S.%f")
        else:
            return None

    @modified_date_time.setter
    def modified_date_time(self, val):
        self._prop_dict["modifiedDateTime"] = val.isoformat()+"Z"

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
    def body_text(self):
        """
        Gets and sets the bodyText
        
        Returns:
            str:
                The bodyText
        """
        if "bodyText" in self._prop_dict:
            return self._prop_dict["bodyText"]
        else:
            return None

    @body_text.setter
    def body_text(self, val):
        self._prop_dict["bodyText"] = val

    @property
    def acceptance_statement(self):
        """
        Gets and sets the acceptanceStatement
        
        Returns:
            str:
                The acceptanceStatement
        """
        if "acceptanceStatement" in self._prop_dict:
            return self._prop_dict["acceptanceStatement"]
        else:
            return None

    @acceptance_statement.setter
    def acceptance_statement(self, val):
        self._prop_dict["acceptanceStatement"] = val

    @property
    def version(self):
        """
        Gets and sets the version
        
        Returns:
            int:
                The version
        """
        if "version" in self._prop_dict:
            return self._prop_dict["version"]
        else:
            return None

    @version.setter
    def version(self, val):
        self._prop_dict["version"] = val

    @property
    def group_assignments(self):
        """Gets and sets the groupAssignments
        
        Returns: 
            :class:`GroupAssignmentsCollectionPage<onedrivesdk.request.group_assignments_collection.GroupAssignmentsCollectionPage>`:
                The groupAssignments
        """
        if "groupAssignments" in self._prop_dict:
            return GroupAssignmentsCollectionPage(self._prop_dict["groupAssignments"])
        else:
            return None

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

    @property
    def acceptance_statuses(self):
        """Gets and sets the acceptanceStatuses
        
        Returns: 
            :class:`AcceptanceStatusesCollectionPage<onedrivesdk.request.acceptance_statuses_collection.AcceptanceStatusesCollectionPage>`:
                The acceptanceStatuses
        """
        if "acceptanceStatuses" in self._prop_dict:
            return AcceptanceStatusesCollectionPage(self._prop_dict["acceptanceStatuses"])
        else:
            return None

