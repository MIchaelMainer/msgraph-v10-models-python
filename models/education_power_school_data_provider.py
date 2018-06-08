# -*- coding: utf-8 -*- 
'''
# Copyright (c) Microsoft Corporation.  All Rights Reserved.  Licensed under the MIT License.  See License in the project root for license information.
# 
#  This file was generated and any changes will be overwritten.
'''

from __future__ import unicode_literals
from ..model.education_synchronization_customizations import EducationSynchronizationCustomizations
from ..one_drive_object_base import OneDriveObjectBase


class EducationPowerSchoolDataProvider(OneDriveObjectBase):

    def __init__(self, prop_dict={}):
        self._prop_dict = prop_dict

    @property
    def connection_url(self):
        """Gets and sets the connectionUrl
        
        Returns: 
            str:
                The connectionUrl
        """
        if "connectionUrl" in self._prop_dict:
            return self._prop_dict["connectionUrl"]
        else:
            return None

    @connection_url.setter
    def connection_url(self, val):
        self._prop_dict["connectionUrl"] = val

    @property
    def client_id(self):
        """Gets and sets the clientId
        
        Returns: 
            str:
                The clientId
        """
        if "clientId" in self._prop_dict:
            return self._prop_dict["clientId"]
        else:
            return None

    @client_id.setter
    def client_id(self, val):
        self._prop_dict["clientId"] = val

    @property
    def client_secret(self):
        """Gets and sets the clientSecret
        
        Returns: 
            str:
                The clientSecret
        """
        if "clientSecret" in self._prop_dict:
            return self._prop_dict["clientSecret"]
        else:
            return None

    @client_secret.setter
    def client_secret(self, val):
        self._prop_dict["clientSecret"] = val

    @property
    def schools_ids(self):
        """Gets and sets the schoolsIds
        
        Returns: 
            str:
                The schoolsIds
        """
        if "schoolsIds" in self._prop_dict:
            return self._prop_dict["schoolsIds"]
        else:
            return None

    @schools_ids.setter
    def schools_ids(self, val):
        self._prop_dict["schoolsIds"] = val

    @property
    def school_year(self):
        """Gets and sets the schoolYear
        
        Returns: 
            str:
                The schoolYear
        """
        if "schoolYear" in self._prop_dict:
            return self._prop_dict["schoolYear"]
        else:
            return None

    @school_year.setter
    def school_year(self, val):
        self._prop_dict["schoolYear"] = val

    @property
    def allow_teachers_in_multiple_schools(self):
        """Gets and sets the allowTeachersInMultipleSchools
        
        Returns: 
            bool:
                The allowTeachersInMultipleSchools
        """
        if "allowTeachersInMultipleSchools" in self._prop_dict:
            return self._prop_dict["allowTeachersInMultipleSchools"]
        else:
            return None

    @allow_teachers_in_multiple_schools.setter
    def allow_teachers_in_multiple_schools(self, val):
        self._prop_dict["allowTeachersInMultipleSchools"] = val

    @property
    def customizations(self):
        """
        Gets and sets the customizations
        
        Returns: 
            :class:`EducationSynchronizationCustomizations<onedrivesdk.model.education_synchronization_customizations.EducationSynchronizationCustomizations>`:
                The customizations
        """
        if "customizations" in self._prop_dict:
            if isinstance(self._prop_dict["customizations"], OneDriveObjectBase):
                return self._prop_dict["customizations"]
            else :
                self._prop_dict["customizations"] = EducationSynchronizationCustomizations(self._prop_dict["customizations"])
                return self._prop_dict["customizations"]

        return None

    @customizations.setter
    def customizations(self, val):
        self._prop_dict["customizations"] = val
