# -*- coding: utf-8 -*- 
'''
# Copyright (c) Microsoft Corporation.  All Rights Reserved.  Licensed under the MIT License.  See License in the project root for license information.
# 
#  This file was generated and any changes will be overwritten.
'''

from __future__ import unicode_literals
from ..model.air_print_destination import AirPrintDestination
from ..one_drive_object_base import OneDriveObjectBase


class AppleDeviceFeaturesConfigurationBase(OneDriveObjectBase):

    def __init__(self, prop_dict={}):
        self._prop_dict = prop_dict

    @property
    def air_print_destinations(self):
        """Gets and sets the airPrintDestinations
        
        Returns: 
            :class:`AirPrintDestinationsCollectionPage<onedrivesdk.request.air_print_destinations_collection.AirPrintDestinationsCollectionPage>`:
                The airPrintDestinations
        """
        if "airPrintDestinations" in self._prop_dict:
            return AirPrintDestinationsCollectionPage(self._prop_dict["airPrintDestinations"])
        else:
            return None

