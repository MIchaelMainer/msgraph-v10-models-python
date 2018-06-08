# -*- coding: utf-8 -*- 
'''
# Copyright (c) Microsoft Corporation.  All Rights Reserved.  Licensed under the MIT License.  See License in the project root for license information.
# 
#  This file was generated and any changes will be overwritten.
'''

from __future__ import unicode_literals
from ..model.mime_content import MimeContent
from ..model.managed_e_book_assignment import ManagedEBookAssignment
from ..model.e_book_install_summary import EBookInstallSummary
from ..model.device_install_state import DeviceInstallState
from ..model.user_install_state_summary import UserInstallStateSummary
from datetime import datetime
from ..one_drive_object_base import OneDriveObjectBase


class ManagedEBook(OneDriveObjectBase):

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
    def publisher(self):
        """
        Gets and sets the publisher
        
        Returns:
            str:
                The publisher
        """
        if "publisher" in self._prop_dict:
            return self._prop_dict["publisher"]
        else:
            return None

    @publisher.setter
    def publisher(self, val):
        self._prop_dict["publisher"] = val

    @property
    def published_date_time(self):
        """
        Gets and sets the publishedDateTime
        
        Returns:
            datetime:
                The publishedDateTime
        """
        if "publishedDateTime" in self._prop_dict:
            return datetime.strptime(self._prop_dict["publishedDateTime"].replace("Z", ""), "%Y-%m-%dT%H:%M:%S.%f")
        else:
            return None

    @published_date_time.setter
    def published_date_time(self, val):
        self._prop_dict["publishedDateTime"] = val.isoformat()+"Z"

    @property
    def large_cover(self):
        """
        Gets and sets the largeCover
        
        Returns: 
            :class:`MimeContent<onedrivesdk.model.mime_content.MimeContent>`:
                The largeCover
        """
        if "largeCover" in self._prop_dict:
            if isinstance(self._prop_dict["largeCover"], OneDriveObjectBase):
                return self._prop_dict["largeCover"]
            else :
                self._prop_dict["largeCover"] = MimeContent(self._prop_dict["largeCover"])
                return self._prop_dict["largeCover"]

        return None

    @large_cover.setter
    def large_cover(self, val):
        self._prop_dict["largeCover"] = val

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
    def information_url(self):
        """
        Gets and sets the informationUrl
        
        Returns:
            str:
                The informationUrl
        """
        if "informationUrl" in self._prop_dict:
            return self._prop_dict["informationUrl"]
        else:
            return None

    @information_url.setter
    def information_url(self, val):
        self._prop_dict["informationUrl"] = val

    @property
    def privacy_information_url(self):
        """
        Gets and sets the privacyInformationUrl
        
        Returns:
            str:
                The privacyInformationUrl
        """
        if "privacyInformationUrl" in self._prop_dict:
            return self._prop_dict["privacyInformationUrl"]
        else:
            return None

    @privacy_information_url.setter
    def privacy_information_url(self, val):
        self._prop_dict["privacyInformationUrl"] = val

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
    def install_summary(self):
        """
        Gets and sets the installSummary
        
        Returns: 
            :class:`EBookInstallSummary<onedrivesdk.model.e_book_install_summary.EBookInstallSummary>`:
                The installSummary
        """
        if "installSummary" in self._prop_dict:
            if isinstance(self._prop_dict["installSummary"], OneDriveObjectBase):
                return self._prop_dict["installSummary"]
            else :
                self._prop_dict["installSummary"] = EBookInstallSummary(self._prop_dict["installSummary"])
                return self._prop_dict["installSummary"]

        return None

    @install_summary.setter
    def install_summary(self, val):
        self._prop_dict["installSummary"] = val

    @property
    def device_states(self):
        """Gets and sets the deviceStates
        
        Returns: 
            :class:`DeviceStatesCollectionPage<onedrivesdk.request.device_states_collection.DeviceStatesCollectionPage>`:
                The deviceStates
        """
        if "deviceStates" in self._prop_dict:
            return DeviceStatesCollectionPage(self._prop_dict["deviceStates"])
        else:
            return None

    @property
    def user_state_summary(self):
        """Gets and sets the userStateSummary
        
        Returns: 
            :class:`UserStateSummaryCollectionPage<onedrivesdk.request.user_state_summary_collection.UserStateSummaryCollectionPage>`:
                The userStateSummary
        """
        if "userStateSummary" in self._prop_dict:
            return UserStateSummaryCollectionPage(self._prop_dict["userStateSummary"])
        else:
            return None

