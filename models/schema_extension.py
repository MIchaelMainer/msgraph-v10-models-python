# -*- coding: utf-8 -*- 
'''
# Copyright (c) Microsoft Corporation.  All Rights Reserved.  Licensed under the MIT License.  See License in the project root for license information.
# 
#  This file was generated and any changes will be overwritten.
'''

from __future__ import unicode_literals
from ..model.extension_schema_property import ExtensionSchemaProperty
from ..one_drive_object_base import OneDriveObjectBase


class SchemaExtension(OneDriveObjectBase):

    def __init__(self, prop_dict={}):
        self._prop_dict = prop_dict

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
    def target_types(self):
        """
        Gets and sets the targetTypes
        
        Returns:
            str:
                The targetTypes
        """
        if "targetTypes" in self._prop_dict:
            return self._prop_dict["targetTypes"]
        else:
            return None

    @target_types.setter
    def target_types(self, val):
        self._prop_dict["targetTypes"] = val

    @property
    def properties(self):
        """Gets and sets the properties
        
        Returns: 
            :class:`PropertiesCollectionPage<onedrivesdk.request.properties_collection.PropertiesCollectionPage>`:
                The properties
        """
        if "properties" in self._prop_dict:
            return PropertiesCollectionPage(self._prop_dict["properties"])
        else:
            return None

    @property
    def status(self):
        """
        Gets and sets the status
        
        Returns:
            str:
                The status
        """
        if "status" in self._prop_dict:
            return self._prop_dict["status"]
        else:
            return None

    @status.setter
    def status(self, val):
        self._prop_dict["status"] = val

    @property
    def owner(self):
        """
        Gets and sets the owner
        
        Returns:
            str:
                The owner
        """
        if "owner" in self._prop_dict:
            return self._prop_dict["owner"]
        else:
            return None

    @owner.setter
    def owner(self, val):
        self._prop_dict["owner"] = val

