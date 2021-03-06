# -*- coding: utf-8 -*- 
'''
# Copyright (c) Microsoft Corporation.  All Rights Reserved.  Licensed under the MIT License.  See License in the project root for license information.
# 
#  This file was generated and any changes will be overwritten.
'''

from __future__ import unicode_literals
from ..model.workbook_chart_fill import WorkbookChartFill
from ..model.workbook_chart_font import WorkbookChartFont
from ..one_drive_object_base import OneDriveObjectBase


class WorkbookChartLegendFormat(OneDriveObjectBase):

    def __init__(self, prop_dict={}):
        self._prop_dict = prop_dict

    @property
    def fill(self):
        """
        Gets and sets the fill
        
        Returns: 
            :class:`WorkbookChartFill<onedrivesdk.model.workbook_chart_fill.WorkbookChartFill>`:
                The fill
        """
        if "fill" in self._prop_dict:
            if isinstance(self._prop_dict["fill"], OneDriveObjectBase):
                return self._prop_dict["fill"]
            else :
                self._prop_dict["fill"] = WorkbookChartFill(self._prop_dict["fill"])
                return self._prop_dict["fill"]

        return None

    @fill.setter
    def fill(self, val):
        self._prop_dict["fill"] = val

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

