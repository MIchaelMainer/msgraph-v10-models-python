# -*- coding: utf-8 -*- 
'''
# Copyright (c) Microsoft Corporation.  All Rights Reserved.  Licensed under the MIT License.  See License in the project root for license information.
# 
#  This file was generated and any changes will be overwritten.
'''

from __future__ import unicode_literals
from ..one_drive_object_base import OneDriveObjectBase


class MentionsPreview(OneDriveObjectBase):

    def __init__(self, prop_dict={}):
        self._prop_dict = prop_dict

    @property
    def is_mentioned(self):
        """Gets and sets the isMentioned
        
        Returns: 
            bool:
                The isMentioned
        """
        if "isMentioned" in self._prop_dict:
            return self._prop_dict["isMentioned"]
        else:
            return None

    @is_mentioned.setter
    def is_mentioned(self, val):
        self._prop_dict["isMentioned"] = val

