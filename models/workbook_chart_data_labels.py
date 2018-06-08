# -*- coding: utf-8 -*- 
'''
# Copyright (c) Microsoft Corporation.  All Rights Reserved.  Licensed under the MIT License.  See License in the project root for license information.
# 
#  This file was generated and any changes will be overwritten.
'''

from __future__ import unicode_literals
from ..model.workbook_chart_data_label_format import WorkbookChartDataLabelFormat
from ..one_drive_object_base import OneDriveObjectBase


class WorkbookChartDataLabels(OneDriveObjectBase):

    def __init__(self, prop_dict={}):
        self._prop_dict = prop_dict

    @property
    def position(self):
        """
        Gets and sets the position
        
        Returns:
            str:
                The position
        """
        if "position" in self._prop_dict:
            return self._prop_dict["position"]
        else:
            return None

    @position.setter
    def position(self, val):
        self._prop_dict["position"] = val

    @property
    def separator(self):
        """
        Gets and sets the separator
        
        Returns:
            str:
                The separator
        """
        if "separator" in self._prop_dict:
            return self._prop_dict["separator"]
        else:
            return None

    @separator.setter
    def separator(self, val):
        self._prop_dict["separator"] = val

    @property
    def show_bubble_size(self):
        """
        Gets and sets the showBubbleSize
        
        Returns:
            bool:
                The showBubbleSize
        """
        if "showBubbleSize" in self._prop_dict:
            return self._prop_dict["showBubbleSize"]
        else:
            return None

    @show_bubble_size.setter
    def show_bubble_size(self, val):
        self._prop_dict["showBubbleSize"] = val

    @property
    def show_category_name(self):
        """
        Gets and sets the showCategoryName
        
        Returns:
            bool:
                The showCategoryName
        """
        if "showCategoryName" in self._prop_dict:
            return self._prop_dict["showCategoryName"]
        else:
            return None

    @show_category_name.setter
    def show_category_name(self, val):
        self._prop_dict["showCategoryName"] = val

    @property
    def show_legend_key(self):
        """
        Gets and sets the showLegendKey
        
        Returns:
            bool:
                The showLegendKey
        """
        if "showLegendKey" in self._prop_dict:
            return self._prop_dict["showLegendKey"]
        else:
            return None

    @show_legend_key.setter
    def show_legend_key(self, val):
        self._prop_dict["showLegendKey"] = val

    @property
    def show_percentage(self):
        """
        Gets and sets the showPercentage
        
        Returns:
            bool:
                The showPercentage
        """
        if "showPercentage" in self._prop_dict:
            return self._prop_dict["showPercentage"]
        else:
            return None

    @show_percentage.setter
    def show_percentage(self, val):
        self._prop_dict["showPercentage"] = val

    @property
    def show_series_name(self):
        """
        Gets and sets the showSeriesName
        
        Returns:
            bool:
                The showSeriesName
        """
        if "showSeriesName" in self._prop_dict:
            return self._prop_dict["showSeriesName"]
        else:
            return None

    @show_series_name.setter
    def show_series_name(self, val):
        self._prop_dict["showSeriesName"] = val

    @property
    def show_value(self):
        """
        Gets and sets the showValue
        
        Returns:
            bool:
                The showValue
        """
        if "showValue" in self._prop_dict:
            return self._prop_dict["showValue"]
        else:
            return None

    @show_value.setter
    def show_value(self, val):
        self._prop_dict["showValue"] = val

    @property
    def format(self):
        """
        Gets and sets the format
        
        Returns: 
            :class:`WorkbookChartDataLabelFormat<onedrivesdk.model.workbook_chart_data_label_format.WorkbookChartDataLabelFormat>`:
                The format
        """
        if "format" in self._prop_dict:
            if isinstance(self._prop_dict["format"], OneDriveObjectBase):
                return self._prop_dict["format"]
            else :
                self._prop_dict["format"] = WorkbookChartDataLabelFormat(self._prop_dict["format"])
                return self._prop_dict["format"]

        return None

    @format.setter
    def format(self, val):
        self._prop_dict["format"] = val

