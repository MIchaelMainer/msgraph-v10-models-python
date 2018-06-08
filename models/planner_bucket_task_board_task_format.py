# -*- coding: utf-8 -*- 
'''
# Copyright (c) Microsoft Corporation.  All Rights Reserved.  Licensed under the MIT License.  See License in the project root for license information.
# 
#  This file was generated and any changes will be overwritten.
'''

from __future__ import unicode_literals
from ..one_drive_object_base import OneDriveObjectBase


class PlannerBucketTaskBoardTaskFormat(OneDriveObjectBase):

    def __init__(self, prop_dict={}):
        self._prop_dict = prop_dict

    @property
    def order_hint(self):
        """
        Gets and sets the orderHint
        
        Returns:
            str:
                The orderHint
        """
        if "orderHint" in self._prop_dict:
            return self._prop_dict["orderHint"]
        else:
            return None

    @order_hint.setter
    def order_hint(self, val):
        self._prop_dict["orderHint"] = val

