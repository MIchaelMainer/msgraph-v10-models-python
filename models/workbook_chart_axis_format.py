# -*- coding: utf-8 -*- 
'''
# Copyright (c) Microsoft Corporation.  All Rights Reserved.  Licensed under the MIT License.  See License in the project root for license information.
# 
#  This file was generated and any changes will be overwritten.
'''

from __future__ import unicode_literals
from ..model.workbook_chart_font import WorkbookChartFont
from ..model.workbook_chart_line_format import WorkbookChartLineFormat
from ..one_drive_object_base import OneDriveObjectBase


class WorkbookChartAxisFormat(OneDriveObjectBase):

    def __init__(self, prop_dict={}):
        self._prop_dict = prop_dict

    @property
    def font(self):
        """
        Gets and sets the font
        
        Returns: 
            :class:`WorkbookChartFont<onedrivesdk.model.workbook_chart_font.WorkbookChartFont>`:
                The font
        """
        if "font" in self._prop_dict:
            if isinstance(self._prop_dict["font"], OneDriveObjectBase):
                return self._prop_dict["font"]
            else :
                self._prop_dict["font"] = WorkbookChartFont(self._prop_dict["font"])
                return self._prop_dict["font"]

        return None

    @font.setter
    def font(self, val):
        self._prop_dict["font"] = val

    @property
    def line(self):
        """
        Gets and sets the line
        
        Returns: 
            :class:`WorkbookChartLineFormat<onedrivesdk.model.workbook_chart_line_format.WorkbookChartLineFormat>`:
                The line
        """
        if "line" in self._prop_dict:
            if isinstance(self._prop_dict["line"], OneDriveObjectBase):
                return self._prop_dict["line"]
            else :
                self._prop_dict["line"] = WorkbookChartLineFormat(self._prop_dict["line"])
                return self._prop_dict["line"]

        return None

    @line.setter
    def line(self, val):
        self._prop_dict["line"] = val

