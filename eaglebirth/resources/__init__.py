# This file re-exports resources from the parent module
# to fix the import path issue in client.py

import sys
from pathlib import Path

# Import from sibling resources.py file (not parent)
# We need to import from eaglebirth.resources module (the .py file)
import importlib.util

# Get the path to resources.py (sibling file in parent directory)
resources_py_path = Path(__file__).parent.parent / 'resources.py'

# Load the resources.py module
spec = importlib.util.spec_from_file_location("_resources_module", resources_py_path)
_resources_module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(_resources_module)

# Re-export all classes
BaseResource = _resources_module.BaseResource
EmailResource = _resources_module.EmailResource
SMSResource = _resources_module.SMSResource
WhatsAppResource = _resources_module.WhatsAppResource
OTPResource = _resources_module.OTPResource
QRCodeResource = _resources_module.QRCodeResource
ImageProcessingResource = _resources_module.ImageProcessingResource
StorageResource = _resources_module.StorageResource

__all__ = [
    'BaseResource',
    'EmailResource',
    'SMSResource',
    'WhatsAppResource',
    'OTPResource',
    'QRCodeResource',
    'ImageProcessingResource',
    'StorageResource',
]
