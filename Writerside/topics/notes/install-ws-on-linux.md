<note id="info-install-ws-on-linux">

The %toolbox% is packaged in [AppImage](https://appimage.org) and requires FUSE to run.
If your distribution doesn't use the `libfuse2` package, install it by running the following command:

```Bash
sudo apt install libfuse2
```

Additionally, make sure that the following required packages are installed: `libxi6`, `libxrender1`, `libxtst6`, `mesa-utils`, `libfontconfig`, `libgtk-3-bin`.

<procedure title="Ways to check installed packages" collapsible="true">
    <step>You can use the `dpkg` command to check if a package is installed:
        <code-block>
        dpkg -s libxi6 libxrender1 libxtst6 mesa-utils libfontconfig1 libgtk-3-bin
        </code-block>
    </step>
    <step>Alternatively, you can use `apt`:
        <code-block>
        apt list --installed libxi6 libxrender1 libxtst6 mesa-utils libfontconfig1 libgtk-3-bin
        </code-block>
    </step>
</procedure>

</note>