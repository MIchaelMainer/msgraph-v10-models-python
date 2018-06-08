# -*- coding: utf-8 -*- 
'''
# Copyright (c) Microsoft Corporation.  All Rights Reserved.  Licensed under the MIT License.  See License in the project root for license information.
# 
#  This file was generated and any changes will be overwritten.
'''

from __future__ import unicode_literals
from ..one_drive_object_base import OneDriveObjectBase


class Video(OneDriveObjectBase):

    def __init__(self, prop_dict={}):
        self._prop_dict = prop_dict

    @property
    def audio_bits_per_sample(self):
        """Gets and sets the audioBitsPerSample
        
        Returns: 
            int:
                The audioBitsPerSample
        """
        if "audioBitsPerSample" in self._prop_dict:
            return self._prop_dict["audioBitsPerSample"]
        else:
            return None

    @audio_bits_per_sample.setter
    def audio_bits_per_sample(self, val):
        self._prop_dict["audioBitsPerSample"] = val

    @property
    def audio_channels(self):
        """Gets and sets the audioChannels
        
        Returns: 
            int:
                The audioChannels
        """
        if "audioChannels" in self._prop_dict:
            return self._prop_dict["audioChannels"]
        else:
            return None

    @audio_channels.setter
    def audio_channels(self, val):
        self._prop_dict["audioChannels"] = val

    @property
    def audio_format(self):
        """Gets and sets the audioFormat
        
        Returns: 
            str:
                The audioFormat
        """
        if "audioFormat" in self._prop_dict:
            return self._prop_dict["audioFormat"]
        else:
            return None

    @audio_format.setter
    def audio_format(self, val):
        self._prop_dict["audioFormat"] = val

    @property
    def audio_samples_per_second(self):
        """Gets and sets the audioSamplesPerSecond
        
        Returns: 
            int:
                The audioSamplesPerSecond
        """
        if "audioSamplesPerSecond" in self._prop_dict:
            return self._prop_dict["audioSamplesPerSecond"]
        else:
            return None

    @audio_samples_per_second.setter
    def audio_samples_per_second(self, val):
        self._prop_dict["audioSamplesPerSecond"] = val

    @property
    def bitrate(self):
        """Gets and sets the bitrate
        
        Returns: 
            int:
                The bitrate
        """
        if "bitrate" in self._prop_dict:
            return self._prop_dict["bitrate"]
        else:
            return None

    @bitrate.setter
    def bitrate(self, val):
        self._prop_dict["bitrate"] = val

    @property
    def duration(self):
        """Gets and sets the duration
        
        Returns: 
            int:
                The duration
        """
        if "duration" in self._prop_dict:
            return self._prop_dict["duration"]
        else:
            return None

    @duration.setter
    def duration(self, val):
        self._prop_dict["duration"] = val

    @property
    def four_cc(self):
        """Gets and sets the fourCC
        
        Returns: 
            str:
                The fourCC
        """
        if "fourCC" in self._prop_dict:
            return self._prop_dict["fourCC"]
        else:
            return None

    @four_cc.setter
    def four_cc(self, val):
        self._prop_dict["fourCC"] = val

    @property
    def frame_rate(self):
        """Gets and sets the frameRate
        
        Returns: 
            float:
                The frameRate
        """
        if "frameRate" in self._prop_dict:
            return self._prop_dict["frameRate"]
        else:
            return None

    @frame_rate.setter
    def frame_rate(self, val):
        self._prop_dict["frameRate"] = val

    @property
    def height(self):
        """Gets and sets the height
        
        Returns: 
            int:
                The height
        """
        if "height" in self._prop_dict:
            return self._prop_dict["height"]
        else:
            return None

    @height.setter
    def height(self, val):
        self._prop_dict["height"] = val

    @property
    def width(self):
        """Gets and sets the width
        
        Returns: 
            int:
                The width
        """
        if "width" in self._prop_dict:
            return self._prop_dict["width"]
        else:
            return None

    @width.setter
    def width(self, val):
        self._prop_dict["width"] = val

