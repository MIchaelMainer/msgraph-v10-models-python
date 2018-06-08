# -*- coding: utf-8 -*- 
'''
# Copyright (c) Microsoft Corporation.  All Rights Reserved.  Licensed under the MIT License.  See License in the project root for license information.
# 
#  This file was generated and any changes will be overwritten.
'''

from __future__ import unicode_literals
from ..one_drive_object_base import OneDriveObjectBase


class EducationTeacher(OneDriveObjectBase):

    def __init__(self, prop_dict={}):
        self._prop_dict = prop_dict

    @property
    def teacher_number(self):
        """Gets and sets the teacherNumber
        
        Returns: 
            str:
                The teacherNumber
        """
        if "teacherNumber" in self._prop_dict:
            return self._prop_dict["teacherNumber"]
        else:
            return None

    @teacher_number.setter
    def teacher_number(self, val):
        self._prop_dict["teacherNumber"] = val

    @property
    def external_id(self):
        """Gets and sets the externalId
        
        Returns: 
            str:
                The externalId
        """
        if "externalId" in self._prop_dict:
            return self._prop_dict["externalId"]
        else:
            return None

    @external_id.setter
    def external_id(self, val):
        self._prop_dict["externalId"] = val

