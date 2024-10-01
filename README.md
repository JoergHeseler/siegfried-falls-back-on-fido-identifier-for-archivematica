# siegfried_falls_back_on_fido_identifier_for_archivematica

**siegfried_falls_back_on_fido_identifier_for_archivematica** is a custom identification tool for [Archivematica](https://www.archivematica.org/) that falls back on the [Fido](https://openpreservation.org/tools/fido/) tool if [Siegfried](https://www.itforarchivists.com/siegfried) fails to identify a file.

## Installation

To install **siegfried_falls_back_on_fido_identifier_for_archivematica**, follow these steps:

### 1. Create a new identification tool
- In the Archivematica frontend, navigate to **Preservation planning** > **Identification** > **Tools** > **Create new tool** or go directly to [this link](http://10.10.10.20/fpr/idtool/create/).
- Enter the following parameters:
    - **Description**: Enter `siegfried_falls_back_on_fido`.
    - **Version**: Enter `1.0`.
- Click **Save**.

### 2. Create a new identification command
- In the Archivematica frontend, navigate to **Preservation planning** > **Identification** > **Commands** > **Create new command** or go directly to [this link](http://10.10.10.20/fpr/idcommand/create/).
- Fill in the following fields:
    - **Description**: Enter `Identify using siegfried_falls_back_on_fido`.
    - **Configuration**: Select **PUID**.
    - **Script type**: Select **Python script**.
    - **Script**: Paste the entire content of the **siegfried_falls_back_on_fido_identifier.py** file.
- Click **Save**.

### 3. Enable the new identification command
- In the Archivematica frontend, navigate to **Preservation planning** > **Identification** > **Commands** or go directly to [this link](http://10.10.10.20/fpr/idcommand/).
- Find **Identify using siegfried_falls_back_on_fido**. 
- Click **Enable**.

## Test

To test this validator you can use the sample files located in the [`test`](./test/) folder.

You can view the error codes and detailed validation results in the Archivmatica frontend after starting a transfer by expanding the `▸ Microservice: Identify file format` section and clicking on the gear icon of `Job Identify file format`.

Files with no errors end with the filename `_valid` and should pass validation with this script (i. e. return error code **0**) when validated with this script. However, all other files contain errors and should fail validation (i. e. return error code **1**).

## Dependencies

[Archivematica 1.13.2](https://github.com/artefactual/archivematica/releases/tag/v1.13.2), [Siegfried 1.10.1](https://github.com/richardlehane/siegfried/releases/tag/v1.10.1) and [Fido 1.4.1](https://github.com/openpreserve/fido/releases/tag/v1.4.1) were used to analyze, design, develop and test this script.

## Background

As part of the [NFDI4Culture](https://nfdi4culture.de/) initiative, efforts are being made to enhance the ability of open-source digital preservation software like Archivematica to identify, validate and preserve 3D file formats. This repository provides the **siegfried_falls_back_on_fido_identifier_for_archivematica** script, which combines two tools: Siegfried as the primary identifier and Fido as a fallback when Siegfried fails to recognize a format. 

By default, Archivematica 1.13.2 can only use one identification tool. The advantage of this script is that it allows the combined use of both signature-based tools pre-installed in Archivematica, i. e. Siegfried and Fido, thus improving the overall identification process.

Previously, individual subversions of the archive-friendly 3D formats glTF or STL were often not recognized at all or misidentified. Now, with **siegfried_falls_back_on_fido_identifier_for_archivematica**, the accuracy of format identification has significantly improved, ensuring better support for the preservation of 3D files in Archivematica. The following table shows the results of the individual recognizer tools in comparison:

| 3D format                    | Siegfried 1.10.1     | Fido 1.4.1           | siegfried_falls_back_on_fido |
| ---------------------------- | -------------------- | -------------------- | ---------------------------- |
| **glTF 2.0 ASCII embedded**  | correctly recognized | wrongly recognized   | correctly recognized         |
| **glTF 2.0 ASCII separated** | correctly recognized | wrongly recognized   | correctly recognized         |
| **glTF 1.0 ASCII embedded**  | correctly recognized | correctly recognized | correctly recognized         |
| **glTF 1.0 ASCII separated** | correctly recognized | correctly recognized | correctly recognized         |
| **glTF 1.0 binary**          | not recognized       | correctly recognized | correctly recognized         |
| **glTF 2.0 binary**          | correctly recognized | correctly recognized | correctly recognized         |
| **STL ASCII**                | correctly recognized | correctly recognized | correctly recognized         |
| **STL binary**               | correctly recognized | wrongly recognized   | correctly recognized         |

## Related projects

- [dae_validator_for_archivematica](https://github.com/JoergHeseler/dae_validator_for_archivematica)
- [gltf_validator_for_archivematica](https://github.com/JoergHeseler/gltf_validator_for_archivematica)
- [stl_validator_for_archivematica](https://github.com/JoergHeseler/stl_validator_for_archivematica)
- [x3d_validator_for_archivematica](https://github.com/JoergHeseler/x3d_validator_for_archivematica)

## Imprint

[NFDI4Culture](https://nfdi4culture.de/) – Consortium for Research Data on Material and Immaterial Cultural Heritage

NFDI4Culture is a consortium within the German [National Research Data Infrastructure (NFDI)](https://www.nfdi.de/).

Author: [Jörg Heseler](https://orcid.org/0000-0002-1497-627X)

This project is licensed under a [Creative Commons Attribution 4.0 International License (CC BY 4.0)](https://creativecommons.org/licenses/by/4.0/).

NFDI4Culture is funded by the German Research Foundation (DFG) – Project number – [441958017](https://gepris.dfg.de/gepris/projekt/441958017).