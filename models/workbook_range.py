# -*- coding: utf-8 -*- 
'''
# Copyright (c) Microsoft Corporation.  All Rights Reserved.  Licensed under the MIT License.  See License in the project root for license information.
# 
#  This file was generated and any changes will be overwritten.
'''

from __future__ import unicode_literals
from ..model.json import Json
from ..model.workbook_range_format import WorkbookRangeFormat
from ..model.workbook_range_sort import WorkbookRangeSort
from ..model.workbook_worksheet import WorkbookWorksheet
from ..one_drive_object_base import OneDriveObjectBase


class WorkbookRange(OneDriveObjectBase):

    def __init__(self, prop_dict={}):
        self._prop_dict = prop_dict

    @property
    def address(self):
        """
        Gets and sets the address
        
        Returns:
            str:
                The address
        """
        if "address" in self._prop_dict:
            return self._prop_dict["address"]
        else:
            return None

    @address.setter
    def address(self, val):
        self._prop_dict["address"] = val

    @property
    def address_local(self):
        """
        Gets and sets the addressLocal
        
        Returns:
            str:
                The addressLocal
        """
        if "addressLocal" in self._prop_dict:
            return self._prop_dict["addressLocal"]
        else:
            return None

    @address_local.setter
    def address_local(self, val):
        self._prop_dict["addressLocal"] = val

    @property
    def cell_count(self):
        """
        Gets and sets the cellCount
        
        Returns:
            int:
                The cellCount
        """
        if "cellCount" in self._prop_dict:
            return self._prop_dict["cellCount"]
        else:
            return None

    @cell_count.setter
    def cell_count(self, val):
        self._prop_dict["cellCount"] = val

    @property
    def column_count(self):
        """
        Gets and sets the columnCount
        
        Returns:
            int:
                The columnCount
        """
        if "columnCount" in self._prop_dict:
            return self._prop_dict["columnCount"]
        else:
            return None

    @column_count.setter
    def column_count(self, val):
        self._prop_dict["columnCount"] = val

    @property
    def column_hidden(self):
        """
        Gets and sets the columnHidden
        
        Returns:
            bool:
                The columnHidden
        """
        if "columnHidden" in self._prop_dict:
            return self._prop_dict["columnHidden"]
        else:
            return None

    @column_hidden.setter
    def column_hidden(self, val):
        self._prop_dict["columnHidden"] = val

    @property
    def column_index(self):
        """
        Gets and sets the columnIndex
        
        Returns:
            int:
                The columnIndex
        """
        if "columnIndex" in self._prop_dict:
            return self._prop_dict["columnIndex"]
        else:
            return None

    @column_index.setter
    def column_index(self, val):
        self._prop_dict["columnIndex"] = val

    @property
    def formulas(self):
        """
        Gets and sets the formulas
        
        Returns: 
            :class:`Json<onedrivesdk.model.json.Json>`:
                The formulas
        """
        if "formulas" in self._prop_dict:
            if isinstance(self._prop_dict["formulas"], OneDriveObjectBase):
                return self._prop_dict["formulas"]
            else :
                self._prop_dict["formulas"] = Json(self._prop_dict["formulas"])
                return self._prop_dict["formulas"]

        return None

    @formulas.setter
    def formulas(self, val):
        self._prop_dict["formulas"] = val

    @property
    def formulas_local(self):
        """
        Gets and sets the formulasLocal
        
        Returns: 
            :class:`Json<onedrivesdk.model.json.Json>`:
                The formulasLocal
        """
        if "formulasLocal" in self._prop_dict:
            if isinstance(self._prop_dict["formulasLocal"], OneDriveObjectBase):
                return self._prop_dict["formulasLocal"]
            else :
                self._prop_dict["formulasLocal"] = Json(self._prop_dict["formulasLocal"])
                return self._prop_dict["formulasLocal"]

        return None

    @formulas_local.setter
    def formulas_local(self, val):
        self._prop_dict["formulasLocal"] = val

    @property
    def formulas_r1_c1(self):
        """
        Gets and sets the formulasR1C1
        
        Returns: 
            :class:`Json<onedrivesdk.model.json.Json>`:
                The formulasR1C1
        """
        if "formulasR1C1" in self._prop_dict:
            if isinstance(self._prop_dict["formulasR1C1"], OneDriveObjectBase):
                return self._prop_dict["formulasR1C1"]
            else :
                self._prop_dict["formulasR1C1"] = Json(self._prop_dict["formulasR1C1"])
                return self._prop_dict["formulasR1C1"]

        return None

    @formulas_r1_c1.setter
    def formulas_r1_c1(self, val):
        self._prop_dict["formulasR1C1"] = val

    @property
    def hidden(self):
        """
        Gets and sets the hidden
        
        Returns:
            bool:
                The hidden
        """
        if "hidden" in self._prop_dict:
            return self._prop_dict["hidden"]
        else:
            return None

    @hidden.setter
    def hidden(self, val):
        self._prop_dict["hidden"] = val

    @property
    def number_format(self):
        """
        Gets and sets the numberFormat
        
        Returns: 
            :class:`Json<onedrivesdk.model.json.Json>`:
                The numberFormat
        """
        if "numberFormat" in self._prop_dict:
            if isinstance(self._prop_dict["numberFormat"], OneDriveObjectBase):
                return self._prop_dict["numberFormat"]
            else :
                self._prop_dict["numberFormat"] = Json(self._prop_dict["numberFormat"])
                return self._prop_dict["numberFormat"]

        return None

    @number_format.setter
    def number_format(self, val):
        self._prop_dict["numberFormat"] = val

    @property
    def row_count(self):
        """
        Gets and sets the rowCount
        
        Returns:
            int:
                The rowCount
        """
        if "rowCount" in self._prop_dict:
            return self._prop_dict["rowCount"]
        else:
            return None

    @row_count.setter
    def row_count(self, val):
        self._prop_dict["rowCount"] = val

    @property
    def row_hidden(self):
        """
        Gets and sets the rowHidden
        
        Returns:
            bool:
                The rowHidden
        """
        if "rowHidden" in self._prop_dict:
            return self._prop_dict["rowHidden"]
        else:
            return None

    @row_hidden.setter
    def row_hidden(self, val):
        self._prop_dict["rowHidden"] = val

    @property
    def row_index(self):
        """
        Gets and sets the rowIndex
        
        Returns:
            int:
                The rowIndex
        """
        if "rowIndex" in self._prop_dict:
            return self._prop_dict["rowIndex"]
        else:
            return None

    @row_index.setter
    def row_index(self, val):
        self._prop_dict["rowIndex"] = val

    @property
    def text(self):
        """
        Gets and sets the text
        
        Returns: 
            :class:`Json<onedrivesdk.model.json.Json>`:
                The text
        """
        if "text" in self._prop_dict:
            if isinstance(self._prop_dict["text"], OneDriveObjectBase):
                return self._prop_dict["text"]
            else :
                self._prop_dict["text"] = Json(self._prop_dict["text"])
                return self._prop_dict["text"]

        return None

    @text.setter
    def text(self, val):
        self._prop_dict["text"] = val

    @property
    def value_types(self):
        """
        Gets and sets the valueTypes
        
        Returns: 
            :class:`Json<onedrivesdk.model.json.Json>`:
                The valueTypes
        """
        if "valueTypes" in self._prop_dict:
            if isinstance(self._prop_dict["valueTypes"], OneDriveObjectBase):
                return self._prop_dict["valueTypes"]
            else :
                self._prop_dict["valueTypes"] = Json(self._prop_dict["valueTypes"])
                return self._prop_dict["valueTypes"]

        return None

    @value_types.setter
    def value_types(self, val):
        self._prop_dict["valueTypes"] = val

    @property
    def values(self):
        """
        Gets and sets the values
        
        Returns: 
            :class:`Json<onedrivesdk.model.json.Json>`:
                The values
        """
        if "values" in self._prop_dict:
            if isinstance(self._prop_dict["values"], OneDriveObjectBase):
                return self._prop_dict["values"]
            else :
                self._prop_dict["values"] = Json(self._prop_dict["values"])
                return self._prop_dict["values"]

        return None

    @values.setter
    def values(self, val):
        self._prop_dict["values"] = val

    @property
    def format(self):
        """
        Gets and sets the format
        
        Returns: 
            :class:`WorkbookRangeFormat<onedrivesdk.model.workbook_range_format.WorkbookRangeFormat>`:
                The format
        """
        if "format" in self._prop_dict:
            if isinstance(self._prop_dict["format"], OneDriveObjectBase):
                return self._prop_dict["format"]
            else :
                self._prop_dict["format"] = WorkbookRangeFormat(self._prop_dict["format"])
                return self._prop_dict["format"]

        return None

    @format.setter
    def format(self, val):
        self._prop_dict["format"] = val

    @property
    def sort(self):
        """
        Gets and sets the sort
        
        Returns: 
            :class:`WorkbookRangeSort<onedrivesdk.model.workbook_range_sort.WorkbookRangeSort>`:
                The sort
        """
        if "sort" in self._prop_dict:
            if isinstance(self._prop_dict["sort"], OneDriveObjectBase):
                return self._prop_dict["sort"]
            else :
                self._prop_dict["sort"] = WorkbookRangeSort(self._prop_dict["sort"])
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

