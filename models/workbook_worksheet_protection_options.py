# -*- coding: utf-8 -*- 
'''
# Copyright (c) Microsoft Corporation.  All Rights Reserved.  Licensed under the MIT License.  See License in the project root for license information.
# 
#  This file was generated and any changes will be overwritten.
'''

from __future__ import unicode_literals
from ..one_drive_object_base import OneDriveObjectBase


class WorkbookWorksheetProtectionOptions(OneDriveObjectBase):

    def __init__(self, prop_dict={}):
        self._prop_dict = prop_dict

    @property
    def allow_auto_filter(self):
        """Gets and sets the allowAutoFilter
        
        Returns: 
            bool:
                The allowAutoFilter
        """
        if "allowAutoFilter" in self._prop_dict:
            return self._prop_dict["allowAutoFilter"]
        else:
            return None

    @allow_auto_filter.setter
    def allow_auto_filter(self, val):
        self._prop_dict["allowAutoFilter"] = val

    @property
    def allow_delete_columns(self):
        """Gets and sets the allowDeleteColumns
        
        Returns: 
            bool:
                The allowDeleteColumns
        """
        if "allowDeleteColumns" in self._prop_dict:
            return self._prop_dict["allowDeleteColumns"]
        else:
            return None

    @allow_delete_columns.setter
    def allow_delete_columns(self, val):
        self._prop_dict["allowDeleteColumns"] = val

    @property
    def allow_delete_rows(self):
        """Gets and sets the allowDeleteRows
        
        Returns: 
            bool:
                The allowDeleteRows
        """
        if "allowDeleteRows" in self._prop_dict:
            return self._prop_dict["allowDeleteRows"]
        else:
            return None

    @allow_delete_rows.setter
    def allow_delete_rows(self, val):
        self._prop_dict["allowDeleteRows"] = val

    @property
    def allow_format_cells(self):
        """Gets and sets the allowFormatCells
        
        Returns: 
            bool:
                The allowFormatCells
        """
        if "allowFormatCells" in self._prop_dict:
            return self._prop_dict["allowFormatCells"]
        else:
            return None

    @allow_format_cells.setter
    def allow_format_cells(self, val):
        self._prop_dict["allowFormatCells"] = val

    @property
    def allow_format_columns(self):
        """Gets and sets the allowFormatColumns
        
        Returns: 
            bool:
                The allowFormatColumns
        """
        if "allowFormatColumns" in self._prop_dict:
            return self._prop_dict["allowFormatColumns"]
        else:
            return None

    @allow_format_columns.setter
    def allow_format_columns(self, val):
        self._prop_dict["allowFormatColumns"] = val

    @property
    def allow_format_rows(self):
        """Gets and sets the allowFormatRows
        
        Returns: 
            bool:
                The allowFormatRows
        """
        if "allowFormatRows" in self._prop_dict:
            return self._prop_dict["allowFormatRows"]
        else:
            return None

    @allow_format_rows.setter
    def allow_format_rows(self, val):
        self._prop_dict["allowFormatRows"] = val

    @property
    def allow_insert_columns(self):
        """Gets and sets the allowInsertColumns
        
        Returns: 
            bool:
                The allowInsertColumns
        """
        if "allowInsertColumns" in self._prop_dict:
            return self._prop_dict["allowInsertColumns"]
        else:
            return None

    @allow_insert_columns.setter
    def allow_insert_columns(self, val):
        self._prop_dict["allowInsertColumns"] = val

    @property
    def allow_insert_hyperlinks(self):
        """Gets and sets the allowInsertHyperlinks
        
        Returns: 
            bool:
                The allowInsertHyperlinks
        """
        if "allowInsertHyperlinks" in self._prop_dict:
            return self._prop_dict["allowInsertHyperlinks"]
        else:
            return None

    @allow_insert_hyperlinks.setter
    def allow_insert_hyperlinks(self, val):
        self._prop_dict["allowInsertHyperlinks"] = val

    @property
    def allow_insert_rows(self):
        """Gets and sets the allowInsertRows
        
        Returns: 
            bool:
                The allowInsertRows
        """
        if "allowInsertRows" in self._prop_dict:
            return self._prop_dict["allowInsertRows"]
        else:
            return None

    @allow_insert_rows.setter
    def allow_insert_rows(self, val):
        self._prop_dict["allowInsertRows"] = val

    @property
    def allow_pivot_tables(self):
        """Gets and sets the allowPivotTables
        
        Returns: 
            bool:
                The allowPivotTables
        """
        if "allowPivotTables" in self._prop_dict:
            return self._prop_dict["allowPivotTables"]
        else:
            return None

    @allow_pivot_tables.setter
    def allow_pivot_tables(self, val):
        self._prop_dict["allowPivotTables"] = val

    @property
    def allow_sort(self):
        """Gets and sets the allowSort
        
        Returns: 
            bool:
                The allowSort
        """
        if "allowSort" in self._prop_dict:
            return self._prop_dict["allowSort"]
        else:
            return None

    @allow_sort.setter
    def allow_sort(self, val):
        self._prop_dict["allowSort"] = val

