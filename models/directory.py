# -*- coding: utf-8 -*- 
'''
# Copyright (c) Microsoft Corporation.  All Rights Reserved.  Licensed under the MIT License.  See License in the project root for license information.
# 
#  This file was generated and any changes will be overwritten.
'''

from __future__ import unicode_literals
from ..model.directory_object import DirectoryObject
from ..one_drive_object_base import OneDriveObjectBase


class Directory(OneDriveObjectBase):

    def __init__(self, prop_dict={}):
        self._prop_dict = prop_dict

    @property
    def deleted_items(self):
        """Gets and sets the deletedItems
        
        Returns: 
            :class:`DeletedItemsCollectionPage<onedrivesdk.request.deleted_items_collection.DeletedItemsCollectionPage>`:
                The deletedItems
        """
        if "deletedItems" in self._prop_dict:
            return DeletedItemsCollectionPage(self._prop_dict["deletedItems"])
        else:
            return None

