# -*- coding: utf-8 -*- 
'''
# Copyright (c) Microsoft Corporation.  All Rights Reserved.  Licensed under the MIT License.  See License in the project root for license information.
# 
#  This file was generated and any changes will be overwritten.
'''

from __future__ import unicode_literals
from ..model.selection_likelihood_info import SelectionLikelihoodInfo
from ..one_drive_object_base import OneDriveObjectBase


class ScoredEmailAddress(OneDriveObjectBase):

    def __init__(self, prop_dict={}):
        self._prop_dict = prop_dict

    @property
    def address(self):
        """Gets and sets the address
        
        Returns: 
            str:
                The address
        """
        if "address" in self._prop_dict:
            return self._prop_dict["address"]
        else:
            return None

    @address.setter
    def address(self, val):
        self._prop_dict["address"] = val

    @property
    def relevance_score(self):
        """Gets and sets the relevanceScore
        
        Returns: 
            float:
                The relevanceScore
        """
        if "relevanceScore" in self._prop_dict:
            return self._prop_dict["relevanceScore"]
        else:
            return None

    @relevance_score.setter
    def relevance_score(self, val):
        self._prop_dict["relevanceScore"] = val

    @property
    def selection_likelihood(self):
        """
        Gets and sets the selectionLikelihood
        
        Returns: 
            :class:`SelectionLikelihoodInfo<onedrivesdk.model.selection_likelihood_info.SelectionLikelihoodInfo>`:
                The selectionLikelihood
        """
        if "selectionLikelihood" in self._prop_dict:
            if isinstance(self._prop_dict["selectionLikelihood"], OneDriveObjectBase):
                return self._prop_dict["selectionLikelihood"]
            else :
                self._prop_dict["selectionLikelihood"] = SelectionLikelihoodInfo(self._prop_dict["selectionLikelihood"])
                return self._prop_dict["selectionLikelihood"]

        return None

    @selection_likelihood.setter
    def selection_likelihood(self, val):
        self._prop_dict["selectionLikelihood"] = val
