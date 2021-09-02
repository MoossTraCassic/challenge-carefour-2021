# Copyright 2020 Google Inc. All Rights Reserved.
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

# pylint: skip-file

"""Module to pre load python and Javascript libs before their usages."""

try:
  import apache_beam as beam
  import apache_beam.runners.interactive.interactive_beam as ib
  from apache_beam.runners.interactive.interactive_runner import InteractiveRunner
  # Below only takes effect when frontends are connected to the kernel during
  # the kernel startup, which is not guaranteed.
  from IPython.core.display import display
  from IPython.core.display import HTML
  display(
      HTML("""
    <script src="https://ajax.googleapis.com/ajax/libs/jquery/2.2.4/jquery.min.js"></script>
    <script src="https://cdn.datatables.net/1.10.20/js/jquery.dataTables.min.js"></script>
  """))
except ImportError:
  pass
