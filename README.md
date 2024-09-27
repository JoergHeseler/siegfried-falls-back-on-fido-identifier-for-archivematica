
# Siegfried Falls Back on Fido

**siegfried_falls_back_on_fido** is a custom identification tool for Archivematica that falls back on the Fido tool if Siegfried fails to identify a file.


## Installation

To install the **siegfried_falls_back_on_fido** identification script in Archivematica, follow these steps:

### 1. Create a new identification tool
- In the Archivematica frontend, navigate to **Preservation planning** > **Identification** > **Tools** > **Create new tool** or go directly to [this link](http://10.10.10.20/fpr/idtool/create/).
- Enter the following parameters:
    - **Description**: Enter `"siegfried_falls_back_on_fido"`.
    - **Version**: Enter `"1.0"`.
- Click **Save**.

### 2. Create a new identification command
- In the Archivematica frontend, navigate to **Preservation planning** > **Identification** > **Commands** > **Create new command** or go directly to [this link](http://10.10.10.20/fpr/idcommand/create/).
- Fill in the following fields:
    - **Description**: Enter `"Identify using siegfried_falls_back_on_fido"`.
    - **Configuration**: Select **PUID**.
    - **Script type**: Select **Python script**.
    - **Script**: Paste the entire content of the **siegfried_falls_back_on_fido.py** file.
- Click **Save**.

### 3. Enable the new identification command
- In the Archivematica frontend, navigate to **Preservation planning** > **Identification** > **Commands** or go directly to [this link](http://10.10.10.20/fpr/idcommand/).
- Find **Identify using siegfried_falls_back_on_fido**. 
- Click **Enable**.

## Requirements

- Archivematica (version 1.13.2 or higher)
- Siegfried
- Fido

## Usage

After setting up the tool, follow these steps to identify files:
1. Go to the Archivematica interface.
2. Select the new identifier tool **siegfried_falls_back_on_fido**.
3. Test with sample files to verify.

## Imprint

[NFDI4Culture](https://nfdi4culture.de/) – Consortium for Research Data on Material and Immaterial Cultural Heritage

NFDI4Culture is a consortium within the German [National Research Data Infrastructure (NFDI)](https://www.nfdi.de/).

Author: [Jörg Heseler](https://orcid.org/0000-0002-1497-627X)

This project is licensed under a [Creative Commons Attribution 4.0 International License (CC BY 4.0)](https://creativecommons.org/licenses/by/4.0/).

NFDI4Culture is funded by the German Research Foundation (DFG) – Project number – [441958017](https://gepris.dfg.de/gepris/projekt/441958017?context=projekt&task=showDetail&id=441958017&)
