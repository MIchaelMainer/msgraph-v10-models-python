# -*- coding: utf-8 -*- 
'''
# Copyright (c) Microsoft Corporation.  All Rights Reserved.  Licensed under the MIT License.  See License in the project root for license information.
# 
#  This file was generated and any changes will be overwritten.
'''

from __future__ import unicode_literals
from ..model.workbook_chart_axis import WorkbookChartAxis
from ..one_drive_object_base import OneDriveObjectBase


class WorkbookChartAxes(OneDriveObjectBase):

    def __init__(self, prop_dict={}):
        self._prop_dict = prop_dict

    @property
    def category_axis(self):
        """
        Gets and sets the categoryAxis
        
        Returns: 
            :class:`WorkbookChartAxis<onedrivesdk.model.workbook_chart_axis.WorkbookChartAxis>`:
                The categoryAxis
        """
        if "categoryAxis" in self._prop_dict:
            if isinstance(self._prop_dict["categoryAxis"], OneDriveObjectBase):
                return self._prop_dict["categoryAxis"]
            else :
                self._prop_dict["categoryAxis"] = WorkbookChartAxis(self._prop_dict["categoryAxis"])
                return self._prop_dict["categoryAxis"]

        return None

    @category_axis.setter
    def category_axis(self, val):
        self._prop_dict["categoryAxis"] = val

    @property
    def series_axis(self):
        """
        Gets and sets the seriesAxis
        
        Returns: 
            :class:`WorkbookChartAxis<onedrivesdk.model.workbook_chart_axis.WorkbookChartAxis>`:
                The seriesAxis
        """
        if "seriesAxis" in self._prop_dict:
            if isinstance(self._prop_dict["seriesAxis"], OneDriveObjectBase):
                return self._prop_dict["seriesAxis"]
            else :
                self._prop_dict["seriesAxis"] = WorkbookChartAxis(self._prop_dict["seriesAxis"])
                return self._prop_dict["seriesAxis"]

        return None

    @series_axis.setter
    def series_axis(self, val):
        self._prop_dict["seriesAxis"] = val

    @property
    def value_axis(self):
        """
        Gets and sets the valueAxis
        
        Returns: 
            :class:`WorkbookChartAxis<onedrivesdk.model.workbook_chart_axis.WorkbookChartAxis>`:
                The valueAxis
        """
        if "valueAxis" in self._prop_dict:
            if isinstance(self._prop_dict["valueAxis"], OneDriveObjectBase):
                return self._prop_dict["valueAxis"]
            else :
                self._prop_dict["valueAxis"] = WorkbookChartAxis(self._prop_dict["valueAxis"])
                return self._prop_dict["valueAxis"]

        return None

    @value_axis.setter
    def value_axis(self, val):
        self._prop_dict["valueAxis"] = val

