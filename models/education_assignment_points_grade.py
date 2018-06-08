# -*- coding: utf-8 -*- 
'''
# Copyright (c) Microsoft Corporation.  All Rights Reserved.  Licensed under the MIT License.  See License in the project root for license information.
# 
#  This file was generated and any changes will be overwritten.
'''

from __future__ import unicode_literals
from ..model.single import Single
from ..one_drive_object_base import OneDriveObjectBase


class EducationAssignmentPointsGrade(OneDriveObjectBase):

    def __init__(self, prop_dict={}):
        self._prop_dict = prop_dict

    @property
    def points(self):
        """
        Gets and sets the points
        
        Returns: 
            :class:`Single<onedrivesdk.model.single.Single>`:
                The points
        """
        if "points" in self._prop_dict:
            if isinstance(self._prop_dict["points"], OneDriveObjectBase):
                return self._prop_dict["points"]
            else :
                self._prop_dict["points"] = Single(self._prop_dict["points"])
                return self._prop_dict["points"]

        return None

    @points.setter
    def points(self, val):
        self._prop_dict["points"] = val
