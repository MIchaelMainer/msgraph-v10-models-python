# -*- coding: utf-8 -*- 
'''
# Copyright (c) Microsoft Corporation.  All Rights Reserved.  Licensed under the MIT License.  See License in the project root for license information.
# 
#  This file was generated and any changes will be overwritten.
'''

from __future__ import unicode_literals
from ..one_drive_object_base import OneDriveObjectBase


class EducationOneNoteResource(OneDriveObjectBase):

    def __init__(self, prop_dict={}):
        self._prop_dict = prop_dict

    @property
    def section_name(self):
        """Gets and sets the sectionName
        
        Returns: 
            str:
                The sectionName
        """
        if "sectionName" in self._prop_dict:
            return self._prop_dict["sectionName"]
        else:
            return None

    @section_name.setter
    def section_name(self, val):
        self._prop_dict["sectionName"] = val

    @property
    def page_url(self):
        """Gets and sets the pageUrl
        
        Returns: 
            str:
                The pageUrl
        """
        if "pageUrl" in self._prop_dict:
            return self._prop_dict["pageUrl"]
        else:
            return None

    @page_url.setter
    def page_url(self, val):
        self._prop_dict["pageUrl"] = val

