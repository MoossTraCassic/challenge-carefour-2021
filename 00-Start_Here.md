<!--
Licensed to the Apache Software Foundation (ASF) under one
or more contributor license agreements.  See the NOTICE file
distributed with this work for additional information
regarding copyright ownership.  The ASF licenses this file
to you under the Apache License, Version 2.0 (the
"License"); you may not use this file except in compliance
with the License.  You may obtain a copy of the License at

  http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing,
software distributed under the License is distributed on an
"AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY
KIND, either express or implied.  See the License for the
specific language governing permissions and limitations
under the License.
-->

# Welcome to Apache Beam Notebooks!

[Apache Beam](https://beam.apache.org/) is an open source, unified model for defining both batch and streaming data-parallel processing pipelines.

These notebooks assume you have basic knowledge of
[notebooks](https://jupyterlab.readthedocs.io/en/stable/user/notebook.html) and
the [Python programming language](https://python.org). They are designed to help
you learn the Python SDK of Apache Beam. You can build, iteratively augment your
Apache Beam pipelines, and explore the data in PCollections while doing so.

*   [Example 1: Word Count](Examples/01-Word_Count.ipynb) demonstrates a simple
    batch pipeline that counts words from a text file.
*   [Example 2: Streaming Word Count](Examples/02-Streaming_Word_Count.ipynb)
    demonstrates a simple streaming pipeline that counts words from a stream.
*   [Example 3: Streaming NYC Taxi Ride Data](Examples/03-Streaming_NYC_Taxi_Ride_Data.ipynb)
    demonstrates a streaming pipeline that processes a taxi ride data stream.

We also have:

*   A set of [tutorials](Tutorials/0_START_HERE.md) that go through the basic
    operations of Apache Beam with exercises.
*   A [notebook](Examples/Dataflow_Word_Count.ipynb) that shows you how to
    launch a Dataflow job based on
    [Example 1: Word Count](Examples/01-Word_Count.ipynb).
*   A [notebook](Examples/Visualize_Data.ipynb) that shows you how to visualize
    collected PCollection data with native Interactive Beam visualization and
    various third party visualization libraries.

If you have issues using the notebook, check these
[frequently asked questions](faq.md).

If you have any feedback on these notebooks, drop us a line at
beam-notebooks-feedback@google.com.
