# -*- coding: utf-8 -*- 
'''
# Copyright (c) Microsoft Corporation.  All Rights Reserved.  Licensed under the MIT License.  See License in the project root for license information.
# 
#  This file was generated and any changes will be overwritten.
'''

from __future__ import unicode_literals
from ..model.outlook_category import OutlookCategory
from ..one_drive_object_base import OneDriveObjectBase


class OutlookUser(OneDriveObjectBase):

    def __init__(self, prop_dict={}):
        self._prop_dict = prop_dict

    @property
    def master_categories(self):
        """Gets and sets the masterCategories
        
        Returns: 
            :class:`MasterCategoriesCollectionPage<onedrivesdk.request.master_categories_collection.MasterCategoriesCollectionPage>`:
                The masterCategories
        """
        if "masterCategories" in self._prop_dict:
            return MasterCategoriesCollectionPage(self._prop_dict["masterCategories"])
        else:
            return None

