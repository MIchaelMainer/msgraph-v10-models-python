# -*- coding: utf-8 -*- 
'''
# Copyright (c) Microsoft Corporation.  All Rights Reserved.  Licensed under the MIT License.  See License in the project root for license information.
# 
#  This file was generated and any changes will be overwritten.
'''

from __future__ import unicode_literals
from ..model.external_link import ExternalLink
from ..one_drive_object_base import OneDriveObjectBase


class NotebookLinks(OneDriveObjectBase):

    def __init__(self, prop_dict={}):
        self._prop_dict = prop_dict

    @property
    def one_note_client_url(self):
        """
        Gets and sets the oneNoteClientUrl
        
        Returns: 
            :class:`ExternalLink<onedrivesdk.model.external_link.ExternalLink>`:
                The oneNoteClientUrl
        """
        if "oneNoteClientUrl" in self._prop_dict:
            if isinstance(self._prop_dict["oneNoteClientUrl"], OneDriveObjectBase):
                return self._prop_dict["oneNoteClientUrl"]
            else :
                self._prop_dict["oneNoteClientUrl"] = ExternalLink(self._prop_dict["oneNoteClientUrl"])
                return self._prop_dict["oneNoteClientUrl"]

        return None

    @one_note_client_url.setter
    def one_note_client_url(self, val):
        self._prop_dict["oneNoteClientUrl"] = val
    @property
    def one_note_web_url(self):
        """
        Gets and sets the oneNoteWebUrl
        
        Returns: 
            :class:`ExternalLink<onedrivesdk.model.external_link.ExternalLink>`:
                The oneNoteWebUrl
        """
        if "oneNoteWebUrl" in self._prop_dict:
            if isinstance(self._prop_dict["oneNoteWebUrl"], OneDriveObjectBase):
                return self._prop_dict["oneNoteWebUrl"]
            else :
                self._prop_dict["oneNoteWebUrl"] = ExternalLink(self._prop_dict["oneNoteWebUrl"])
                return self._prop_dict["oneNoteWebUrl"]

        return None

    @one_note_web_url.setter
    def one_note_web_url(self, val):
        self._prop_dict["oneNoteWebUrl"] = val
