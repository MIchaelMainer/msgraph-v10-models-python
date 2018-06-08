# -*- coding: utf-8 -*- 
'''
# Copyright (c) Microsoft Corporation.  All Rights Reserved.  Licensed under the MIT License.  See License in the project root for license information.
# 
#  This file was generated and any changes will be overwritten.
'''

from __future__ import unicode_literals
from ..model.date import Date
from ..model.education_gender import EducationGender
from ..one_drive_object_base import OneDriveObjectBase


class EducationStudent(OneDriveObjectBase):

    def __init__(self, prop_dict={}):
        self._prop_dict = prop_dict

    @property
    def graduation_year(self):
        """Gets and sets the graduationYear
        
        Returns: 
            str:
                The graduationYear
        """
        if "graduationYear" in self._prop_dict:
            return self._prop_dict["graduationYear"]
        else:
            return None

    @graduation_year.setter
    def graduation_year(self, val):
        self._prop_dict["graduationYear"] = val

    @property
    def grade(self):
        """Gets and sets the grade
        
        Returns: 
            str:
                The grade
        """
        if "grade" in self._prop_dict:
            return self._prop_dict["grade"]
        else:
            return None

    @grade.setter
    def grade(self, val):
        self._prop_dict["grade"] = val

    @property
    def birth_date(self):
        """
        Gets and sets the birthDate
        
        Returns: 
            :class:`Date<onedrivesdk.model.date.Date>`:
                The birthDate
        """
        if "birthDate" in self._prop_dict:
            if isinstance(self._prop_dict["birthDate"], OneDriveObjectBase):
                return self._prop_dict["birthDate"]
            else :
                self._prop_dict["birthDate"] = Date(self._prop_dict["birthDate"])
                return self._prop_dict["birthDate"]

        return None

    @birth_date.setter
    def birth_date(self, val):
        self._prop_dict["birthDate"] = val
    @property
    def gender(self):
        """
        Gets and sets the gender
        
        Returns: 
            :class:`EducationGender<onedrivesdk.model.education_gender.EducationGender>`:
                The gender
        """
        if "gender" in self._prop_dict:
            if isinstance(self._prop_dict["gender"], OneDriveObjectBase):
                return self._prop_dict["gender"]
            else :
                self._prop_dict["gender"] = EducationGender(self._prop_dict["gender"])
                return self._prop_dict["gender"]

        return None

    @gender.setter
    def gender(self, val):
        self._prop_dict["gender"] = val
    @property
    def student_number(self):
        """Gets and sets the studentNumber
        
        Returns: 
            str:
                The studentNumber
        """
        if "studentNumber" in self._prop_dict:
            return self._prop_dict["studentNumber"]
        else:
            return None

    @student_number.setter
    def student_number(self, val):
        self._prop_dict["studentNumber"] = val

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

