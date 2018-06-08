# -*- coding: utf-8 -*- 
'''
# Copyright (c) Microsoft Corporation.  All Rights Reserved.  Licensed under the MIT License.  See License in the project root for license information.
# 
#  This file was generated and any changes will be overwritten.
'''

from __future__ import unicode_literals
from ..model.workbook_chart_axes import WorkbookChartAxes
from ..model.workbook_chart_data_labels import WorkbookChartDataLabels
from ..model.workbook_chart_area_format import WorkbookChartAreaFormat
from ..model.workbook_chart_legend import WorkbookChartLegend
from ..model.workbook_chart_series import WorkbookChartSeries
from ..model.workbook_chart_title import WorkbookChartTitle
from ..model.workbook_worksheet import WorkbookWorksheet
from ..one_drive_object_base import OneDriveObjectBase


class WorkbookChart(OneDriveObjectBase):

    def __init__(self, prop_dict={}):
        self._prop_dict = prop_dict

    @property
    def height(self):
        """
        Gets and sets the height
        
        Returns:
            float:
                The height
        """
        if "height" in self._prop_dict:
            return self._prop_dict["height"]
        else:
            return None

    @height.setter
    def height(self, val):
        self._prop_dict["height"] = val

    @property
    def left(self):
        """
        Gets and sets the left
        
        Returns:
            float:
                The left
        """
        if "left" in self._prop_dict:
            return self._prop_dict["left"]
        else:
            return None

    @left.setter
    def left(self, val):
        self._prop_dict["left"] = val

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
    def top(self):
        """
        Gets and sets the top
        
        Returns:
            float:
                The top
        """
        if "top" in self._prop_dict:
            return self._prop_dict["top"]
        else:
            return None

    @top.setter
    def top(self, val):
        self._prop_dict["top"] = val

    @property
    def width(self):
        """
        Gets and sets the width
        
        Returns:
            float:
                The width
        """
        if "width" in self._prop_dict:
            return self._prop_dict["width"]
        else:
            return None

    @width.setter
    def width(self, val):
        self._prop_dict["width"] = val

    @property
    def axes(self):
        """
        Gets and sets the axes
        
        Returns: 
            :class:`WorkbookChartAxes<onedrivesdk.model.workbook_chart_axes.WorkbookChartAxes>`:
                The axes
        """
        if "axes" in self._prop_dict:
            if isinstance(self._prop_dict["axes"], OneDriveObjectBase):
                return self._prop_dict["axes"]
            else :
                self._prop_dict["axes"] = WorkbookChartAxes(self._prop_dict["axes"])
                return self._prop_dict["axes"]

        return None

    @axes.setter
    def axes(self, val):
        self._prop_dict["axes"] = val

    @property
    def data_labels(self):
        """
        Gets and sets the dataLabels
        
        Returns: 
            :class:`WorkbookChartDataLabels<onedrivesdk.model.workbook_chart_data_labels.WorkbookChartDataLabels>`:
                The dataLabels
        """
        if "dataLabels" in self._prop_dict:
            if isinstance(self._prop_dict["dataLabels"], OneDriveObjectBase):
                return self._prop_dict["dataLabels"]
            else :
                self._prop_dict["dataLabels"] = WorkbookChartDataLabels(self._prop_dict["dataLabels"])
                return self._prop_dict["dataLabels"]

        return None

    @data_labels.setter
    def data_labels(self, val):
        self._prop_dict["dataLabels"] = val

    @property
    def format(self):
        """
        Gets and sets the format
        
        Returns: 
            :class:`WorkbookChartAreaFormat<onedrivesdk.model.workbook_chart_area_format.WorkbookChartAreaFormat>`:
                The format
        """
        if "format" in self._prop_dict:
            if isinstance(self._prop_dict["format"], OneDriveObjectBase):
                return self._prop_dict["format"]
            else :
                self._prop_dict["format"] = WorkbookChartAreaFormat(self._prop_dict["format"])
                return self._prop_dict["format"]

        return None

    @format.setter
    def format(self, val):
        self._prop_dict["format"] = val

    @property
    def legend(self):
        """
        Gets and sets the legend
        
        Returns: 
            :class:`WorkbookChartLegend<onedrivesdk.model.workbook_chart_legend.WorkbookChartLegend>`:
                The legend
        """
        if "legend" in self._prop_dict:
            if isinstance(self._prop_dict["legend"], OneDriveObjectBase):
                return self._prop_dict["legend"]
            else :
                self._prop_dict["legend"] = WorkbookChartLegend(self._prop_dict["legend"])
                return self._prop_dict["legend"]

        return None

    @legend.setter
    def legend(self, val):
        self._prop_dict["legend"] = val

    @property
    def series(self):
        """Gets and sets the series
        
        Returns: 
            :class:`SeriesCollectionPage<onedrivesdk.request.series_collection.SeriesCollectionPage>`:
                The series
        """
        if "series" in self._prop_dict:
            return SeriesCollectionPage(self._prop_dict["series"])
        else:
            return None

    @property
    def title(self):
        """
        Gets and sets the title
        
        Returns: 
            :class:`WorkbookChartTitle<onedrivesdk.model.workbook_chart_title.WorkbookChartTitle>`:
                The title
        """
        if "title" in self._prop_dict:
            if isinstance(self._prop_dict["title"], OneDriveObjectBase):
                return self._prop_dict["title"]
            else :
                self._prop_dict["title"] = WorkbookChartTitle(self._prop_dict["title"])
                return self._prop_dict["title"]

        return None

    @title.setter
    def title(self, val):
        self._prop_dict["title"] = val

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

