# Install %product%

To install %product%, you can use the recommended tool for [installing](#install-by-toolbox) JetBrains products, the %toolbox%, or [install](#directly-install) %product% directly.

## Install %product% using the %toolbox% {id="install-by-toolbox"}

<tabs group="install" id="install-ws-by-toolbox-tabs">
<tab title="Windows" group-key="Windows" id="install-ws-by-toolbox-windows">

1. Download the installer (.exe for Windows) from the [%toolbox%](https://www.jetbrains.com/toolbox-app/) web page.
1. Run the installer and follow the wizard steps.
1. The %toolbox% starts automatically after installation. If the app does not start automatically, click on ![JB-Tool-Box-icon](https://resources.jetbrains.com/help/img/idea/2024.3/app.nodes.toolbox.svg){width=%inline-icon-width%}.
1. Click on **install** button to install %product%:

    <img src="ws-install-by-toolbox.jpg" alt="JB-Tool-Box" width="%img-def-size-in-tabs%"/>
    <include from="toolbox-setup-def-location.md" element-id="toolbox-setup-info-windows"></include>

1. After install %product%, run the IDE by clicking on the icon ![ws-icon](https://plugins.jetbrains.com/files/20158/631757/icon/pluginIcon.svg){width=%inline-icon-width%} in the **Installed** area:

    <img src="install-ws-complete.png" alt="run-ws-toolbox" width="%img-def-size-in-tabs%"/>

Or run IDE from the Windows **Start menu**.

</tab>
<tab title="MacOS" group-key="MacOS" id="install-ws-by-toolbox-macos">

1. Download the installer %toolbox% `.dmg macOS Intel` for `Intel` processors or `.dmg macOS Apple Silicon` for `M1` and higher processors from the [%toolbox%](https://www.jetbrains.com/toolbox-app/) web page.
1. Mount `.dmg` by double-clicking on it and add %toolbox% to the `Applications` menu by drag and drop: 

    <img src="add-toolbox-to-apps-mac-os.png" alt="add-ws-to-apps-mac-os" width="%img-def-size-in-tabs%"/>

    Now you can run %toolbox% from **Launchpad**.

1. Run %toolbox% and click on **install** button to install %product%:

    <img src="ws-install-by-toolbox.jpg" alt="JB-Tool-Box" width="%img-def-size-in-tabs%"/>
    <include from="toolbox-setup-def-location.md" element-id="toolbox-setup-info-macos"></include>

2. After install %product%, run the IDE by clicking on the icon ![ws-icon](https://plugins.jetbrains.com/files/20158/631757/icon/pluginIcon.svg){width=%inline-icon-width%} in the **Installed** area:<img src="install-ws-complete.png" alt="run-ws-toolbox" width="%img-def-size-in-tabs%/>
Or run IDE from the **Launchpad**.
</tab>

<tab title="Linux" group-key="Linux" id="install-ws-by-toolbox-linux">
<include from="install-ws-on-linux.md" element-id="info-install-ws-on-linux"></include>

1. Download the tarball `.tar.gz` from the %toolbox% App [web page](%toolbox-link%) for your type of OS (`Linux 64-bit x86` or `Linux ARM64`) or use `wget`:
    <code-block lang="bash">
    wget https://download.jetbrains.com/toolbox/jetbrains-toolbox-%actual-ver-ws%.tar.gz
    </code-block>
1. Extract the tarball and launch the executable:
    <code-block lang="Bash">
    tar -xzf jetbrains-toolbox-%actual-ver-ws%.tar.gz && cd jetbrains-toolbox-%actual-ver-ws% && ./jetbrains-toolbox
    </code-block>
1. The %toolbox% App will install itself into `$HOME/.local/share/JetBrains/Toolbox/bin` and run from there.
   After you run the %toolbox% App for the first time, it will automatically add the %toolbox% App icon ![ws-icon](https://plugins.jetbrains.com/files/20158/631757/icon/pluginIcon.svg){width=%inline-icon-width%} to the **main menu**.
1. Run %toolbox% and click on **install** button to install %product%:
    
   <img src="ws-install-by-toolbox.jpg" alt="ws-install-by-toolbox" width="%img-def-size-in-tabs%"/>

1. After install %product%, run the IDE by clicking on the icon ![ws-icon](https://plugins.jetbrains.com/files/20158/631757/icon/pluginIcon.svg){width=%inline-icon-width%} in the **Installed** area:

    <img src="install-ws-complete.png" alt="run-ws-toolbox" width="%img-def-size-in-tabs%"/>
    
   Or run IDE from the **Application menu**.

</tab>
</tabs>

## Standalone installation {id="directly-install"}

Install %product% manually to manage the location of every instance and all the configuration files. For example, if you have a policy that requires specific install locations.

<tabs group="install" id="install-ws-by-standalone-tabs">
<tab title="Windows" group-key="Windows" id="install-ws-by-standalone-windows">

1. Download the %product% [installer](https://www.jetbrains.com/writerside/download/#section=windows) (`.exe`) for Windows `x86` or Windows `ARM`.
1. Run the installer and follow the wizard steps:
    * Choose **Create Desktop Shortcut** option to create a shortcut on your desktop;
    * Choose **Update Context Menu** to add **Open folder as Project**;
    * Choose **Create Associations** to associate `.topic` and `.tree` files with %product%;
    * Choose **Update PATH Variables** to add `bin` folder to the `PATH`.
1. To run %product%, find it in the Windows **Start** menu or use the desktop shortcut.
</tab>
<tab title="MacOS" group-key="MacOS" id="install-ws-by-standalone-macos">

1. Download the [disk image](https://www.jetbrains.com/writerside/download/#section=mac) `.dmg` for Intel or Apple Silicon.
1. Mount the image by double-clicking on it and drag the %product% to the **Applications** folder.
1. Run the %product% app from the **Applications** directory, **Launchpad**, or **Spotlight**.
</tab>
<tab title="Linux" group-key="Linux" id="install-ws-by-standalone-linux">

1. Download the [tarball](https://www.jetbrains.com/writerside/download/#section=linux) for `Linux x86` or `Linux ARM64`.
    <include from="install-ws-on-ubuntu.md" element-id="install-ws-on-ubuntu"></include>
1. Unpack the writerside-*.tar.gz file to a different folder, if your current `Download` folder doesn't support file execution:
   <code-block lang="Bash"><![CDATA[tar xzf pycharm-*.tar.gz -C <new_archive_folder>]]></code-block>
1. The recommended installation location according to the filesystem hierarchy standard (FHS) is `/opt`.
To install %product% into this directory, enter the following command:
    <code-block lang="Bash">sudo tar xzf pycharm-*.tar.gz -C /opt/</code-block>
1. Switch to the `bin` subdirectory:
    <code-block lang="Bash"><![CDATA[cd <new archive folder>/writerside-*/bin]]></code-block>
    For example:
    <code-block lang="Bash">cd /opt/writerside-243.21565.432/bin</code-block>
1. Run `writerside.sh` from the `bin` subdirectory:
    <code-block lang="Bash">sh writerside.sh</code-block>
</tab>
</tabs>

After installing and running %product% for the first time, we recommend taking a tour of the IDE interface.
You can find the GUI guides in this documentation chapter.