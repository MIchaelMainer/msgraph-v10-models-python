# -*- coding: utf-8 -*- 
'''
# Copyright (c) Microsoft Corporation.  All Rights Reserved.  Licensed under the MIT License.  See License in the project root for license information.
# 
#  This file was generated and any changes will be overwritten.
'''

from __future__ import unicode_literals
from ..model.education_synchronization_customization import EducationSynchronizationCustomization
from ..one_drive_object_base import OneDriveObjectBase


class EducationSynchronizationCustomizations(OneDriveObjectBase):

    def __init__(self, prop_dict={}):
        self._prop_dict = prop_dict

    @property
    def school(self):
        """
        Gets and sets the school
        
        Returns: 
            :class:`EducationSynchronizationCustomization<onedrivesdk.model.education_synchronization_customization.EducationSynchronizationCustomization>`:
                The school
        """
        if "school" in self._prop_dict:
            if isinstance(self._prop_dict["school"], OneDriveObjectBase):
                return self._prop_dict["school"]
            else :
                self._prop_dict["school"] = EducationSynchronizationCustomization(self._prop_dict["school"])
                return self._prop_dict["school"]

        return None

    @school.setter
    def school(self, val):
        self._prop_dict["school"] = val
    @property
    def section(self):
        """
        Gets and sets the section
        
        Returns: 
            :class:`EducationSynchronizationCustomization<onedrivesdk.model.education_synchronization_customization.EducationSynchronizationCustomization>`:
                The section
        """
        if "section" in self._prop_dict:
            if isinstance(self._prop_dict["section"], OneDriveObjectBase):
                return self._prop_dict["section"]
            else :
                self._prop_dict["section"] = EducationSynchronizationCustomization(self._prop_dict["section"])
                return self._prop_dict["section"]

        return None

    @section.setter
    def section(self, val):
        self._prop_dict["section"] = val
    @property
    def student(self):
        """
        Gets and sets the student
        
        Returns: 
            :class:`EducationSynchronizationCustomization<onedrivesdk.model.education_synchronization_customization.EducationSynchronizationCustomization>`:
                The student
        """
        if "student" in self._prop_dict:
            if isinstance(self._prop_dict["student"], OneDriveObjectBase):
                return self._prop_dict["student"]
            else :
                self._prop_dict["student"] = EducationSynchronizationCustomization(self._prop_dict["student"])
                return self._prop_dict["student"]

        return None

    @student.setter
    def student(self, val):
        self._prop_dict["student"] = val
    @property
    def teacher(self):
        """
        Gets and sets the teacher
        
        Returns: 
            :class:`EducationSynchronizationCustomization<onedrivesdk.model.education_synchronization_customization.EducationSynchronizationCustomization>`:
                The teacher
        """
        if "teacher" in self._prop_dict:
            if isinstance(self._prop_dict["teacher"], OneDriveObjectBase):
                return self._prop_dict["teacher"]
            else :
                self._prop_dict["teacher"] = EducationSynchronizationCustomization(self._prop_dict["teacher"])
                return self._prop_dict["teacher"]

        return None

    @teacher.setter
    def teacher(self, val):
        self._prop_dict["teacher"] = val
    @property
    def student_enrollment(self):
        """
        Gets and sets the studentEnrollment
        
        Returns: 
            :class:`EducationSynchronizationCustomization<onedrivesdk.model.education_synchronization_customization.EducationSynchronizationCustomization>`:
                The studentEnrollment
        """
        if "studentEnrollment" in self._prop_dict:
            if isinstance(self._prop_dict["studentEnrollment"], OneDriveObjectBase):
                return self._prop_dict["studentEnrollment"]
            else :
                self._prop_dict["studentEnrollment"] = EducationSynchronizationCustomization(self._prop_dict["studentEnrollment"])
                return self._prop_dict["studentEnrollment"]

        return None

    @student_enrollment.setter
    def student_enrollment(self, val):
        self._prop_dict["studentEnrollment"] = val
    @property
    def teacher_roster(self):
        """
        Gets and sets the teacherRoster
        
        Returns: 
            :class:`EducationSynchronizationCustomization<onedrivesdk.model.education_synchronization_customization.EducationSynchronizationCustomization>`:
                The teacherRoster
        """
        if "teacherRoster" in self._prop_dict:
            if isinstance(self._prop_dict["teacherRoster"], OneDriveObjectBase):
                return self._prop_dict["teacherRoster"]
            else :
                self._prop_dict["teacherRoster"] = EducationSynchronizationCustomization(self._prop_dict["teacherRoster"])
                return self._prop_dict["teacherRoster"]

        return None

    @teacher_roster.setter
    def teacher_roster(self, val):
        self._prop_dict["teacherRoster"] = val
