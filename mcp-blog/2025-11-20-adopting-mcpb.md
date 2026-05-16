# Adopting the MCP Bundle format (.mcpb) for portable local servers

*2025-11-20*

---

**Summary:** The MCP Bundle format (MCPB) is now part of the Model Context Protocol project. This distribution format simplifies how developers package and share local MCP servers, enabling users to install them across any compatible client, including the Claude desktop app, Claude Code, and MCP for Windows.
What are MCP Bundles?
MCP Bundles are ZIP archives containing a local MCP server and a manifest.json that describes the server and its capabilities. The format is similar to Chrome extensions (.crx) or VS Code extensions (.vsix), enabling end users to install local MCP servers with a single click.

TheMCP Bundle format(MCPB) is now part of theModel Context Protocol project. This distribution format simplifies how developers package and share local MCP servers, enabling users to install them across any compatible client, including theClaude desktop app,Claude Code, andMCP for Windows.


## What are MCP Bundles?#


MCP Bundles are ZIP archives containing a local MCP server and amanifest.jsonthat describes the server and its capabilities. The format is similar to Chrome extensions (.crx) or VS Code extensions (.vsix), enabling end users to install local MCP servers with a single click.


```
manifest.json
```



```
.crx
```



```
.vsix
```


A basic bundle structure looks like:


```
bundle.mcpb (ZIP file)├── manifest.json      # Required: Bundle metadata and configuration├── server/            # Server implementation│   └── index.js├── node_modules/      # Bundled dependencies└── icon.png           # Optional: Bundle icon
```


The format supports servers written in Node.js, Python, or compiled binaries, giving developers flexibility in how they build their integrations, while maintaining a consistent distribution mechanism for users.


## Why move MCPB to the MCP project?#


Anthropic originally developed MCPB (previously called DXT) for Claude’s desktop applications. However, we believe the local MCP server ecosystem benefits when portability extends beyond any single client. By moving thebundle specification,CLI tooling, andreference implementationto the MCP project, we’re enabling:

Cross-client compatibility:A bundle created for one MCP-compatible application should work in any other that implements the specification. Developers can distribute their work once and reach users across the ecosystem.Ecosystem-wide tooling:ThemcpbCLI and associated libraries are now open for the community to extend, improve, and build upon. Client developers can adopt standardized code for loading and verifying bundles.User-friendly installation:End users benefit from a consistent installation experience regardless of which AI application they prefer. Configuration variables, permissions, and updates can be handled uniformly.Shared community:MCPB contributors can now collaborate in the open with the rest of theMCP community.

- Cross-client compatibility:A bundle created for one MCP-compatible application should work in any other that implements the specification. Developers can distribute their work once and reach users across the ecosystem.

- Ecosystem-wide tooling:ThemcpbCLI and associated libraries are now open for the community to extend, improve, and build upon. Client developers can adopt standardized code for loading and verifying bundles.


```
mcpb
```


- User-friendly installation:End users benefit from a consistent installation experience regardless of which AI application they prefer. Configuration variables, permissions, and updates can be handled uniformly.

- Shared community:MCPB contributors can now collaborate in the open with the rest of theMCP community.


## What this means for developers#


This transition is mostly a logistical change, but also brings some benefits to implementers. For those that are building:

Servers:You can use MCPB to package your local MCP servers for distribution across multiple clients. ThemcpbCLI helps you create amanifest.jsonand package your server into a.mcpbfile. Once packaged, users can install your server with a single click in any client that supports MCP Bundles.Clients:You can add support for MCP Bundles to your application using the open source toolchain.The repositoryincludes the schemas and key functions used by Claude for macOS and Windows to implement bundle support, which you can adapt for your own client.

- Servers:You can use MCPB to package your local MCP servers for distribution across multiple clients. ThemcpbCLI helps you create amanifest.jsonand package your server into a.mcpbfile. Once packaged, users can install your server with a single click in any client that supports MCP Bundles.


```
mcpb
```



```
manifest.json
```



```
.mcpb
```


- Clients:You can add support for MCP Bundles to your application using the open source toolchain.The repositoryincludes the schemas and key functions used by Claude for macOS and Windows to implement bundle support, which you can adapt for your own client.


## Getting started#


Check out the repo to get started:modelcontextprotocol/mcpb. We encouragefeedbackand contributions!


## Acknowledgements#


Thanks to the MCP contributors and maintainers involved in making this happen, including:

David Soria Parra(MCP Lead Maintainer)Adam Jones(MCP Maintainer)Joan Xie(MCPB Maintainer)Felix Rieseberg(MCPB Maintainer)Alex Sklar(MCPB Maintainer)

- David Soria Parra(MCP Lead Maintainer)

- Adam Jones(MCP Maintainer)

- Joan Xie(MCPB Maintainer)

- Felix Rieseberg(MCPB Maintainer)

- Alex Sklar(MCPB Maintainer)

---

**Source:** http://blog.modelcontextprotocol.io/posts/2025-11-20-adopting-mcpb/

*This is a mirror of the MCP blog for offline reading. All content is copyright the Model Context Protocol project.*