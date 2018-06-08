# -*- coding: utf-8 -*- 
'''
# Copyright (c) Microsoft Corporation.  All Rights Reserved.  Licensed under the MIT License.  See License in the project root for license information.
# 
#  This file was generated and any changes will be overwritten.
'''

from __future__ import unicode_literals
from ..model.inference_classification_override import InferenceClassificationOverride
from ..one_drive_object_base import OneDriveObjectBase


class InferenceClassification(OneDriveObjectBase):

    def __init__(self, prop_dict={}):
        self._prop_dict = prop_dict

    @property
    def overrides(self):
        """Gets and sets the overrides
        
        Returns: 
            :class:`OverridesCollectionPage<onedrivesdk.request.overrides_collection.OverridesCollectionPage>`:
                The overrides
        """
        if "overrides" in self._prop_dict:
            return OverridesCollectionPage(self._prop_dict["overrides"])
        else:
            return None

