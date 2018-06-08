# -*- coding: utf-8 -*- 
'''
# Copyright (c) Microsoft Corporation.  All Rights Reserved.  Licensed under the MIT License.  See License in the project root for license information.
# 
#  This file was generated and any changes will be overwritten.
'''

from __future__ import unicode_literals
from ..model.giphy_rating_type import GiphyRatingType
from ..one_drive_object_base import OneDriveObjectBase


class TeamFunSettings(OneDriveObjectBase):

    def __init__(self, prop_dict={}):
        self._prop_dict = prop_dict

    @property
    def allow_giphy(self):
        """Gets and sets the allowGiphy
        
        Returns: 
            bool:
                The allowGiphy
        """
        if "allowGiphy" in self._prop_dict:
            return self._prop_dict["allowGiphy"]
        else:
            return None

    @allow_giphy.setter
    def allow_giphy(self, val):
        self._prop_dict["allowGiphy"] = val

    @property
    def giphy_content_rating(self):
        """
        Gets and sets the giphyContentRating
        
        Returns: 
            :class:`GiphyRatingType<onedrivesdk.model.giphy_rating_type.GiphyRatingType>`:
                The giphyContentRating
        """
        if "giphyContentRating" in self._prop_dict:
            if isinstance(self._prop_dict["giphyContentRating"], OneDriveObjectBase):
                return self._prop_dict["giphyContentRating"]
            else :
                self._prop_dict["giphyContentRating"] = GiphyRatingType(self._prop_dict["giphyContentRating"])
                return self._prop_dict["giphyContentRating"]

        return None

    @giphy_content_rating.setter
    def giphy_content_rating(self, val):
        self._prop_dict["giphyContentRating"] = val
    @property
    def allow_stickers_and_memes(self):
        """Gets and sets the allowStickersAndMemes
        
        Returns: 
            bool:
                The allowStickersAndMemes
        """
        if "allowStickersAndMemes" in self._prop_dict:
            return self._prop_dict["allowStickersAndMemes"]
        else:
            return None

    @allow_stickers_and_memes.setter
    def allow_stickers_and_memes(self, val):
        self._prop_dict["allowStickersAndMemes"] = val

    @property
    def allow_custom_memes(self):
        """Gets and sets the allowCustomMemes
        
        Returns: 
            bool:
                The allowCustomMemes
        """
        if "allowCustomMemes" in self._prop_dict:
            return self._prop_dict["allowCustomMemes"]
        else:
            return None

    @allow_custom_memes.setter
    def allow_custom_memes(self, val):
        self._prop_dict["allowCustomMemes"] = val

