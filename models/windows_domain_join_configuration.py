# -*- coding: utf-8 -*- 
'''
# Copyright (c) Microsoft Corporation.  All Rights Reserved.  Licensed under the MIT License.  See License in the project root for license information.
# 
#  This file was generated and any changes will be overwritten.
'''

from __future__ import unicode_literals
from ..model.device_configuration import DeviceConfiguration
from ..one_drive_object_base import OneDriveObjectBase


class WindowsDomainJoinConfiguration(OneDriveObjectBase):

    def __init__(self, prop_dict={}):
        self._prop_dict = prop_dict

    @property
    def computer_name_static_prefix(self):
        """
        Gets and sets the computerNameStaticPrefix
        
        Returns:
            str:
                The computerNameStaticPrefix
        """
        if "computerNameStaticPrefix" in self._prop_dict:
            return self._prop_dict["computerNameStaticPrefix"]
        else:
            return None

    @computer_name_static_prefix.setter
    def computer_name_static_prefix(self, val):
        self._prop_dict["computerNameStaticPrefix"] = val

    @property
    def computer_name_suffix_random_char_count(self):
        """
        Gets and sets the computerNameSuffixRandomCharCount
        
        Returns:
            int:
                The computerNameSuffixRandomCharCount
        """
        if "computerNameSuffixRandomCharCount" in self._prop_dict:
            return self._prop_dict["computerNameSuffixRandomCharCount"]
        else:
            return None

    @computer_name_suffix_random_char_count.setter
    def computer_name_suffix_random_char_count(self, val):
        self._prop_dict["computerNameSuffixRandomCharCount"] = val

    @property
    def active_directory_domain_name(self):
        """
        Gets and sets the activeDirectoryDomainName
        
        Returns:
            str:
                The activeDirectoryDomainName
        """
        if "activeDirectoryDomainName" in self._prop_dict:
            return self._prop_dict["activeDirectoryDomainName"]
        else:
            return None

    @active_directory_domain_name.setter
    def active_directory_domain_name(self, val):
        self._prop_dict["activeDirectoryDomainName"] = val

    @property
    def network_access_configurations(self):
        """Gets and sets the networkAccessConfigurations
        
        Returns: 
            :class:`NetworkAccessConfigurationsCollectionPage<onedrivesdk.request.network_access_configurations_collection.NetworkAccessConfigurationsCollectionPage>`:
                The networkAccessConfigurations
        """
        if "networkAccessConfigurations" in self._prop_dict:
            return NetworkAccessConfigurationsCollectionPage(self._prop_dict["networkAccessConfigurations"])
        else:
            return None

