# -*- coding: utf-8 -*- 
'''
# Copyright (c) Microsoft Corporation.  All Rights Reserved.  Licensed under the MIT License.  See License in the project root for license information.
# 
#  This file was generated and any changes will be overwritten.
'''

from __future__ import unicode_literals
from ..model.section_links import SectionLinks
from ..model.notebook import Notebook
from ..model.section_group import SectionGroup
from ..model.onenote_page import OnenotePage
from ..one_drive_object_base import OneDriveObjectBase


class OnenoteSection(OneDriveObjectBase):

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
    def links(self):
        """
        Gets and sets the links
        
        Returns: 
            :class:`SectionLinks<onedrivesdk.model.section_links.SectionLinks>`:
                The links
        """
        if "links" in self._prop_dict:
            if isinstance(self._prop_dict["links"], OneDriveObjectBase):
                return self._prop_dict["links"]
            else :
                self._prop_dict["links"] = SectionLinks(self._prop_dict["links"])
                return self._prop_dict["links"]

        return None

    @links.setter
    def links(self, val):
        self._prop_dict["links"] = val

    @property
    def pages_url(self):
        """
        Gets and sets the pagesUrl
        
        Returns:
            str:
                The pagesUrl
        """
        if "pagesUrl" in self._prop_dict:
            return self._prop_dict["pagesUrl"]
        else:
            return None

    @pages_url.setter
    def pages_url(self, val):
        self._prop_dict["pagesUrl"] = val

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

