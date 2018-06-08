# -*- coding: utf-8 -*- 
'''
# Copyright (c) Microsoft Corporation.  All Rights Reserved.  Licensed under the MIT License.  See License in the project root for license information.
# 
#  This file was generated and any changes will be overwritten.
'''

from __future__ import unicode_literals
from ..model.sensitive_type import SensitiveType
from ..model.job_response_base import JobResponseBase
from ..model.text_classification_request import TextClassificationRequest
from ..model.file_classification_request import FileClassificationRequest
from ..one_drive_object_base import OneDriveObjectBase


class DataClassificationService(OneDriveObjectBase):

    def __init__(self, prop_dict={}):
        self._prop_dict = prop_dict

    @property
    def sensitive_types(self):
        """Gets and sets the sensitiveTypes
        
        Returns: 
            :class:`SensitiveTypesCollectionPage<onedrivesdk.request.sensitive_types_collection.SensitiveTypesCollectionPage>`:
                The sensitiveTypes
        """
        if "sensitiveTypes" in self._prop_dict:
            return SensitiveTypesCollectionPage(self._prop_dict["sensitiveTypes"])
        else:
            return None

    @property
    def jobs(self):
        """Gets and sets the jobs
        
        Returns: 
            :class:`JobsCollectionPage<onedrivesdk.request.jobs_collection.JobsCollectionPage>`:
                The jobs
        """
        if "jobs" in self._prop_dict:
            return JobsCollectionPage(self._prop_dict["jobs"])
        else:
            return None

    @property
    def classify_text(self):
        """Gets and sets the classifyText
        
        Returns: 
            :class:`ClassifyTextCollectionPage<onedrivesdk.request.classify_text_collection.ClassifyTextCollectionPage>`:
                The classifyText
        """
        if "classifyText" in self._prop_dict:
            return ClassifyTextCollectionPage(self._prop_dict["classifyText"])
        else:
            return None

    @property
    def classify_file(self):
        """Gets and sets the classifyFile
        
        Returns: 
            :class:`ClassifyFileCollectionPage<onedrivesdk.request.classify_file_collection.ClassifyFileCollectionPage>`:
                The classifyFile
        """
        if "classifyFile" in self._prop_dict:
            return ClassifyFileCollectionPage(self._prop_dict["classifyFile"])
        else:
            return None

