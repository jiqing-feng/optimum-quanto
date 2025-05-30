# Copyright 2024 The HuggingFace Team. All rights reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import platform

import torch
from packaging import version

from .cpp import *
from .extension import *


if torch.cuda.is_available() and platform.system() == "Linux":
    if torch.version.cuda:
        from .cuda import *
    elif torch.version.hip:
        from .hip import *

if torch.backends.mps.is_available():
    from .mps import *


def _is_xpu_available():
    # SYCL extension support is added in torch>=2.7 on Linux
    if platform.system() != "Linux":
        return False
    if version.parse(torch.__version__).release < version.parse("2.7").release:
        return False
    return torch.xpu.is_available()


if _is_xpu_available():
    from .xpu import *
