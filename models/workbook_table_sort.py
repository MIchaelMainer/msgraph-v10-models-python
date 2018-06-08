# -*- coding: utf-8 -*- 
'''
# Copyright (c) Microsoft Corporation.  All Rights Reserved.  Licensed under the MIT License.  See License in the project root for license information.
# 
#  This file was generated and any changes will be overwritten.
'''

from __future__ import unicode_literals
from ..model.workbook_sort_field import WorkbookSortField
from ..one_drive_object_base import OneDriveObjectBase


class WorkbookTableSort(OneDriveObjectBase):

    def __init__(self, prop_dict={}):
        self._prop_dict = prop_dict

    @property
    def fields(self):
        """Gets and sets the fields
        
        Returns: 
            :class:`FieldsCollectionPage<onedrivesdk.request.fields_collection.FieldsCollectionPage>`:
                The fields
        """
        if "fields" in self._prop_dict:
            return FieldsCollectionPage(self._prop_dict["fields"])
        else:
            return None

    @property
    def match_case(self):
        """
        Gets and sets the matchCase
        
        Returns:
            bool:
                The matchCase
        """
        if "matchCase" in self._prop_dict:
            return self._prop_dict["matchCase"]
        else:
            return None

    @match_case.setter
    def match_case(self, val):
        self._prop_dict["matchCase"] = val

    @property
    def method(self):
        """
        Gets and sets the method
        
        Returns:
            str:
                The method
        """
        if "method" in self._prop_dict:
            return self._prop_dict["method"]
        else:
            return None

    @method.setter
    def method(self, val):
        self._prop_dict["method"] = val

