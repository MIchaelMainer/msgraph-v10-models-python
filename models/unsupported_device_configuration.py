# -*- coding: utf-8 -*- 
'''
# Copyright (c) Microsoft Corporation.  All Rights Reserved.  Licensed under the MIT License.  See License in the project root for license information.
# 
#  This file was generated and any changes will be overwritten.
'''

from __future__ import unicode_literals
from ..model.unsupported_device_configuration_detail import UnsupportedDeviceConfigurationDetail
from ..one_drive_object_base import OneDriveObjectBase


class UnsupportedDeviceConfiguration(OneDriveObjectBase):

    def __init__(self, prop_dict={}):
        self._prop_dict = prop_dict

    @property
    def original_entity_type_name(self):
        """
        Gets and sets the originalEntityTypeName
        
        Returns:
            str:
                The originalEntityTypeName
        """
        if "originalEntityTypeName" in self._prop_dict:
            return self._prop_dict["originalEntityTypeName"]
        else:
            return None

    @original_entity_type_name.setter
    def original_entity_type_name(self, val):
        self._prop_dict["originalEntityTypeName"] = val

    @property
    def details(self):
        """Gets and sets the details
        
        Returns: 
            :class:`DetailsCollectionPage<onedrivesdk.request.details_collection.DetailsCollectionPage>`:
                The details
        """
        if "details" in self._prop_dict:
            return DetailsCollectionPage(self._prop_dict["details"])
        else:
            return None

