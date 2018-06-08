# -*- coding: utf-8 -*- 
'''
# Copyright (c) Microsoft Corporation.  All Rights Reserved.  Licensed under the MIT License.  See License in the project root for license information.
# 
#  This file was generated and any changes will be overwritten.
'''

from __future__ import unicode_literals
from ..model.notebook import Notebook
from ..model.onenote_section import OnenoteSection
from ..one_drive_object_base import OneDriveObjectBase


class SectionGroup(OneDriveObjectBase):

    def __init__(self, prop_dict={}):
        self._prop_dict = prop_dict

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
    def parent_notebook(self):
        """
        Gets and sets the parentNotebook
        
        Returns: 
            :class:`Notebook<onedrivesdk.model.notebook.Notebook>`:
                The parentNotebook
        """
        if "parentNotebook" in self._prop_dict:
            if isinstance(self._prop_dict["parentNotebook"], OneDriveObjectBase):
                return self._prop_dict["parentNotebook"]
            else :
                self._prop_dict["parentNotebook"] = Notebook(self._prop_dict["parentNotebook"])
                return self._prop_dict["parentNotebook"]

        return None

    @parent_notebook.setter
    def parent_notebook(self, val):
        self._prop_dict["parentNotebook"] = val

    @property
    def parent_section_group(self):
        """
        Gets and sets the parentSectionGroup
        
        Returns: 
            :class:`SectionGroup<onedrivesdk.model.section_group.SectionGroup>`:
                The parentSectionGroup
        """
        if "parentSectionGroup" in self._prop_dict:
            if isinstance(self._prop_dict["parentSectionGroup"], OneDriveObjectBase):
                return self._prop_dict["parentSectionGroup"]
            else :
                self._prop_dict["parentSectionGroup"] = SectionGroup(self._prop_dict["parentSectionGroup"])
                return self._prop_dict["parentSectionGroup"]

        return None

    @parent_section_group.setter
    def parent_section_group(self, val):
        self._prop_dict["parentSectionGroup"] = val

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

