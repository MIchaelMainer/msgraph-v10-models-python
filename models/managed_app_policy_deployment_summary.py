# -*- coding: utf-8 -*- 
'''
# Copyright (c) Microsoft Corporation.  All Rights Reserved.  Licensed under the MIT License.  See License in the project root for license information.
# 
#  This file was generated and any changes will be overwritten.
'''

from __future__ import unicode_literals
from ..model.managed_app_policy_deployment_summary_per_app import ManagedAppPolicyDeploymentSummaryPerApp
from datetime import datetime
from ..one_drive_object_base import OneDriveObjectBase


class ManagedAppPolicyDeploymentSummary(OneDriveObjectBase):

    def __init__(self, prop_dict={}):
        self._prop_dict = prop_dict

    @property
    def display_name(self):
        """
        Gets and sets the displayName
        
        Returns:
            str:
                The displayName
        """
        if "displayName" in self._prop_dict:
            return self._prop_dict["displayName"]
        else:
            return None

    @display_name.setter
    def display_name(self, val):
        self._prop_dict["displayName"] = val

    @property
    def configuration_deployed_user_count(self):
        """
        Gets and sets the configurationDeployedUserCount
        
        Returns:
            int:
                The configurationDeployedUserCount
        """
        if "configurationDeployedUserCount" in self._prop_dict:
            return self._prop_dict["configurationDeployedUserCount"]
        else:
            return None

    @configuration_deployed_user_count.setter
    def configuration_deployed_user_count(self, val):
        self._prop_dict["configurationDeployedUserCount"] = val

    @property
    def last_refresh_time(self):
        """
        Gets and sets the lastRefreshTime
        
        Returns:
            datetime:
                The lastRefreshTime
        """
        if "lastRefreshTime" in self._prop_dict:
            return datetime.strptime(self._prop_dict["lastRefreshTime"].replace("Z", ""), "%Y-%m-%dT%H:%M:%S.%f")
        else:
            return None

    @last_refresh_time.setter
    def last_refresh_time(self, val):
        self._prop_dict["lastRefreshTime"] = val.isoformat()+"Z"

    @property
    def configuration_deployment_summary_per_app(self):
        """Gets and sets the configurationDeploymentSummaryPerApp
        
        Returns: 
            :class:`ConfigurationDeploymentSummaryPerAppCollectionPage<onedrivesdk.request.configuration_deployment_summary_per_app_collection.ConfigurationDeploymentSummaryPerAppCollectionPage>`:
                The configurationDeploymentSummaryPerApp
        """
        if "configurationDeploymentSummaryPerApp" in self._prop_dict:
            return ConfigurationDeploymentSummaryPerAppCollectionPage(self._prop_dict["configurationDeploymentSummaryPerApp"])
        else:
            return None

    @property
    def version(self):
        """
        Gets and sets the version
        
        Returns:
            str:
                The version
        """
        if "version" in self._prop_dict:
            return self._prop_dict["version"]
        else:
            return None

    @version.setter
    def version(self, val):
        self._prop_dict["version"] = val

