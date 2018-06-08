# -*- coding: utf-8 -*- 
'''
# Copyright (c) Microsoft Corporation.  All Rights Reserved.  Licensed under the MIT License.  See License in the project root for license information.
# 
#  This file was generated and any changes will be overwritten.
'''

from __future__ import unicode_literals
from ..model.identity_set import IdentitySet
from datetime import datetime
from ..one_drive_object_base import OneDriveObjectBase


class EducationAssignmentGrade(OneDriveObjectBase):

    def __init__(self, prop_dict={}):
        self._prop_dict = prop_dict

    @property
    def graded_by(self):
        """
        Gets and sets the gradedBy
        
        Returns: 
            :class:`IdentitySet<onedrivesdk.model.identity_set.IdentitySet>`:
                The gradedBy
        """
        if "gradedBy" in self._prop_dict:
            if isinstance(self._prop_dict["gradedBy"], OneDriveObjectBase):
                return self._prop_dict["gradedBy"]
            else :
                self._prop_dict["gradedBy"] = IdentitySet(self._prop_dict["gradedBy"])
                return self._prop_dict["gradedBy"]

        return None

    @graded_by.setter
    def graded_by(self, val):
        self._prop_dict["gradedBy"] = val
    @property
    def graded_date_time(self):
        """Gets and sets the gradedDateTime
        
        Returns: 
            datetime:
                The gradedDateTime
        """
        if "gradedDateTime" in self._prop_dict:
            return datetime.strptime(self._prop_dict["gradedDateTime"].replace("Z", ""), "%Y-%m-%dT%H:%M:%S.%f")
        else:
            return None

    @graded_date_time.setter
    def graded_date_time(self, val):
        self._prop_dict["gradedDateTime"] = val.isoformat()+"Z"

