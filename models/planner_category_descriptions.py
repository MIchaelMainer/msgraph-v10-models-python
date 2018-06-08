# -*- coding: utf-8 -*- 
'''
# Copyright (c) Microsoft Corporation.  All Rights Reserved.  Licensed under the MIT License.  See License in the project root for license information.
# 
#  This file was generated and any changes will be overwritten.
'''

from __future__ import unicode_literals
from ..one_drive_object_base import OneDriveObjectBase


class PlannerCategoryDescriptions(OneDriveObjectBase):

    def __init__(self, prop_dict={}):
        self._prop_dict = prop_dict

    @property
    def category1(self):
        """Gets and sets the category1
        
        Returns: 
            str:
                The category1
        """
        if "category1" in self._prop_dict:
            return self._prop_dict["category1"]
        else:
            return None

    @category1.setter
    def category1(self, val):
        self._prop_dict["category1"] = val

    @property
    def category2(self):
        """Gets and sets the category2
        
        Returns: 
            str:
                The category2
        """
        if "category2" in self._prop_dict:
            return self._prop_dict["category2"]
        else:
            return None

    @category2.setter
    def category2(self, val):
        self._prop_dict["category2"] = val

    @property
    def category3(self):
        """Gets and sets the category3
        
        Returns: 
            str:
                The category3
        """
        if "category3" in self._prop_dict:
            return self._prop_dict["category3"]
        else:
            return None

    @category3.setter
    def category3(self, val):
        self._prop_dict["category3"] = val

    @property
    def category4(self):
        """Gets and sets the category4
        
        Returns: 
            str:
                The category4
        """
        if "category4" in self._prop_dict:
            return self._prop_dict["category4"]
        else:
            return None

    @category4.setter
    def category4(self, val):
        self._prop_dict["category4"] = val

    @property
    def category5(self):
        """Gets and sets the category5
        
        Returns: 
            str:
                The category5
        """
        if "category5" in self._prop_dict:
            return self._prop_dict["category5"]
        else:
            return None

    @category5.setter
    def category5(self, val):
        self._prop_dict["category5"] = val

    @property
    def category6(self):
        """Gets and sets the category6
        
        Returns: 
            str:
                The category6
        """
        if "category6" in self._prop_dict:
            return self._prop_dict["category6"]
        else:
            return None

    @category6.setter
    def category6(self, val):
        self._prop_dict["category6"] = val

