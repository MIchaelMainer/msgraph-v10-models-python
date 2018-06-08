# -*- coding: utf-8 -*- 
'''
# Copyright (c) Microsoft Corporation.  All Rights Reserved.  Licensed under the MIT License.  See License in the project root for license information.
# 
#  This file was generated and any changes will be overwritten.
'''

from __future__ import unicode_literals
from datetime import datetime
from ..one_drive_object_base import OneDriveObjectBase


class PlannerPlanContext(OneDriveObjectBase):

    def __init__(self, prop_dict={}):
        self._prop_dict = prop_dict

    @property
    def association_type(self):
        """Gets and sets the associationType
        
        Returns: 
            str:
                The associationType
        """
        if "associationType" in self._prop_dict:
            return self._prop_dict["associationType"]
        else:
            return None

    @association_type.setter
    def association_type(self, val):
        self._prop_dict["associationType"] = val

    @property
    def created_date_time(self):
        """Gets and sets the createdDateTime
        
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
    def display_name_segments(self):
        """Gets and sets the displayNameSegments
        
        Returns: 
            str:
                The displayNameSegments
        """
        if "displayNameSegments" in self._prop_dict:
            return self._prop_dict["displayNameSegments"]
        else:
            return None

    @display_name_segments.setter
    def display_name_segments(self, val):
        self._prop_dict["displayNameSegments"] = val

    @property
    def owner_app_id(self):
        """Gets and sets the ownerAppId
        
        Returns: 
            str:
                The ownerAppId
        """
        if "ownerAppId" in self._prop_dict:
            return self._prop_dict["ownerAppId"]
        else:
            return None

    @owner_app_id.setter
    def owner_app_id(self, val):
        self._prop_dict["ownerAppId"] = val

