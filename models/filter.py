# -*- coding: utf-8 -*- 
'''
# Copyright (c) Microsoft Corporation.  All Rights Reserved.  Licensed under the MIT License.  See License in the project root for license information.
# 
#  This file was generated and any changes will be overwritten.
'''

from __future__ import unicode_literals
from ..model.filter_group import FilterGroup
from ..one_drive_object_base import OneDriveObjectBase


class Filter(OneDriveObjectBase):

    def __init__(self, prop_dict={}):
        self._prop_dict = prop_dict

    @property
    def groups(self):
        """
        Gets and sets the groups
        
        Returns: 
            :class:`FilterGroup<onedrivesdk.model.filter_group.FilterGroup>`:
                The groups
        """
        if "groups" in self._prop_dict:
            if isinstance(self._prop_dict["groups"], OneDriveObjectBase):
                return self._prop_dict["groups"]
            else :
                self._prop_dict["groups"] = FilterGroup(self._prop_dict["groups"])
                return self._prop_dict["groups"]

        return None

    @groups.setter
    def groups(self, val):
        self._prop_dict["groups"] = val
    @property
    def input_filter_groups(self):
        """
        Gets and sets the inputFilterGroups
        
        Returns: 
            :class:`FilterGroup<onedrivesdk.model.filter_group.FilterGroup>`:
                The inputFilterGroups
        """
        if "inputFilterGroups" in self._prop_dict:
            if isinstance(self._prop_dict["inputFilterGroups"], OneDriveObjectBase):
                return self._prop_dict["inputFilterGroups"]
            else :
                self._prop_dict["inputFilterGroups"] = FilterGroup(self._prop_dict["inputFilterGroups"])
                return self._prop_dict["inputFilterGroups"]

        return None

    @input_filter_groups.setter
    def input_filter_groups(self, val):
        self._prop_dict["inputFilterGroups"] = val
    @property
    def category_filter_groups(self):
        """
        Gets and sets the categoryFilterGroups
        
        Returns: 
            :class:`FilterGroup<onedrivesdk.model.filter_group.FilterGroup>`:
                The categoryFilterGroups
        """
        if "categoryFilterGroups" in self._prop_dict:
            if isinstance(self._prop_dict["categoryFilterGroups"], OneDriveObjectBase):
                return self._prop_dict["categoryFilterGroups"]
            else :
                self._prop_dict["categoryFilterGroups"] = FilterGroup(self._prop_dict["categoryFilterGroups"])
                return self._prop_dict["categoryFilterGroups"]

        return None

    @category_filter_groups.setter
    def category_filter_groups(self, val):
        self._prop_dict["categoryFilterGroups"] = val
