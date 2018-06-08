# -*- coding: utf-8 -*- 
'''
# Copyright (c) Microsoft Corporation.  All Rights Reserved.  Licensed under the MIT License.  See License in the project root for license information.
# 
#  This file was generated and any changes will be overwritten.
'''

from __future__ import unicode_literals
from ..model.mime_content import MimeContent
from ..model.mobile_app_publishing_state import MobileAppPublishingState
from ..model.mobile_app_category import MobileAppCategory
from ..model.mobile_app_assignment import MobileAppAssignment
from datetime import datetime
from ..one_drive_object_base import OneDriveObjectBase


class MobileApp(OneDriveObjectBase):

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
    def large_icon(self):
        """
        Gets and sets the largeIcon
        
        Returns: 
            :class:`MimeContent<onedrivesdk.model.mime_content.MimeContent>`:
                The largeIcon
        """
        if "largeIcon" in self._prop_dict:
            if isinstance(self._prop_dict["largeIcon"], OneDriveObjectBase):
                return self._prop_dict["largeIcon"]
            else :
                self._prop_dict["largeIcon"] = MimeContent(self._prop_dict["largeIcon"])
                return self._prop_dict["largeIcon"]

        return None

    @large_icon.setter
    def large_icon(self, val):
        self._prop_dict["largeIcon"] = val

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
    def is_featured(self):
        """
        Gets and sets the isFeatured
        
        Returns:
            bool:
                The isFeatured
        """
        if "isFeatured" in self._prop_dict:
            return self._prop_dict["isFeatured"]
        else:
            return None

    @is_featured.setter
    def is_featured(self, val):
        self._prop_dict["isFeatured"] = val

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
    def owner(self):
        """
        Gets and sets the owner
        
        Returns:
            str:
                The owner
        """
        if "owner" in self._prop_dict:
            return self._prop_dict["owner"]
        else:
            return None

    @owner.setter
    def owner(self, val):
        self._prop_dict["owner"] = val

    @property
    def developer(self):
        """
        Gets and sets the developer
        
        Returns:
            str:
                The developer
        """
        if "developer" in self._prop_dict:
            return self._prop_dict["developer"]
        else:
            return None

    @developer.setter
    def developer(self, val):
        self._prop_dict["developer"] = val

    @property
    def notes(self):
        """
        Gets and sets the notes
        
        Returns:
            str:
                The notes
        """
        if "notes" in self._prop_dict:
            return self._prop_dict["notes"]
        else:
            return None

    @notes.setter
    def notes(self, val):
        self._prop_dict["notes"] = val

    @property
    def publishing_state(self):
        """
        Gets and sets the publishingState
        
        Returns: 
            :class:`MobileAppPublishingState<onedrivesdk.model.mobile_app_publishing_state.MobileAppPublishingState>`:
                The publishingState
        """
        if "publishingState" in self._prop_dict:
            if isinstance(self._prop_dict["publishingState"], OneDriveObjectBase):
                return self._prop_dict["publishingState"]
            else :
                self._prop_dict["publishingState"] = MobileAppPublishingState(self._prop_dict["publishingState"])
                return self._prop_dict["publishingState"]

        return None

    @publishing_state.setter
    def publishing_state(self, val):
        self._prop_dict["publishingState"] = val

    @property
    def categories(self):
        """Gets and sets the categories
        
        Returns: 
            :class:`CategoriesCollectionPage<onedrivesdk.request.categories_collection.CategoriesCollectionPage>`:
                The categories
        """
        if "categories" in self._prop_dict:
            return CategoriesCollectionPage(self._prop_dict["categories"])
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

