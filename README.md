# qPCR for TSA_CRAFT
Some codes to rearrange raw data from QuantStudio3 qPCR machine for TSA_CRAFT, so users don't need to copy paste one by one.

17 March 2021: TSASort.py

4 May 2022: TSASortv2.py

Data sorting for TSA-CRAFT (https://journals.sagepub.com/doi/full/10.1177/2472555218823547)

TSA-CRAFT is an open source software to process Thermal Shift Assay data obtained from qPCR machines.
Here, I wrote a simple code which takes the raw data from QuantStudio 3. The .eds file from QuantStudio 3 is exported to Excel ("rawDataSample.xlsx") using Design & Analysis Software 2.6.0 (https://www.thermofisher.com/sg/en/home/global/forms/life-science/quantstudio-3-5-software.html).

By using the TSACraftv2.sort, user will get a sorted fluorescence data in the format required by TSA_CRAFT ("rawDataSampleSorted.xlsx").
