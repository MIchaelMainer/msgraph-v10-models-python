# -*- coding: utf-8 -*- 
'''
# Copyright (c) Microsoft Corporation.  All Rights Reserved.  Licensed under the MIT License.  See License in the project root for license information.
# 
#  This file was generated and any changes will be overwritten.
'''

from __future__ import unicode_literals
from ..one_drive_object_base import OneDriveObjectBase


class SensitiveType(OneDriveObjectBase):

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
    def description(self):
        """
        Gets and sets the description
        
        Returns:
            str:
                The description
        """
        if "description" in self._prop_dict:
            return self._prop_dict["description"]
        else:
            return None

    @description.setter
    def description(self, val):
        self._prop_dict["description"] = val

    @property
    def rule_package_id(self):
        """
        Gets and sets the rulePackageId
        
        Returns:
            str:
                The rulePackageId
        """
        if "rulePackageId" in self._prop_dict:
            return self._prop_dict["rulePackageId"]
        else:
            return None

    @rule_package_id.setter
    def rule_package_id(self, val):
        self._prop_dict["rulePackageId"] = val

    @property
    def rule_package_type(self):
        """
        Gets and sets the rulePackageType
        
        Returns:
            str:
                The rulePackageType
        """
        if "rulePackageType" in self._prop_dict:
            return self._prop_dict["rulePackageType"]
        else:
            return None

    @rule_package_type.setter
    def rule_package_type(self, val):
        self._prop_dict["rulePackageType"] = val

    @property
    def publisher_name(self):
        """
        Gets and sets the publisherName
        
        Returns:
            str:
                The publisherName
        """
        if "publisherName" in self._prop_dict:
            return self._prop_dict["publisherName"]
        else:
            return None

    @publisher_name.setter
    def publisher_name(self, val):
        self._prop_dict["publisherName"] = val

