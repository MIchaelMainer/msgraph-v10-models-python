# -*- coding: utf-8 -*- 
'''
# Copyright (c) Microsoft Corporation.  All Rights Reserved.  Licensed under the MIT License.  See License in the project root for license information.
# 
#  This file was generated and any changes will be overwritten.
'''

from __future__ import unicode_literals
from ..model.workbook_chart_line_format import WorkbookChartLineFormat
from ..one_drive_object_base import OneDriveObjectBase


class WorkbookChartGridlinesFormat(OneDriveObjectBase):

    def __init__(self, prop_dict={}):
        self._prop_dict = prop_dict

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

