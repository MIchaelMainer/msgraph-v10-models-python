# -*- coding: utf-8 -*- 
'''
# Copyright (c) Microsoft Corporation.  All Rights Reserved.  Licensed under the MIT License.  See License in the project root for license information.
# 
#  This file was generated and any changes will be overwritten.
'''

from __future__ import unicode_literals
from ..model.page_links import PageLinks
from ..model.onenote_section import OnenoteSection
from ..model.notebook import Notebook
from datetime import datetime
from ..one_drive_object_base import OneDriveObjectBase


class OnenotePage(OneDriveObjectBase):

    def __init__(self, prop_dict={}):
        self._prop_dict = prop_dict

    @property
    def title(self):
        """
        Gets and sets the title
        
        Returns:
            str:
                The title
        """
        if "title" in self._prop_dict:
            return self._prop_dict["title"]
        else:
            return None

    @title.setter
    def title(self, val):
        self._prop_dict["title"] = val

    @property
    def created_by_app_id(self):
        """
        Gets and sets the createdByAppId
        
        Returns:
            str:
                The createdByAppId
        """
        if "createdByAppId" in self._prop_dict:
            return self._prop_dict["createdByAppId"]
        else:
            return None

    @created_by_app_id.setter
    def created_by_app_id(self, val):
        self._prop_dict["createdByAppId"] = val

    @property
    def links(self):
        """
        Gets and sets the links
        
        Returns: 
            :class:`PageLinks<onedrivesdk.model.page_links.PageLinks>`:
                The links
        """
        if "links" in self._prop_dict:
            if isinstance(self._prop_dict["links"], OneDriveObjectBase):
                return self._prop_dict["links"]
            else :
                self._prop_dict["links"] = PageLinks(self._prop_dict["links"])
                return self._prop_dict["links"]

        return None

    @links.setter
    def links(self, val):
        self._prop_dict["links"] = val

    @property
    def content_url(self):
        """
        Gets and sets the contentUrl
        
        Returns:
            str:
                The contentUrl
        """
        if "contentUrl" in self._prop_dict:
            return self._prop_dict["contentUrl"]
        else:
            return None

    @content_url.setter
    def content_url(self, val):
        self._prop_dict["contentUrl"] = val

    @property
    def last_modified_date_time(self):
        """
        Gets and sets the lastModifiedDateTime
        
        Returns:
            datetime:
                The lastModifiedDateTime
        """
        if "lastModifiedDateTime" in self._prop_dict:
            return datetime.strptime(self._prop_dict["lastModifiedDateTime"].replace("Z", ""), "%Y-%m-%dT%H:%M:%S.%f")
        else:
            return None

    @last_modified_date_time.setter
    def last_modified_date_time(self, val):
        self._prop_dict["lastModifiedDateTime"] = val.isoformat()+"Z"

    @property
    def level(self):
        """
        Gets and sets the level
        
        Returns:
            int:
                The level
        """
        if "level" in self._prop_dict:
            return self._prop_dict["level"]
        else:
            return None

    @level.setter
    def level(self, val):
        self._prop_dict["level"] = val

    @property
    def order(self):
        """
        Gets and sets the order
        
        Returns:
            int:
                The order
        """
        if "order" in self._prop_dict:
            return self._prop_dict["order"]
        else:
            return None

    @order.setter
    def order(self, val):
        self._prop_dict["order"] = val

    @property
    def user_tags(self):
        """
        Gets and sets the userTags
        
        Returns:
            str:
                The userTags
        """
        if "userTags" in self._prop_dict:
            return self._prop_dict["userTags"]
        else:
            return None

    @user_tags.setter
    def user_tags(self, val):
        self._prop_dict["userTags"] = val

    @property
    def parent_section(self):
        """
        Gets and sets the parentSection
        
        Returns: 
            :class:`OnenoteSection<onedrivesdk.model.onenote_section.OnenoteSection>`:
                The parentSection
        """
        if "parentSection" in self._prop_dict:
            if isinstance(self._prop_dict["parentSection"], OneDriveObjectBase):
                return self._prop_dict["parentSection"]
            else :
                self._prop_dict["parentSection"] = OnenoteSection(self._prop_dict["parentSection"])
                return self._prop_dict["parentSection"]

        return None

    @parent_section.setter
    def parent_section(self, val):
        self._prop_dict["parentSection"] = val

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

