# -*- coding: utf-8 -*- 
'''
# Copyright (c) Microsoft Corporation.  All Rights Reserved.  Licensed under the MIT License.  See License in the project root for license information.
# 
#  This file was generated and any changes will be overwritten.
'''

from __future__ import unicode_literals
from ..model.metadata_entry import MetadataEntry
from ..model.synchronization_schema import SynchronizationSchema
from ..one_drive_object_base import OneDriveObjectBase


class SynchronizationTemplate(OneDriveObjectBase):

    def __init__(self, prop_dict={}):
        self._prop_dict = prop_dict

    @property
    def application_id(self):
        """
        Gets and sets the applicationId
        
        Returns:
            UUID:
                The applicationId
        """
        if "applicationId" in self._prop_dict:
            return self._prop_dict["applicationId"]
        else:
            return None

    @application_id.setter
    def application_id(self, val):
        self._prop_dict["applicationId"] = val

    @property
    def default(self):
        """
        Gets and sets the default
        
        Returns:
            bool:
                The default
        """
        if "default" in self._prop_dict:
            return self._prop_dict["default"]
        else:
            return None

    @default.setter
    def default(self, val):
        self._prop_dict["default"] = val

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
    def discoverable(self):
        """
        Gets and sets the discoverable
        
        Returns:
            bool:
                The discoverable
        """
        if "discoverable" in self._prop_dict:
            return self._prop_dict["discoverable"]
        else:
            return None

    @discoverable.setter
    def discoverable(self, val):
        self._prop_dict["discoverable"] = val

    @property
    def factory_tag(self):
        """
        Gets and sets the factoryTag
        
        Returns:
            str:
                The factoryTag
        """
        if "factoryTag" in self._prop_dict:
            return self._prop_dict["factoryTag"]
        else:
            return None

    @factory_tag.setter
    def factory_tag(self, val):
        self._prop_dict["factoryTag"] = val

    @property
    def metadata(self):
        """Gets and sets the metadata
        
        Returns: 
            :class:`MetadataCollectionPage<onedrivesdk.request.metadata_collection.MetadataCollectionPage>`:
                The metadata
        """
        if "metadata" in self._prop_dict:
            return MetadataCollectionPage(self._prop_dict["metadata"])
        else:
            return None

    @property
    def schema(self):
        """
        Gets and sets the schema
        
        Returns: 
            :class:`SynchronizationSchema<onedrivesdk.model.synchronization_schema.SynchronizationSchema>`:
                The schema
        """
        if "schema" in self._prop_dict:
            if isinstance(self._prop_dict["schema"], OneDriveObjectBase):
                return self._prop_dict["schema"]
            else :
                self._prop_dict["schema"] = SynchronizationSchema(self._prop_dict["schema"])
                return self._prop_dict["schema"]

        return None

    @schema.setter
    def schema(self, val):
        self._prop_dict["schema"] = val

