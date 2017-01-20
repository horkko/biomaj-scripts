# biomaj-scripts
================

This project aims to centralize and make accessible some scripts that the community using [biomaj](https://biomaj.github.io)
or [biomaj-manager](https://github.com/horkko/biomaj-manager) have developped for their own usage.

* *Scripts*
  * `bm_bank_sections.py`: This script is used to get the list of available db or db sub sections for a particular tool.
                           For now only `blast2` and `golden` tool are supported.
                           To use it, you'll need to have `biomaj-manager` installed.
    * Usage: `bm_bank_sections.py <bank> <tool>`
    * Output: A db/sub db per line
    ```
    <protein db a>
    <protein db b>
    ...
    <protein sub db 1>
    <protein sub db 2>
    ...
    <nucleic db a>
    <nucleic db b>
    ...
    <nucleic sub db 1>
    <nucleic sub db 2>
    ```
