# -*- coding: utf-8 -*- 
'''
# Copyright (c) Microsoft Corporation.  All Rights Reserved.  Licensed under the MIT License.  See License in the project root for license information.
# 
#  This file was generated and any changes will be overwritten.
'''

from __future__ import unicode_literals
from ..model.onenote_user_role import OnenoteUserRole
from ..model.notebook_links import NotebookLinks
from ..model.onenote_section import OnenoteSection
from ..model.section_group import SectionGroup
from ..one_drive_object_base import OneDriveObjectBase


class Notebook(OneDriveObjectBase):

    def __init__(self, prop_dict={}):
        self._prop_dict = prop_dict

    @property
    def is_default(self):
        """
        Gets and sets the isDefault
        
        Returns:
            bool:
                The isDefault
        """
        if "isDefault" in self._prop_dict:
            return self._prop_dict["isDefault"]
        else:
            return None

    @is_default.setter
    def is_default(self, val):
        self._prop_dict["isDefault"] = val

    @property
    def user_role(self):
        """
        Gets and sets the userRole
        
        Returns: 
            :class:`OnenoteUserRole<onedrivesdk.model.onenote_user_role.OnenoteUserRole>`:
                The userRole
        """
        if "userRole" in self._prop_dict:
            if isinstance(self._prop_dict["userRole"], OneDriveObjectBase):
                return self._prop_dict["userRole"]
            else :
                self._prop_dict["userRole"] = OnenoteUserRole(self._prop_dict["userRole"])
                return self._prop_dict["userRole"]

        return None

    @user_role.setter
    def user_role(self, val):
        self._prop_dict["userRole"] = val

    @property
    def is_shared(self):
        """
        Gets and sets the isShared
        
        Returns:
            bool:
                The isShared
        """
        if "isShared" in self._prop_dict:
            return self._prop_dict["isShared"]
        else:
            return None

    @is_shared.setter
    def is_shared(self, val):
        self._prop_dict["isShared"] = val

    @property
    def sections_url(self):
        """
        Gets and sets the sectionsUrl
        
        Returns:
            str:
                The sectionsUrl
        """
        if "sectionsUrl" in self._prop_dict:
            return self._prop_dict["sectionsUrl"]
        else:
            return None

    @sections_url.setter
    def sections_url(self, val):
        self._prop_dict["sectionsUrl"] = val

    @property
    def section_groups_url(self):
        """
        Gets and sets the sectionGroupsUrl
        
        Returns:
            str:
                The sectionGroupsUrl
        """
        if "sectionGroupsUrl" in self._prop_dict:
            return self._prop_dict["sectionGroupsUrl"]
        else:
            return None

    @section_groups_url.setter
    def section_groups_url(self, val):
        self._prop_dict["sectionGroupsUrl"] = val

    @property
    def links(self):
        """
        Gets and sets the links
        
        Returns: 
            :class:`NotebookLinks<onedrivesdk.model.notebook_links.NotebookLinks>`:
                The links
        """
        if "links" in self._prop_dict:
            if isinstance(self._prop_dict["links"], OneDriveObjectBase):
                return self._prop_dict["links"]
            else :
                self._prop_dict["links"] = NotebookLinks(self._prop_dict["links"])
                return self._prop_dict["links"]

        return None

    @links.setter
    def links(self, val):
        self._prop_dict["links"] = val

    @property
    def sections(self):
        """Gets and sets the sections
        
        Returns: 
            :class:`SectionsCollectionPage<onedrivesdk.request.sections_collection.SectionsCollectionPage>`:
                The sections
        """
        if "sections" in self._prop_dict:
            return SectionsCollectionPage(self._prop_dict["sections"])
        else:
            return None

    @property
    def section_groups(self):
        """Gets and sets the sectionGroups
        
        Returns: 
            :class:`SectionGroupsCollectionPage<onedrivesdk.request.section_groups_collection.SectionGroupsCollectionPage>`:
                The sectionGroups
        """
        if "sectionGroups" in self._prop_dict:
            return SectionGroupsCollectionPage(self._prop_dict["sectionGroups"])
        else:
            return None

