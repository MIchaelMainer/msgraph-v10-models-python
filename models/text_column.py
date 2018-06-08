# -*- coding: utf-8 -*- 
'''
# Copyright (c) Microsoft Corporation.  All Rights Reserved.  Licensed under the MIT License.  See License in the project root for license information.
# 
#  This file was generated and any changes will be overwritten.
'''

from __future__ import unicode_literals
from ..one_drive_object_base import OneDriveObjectBase


class TextColumn(OneDriveObjectBase):

    def __init__(self, prop_dict={}):
        self._prop_dict = prop_dict

    @property
    def allow_multiple_lines(self):
        """Gets and sets the allowMultipleLines
        
        Returns: 
            bool:
                The allowMultipleLines
        """
        if "allowMultipleLines" in self._prop_dict:
            return self._prop_dict["allowMultipleLines"]
        else:
            return None

    @allow_multiple_lines.setter
    def allow_multiple_lines(self, val):
        self._prop_dict["allowMultipleLines"] = val

    @property
    def append_changes_to_existing_text(self):
        """Gets and sets the appendChangesToExistingText
        
        Returns: 
            bool:
                The appendChangesToExistingText
        """
        if "appendChangesToExistingText" in self._prop_dict:
            return self._prop_dict["appendChangesToExistingText"]
        else:
            return None

    @append_changes_to_existing_text.setter
    def append_changes_to_existing_text(self, val):
        self._prop_dict["appendChangesToExistingText"] = val

    @property
    def lines_for_editing(self):
        """Gets and sets the linesForEditing
        
        Returns: 
            int:
                The linesForEditing
        """
        if "linesForEditing" in self._prop_dict:
            return self._prop_dict["linesForEditing"]
        else:
            return None

    @lines_for_editing.setter
    def lines_for_editing(self, val):
        self._prop_dict["linesForEditing"] = val

    @property
    def max_length(self):
        """Gets and sets the maxLength
        
        Returns: 
            int:
                The maxLength
        """
        if "maxLength" in self._prop_dict:
            return self._prop_dict["maxLength"]
        else:
            return None

    @max_length.setter
    def max_length(self, val):
        self._prop_dict["maxLength"] = val

    @property
    def text_type(self):
        """Gets and sets the textType
        
        Returns: 
            str:
                The textType
        """
        if "textType" in self._prop_dict:
            return self._prop_dict["textType"]
        else:
            return None

    @text_type.setter
    def text_type(self, val):
        self._prop_dict["textType"] = val

