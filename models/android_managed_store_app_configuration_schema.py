# -*- coding: utf-8 -*- 
'''
# Copyright (c) Microsoft Corporation.  All Rights Reserved.  Licensed under the MIT License.  See License in the project root for license information.
# 
#  This file was generated and any changes will be overwritten.
'''

from __future__ import unicode_literals
from ..model.android_managed_store_app_configuration_schema_item import AndroidManagedStoreAppConfigurationSchemaItem
from ..one_drive_object_base import OneDriveObjectBase


class AndroidManagedStoreAppConfigurationSchema(OneDriveObjectBase):

    def __init__(self, prop_dict={}):
        self._prop_dict = prop_dict

    @property
    def schema_items(self):
        """Gets and sets the schemaItems
        
        Returns: 
            :class:`SchemaItemsCollectionPage<onedrivesdk.request.schema_items_collection.SchemaItemsCollectionPage>`:
                The schemaItems
        """
        if "schemaItems" in self._prop_dict:
            return SchemaItemsCollectionPage(self._prop_dict["schemaItems"])
        else:
            return None

