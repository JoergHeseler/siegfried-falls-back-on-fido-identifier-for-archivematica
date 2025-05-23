# Siegfried Falls Back on Fido Identifier for Archivematica

This repository provides an identification script for [Archivematica](https://www.archivematica.org/) that falls back on the [Fido](https://openpreservation.org/tools/fido/) tool if the [Siegfried](https://www.itforarchivists.com/siegfried) tool fails to identify a file.

## Installation

To install this script, follow these steps:

### 1. Create a new identification tool

- In the Archivematica frontend, navigate to **Preservation planning** > **Identification** > **Tools** > **Create new tool** or go directly to [this link](http://10.10.10.20/fpr/idtool/create/).
- Enter the following parameters:
  - **Description**: Enter `siegfried-falls-back-on-fido`.
  - **Version**: Enter `1.0.0`.
- Click **Save**.

### 2. Create a new identification command

- In the Archivematica frontend, navigate to **Preservation planning** > **Identification** > **Commands** > **Create new command** or go directly to [this link](http://10.10.10.20/fpr/idcommand/create/).
- Fill in the following fields:
  - **The related tool**: Select **siegfried-falls-back-on-fido**.
  - **Description**: Enter `Identify using siegfried-falls-back-on-fido`.
  - **Configuration**: Select **PUID**.
  - **Script type**: Select **Python script**.
  - **Script**: Paste the entire content of the [**siegfried-falls-back-on-fido-identifier.py**](./src/siegfried-falls-back-on-fido-identifier.py) file.
- Click **Save**.

### 3. Enable the new identification command

- In the Archivematica frontend, navigate to **Preservation planning** > **Identification** > **Commands** or go directly to [this link](http://10.10.10.20/fpr/idcommand/).
- Find **Identify using siegfried-falls-back-on-fido**.
- It should be enabled by default. Otherwise, click **Enable**.

## Test

To test this identifier, you can use the sample files located [here](https://github.com/JoergHeseler/mesh-samples-for-preservation-testing/tree/main/).

You can view the detailed identification results in the Archivmatica frontend after starting a transfer by expanding the `▸ Microservice: Identify file format` section and clicking on the gear icon of `Job Identify file format`.

Files with no errors end with `valid` in their name and should be correctly identified with this script. However, all other files contain errors and are either not identified at all or incorrectly identified as other file formats.

## Dependencies

[Archivematica 1.13.2](https://github.com/artefactual/archivematica/releases/tag/v1.13.2), [Siegfried 1.10.1](https://github.com/richardlehane/siegfried/releases/tag/v1.10.1) and [Fido 1.4.1](https://github.com/openpreserve/fido/releases/tag/v1.4.1) were used to analyze, design, develop and test this script.

## Background

As part of the [NFDI4Culture](https://nfdi4culture.de/) initiative, efforts are being made to enhance the ability of open-source digital preservation software like Archivematica to identify, validate and preserve 3D file formats. This repository provides a script, which combines two tools: Siegfried as the primary identifier and Fido as a fallback when Siegfried fails to recognize a format.

By default, Archivematica 1.13.2 can only use one identification tool. The advantage of this script is that it allows the combined use of both signature-based tools pre-installed in Archivematica, i. e. Siegfried and Fido, thus improving the overall identification process.

Previously, individual subversions of the archive-friendly 3D formats glTF or STL were often not recognized at all or misidentified. Now, with this new script, the accuracy of format identification has significantly improved, ensuring better support for the preservation of 3D files in Archivematica. The following table shows the results of the individual recognizer tools in comparison:

| 3D format                    | Siegfried 1.10.1     | Fido 1.4.1           | siegfried-falls-back-on-fido |
| ---------------------------- | -------------------- | -------------------- | ---------------------------- |
| **glTF 2.0 ASCII embedded**  | correctly recognized | wrongly recognized   | correctly recognized         |
| **glTF 2.0 ASCII separated** | correctly recognized | wrongly recognized   | correctly recognized         |
| **glTF 1.0 ASCII embedded**  | correctly recognized | correctly recognized | correctly recognized         |
| **glTF 1.0 ASCII separated** | correctly recognized | correctly recognized | correctly recognized         |
| **glTF 1.0 binary**          | not recognized       | correctly recognized | correctly recognized         |
| **glTF 2.0 binary**          | correctly recognized | correctly recognized | correctly recognized         |
| **STL ASCII**                | correctly recognized | correctly recognized | correctly recognized         |
| **STL binary**               | correctly recognized | wrongly recognized   | correctly recognized         |

## Related Projects

- [NFDI4Culture 3D Reference Implementations](https://github.com/JoergHeseler/nfdi4culture-3d-reference-implementations)

## Contributing

Contributions are welcome! Please open an issue or submit a pull request.

## Acknowledgments

Special thanks to the colleagues from the SLUB Dresden, specifically from the Infrastructure and Long-Term Availability division, for their support and valuable feedback during the development.

## Imprint

[NFDI4Culture](https://nfdi4culture.de/) – Consortium for Research Data on Material and Immaterial Cultural Heritage.  
Funded by the German Research Foundation (DFG), Project No. [441958017](https://gepris.dfg.de/gepris/projekt/441958017).

**Author**: [Jörg Heseler](https://orcid.org/0000-0002-1497-627X)  
**License**: [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/)
