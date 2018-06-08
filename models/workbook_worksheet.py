# -*- coding: utf-8 -*- 
'''
# Copyright (c) Microsoft Corporation.  All Rights Reserved.  Licensed under the MIT License.  See License in the project root for license information.
# 
#  This file was generated and any changes will be overwritten.
'''

from __future__ import unicode_literals
from ..model.workbook_chart import WorkbookChart
from ..model.workbook_named_item import WorkbookNamedItem
from ..model.workbook_pivot_table import WorkbookPivotTable
from ..model.workbook_worksheet_protection import WorkbookWorksheetProtection
from ..model.workbook_table import WorkbookTable
from ..one_drive_object_base import OneDriveObjectBase


class WorkbookWorksheet(OneDriveObjectBase):

    def __init__(self, prop_dict={}):
        self._prop_dict = prop_dict

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
    def position(self):
        """
        Gets and sets the position
        
        Returns:
            int:
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
    def visibility(self):
        """
        Gets and sets the visibility
        
        Returns:
            str:
                The visibility
        """
        if "visibility" in self._prop_dict:
            return self._prop_dict["visibility"]
        else:
            return None

    @visibility.setter
    def visibility(self, val):
        self._prop_dict["visibility"] = val

    @property
    def charts(self):
        """Gets and sets the charts
        
        Returns: 
            :class:`ChartsCollectionPage<onedrivesdk.request.charts_collection.ChartsCollectionPage>`:
                The charts
        """
        if "charts" in self._prop_dict:
            return ChartsCollectionPage(self._prop_dict["charts"])
        else:
            return None

    @property
    def names(self):
        """Gets and sets the names
        
        Returns: 
            :class:`NamesCollectionPage<onedrivesdk.request.names_collection.NamesCollectionPage>`:
                The names
        """
        if "names" in self._prop_dict:
            return NamesCollectionPage(self._prop_dict["names"])
        else:
            return None

    @property
    def pivot_tables(self):
        """Gets and sets the pivotTables
        
        Returns: 
            :class:`PivotTablesCollectionPage<onedrivesdk.request.pivot_tables_collection.PivotTablesCollectionPage>`:
                The pivotTables
        """
        if "pivotTables" in self._prop_dict:
            return PivotTablesCollectionPage(self._prop_dict["pivotTables"])
        else:
            return None

    @property
    def protection(self):
        """
        Gets and sets the protection
        
        Returns: 
            :class:`WorkbookWorksheetProtection<onedrivesdk.model.workbook_worksheet_protection.WorkbookWorksheetProtection>`:
                The protection
        """
        if "protection" in self._prop_dict:
            if isinstance(self._prop_dict["protection"], OneDriveObjectBase):
                return self._prop_dict["protection"]
            else :
                self._prop_dict["protection"] = WorkbookWorksheetProtection(self._prop_dict["protection"])
                return self._prop_dict["protection"]

        return None

    @protection.setter
    def protection(self, val):
        self._prop_dict["protection"] = val

    @property
    def tables(self):
        """Gets and sets the tables
        
        Returns: 
            :class:`TablesCollectionPage<onedrivesdk.request.tables_collection.TablesCollectionPage>`:
                The tables
        """
        if "tables" in self._prop_dict:
            return TablesCollectionPage(self._prop_dict["tables"])
        else:
            return None

