# -*- coding: utf-8 -*- 
'''
# Copyright (c) Microsoft Corporation.  All Rights Reserved.  Licensed under the MIT License.  See License in the project root for license information.
# 
#  This file was generated and any changes will be overwritten.
'''

from __future__ import unicode_literals
from ..model.education_class import EducationClass
from ..model.education_school import EducationSchool
from ..model.education_user import EducationUser
from ..one_drive_object_base import OneDriveObjectBase


class EducationRoot(OneDriveObjectBase):

    def __init__(self, prop_dict={}):
        self._prop_dict = prop_dict

    @property
    def classes(self):
        """Gets and sets the classes
        
        Returns: 
            :class:`ClassesCollectionPage<onedrivesdk.request.classes_collection.ClassesCollectionPage>`:
                The classes
        """
        if "classes" in self._prop_dict:
            return ClassesCollectionPage(self._prop_dict["classes"])
        else:
            return None

    @property
    def schools(self):
        """Gets and sets the schools
        
        Returns: 
            :class:`SchoolsCollectionPage<onedrivesdk.request.schools_collection.SchoolsCollectionPage>`:
                The schools
        """
        if "schools" in self._prop_dict:
            return SchoolsCollectionPage(self._prop_dict["schools"])
        else:
            return None

    @property
    def users(self):
        """Gets and sets the users
        
        Returns: 
            :class:`UsersCollectionPage<onedrivesdk.request.users_collection.UsersCollectionPage>`:
                The users
        """
        if "users" in self._prop_dict:
            return UsersCollectionPage(self._prop_dict["users"])
        else:
            return None

    @property
    def me(self):
        """
        Gets and sets the me
        
        Returns: 
            :class:`EducationUser<onedrivesdk.model.education_user.EducationUser>`:
                The me
        """
        if "me" in self._prop_dict:
            if isinstance(self._prop_dict["me"], OneDriveObjectBase):
                return self._prop_dict["me"]
            else :
                self._prop_dict["me"] = EducationUser(self._prop_dict["me"])
                return self._prop_dict["me"]

        return None

    @me.setter
    def me(self, val):
        self._prop_dict["me"] = val

