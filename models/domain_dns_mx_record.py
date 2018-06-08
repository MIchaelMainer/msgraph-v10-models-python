# -*- coding: utf-8 -*- 
'''
# Copyright (c) Microsoft Corporation.  All Rights Reserved.  Licensed under the MIT License.  See License in the project root for license information.
# 
#  This file was generated and any changes will be overwritten.
'''

from __future__ import unicode_literals
from ..one_drive_object_base import OneDriveObjectBase


class DomainDnsMxRecord(OneDriveObjectBase):

    def __init__(self, prop_dict={}):
        self._prop_dict = prop_dict

    @property
    def mail_exchange(self):
        """
        Gets and sets the mailExchange
        
        Returns:
            str:
                The mailExchange
        """
        if "mailExchange" in self._prop_dict:
            return self._prop_dict["mailExchange"]
        else:
            return None

    @mail_exchange.setter
    def mail_exchange(self, val):
        self._prop_dict["mailExchange"] = val

    @property
    def preference(self):
        """
        Gets and sets the preference
        
        Returns:
            int:
                The preference
        """
        if "preference" in self._prop_dict:
            return self._prop_dict["preference"]
        else:
            return None

    @preference.setter
    def preference(self, val):
        self._prop_dict["preference"] = val

