# Introducing the MCP Registry

*2025-09-08*

---

**Summary:** Today, we’re launching the Model Context Protocol (MCP) Registry—an open catalog and API for publicly available MCP servers to improve discoverability and implementation. By standardizing how servers are distributed and discovered, we’re expanding their reach while making it easier for clients to get connected.
The MCP Registry is now available in preview. To get started:

Add your server by following our guide on Adding Servers to the MCP Registry (for server maintainers)
Access server data by following our guide on Accessing MCP Registry Data (for client maintainers)

Single source of truth for MCP servers
In March 2025, we shared that we wanted to build a central registry for the MCP ecosystem. Today we are announcing that we’ve launched https://registry.modelcontextprotocol.io as the official MCP Registry. As part of the MCP project, the MCP Registry, as well as a parent OpenAPI specification, are open source—allowing everyone to build a compatible sub-registry.

Today, we’re launching the Model Context Protocol (MCP) Registry—an open catalog and API for publicly available MCP servers to improve discoverability and implementation. By standardizing how servers are distributed and discovered, we’re expanding their reach while making it easier for clients to get connected.

The MCP Registry is now available in preview. To get started:

Add your serverby following our guide onAdding Servers to the MCP Registry(for server maintainers)Access server databy following our guide onAccessing MCP Registry Data(for client maintainers)

- Add your serverby following our guide onAdding Servers to the MCP Registry(for server maintainers)

- Access server databy following our guide onAccessing MCP Registry Data(for client maintainers)


# Single source of truth for MCP servers#


In March 2025, we shared that we wanted to build a central registry for the MCP ecosystem. Today we are announcing that we’ve launchedhttps://registry.modelcontextprotocol.ioas the official MCP Registry. As part of the MCP project, the MCP Registry, as well as a parentOpenAPI specification, are open source—allowing everyone to build a compatible sub-registry.

Our goal is to standardize how servers are distributed and discovered, providing a primary source of truth that sub-registries can build upon. In turn, this will expand server reach and help clients find servers more easily across the MCP ecosystem.


## Public and private sub-registries#


In building a central registry, it was important to us not to take away from existing registries that the community and companies have built. The MCP Registry serves as a primary source of truth for publicly available MCP servers, and organizations can choose tocreate sub-registriesbased on custom criteria. For example:

Public subregistrieslike opinionated “MCP marketplaces” associated with each MCP client are free to augment and enhance data they ingest from the upstream MCP Registry. Every MCP end-user persona will have different needs, and it is up to the MCP client marketplaces to properly serve their end-users in opinionated ways.

Private subregistrieswill exist within enterprises that have strict privacy and security requirements, but the MCP Registry gives these enterprises a single upstream data source they can build upon. At a minimum, we aim to share API schemas with these private implementations so that associated SDKs and tooling can be shared across the ecosystem.

In both cases, the MCP Registry is the starting point – it’s the centralized location where MCP server maintainers publish and maintain their self-reported information for these downstream consumers to massage and deliver to their end-users.


## Community-driven mechanism for moderation#


The MCP Registry is an official MCP project maintained by the registry working group and permissively licensed. Community members can submit issues to flag servers that violate the MCPmoderation guidelines—such as those containing spam, malicious code, or impersonating legitimate services. Registry maintainers can then denylist these entries and retroactively remove them from public access.


# Getting started#


To get started:

Add your serverby following our guide onAdding Servers to the MCP Registry(for server maintainers)Access server databy following our guide onAccessing MCP Registry Data(for client maintainers)

- Add your serverby following our guide onAdding Servers to the MCP Registry(for server maintainers)

- Access server databy following our guide onAccessing MCP Registry Data(for client maintainers)

This preview of the MCP Registry is meant to help us improve the user experience before general availability and does not provide data durability guarantees or other warranties. We advise MCP adopters to watch development closely as breaking changes may occur before the registry is made generally available.

As we continue to develop the registry, we encourage feedback and contributions on themodelcontextprotocol/registry GitHub repository: Discussion, Issues, and Pull Requests are all welcome.


# Thanks to the MCP community#


The MCP Registry has been a collaborative effort from the beginning and we are incredibly grateful for the enthusiasm and support from the broader developer community.

In February 2025, it began as a grassroots project when MCP creatorsDavid Soria ParraandJustin Spahr-Summersasked thePulseMCPandGooseteams to help build a centralized community registry. Registry MaintainerTadas AntanaviciusfromPulseMCPspearheaded the initial effort in collaboration withAlex HancockfromBlock. They were soon joined by Registry MaintainerToby Padilla, Head of MCP atGitHub, and more recently,Adam JonesfromAnthropicjoined as Registry Maintainer to drive the project towards the launch today. Theinitial announcementof the MCP Registry’s development lists 16 contributing individuals from at least 9 different companies.

Many others made crucial contributions to bring this project to life:Radoslav DimitrovfromStacklok,Avinash SridharfromGitHub,Connor PeetfromVS Code,Joel VerhagenfromNuGet,Preeti DewanifromLast9,Avish PorwalfromMicrosoft,Jonathan Hefner, and many Anthropic and GitHub employees that provided code reviews and development support. We are also grateful to everyone on theRegistry’s contributors logand those who participated indiscussions and issues.

We deeply appreciate everyone investing in this foundational open source infrastructure. Together, we’re helping developers and organizations worldwide to build more reliable, context-aware AI applications. On behalf of the MCP community, thank you.

---

**Source:** http://blog.modelcontextprotocol.io/posts/2025-09-08-mcp-registry-preview/

*This is a mirror of the MCP blog for offline reading. All content is copyright the Model Context Protocol project.*