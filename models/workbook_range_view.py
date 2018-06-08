# -*- coding: utf-8 -*- 
'''
# Copyright (c) Microsoft Corporation.  All Rights Reserved.  Licensed under the MIT License.  See License in the project root for license information.
# 
#  This file was generated and any changes will be overwritten.
'''

from __future__ import unicode_literals
from ..model.json import Json
from ..one_drive_object_base import OneDriveObjectBase


class WorkbookRangeView(OneDriveObjectBase):

    def __init__(self, prop_dict={}):
        self._prop_dict = prop_dict

    @property
    def cell_addresses(self):
        """
        Gets and sets the cellAddresses
        
        Returns: 
            :class:`Json<onedrivesdk.model.json.Json>`:
                The cellAddresses
        """
        if "cellAddresses" in self._prop_dict:
            if isinstance(self._prop_dict["cellAddresses"], OneDriveObjectBase):
                return self._prop_dict["cellAddresses"]
            else :
                self._prop_dict["cellAddresses"] = Json(self._prop_dict["cellAddresses"])
                return self._prop_dict["cellAddresses"]

        return None

    @cell_addresses.setter
    def cell_addresses(self, val):
        self._prop_dict["cellAddresses"] = val

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
    def index(self):
        """
        Gets and sets the index
        
        Returns:
            int:
                The index
        """
        if "index" in self._prop_dict:
            return self._prop_dict["index"]
        else:
            return None

    @index.setter
    def index(self, val):
        self._prop_dict["index"] = val

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

