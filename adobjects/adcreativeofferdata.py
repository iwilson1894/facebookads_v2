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

class AdCreativeOfferData(
    AbstractObject,
):

    def __init__(self, api=None):
        super(AdCreativeOfferData, self).__init__()
        self._isAdCreativeOfferData = True
        self._api = api

    class Field(AbstractObject.Field):
        claim_limit = 'claim_limit'
        coupon_type = 'coupon_type'
        expiration_time = 'expiration_time'
        image_url = 'image_url'
        message = 'message'
        redemption_link = 'redemption_link'
        reminder_time = 'reminder_time'
        title = 'title'

    _field_types = {
        'claim_limit': 'int',
        'coupon_type': 'string',
        'expiration_time': 'string',
        'image_url': 'string',
        'message': 'string',
        'redemption_link': 'string',
        'reminder_time': 'string',
        'title': 'string',
    }

    @classmethod
    def _get_field_enum_info(cls):
        field_enum_info = {}
        return field_enum_info
