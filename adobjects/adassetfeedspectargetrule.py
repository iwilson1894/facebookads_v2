# Copyright 2014 Facebook, Inc.

# You are hereby granted a non-exclusive, worldwide, royalty-free license to
# use, copy, modify, and distribute this software in source code or binary
# form for use in connection with the web services and APIs provided by
# Facebook.

# As with any software that integrates with the Facebook platform, your use
# of this software is subject to the Facebook Developer Principles and
# Policies [http://developers.facebook.com/policy/]. This copyright notice
# shall be included in all copies or substantial portions of the software.

# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL
# THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING
# FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER
# DEALINGS IN THE SOFTWARE.

from facebookads_v2.adobjects.abstractobject import AbstractObject

"""
This class is auto-generated.

For any issues or feature requests related to this class, please let us know on
github and we'll fix in our codegen framework. We'll not be able to accept
pull request for this class.
"""

class AdAssetFeedSpecTargetRule(
    AbstractObject,
):

    def __init__(self, api=None):
        super(AdAssetFeedSpecTargetRule, self).__init__()
        self._isAdAssetFeedSpecTargetRule = True
        self._api = api

    class Field(AbstractObject.Field):
        body_label = 'body_label'
        call_to_action_type_label = 'call_to_action_type_label'
        caption_label = 'caption_label'
        description_label = 'description_label'
        image_label = 'image_label'
        link_url_label = 'link_url_label'
        targeting = 'targeting'
        title_label = 'title_label'
        video_label = 'video_label'

    _field_types = {
        'body_label': 'AdAssetFeedSpecAssetLabel',
        'call_to_action_type_label': 'AdAssetFeedSpecAssetLabel',
        'caption_label': 'AdAssetFeedSpecAssetLabel',
        'description_label': 'AdAssetFeedSpecAssetLabel',
        'image_label': 'AdAssetFeedSpecAssetLabel',
        'link_url_label': 'AdAssetFeedSpecAssetLabel',
        'targeting': 'Object',
        'title_label': 'AdAssetFeedSpecAssetLabel',
        'video_label': 'AdAssetFeedSpecAssetLabel',
    }

    @classmethod
    def _get_field_enum_info(cls):
        field_enum_info = {}
        return field_enum_info
