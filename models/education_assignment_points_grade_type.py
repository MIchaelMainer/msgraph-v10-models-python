# -*- coding: utf-8 -*- 
'''
# Copyright (c) Microsoft Corporation.  All Rights Reserved.  Licensed under the MIT License.  See License in the project root for license information.
# 
#  This file was generated and any changes will be overwritten.
'''

from __future__ import unicode_literals
from ..model.single import Single
from ..one_drive_object_base import OneDriveObjectBase


class EducationAssignmentPointsGradeType(OneDriveObjectBase):

    def __init__(self, prop_dict={}):
        self._prop_dict = prop_dict

    @property
    def max_points(self):
        """
        Gets and sets the maxPoints
        
        Returns: 
            :class:`Single<onedrivesdk.model.single.Single>`:
                The maxPoints
        """
        if "maxPoints" in self._prop_dict:
            if isinstance(self._prop_dict["maxPoints"], OneDriveObjectBase):
                return self._prop_dict["maxPoints"]
            else :
                self._prop_dict["maxPoints"] = Single(self._prop_dict["maxPoints"])
                return self._prop_dict["maxPoints"]

        return None

    @max_points.setter
    def max_points(self, val):
        self._prop_dict["maxPoints"] = val
