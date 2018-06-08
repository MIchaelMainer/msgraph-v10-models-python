# -*- coding: utf-8 -*- 
'''
# Copyright (c) Microsoft Corporation.  All Rights Reserved.  Licensed under the MIT License.  See License in the project root for license information.
# 
#  This file was generated and any changes will be overwritten.
'''

from __future__ import unicode_literals
from ..model.identity_set import IdentitySet
from ..model.education_external_source import EducationExternalSource
from ..model.education_term import EducationTerm
from ..model.education_school import EducationSchool
from ..model.education_user import EducationUser
from ..model.group import Group
from ..one_drive_object_base import OneDriveObjectBase


class EducationClass(OneDriveObjectBase):

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
    def mail_nickname(self):
        """
        Gets and sets the mailNickname
        
        Returns:
            str:
                The mailNickname
        """
        if "mailNickname" in self._prop_dict:
            return self._prop_dict["mailNickname"]
        else:
            return None

    @mail_nickname.setter
    def mail_nickname(self, val):
        self._prop_dict["mailNickname"] = val

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
    def created_by(self):
        """
        Gets and sets the createdBy
        
        Returns: 
            :class:`IdentitySet<onedrivesdk.model.identity_set.IdentitySet>`:
                The createdBy
        """
        if "createdBy" in self._prop_dict:
            if isinstance(self._prop_dict["createdBy"], OneDriveObjectBase):
                return self._prop_dict["createdBy"]
            else :
                self._prop_dict["createdBy"] = IdentitySet(self._prop_dict["createdBy"])
                return self._prop_dict["createdBy"]

        return None

    @created_by.setter
    def created_by(self, val):
        self._prop_dict["createdBy"] = val

    @property
    def class_code(self):
        """
        Gets and sets the classCode
        
        Returns:
            str:
                The classCode
        """
        if "classCode" in self._prop_dict:
            return self._prop_dict["classCode"]
        else:
            return None

    @class_code.setter
    def class_code(self, val):
        self._prop_dict["classCode"] = val

    @property
    def external_name(self):
        """
        Gets and sets the externalName
        
        Returns:
            str:
                The externalName
        """
        if "externalName" in self._prop_dict:
            return self._prop_dict["externalName"]
        else:
            return None

    @external_name.setter
    def external_name(self, val):
        self._prop_dict["externalName"] = val

    @property
    def external_id(self):
        """
        Gets and sets the externalId
        
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

    @property
    def external_source(self):
        """
        Gets and sets the externalSource
        
        Returns: 
            :class:`EducationExternalSource<onedrivesdk.model.education_external_source.EducationExternalSource>`:
                The externalSource
        """
        if "externalSource" in self._prop_dict:
            if isinstance(self._prop_dict["externalSource"], OneDriveObjectBase):
                return self._prop_dict["externalSource"]
            else :
                self._prop_dict["externalSource"] = EducationExternalSource(self._prop_dict["externalSource"])
                return self._prop_dict["externalSource"]

        return None

    @external_source.setter
    def external_source(self, val):
        self._prop_dict["externalSource"] = val

    @property
    def term(self):
        """
        Gets and sets the term
        
        Returns: 
            :class:`EducationTerm<onedrivesdk.model.education_term.EducationTerm>`:
                The term
        """
        if "term" in self._prop_dict:
            if isinstance(self._prop_dict["term"], OneDriveObjectBase):
                return self._prop_dict["term"]
            else :
                self._prop_dict["term"] = EducationTerm(self._prop_dict["term"])
                return self._prop_dict["term"]

        return None

    @term.setter
    def term(self, val):
        self._prop_dict["term"] = val

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
    def members(self):
        """Gets and sets the members
        
        Returns: 
            :class:`MembersCollectionPage<onedrivesdk.request.members_collection.MembersCollectionPage>`:
                The members
        """
        if "members" in self._prop_dict:
            return MembersCollectionPage(self._prop_dict["members"])
        else:
            return None

    @property
    def teachers(self):
        """Gets and sets the teachers
        
        Returns: 
            :class:`TeachersCollectionPage<onedrivesdk.request.teachers_collection.TeachersCollectionPage>`:
                The teachers
        """
        if "teachers" in self._prop_dict:
            return TeachersCollectionPage(self._prop_dict["teachers"])
        else:
            return None

    @property
    def group(self):
        """
        Gets and sets the group
        
        Returns: 
            :class:`Group<onedrivesdk.model.group.Group>`:
                The group
        """
        if "group" in self._prop_dict:
            if isinstance(self._prop_dict["group"], OneDriveObjectBase):
                return self._prop_dict["group"]
            else :
                self._prop_dict["group"] = Group(self._prop_dict["group"])
                return self._prop_dict["group"]

        return None

    @group.setter
    def group(self, val):
        self._prop_dict["group"] = val

