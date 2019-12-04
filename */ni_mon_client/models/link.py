# coding: utf-8

"""
    NI-Mon

    Monitoring module for NI project  # noqa: E501

    OpenAPI spec version: 1.0.0
    Contact: vantu.bkhn@gmail.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six


class Link(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'id': 'str',
        'node1_name': 'str',
        'node2_name': 'str',
        'delay_us': 'int',
        'max_bw_mbps': 'int'
    }

    attribute_map = {
        'id': 'id',
        'node1_name': 'node1_name',
        'node2_name': 'node2_name',
        'delay_us': 'delay_us',
        'max_bw_mbps': 'max_bw_mbps'
    }

    def __init__(self, id=None, node1_name=None, node2_name=None, delay_us=None, max_bw_mbps=None):  # noqa: E501
        """Link - a model defined in Swagger"""  # noqa: E501

        self._id = None
        self._node1_name = None
        self._node2_name = None
        self._delay_us = None
        self._max_bw_mbps = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if node1_name is not None:
            self.node1_name = node1_name
        if node2_name is not None:
            self.node2_name = node2_name
        if delay_us is not None:
            self.delay_us = delay_us
        if max_bw_mbps is not None:
            self.max_bw_mbps = max_bw_mbps

    @property
    def id(self):
        """Gets the id of this Link.  # noqa: E501


        :return: The id of this Link.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this Link.


        :param id: The id of this Link.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def node1_name(self):
        """Gets the node1_name of this Link.  # noqa: E501


        :return: The node1_name of this Link.  # noqa: E501
        :rtype: str
        """
        return self._node1_name

    @node1_name.setter
    def node1_name(self, node1_name):
        """Sets the node1_name of this Link.


        :param node1_name: The node1_name of this Link.  # noqa: E501
        :type: str
        """

        self._node1_name = node1_name

    @property
    def node2_name(self):
        """Gets the node2_name of this Link.  # noqa: E501


        :return: The node2_name of this Link.  # noqa: E501
        :rtype: str
        """
        return self._node2_name

    @node2_name.setter
    def node2_name(self, node2_name):
        """Sets the node2_name of this Link.


        :param node2_name: The node2_name of this Link.  # noqa: E501
        :type: str
        """

        self._node2_name = node2_name

    @property
    def delay_us(self):
        """Gets the delay_us of this Link.  # noqa: E501


        :return: The delay_us of this Link.  # noqa: E501
        :rtype: int
        """
        return self._delay_us

    @delay_us.setter
    def delay_us(self, delay_us):
        """Sets the delay_us of this Link.


        :param delay_us: The delay_us of this Link.  # noqa: E501
        :type: int
        """

        self._delay_us = delay_us

    @property
    def max_bw_mbps(self):
        """Gets the max_bw_mbps of this Link.  # noqa: E501


        :return: The max_bw_mbps of this Link.  # noqa: E501
        :rtype: int
        """
        return self._max_bw_mbps

    @max_bw_mbps.setter
    def max_bw_mbps(self, max_bw_mbps):
        """Sets the max_bw_mbps of this Link.


        :param max_bw_mbps: The max_bw_mbps of this Link.  # noqa: E501
        :type: int
        """

        self._max_bw_mbps = max_bw_mbps

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value
        if issubclass(Link, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, Link):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
