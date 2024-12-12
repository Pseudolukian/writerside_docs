# Run %product% for the first time

%product% welcome window consist from four tabs:
1. [Projects](#projects)
1. Customize
1. Plugins
1. Learn

In this article, we describe only the **Projects** section.

## Projects {id="projects"}
 
<img src="ws-interface-projects.png" alt="%product main window%" thumbnail="true"/>

On the **Projects page**, there are three buttons:
1. The [**New Project**](#new-project) button opens a window with the new project setup wizard.
1. The [**Open**](#open-project) button opens the open project window.
1. The [**Clone Repository**](#clone-repository) button opens a window with a GitHub URL path to the repository.

### New Project {id="new-project"}

This area provides you with many ways and options to create your project. You can utilize various helpful features. 
The **New Project** area includes four tabs:

<tabs>
<tab title="New Project">

<img src="ws-interface-new-project.png"/>

1. The **Location** field is the directory where your project will be saved. By default, the **Location** is:
<code><![CDATA[cd<path_to_your_user_home>\WritersideProjects\untitled]]></code> <br/> <br/> Rename the *untitled* placeholder to the new project name.

2. The **Create help instance** checkbox creates a help instance with a default structure for the project. This option is recommended for beginners. It will help you understand the project's structure.

3. **Help Instance Settings** area:
    * The **Name** field is the name of the instance. Try to name the instance concisely and understandably. You can change the instance name in the future.
    * The **Create first topic** checkbox provides the option to create the first topic (file) in the default instance. The first topic can be created in two formats: `Markdown` or `XML`.
    * The **Template** dropdown list consists of content templates for the first topic.
    * The **Topic title** field sets the topic title (h1 header).

After clicking the **Create** button, your new project will be created and opened in a new window.
</tab>

<tab title="Import from MD">

<img src="ws-interface-import-from-md.png" alt="ws-import-from-md"/>

1. The **Location** field is the directory where your project will be saved. By default, the **Location** is:
<code><![CDATA[cd<path_to_your_user_home>\WritersideProjects\untitled]]></code> <br/> Rename the *untitled* placeholder to the new project name.

2. The **Copy from** field is the path to your `MD` files to import them into the new project.
3. The **Markdown files used to copy** the navigation tree specify which files to include in the new project.
4. The **Copy all media files used in selected Markdown files** checkbox copies the media files associated with the Markdown files to the images folder in the new project.
</tab>
<tab title="Playground">

<img src="ws-interface-playground.jpg" alt="ws-interface-playground"/>

This default project template demonstrates various features of the Docs as Code paradigm implemented in %product%.

Will be created:
* Two help instances;
* Topics with demo content, including math formulas, diagrams, semantic elements, images, content reuse methodology, code snippets, and more;
* Configuration file;
* Categories file;
* Two TOC files.

This project template is very helpful for beginners to understand how %product% concepts and elements work together.

We strongly recommend this template as your first project.

</tab>

<tab title="API Docs">

<img src="ws-interface-api-doc.jpg" alt="ws-interface-api-doc"/>

This new project template creates an Open API specification-ready instance.

The template demonstrates the usability of:
* API Docs semantic markup elements;
* Using the unified Open API YAML standard for constrained API documentation.

With this template, you can easily understand %product%'s API documentation concepts and start creating Open API-ready documentation.
</tab>
</tabs>

### Open {id="open-project"}

If you have a project on your local machine, you can open it by:

<img src="ws-interface-open-project.jpg" alt="ws-interface-open-project"/>

### Clone Repository {id="clone-repository"}

<include from="git-installed-on-machine.md" element-id="install-git-warning"></include>

%product% includes an integrated Git client for working with both local and remote Git repositories. Use the **Clone Repository** feature to clone a repository onto your local machine and keep it synchronized.

<img src="ws-interface-clone-repository.jpg" alt="ws-interface-clone-repository"/>

The **Clone Repository** window includes:

1. The **Version control** dropdown list. Currently, it only has one option: Git.
1. The **URL** field. Copy the URL of your repository from GitHub by navigating to your repository, clicking the 
   **Code** green button, selecting the **HTTPS** section, and then clicking the **Copy URL to clipboard** button. Paste the URL into the **URL** field of the **Clone Repository** window.

   <img src="github-clone-link-to-repo.png" alt="github-clone-link-to-repo"/>

1. The **Directory** field specifies the path where the remote repository will be cloned. The field automatically uses 
the GitHub repository name to reconstruct the full path to your local project.
1. The checkbox option **Shallow clone with a truncated history of [N] commits** allows you to truncate the commit 
   history.

After cloning the repository, you can view the commit history and make new pull requests in your repository. To check the commit history, click on the **Git** button in the left corner or use <shortcut>Alt+9</shortcut> on Windows and <shortcut>⌘ Cmd+9</shortcut> on macOS:

<img src="github-clone-repo-done.jpg" alt="github-clone-repo-done" thumbnail="true"/>