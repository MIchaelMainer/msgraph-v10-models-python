# -*- coding: utf-8 -*- 
'''
# Copyright (c) Microsoft Corporation.  All Rights Reserved.  Licensed under the MIT License.  See License in the project root for license information.
# 
#  This file was generated and any changes will be overwritten.
'''

from __future__ import unicode_literals
from ..model.workbook_application import WorkbookApplication
from ..model.workbook_named_item import WorkbookNamedItem
from ..model.workbook_table import WorkbookTable
from ..model.workbook_worksheet import WorkbookWorksheet
from ..model.workbook_functions import WorkbookFunctions
from ..one_drive_object_base import OneDriveObjectBase


class Workbook(OneDriveObjectBase):

    def __init__(self, prop_dict={}):
        self._prop_dict = prop_dict

    @property
    def application(self):
        """
        Gets and sets the application
        
        Returns: 
            :class:`WorkbookApplication<onedrivesdk.model.workbook_application.WorkbookApplication>`:
                The application
        """
        if "application" in self._prop_dict:
            if isinstance(self._prop_dict["application"], OneDriveObjectBase):
                return self._prop_dict["application"]
            else :
                self._prop_dict["application"] = WorkbookApplication(self._prop_dict["application"])
                return self._prop_dict["application"]

        return None

    @application.setter
    def application(self, val):
        self._prop_dict["application"] = val

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

    @property
    def worksheets(self):
        """Gets and sets the worksheets
        
        Returns: 
            :class:`WorksheetsCollectionPage<onedrivesdk.request.worksheets_collection.WorksheetsCollectionPage>`:
                The worksheets
        """
        if "worksheets" in self._prop_dict:
            return WorksheetsCollectionPage(self._prop_dict["worksheets"])
        else:
            return None

    @property
    def functions(self):
        """
        Gets and sets the functions
        
        Returns: 
            :class:`WorkbookFunctions<onedrivesdk.model.workbook_functions.WorkbookFunctions>`:
                The functions
        """
        if "functions" in self._prop_dict:
            if isinstance(self._prop_dict["functions"], OneDriveObjectBase):
                return self._prop_dict["functions"]
            else :
                self._prop_dict["functions"] = WorkbookFunctions(self._prop_dict["functions"])
                return self._prop_dict["functions"]

        return None

    @functions.setter
    def functions(self, val):
        self._prop_dict["functions"] = val

