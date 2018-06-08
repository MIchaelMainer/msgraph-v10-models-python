# -*- coding: utf-8 -*- 
'''
# Copyright (c) Microsoft Corporation.  All Rights Reserved.  Licensed under the MIT License.  See License in the project root for license information.
# 
#  This file was generated and any changes will be overwritten.
'''

from __future__ import unicode_literals
from ..model.filter_clause import FilterClause
from ..one_drive_object_base import OneDriveObjectBase


class FilterGroup(OneDriveObjectBase):

    def __init__(self, prop_dict={}):
        self._prop_dict = prop_dict

    @property
    def clauses(self):
        """
        Gets and sets the clauses
        
        Returns: 
            :class:`FilterClause<onedrivesdk.model.filter_clause.FilterClause>`:
                The clauses
        """
        if "clauses" in self._prop_dict:
            if isinstance(self._prop_dict["clauses"], OneDriveObjectBase):
                return self._prop_dict["clauses"]
            else :
                self._prop_dict["clauses"] = FilterClause(self._prop_dict["clauses"])
                return self._prop_dict["clauses"]

        return None

    @clauses.setter
    def clauses(self, val):
        self._prop_dict["clauses"] = val
    @property
    def name(self):
        """Gets and sets the name
        
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

