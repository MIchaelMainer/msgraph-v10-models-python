# -*- coding: utf-8 -*- 
'''
# Copyright (c) Microsoft Corporation.  All Rights Reserved.  Licensed under the MIT License.  See License in the project root for license information.
# 
#  This file was generated and any changes will be overwritten.
'''

from __future__ import unicode_literals
from ..model.workbook_chart_axis_title_format import WorkbookChartAxisTitleFormat
from ..one_drive_object_base import OneDriveObjectBase


class WorkbookChartAxisTitle(OneDriveObjectBase):

    def __init__(self, prop_dict={}):
        self._prop_dict = prop_dict

    @property
    def text(self):
        """
        Gets and sets the text
        
        Returns:
            str:
                The text
        """
        if "text" in self._prop_dict:
            return self._prop_dict["text"]
        else:
            return None

    @text.setter
    def text(self, val):
        self._prop_dict["text"] = val

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
    def format(self):
        """
        Gets and sets the format
        
        Returns: 
            :class:`WorkbookChartAxisTitleFormat<onedrivesdk.model.workbook_chart_axis_title_format.WorkbookChartAxisTitleFormat>`:
                The format
        """
        if "format" in self._prop_dict:
            if isinstance(self._prop_dict["format"], OneDriveObjectBase):
                return self._prop_dict["format"]
            else :
                self._prop_dict["format"] = WorkbookChartAxisTitleFormat(self._prop_dict["format"])
                return self._prop_dict["format"]

        return None

    @format.setter
    def format(self, val):
        self._prop_dict["format"] = val

