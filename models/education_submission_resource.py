# -*- coding: utf-8 -*- 
'''
# Copyright (c) Microsoft Corporation.  All Rights Reserved.  Licensed under the MIT License.  See License in the project root for license information.
# 
#  This file was generated and any changes will be overwritten.
'''

from __future__ import unicode_literals
from ..model.education_resource import EducationResource
from ..one_drive_object_base import OneDriveObjectBase


class EducationSubmissionResource(OneDriveObjectBase):

    def __init__(self, prop_dict={}):
        self._prop_dict = prop_dict

    @property
    def resource(self):
        """
        Gets and sets the resource
        
        Returns: 
            :class:`EducationResource<onedrivesdk.model.education_resource.EducationResource>`:
                The resource
        """
        if "resource" in self._prop_dict:
            if isinstance(self._prop_dict["resource"], OneDriveObjectBase):
                return self._prop_dict["resource"]
            else :
                self._prop_dict["resource"] = EducationResource(self._prop_dict["resource"])
                return self._prop_dict["resource"]

        return None

    @resource.setter
    def resource(self, val):
        self._prop_dict["resource"] = val

    @property
    def assignment_resource_url(self):
        """
        Gets and sets the assignmentResourceUrl
        
        Returns:
            str:
                The assignmentResourceUrl
        """
        if "assignmentResourceUrl" in self._prop_dict:
            return self._prop_dict["assignmentResourceUrl"]
        else:
            return None

    @assignment_resource_url.setter
    def assignment_resource_url(self, val):
        self._prop_dict["assignmentResourceUrl"] = val

