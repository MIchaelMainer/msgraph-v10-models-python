# -*- coding: utf-8 -*- 
'''
# Copyright (c) Microsoft Corporation.  All Rights Reserved.  Licensed under the MIT License.  See License in the project root for license information.
# 
#  This file was generated and any changes will be overwritten.
'''

from __future__ import unicode_literals
from ..model.workbook_table_column import WorkbookTableColumn
from ..model.workbook_table_row import WorkbookTableRow
from ..model.workbook_table_sort import WorkbookTableSort
from ..model.workbook_worksheet import WorkbookWorksheet
from ..one_drive_object_base import OneDriveObjectBase


class WorkbookTable(OneDriveObjectBase):

    def __init__(self, prop_dict={}):
        self._prop_dict = prop_dict

    @property
    def highlight_first_column(self):
        """
        Gets and sets the highlightFirstColumn
        
        Returns:
            bool:
                The highlightFirstColumn
        """
        if "highlightFirstColumn" in self._prop_dict:
            return self._prop_dict["highlightFirstColumn"]
        else:
            return None

    @highlight_first_column.setter
    def highlight_first_column(self, val):
        self._prop_dict["highlightFirstColumn"] = val

    @property
    def highlight_last_column(self):
        """
        Gets and sets the highlightLastColumn
        
        Returns:
            bool:
                The highlightLastColumn
        """
        if "highlightLastColumn" in self._prop_dict:
            return self._prop_dict["highlightLastColumn"]
        else:
            return None

    @highlight_last_column.setter
    def highlight_last_column(self, val):
        self._prop_dict["highlightLastColumn"] = val

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
    def show_banded_columns(self):
        """
        Gets and sets the showBandedColumns
        
        Returns:
            bool:
                The showBandedColumns
        """
        if "showBandedColumns" in self._prop_dict:
            return self._prop_dict["showBandedColumns"]
        else:
            return None

    @show_banded_columns.setter
    def show_banded_columns(self, val):
        self._prop_dict["showBandedColumns"] = val

    @property
    def show_banded_rows(self):
        """
        Gets and sets the showBandedRows
        
        Returns:
            bool:
                The showBandedRows
        """
        if "showBandedRows" in self._prop_dict:
            return self._prop_dict["showBandedRows"]
        else:
            return None

    @show_banded_rows.setter
    def show_banded_rows(self, val):
        self._prop_dict["showBandedRows"] = val

    @property
    def show_filter_button(self):
        """
        Gets and sets the showFilterButton
        
        Returns:
            bool:
                The showFilterButton
        """
        if "showFilterButton" in self._prop_dict:
            return self._prop_dict["showFilterButton"]
        else:
            return None

    @show_filter_button.setter
    def show_filter_button(self, val):
        self._prop_dict["showFilterButton"] = val

    @property
    def show_headers(self):
        """
        Gets and sets the showHeaders
        
        Returns:
            bool:
                The showHeaders
        """
        if "showHeaders" in self._prop_dict:
            return self._prop_dict["showHeaders"]
        else:
            return None

    @show_headers.setter
    def show_headers(self, val):
        self._prop_dict["showHeaders"] = val

    @property
    def show_totals(self):
        """
        Gets and sets the showTotals
        
        Returns:
            bool:
                The showTotals
        """
        if "showTotals" in self._prop_dict:
            return self._prop_dict["showTotals"]
        else:
            return None

    @show_totals.setter
    def show_totals(self, val):
        self._prop_dict["showTotals"] = val

    @property
    def style(self):
        """
        Gets and sets the style
        
        Returns:
            str:
                The style
        """
        if "style" in self._prop_dict:
            return self._prop_dict["style"]
        else:
            return None

    @style.setter
    def style(self, val):
        self._prop_dict["style"] = val

    @property
    def columns(self):
        """Gets and sets the columns
        
        Returns: 
            :class:`ColumnsCollectionPage<onedrivesdk.request.columns_collection.ColumnsCollectionPage>`:
                The columns
        """
        if "columns" in self._prop_dict:
            return ColumnsCollectionPage(self._prop_dict["columns"])
        else:
            return None

    @property
    def rows(self):
        """Gets and sets the rows
        
        Returns: 
            :class:`RowsCollectionPage<onedrivesdk.request.rows_collection.RowsCollectionPage>`:
                The rows
        """
        if "rows" in self._prop_dict:
            return RowsCollectionPage(self._prop_dict["rows"])
        else:
            return None

    @property
    def sort(self):
        """
        Gets and sets the sort
        
        Returns: 
            :class:`WorkbookTableSort<onedrivesdk.model.workbook_table_sort.WorkbookTableSort>`:
                The sort
        """
        if "sort" in self._prop_dict:
            if isinstance(self._prop_dict["sort"], OneDriveObjectBase):
                return self._prop_dict["sort"]
            else :
                self._prop_dict["sort"] = WorkbookTableSort(self._prop_dict["sort"])
                return self._prop_dict["sort"]

        return None

    @sort.setter
    def sort(self, val):
        self._prop_dict["sort"] = val

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

