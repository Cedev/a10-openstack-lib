# Copyright (C) 2016 A10 Networks Inc. All rights reserved.

import validators

EXTENSION = 'a10-certificate'

SERVICE = "A10_CERTIFICATE"

CERTIFICATES = 'a10_certificates'
CERTIFICATE = 'a10_certificate'

CERTIFICATE_BINDING = 'a10_certificate_binding'
CERTIFICATE_BINDINGS = 'a10_certificate_bindings'

RESOURCE_ATTRIBUTE_MAP = {
    CERTIFICATES: {
        'id': {
            'allow_post': False,
            'allow_put': True,
            'validate': {
                'type:uuid': None
            },
            'is_visible': True,
            'primary_key': True
        },
        'tenant_id': {
            'allow_post': True,
            'allow_put': False,
            'required_by_policy': True,
            'is_visible': True
        },
        'name': {
            'allow_post': True,
            'allow_put': True,
            'validate': {
                'type:string': None
            },
            'is_visible': True,
            'default': ''
        },
        'description': {
            'allow_post': True,
            'allow_put': True,
            'validate': {
                'type:string': None
            },
            'is_visible': True,
            'default': '',
        },
        'cert_data': {
            'allow_post': True,
            'allow_put': True,
            'validate': {
                'type:string': None
            },
            'is_visible': True,
            'default': ''
        },
        'key_data': {
            'allow_post': True,
            'allow_put': True,
            'validate': {
                'type:string': None
            },
            'is_visible': False,
            'default': ''
        },
        'intermediate_data': {
            'allow_post': True,
            'allow_put': True,
            'validate': {
                'type:string': None,
            },
            'is_visible': True,
            'default': ''
        },
        'password': {
            'allow_post': True,
            'allow_put': True,
            'validate': {
                'type:string': None,
            },
            'is_visible': False,
            'default': ''

        }
    },

    CERTIFICATE_BINDINGS: {
        'id': {
            'allow_post': False,
            'allow_put': False,
            'is_visible': True,
            'primary_key': True,
            'validate': {
                'type:uuid': None
            }
        },
        'tenant_id': {
            'allow_post': True,
            'allow_put': False,
            'required_by_policy': True,
            'is_visible': True
        },
        'certificate_id': {
            'allow_post': True,
            'allow_put': True,
            'validate': {
                'type:uuid': None,
                'a10_type:reference': CERTIFICATE
            },
            'is_visible': True
        },
        'listener_id': {
            'allow_post': True,
            'allow_put': True,
            'validate': {
                'type:uuid': None,
                'a10_type:reference': 'lbaas_listener'
            },
            'is_visible': True
        },
        'certificate_name': {
            'allow_post': False,
            'allow_put': False,
            'is_visible': True
        }
    }
}

VALIDATORS = validators.VALIDATORS
