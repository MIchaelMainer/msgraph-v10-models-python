# -*- coding: utf-8 -*- 
'''
# Copyright (c) Microsoft Corporation.  All Rights Reserved.  Licensed under the MIT License.  See License in the project root for license information.
# 
#  This file was generated and any changes will be overwritten.
'''

from __future__ import unicode_literals
from ..model.json import Json
from ..model.workbook_worksheet import WorkbookWorksheet
from ..one_drive_object_base import OneDriveObjectBase


class WorkbookNamedItem(OneDriveObjectBase):

    def __init__(self, prop_dict={}):
        self._prop_dict = prop_dict

    @property
    def comment(self):
        """
        Gets and sets the comment
        
        Returns:
            str:
                The comment
        """
        if "comment" in self._prop_dict:
            return self._prop_dict["comment"]
        else:
            return None

    @comment.setter
    def comment(self, val):
        self._prop_dict["comment"] = val

    @property
    def name(self):
        """
        Gets and sets the name
        
        Returns:
            str:
                The name
        """
        if "name" in self._prop_dict:
            return self._prop_dict["name"]
        else:
            return None

    @name.setter
    def name(self, val):
        self._prop_dict["name"] = val

    @property
    def scope(self):
        """
        Gets and sets the scope
        
        Returns:
            str:
                The scope
        """
        if "scope" in self._prop_dict:
            return self._prop_dict["scope"]
        else:
            return None

    @scope.setter
    def scope(self, val):
        self._prop_dict["scope"] = val

    @property
    def type(self):
        """
        Gets and sets the type
        
        Returns:
            str:
                The type
        """
        if "type" in self._prop_dict:
            return self._prop_dict["type"]
        else:
            return None

    @type.setter
    def type(self, val):
        self._prop_dict["type"] = val

    @property
    def value(self):
        """
        Gets and sets the value
        
        Returns: 
            :class:`Json<onedrivesdk.model.json.Json>`:
                The value
        """
        if "value" in self._prop_dict:
            if isinstance(self._prop_dict["value"], OneDriveObjectBase):
                return self._prop_dict["value"]
            else :
                self._prop_dict["value"] = Json(self._prop_dict["value"])
                return self._prop_dict["value"]

        return None

    @value.setter
    def value(self, val):
        self._prop_dict["value"] = val

    @property
    def visible(self):
        """
        Gets and sets the visible
        
        Returns:
            bool:
                The visible
        """
        if "visible" in self._prop_dict:
            return self._prop_dict["visible"]
        else:
            return None

    @visible.setter
    def visible(self, val):
        self._prop_dict["visible"] = val

    @property
    def worksheet(self):
        """
        Gets and sets the worksheet
        
        Returns: 
            :class:`WorkbookWorksheet<onedrivesdk.model.workbook_worksheet.WorkbookWorksheet>`:
                The worksheet
        """
        if "worksheet" in self._prop_dict:
            if isinstance(self._prop_dict["worksheet"], OneDriveObjectBase):
                return self._prop_dict["worksheet"]
            else :
                self._prop_dict["worksheet"] = WorkbookWorksheet(self._prop_dict["worksheet"])
                return self._prop_dict["worksheet"]

        return None

    @worksheet.setter
    def worksheet(self, val):
        self._prop_dict["worksheet"] = val

