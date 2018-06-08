# -*- coding: utf-8 -*- 
'''
# Copyright (c) Microsoft Corporation.  All Rights Reserved.  Licensed under the MIT License.  See License in the project root for license information.
# 
#  This file was generated and any changes will be overwritten.
'''

from __future__ import unicode_literals
from ..model.sign_in import SignIn
from ..model.directory_audit import DirectoryAudit
from ..model.restricted_sign_in import RestrictedSignIn
from ..one_drive_object_base import OneDriveObjectBase


class AuditLogRoot(OneDriveObjectBase):

    def __init__(self, prop_dict={}):
        self._prop_dict = prop_dict

    @property
    def sign_ins(self):
        """Gets and sets the signIns
        
        Returns: 
            :class:`SignInsCollectionPage<onedrivesdk.request.sign_ins_collection.SignInsCollectionPage>`:
                The signIns
        """
        if "signIns" in self._prop_dict:
            return SignInsCollectionPage(self._prop_dict["signIns"])
        else:
            return None

    @property
    def directory_audits(self):
        """Gets and sets the directoryAudits
        
        Returns: 
            :class:`DirectoryAuditsCollectionPage<onedrivesdk.request.directory_audits_collection.DirectoryAuditsCollectionPage>`:
                The directoryAudits
        """
        if "directoryAudits" in self._prop_dict:
            return DirectoryAuditsCollectionPage(self._prop_dict["directoryAudits"])
        else:
            return None

    @property
    def restricted_sign_ins(self):
        """Gets and sets the restrictedSignIns
        
        Returns: 
            :class:`RestrictedSignInsCollectionPage<onedrivesdk.request.restricted_sign_ins_collection.RestrictedSignInsCollectionPage>`:
                The restrictedSignIns
        """
        if "restrictedSignIns" in self._prop_dict:
            return RestrictedSignInsCollectionPage(self._prop_dict["restrictedSignIns"])
        else:
            return None

