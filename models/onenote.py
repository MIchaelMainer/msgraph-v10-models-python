# -*- coding: utf-8 -*- 
'''
# Copyright (c) Microsoft Corporation.  All Rights Reserved.  Licensed under the MIT License.  See License in the project root for license information.
# 
#  This file was generated and any changes will be overwritten.
'''

from __future__ import unicode_literals
from ..model.notebook import Notebook
from ..model.onenote_section import OnenoteSection
from ..model.section_group import SectionGroup
from ..model.onenote_page import OnenotePage
from ..model.onenote_resource import OnenoteResource
from ..model.onenote_operation import OnenoteOperation
from ..one_drive_object_base import OneDriveObjectBase


class Onenote(OneDriveObjectBase):

    def __init__(self, prop_dict={}):
        self._prop_dict = prop_dict

    @property
    def notebooks(self):
        """Gets and sets the notebooks
        
        Returns: 
            :class:`NotebooksCollectionPage<onedrivesdk.request.notebooks_collection.NotebooksCollectionPage>`:
                The notebooks
        """
        if "notebooks" in self._prop_dict:
            return NotebooksCollectionPage(self._prop_dict["notebooks"])
        else:
            return None

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

    @property
    def pages(self):
        """Gets and sets the pages
        
        Returns: 
            :class:`PagesCollectionPage<onedrivesdk.request.pages_collection.PagesCollectionPage>`:
                The pages
        """
        if "pages" in self._prop_dict:
            return PagesCollectionPage(self._prop_dict["pages"])
        else:
            return None

    @property
    def resources(self):
        """Gets and sets the resources
        
        Returns: 
            :class:`ResourcesCollectionPage<onedrivesdk.request.resources_collection.ResourcesCollectionPage>`:
                The resources
        """
        if "resources" in self._prop_dict:
            return ResourcesCollectionPage(self._prop_dict["resources"])
        else:
            return None

    @property
    def operations(self):
        """Gets and sets the operations
        
        Returns: 
            :class:`OperationsCollectionPage<onedrivesdk.request.operations_collection.OperationsCollectionPage>`:
                The operations
        """
        if "operations" in self._prop_dict:
            return OperationsCollectionPage(self._prop_dict["operations"])
        else:
            return None

