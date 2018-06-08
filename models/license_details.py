# -*- coding: utf-8 -*- 
'''
# Copyright (c) Microsoft Corporation.  All Rights Reserved.  Licensed under the MIT License.  See License in the project root for license information.
# 
#  This file was generated and any changes will be overwritten.
'''

from __future__ import unicode_literals
from ..model.service_plan_info import ServicePlanInfo
from ..one_drive_object_base import OneDriveObjectBase


class LicenseDetails(OneDriveObjectBase):

    def __init__(self, prop_dict={}):
        self._prop_dict = prop_dict

    @property
    def service_plans(self):
        """Gets and sets the servicePlans
        
        Returns: 
            :class:`ServicePlansCollectionPage<onedrivesdk.request.service_plans_collection.ServicePlansCollectionPage>`:
                The servicePlans
        """
        if "servicePlans" in self._prop_dict:
            return ServicePlansCollectionPage(self._prop_dict["servicePlans"])
        else:
            return None

    @property
    def sku_id(self):
        """
        Gets and sets the skuId
        
        Returns:
            UUID:
                The skuId
        """
        if "skuId" in self._prop_dict:
            return self._prop_dict["skuId"]
        else:
            return None

    @sku_id.setter
    def sku_id(self, val):
        self._prop_dict["skuId"] = val

    @property
    def sku_part_number(self):
        """
        Gets and sets the skuPartNumber
        
        Returns:
            str:
                The skuPartNumber
        """
        if "skuPartNumber" in self._prop_dict:
            return self._prop_dict["skuPartNumber"]
        else:
            return None

    @sku_part_number.setter
    def sku_part_number(self, val):
        self._prop_dict["skuPartNumber"] = val

