# -*- coding: utf-8 -*- 
'''
# Copyright (c) Microsoft Corporation.  All Rights Reserved.  Licensed under the MIT License.  See License in the project root for license information.
# 
#  This file was generated and any changes will be overwritten.
'''

from __future__ import unicode_literals
from ..model.application_permissions_required import ApplicationPermissionsRequired
from ..one_drive_object_base import OneDriveObjectBase


class ApplicationSecurityState(OneDriveObjectBase):

    def __init__(self, prop_dict={}):
        self._prop_dict = prop_dict

    @property
    def deployment_package_url(self):
        """Gets and sets the deploymentPackageUrl
        
        Returns: 
            str:
                The deploymentPackageUrl
        """
        if "deploymentPackageUrl" in self._prop_dict:
            return self._prop_dict["deploymentPackageUrl"]
        else:
            return None

    @deployment_package_url.setter
    def deployment_package_url(self, val):
        self._prop_dict["deploymentPackageUrl"] = val

    @property
    def name(self):
        """Gets and sets the name
        
        Returns: 
            str:
                The name
        """
        if "name" in self._prop_dict:
            return self._prop_dict["name"]
        else:
            return None

    @name.setter
    def name(self, val):
        self._prop_dict["name"] = val

    @property
    def permissions_required(self):
        """
        Gets and sets the permissionsRequired
        
        Returns: 
            :class:`ApplicationPermissionsRequired<onedrivesdk.model.application_permissions_required.ApplicationPermissionsRequired>`:
                The permissionsRequired
        """
        if "permissionsRequired" in self._prop_dict:
            if isinstance(self._prop_dict["permissionsRequired"], OneDriveObjectBase):
                return self._prop_dict["permissionsRequired"]
            else :
                self._prop_dict["permissionsRequired"] = ApplicationPermissionsRequired(self._prop_dict["permissionsRequired"])
                return self._prop_dict["permissionsRequired"]

        return None

    @permissions_required.setter
    def permissions_required(self, val):
        self._prop_dict["permissionsRequired"] = val
    @property
    def publisher(self):
        """Gets and sets the publisher
        
        Returns: 
            str:
                The publisher
        """
        if "publisher" in self._prop_dict:
            return self._prop_dict["publisher"]
        else:
            return None

    @publisher.setter
    def publisher(self, val):
        self._prop_dict["publisher"] = val

    @property
    def risk_score(self):
        """Gets and sets the riskScore
        
        Returns: 
            str:
                The riskScore
        """
        if "riskScore" in self._prop_dict:
            return self._prop_dict["riskScore"]
        else:
            return None

    @risk_score.setter
    def risk_score(self, val):
        self._prop_dict["riskScore"] = val

