# -*- coding: utf-8 -*- 
'''
# Copyright (c) Microsoft Corporation.  All Rights Reserved.  Licensed under the MIT License.  See License in the project root for license information.
# 
#  This file was generated and any changes will be overwritten.
'''

from __future__ import unicode_literals
from ..model.synchronization_secret_key_string_value_pair import SynchronizationSecretKeyStringValuePair
from ..model.synchronization_job import SynchronizationJob
from ..model.synchronization_template import SynchronizationTemplate
from ..one_drive_object_base import OneDriveObjectBase


class Synchronization(OneDriveObjectBase):

    def __init__(self, prop_dict={}):
        self._prop_dict = prop_dict

    @property
    def secrets(self):
        """Gets and sets the secrets
        
        Returns: 
            :class:`SecretsCollectionPage<onedrivesdk.request.secrets_collection.SecretsCollectionPage>`:
                The secrets
        """
        if "secrets" in self._prop_dict:
            return SecretsCollectionPage(self._prop_dict["secrets"])
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
    def templates(self):
        """Gets and sets the templates
        
        Returns: 
            :class:`TemplatesCollectionPage<onedrivesdk.request.templates_collection.TemplatesCollectionPage>`:
                The templates
        """
        if "templates" in self._prop_dict:
            return TemplatesCollectionPage(self._prop_dict["templates"])
        else:
            return None

