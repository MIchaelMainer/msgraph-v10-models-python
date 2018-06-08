# -*- coding: utf-8 -*- 
'''
# Copyright (c) Microsoft Corporation.  All Rights Reserved.  Licensed under the MIT License.  See License in the project root for license information.
# 
#  This file was generated and any changes will be overwritten.
'''

from __future__ import unicode_literals
from ..model.workbook_chart_title_format import WorkbookChartTitleFormat
from ..one_drive_object_base import OneDriveObjectBase


class WorkbookChartTitle(OneDriveObjectBase):

    def __init__(self, prop_dict={}):
        self._prop_dict = prop_dict

    @property
    def overlay(self):
        """
        Gets and sets the overlay
        
        Returns:
            bool:
                The overlay
        """
        if "overlay" in self._prop_dict:
            return self._prop_dict["overlay"]
        else:
            return None

    @overlay.setter
    def overlay(self, val):
        self._prop_dict["overlay"] = val

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
            :class:`WorkbookChartTitleFormat<onedrivesdk.model.workbook_chart_title_format.WorkbookChartTitleFormat>`:
                The format
        """
        if "format" in self._prop_dict:
            if isinstance(self._prop_dict["format"], OneDriveObjectBase):
                return self._prop_dict["format"]
            else :
                self._prop_dict["format"] = WorkbookChartTitleFormat(self._prop_dict["format"])
                return self._prop_dict["format"]

        return None

    @format.setter
    def format(self, val):
        self._prop_dict["format"] = val

