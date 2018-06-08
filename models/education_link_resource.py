# -*- coding: utf-8 -*- 
'''
# Copyright (c) Microsoft Corporation.  All Rights Reserved.  Licensed under the MIT License.  See License in the project root for license information.
# 
#  This file was generated and any changes will be overwritten.
'''

from __future__ import unicode_literals
from ..one_drive_object_base import OneDriveObjectBase


class EducationLinkResource(OneDriveObjectBase):

    def __init__(self, prop_dict={}):
        self._prop_dict = prop_dict

    @property
    def link(self):
        """Gets and sets the link
        
        Returns: 
            str:
                The link
        """
        if "link" in self._prop_dict:
            return self._prop_dict["link"]
        else:
            return None

    @link.setter
    def link(self, val):
        self._prop_dict["link"] = val

