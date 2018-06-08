# -*- coding: utf-8 -*- 
'''
# Copyright (c) Microsoft Corporation.  All Rights Reserved.  Licensed under the MIT License.  See License in the project root for license information.
# 
#  This file was generated and any changes will be overwritten.
'''

from __future__ import unicode_literals
from ..model.trending import Trending
from ..model.shared_insight import SharedInsight
from ..model.used_insight import UsedInsight
from ..one_drive_object_base import OneDriveObjectBase


class OfficeGraphInsights(OneDriveObjectBase):

    def __init__(self, prop_dict={}):
        self._prop_dict = prop_dict

    @property
    def trending(self):
        """Gets and sets the trending
        
        Returns: 
            :class:`TrendingCollectionPage<onedrivesdk.request.trending_collection.TrendingCollectionPage>`:
                The trending
        """
        if "trending" in self._prop_dict:
            return TrendingCollectionPage(self._prop_dict["trending"])
        else:
            return None

    @property
    def shared(self):
        """Gets and sets the shared
        
        Returns: 
            :class:`SharedCollectionPage<onedrivesdk.request.shared_collection.SharedCollectionPage>`:
                The shared
        """
        if "shared" in self._prop_dict:
            return SharedCollectionPage(self._prop_dict["shared"])
        else:
            return None

    @property
    def used(self):
        """Gets and sets the used
        
        Returns: 
            :class:`UsedCollectionPage<onedrivesdk.request.used_collection.UsedCollectionPage>`:
                The used
        """
        if "used" in self._prop_dict:
            return UsedCollectionPage(self._prop_dict["used"])
        else:
            return None

