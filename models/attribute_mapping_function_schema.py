# -*- coding: utf-8 -*- 
'''
# Copyright (c) Microsoft Corporation.  All Rights Reserved.  Licensed under the MIT License.  See License in the project root for license information.
# 
#  This file was generated and any changes will be overwritten.
'''

from __future__ import unicode_literals
from ..model.attribute_mapping_parameter_schema import AttributeMappingParameterSchema
from ..one_drive_object_base import OneDriveObjectBase


class AttributeMappingFunctionSchema(OneDriveObjectBase):

    def __init__(self, prop_dict={}):
        self._prop_dict = prop_dict

    @property
    def parameters(self):
        """Gets and sets the parameters
        
        Returns: 
            :class:`ParametersCollectionPage<onedrivesdk.request.parameters_collection.ParametersCollectionPage>`:
                The parameters
        """
        if "parameters" in self._prop_dict:
            return ParametersCollectionPage(self._prop_dict["parameters"])
        else:
            return None

