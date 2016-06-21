# Copyright 2016, A10 Networks
#
#    Licensed under the Apache License, Version 2.0 (the "License"); you may
#    not use this file except in compliance with the License. You may obtain
#    a copy of the License at
#
#         http://www.apache.org/licenses/LICENSE-2.0
#
#    Unless required by applicable law or agreed to in writing, software
#    distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
#    WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
#    License for the specific language governing permissions and limitations
#    under the License.


def convert_to_lower(input):
    try:
        return input.lower()
    except AttributeError:
        return input


def convert_to_float(input):
    try:
        return float(input)
    except ValueError:
        return input


def convert_nullable(convert_value):
    def f(input):
        if input is not None:
            return convert_value(input)
        return None
    return f


def validate_float(data, options):
    if not isinstance(data, float):
        return "'%s' is not a number" % input


def validate_reference(data, options):
    """Referential integrity is enforced by the data model"""
    return None


def validate_nullable(validators):
    def f(data, options):
        if data is not None:
            for rule in options:
                value_validator = validators[rule]
                reason = value_validator(data, options[rule])
                if reason:
                    return reason
    return f


VALIDATORS = {
    'a10_type:float': lambda validators: validate_float,
    'a10_type:reference': lambda validators: validate_reference,
    'a10_type:nullable': validate_nullable
}
