# -*- coding: utf-8 -*- 
'''
# Copyright (c) Microsoft Corporation.  All Rights Reserved.  Licensed under the MIT License.  See License in the project root for license information.
# 
#  This file was generated and any changes will be overwritten.
'''

from __future__ import unicode_literals
from ..model.recent_notebook_links import RecentNotebookLinks
from ..model.onenote_source_service import OnenoteSourceService
from datetime import datetime
from ..one_drive_object_base import OneDriveObjectBase


class RecentNotebook(OneDriveObjectBase):

    def __init__(self, prop_dict={}):
        self._prop_dict = prop_dict

    @property
    def display_name(self):
        """Gets and sets the displayName
        
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
    def last_accessed_time(self):
        """Gets and sets the lastAccessedTime
        
        Returns: 
            datetime:
                The lastAccessedTime
        """
        if "lastAccessedTime" in self._prop_dict:
            return datetime.strptime(self._prop_dict["lastAccessedTime"].replace("Z", ""), "%Y-%m-%dT%H:%M:%S.%f")
        else:
            return None

    @last_accessed_time.setter
    def last_accessed_time(self, val):
        self._prop_dict["lastAccessedTime"] = val.isoformat()+"Z"

    @property
    def links(self):
        """
        Gets and sets the links
        
        Returns: 
            :class:`RecentNotebookLinks<onedrivesdk.model.recent_notebook_links.RecentNotebookLinks>`:
                The links
        """
        if "links" in self._prop_dict:
            if isinstance(self._prop_dict["links"], OneDriveObjectBase):
                return self._prop_dict["links"]
            else :
                self._prop_dict["links"] = RecentNotebookLinks(self._prop_dict["links"])
                return self._prop_dict["links"]

        return None

    @links.setter
    def links(self, val):
        self._prop_dict["links"] = val
    @property
    def source_service(self):
        """
        Gets and sets the sourceService
        
        Returns: 
            :class:`OnenoteSourceService<onedrivesdk.model.onenote_source_service.OnenoteSourceService>`:
                The sourceService
        """
        if "sourceService" in self._prop_dict:
            if isinstance(self._prop_dict["sourceService"], OneDriveObjectBase):
                return self._prop_dict["sourceService"]
            else :
                self._prop_dict["sourceService"] = OnenoteSourceService(self._prop_dict["sourceService"])
                return self._prop_dict["sourceService"]

        return None

    @source_service.setter
    def source_service(self, val):
        self._prop_dict["sourceService"] = val
