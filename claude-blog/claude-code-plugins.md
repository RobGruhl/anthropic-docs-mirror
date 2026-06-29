# Claude Code mit Plugins anpassen
---
![](https://cdn.prod.website-files.com/68a44d4040f98a4adf2207b6/6903d22d7d4c10df6024f7bc_ee580919acaba2ddc07425f7a7390c8962cadc94-1000x1000.svg)

# Claude Code mit Plugins anpassen

Claude Code unterstützt jetzt Plugins: benutzerdefinierte Sammlungen von Slash-Befehlen, Agenten, MCP-Servern und Hooks, die mit einem einzigen Befehl installiert werden können.

- KategorieProduktankündigungen

- ProduktClaude Code

- Datum9.10.2025

- Lesezeit5Min

- TeilenLink kopierenhttps://claude.com/blog/claude-code-plugins

### Claude Code-Setup mit Plugins freigeben

Slash-Befehle, Agenten, MCP-Server und Hooks sind Erweiterungspunkte, mit denen Sie Claude Code anpassen können. Während der Einführung haben wir gesehen, dass Benutzer immer leistungsfähigere Setups erstellen, die sie mit Teamkollegen und der breiteren Community teilen möchten. Wir haben Plugins entwickelt, um dies zu vereinfachen.

Plugins sind eine einfache Möglichkeit, eine beliebige Kombination aus folgenden Elementen zu paketieren und freizugeben:

- Slash-Befehle: Benutzerdefinierte Verknüpfungen für häufig verwendete Vorgänge erstellen

- Subagenten: Installation spezieller Agenten für spezielle Entwicklungsaufgaben

- MCP-Server: Verbindung zu Tools und Datenquellen über das Model Context Protocol

- Hooks: Anpassung des Verhaltens von Claude Code an wichtigen Punkten im Workflow

Sie können Plugins direkt in Claude Code mit dem Befehl/plugininstallieren, jetzt in der öffentlichen Betaversion. Sie können je nach Bedarf ein- und ausgeschaltet werden. Aktivieren Sie sie, wenn Sie bestimmte Funktionen benötigen, und deaktivieren Sie sie, wenn Sie sie nicht benötigen, um den Kontext und die Komplexität des Systemprompts zu reduzieren.

![Produkt-Screenshot mit dem Plugin-Menü von Claude Code](https://cdn.prod.website-files.com/68a44d4040f98a4adf2207b6/692f21bb6846b72134967ebe_68e95d95ecae26885bafdfde_81805a2d45f087f2cc153168759f8bf015706b04-1920x1035.png)

Künftig werden Plugins zur Standardmethode für die Zusammenstellung und gemeinsame Nutzung von Claude Code-Anpassungen gehören. Wir werden das Format mit weiteren Erweiterungspunkten weiterentwickeln.

### Anwendungsfälle

Plugins helfen Ihnen bei der Standardisierung von Claude Code-Umgebungen anhand gemeinsamer Best Practices. Häufige Plugin-Anwendungsfälle sind:

- Durchsetzung von Standards:Engineering-Führungskräfte können Team-weite Konsistenz gewährleisten, indem sie Plugins verwenden, um sicherzustellen, dass bestimmte Hooks für Codeüberprüfungen oder Test-Workflows ausgeführt werden

- Unterstützung für Benutzer: Open-Source-Betreuer können beispielsweise Slash-Befehle bereitstellen, die Entwicklern helfen, ihre Pakete korrekt zu verwenden

- Freigabe von Workflows:Entwickler, die produktivitätssteigernde Workflows erstellen – z. B. Debugging-Setups, Bereitstellungspipelines oder Testen von Harnesses – können diese problemlos für andere freigeben

- Verbindung von Tools:Teams, die interne Tools und Datenquellen über MCP-Server verbinden müssen, können Plugins mit denselben Sicherheits- und Konfigurationsprotokollen verwenden, um den Prozess zu beschleunigen

- Anpassungen bündeln:Framework-Autoren oder technische Leiter können mehrere Anpassungen zusammenstellen, die für bestimmte Anwendungsfälle zusammengestellt werden

### Plugin-Marktplätze

Um die gemeinsame Nutzung dieser Anpassungen zu erleichtern, kann jeder Plugins erstellen und hosten und Plugin-Marktplätze erstellen – kuratierte Sammlungen, in denen andere Entwickler Plugins entdecken und installieren können.

Sie können Plugin-Marktplätze nutzen, um Plugins für die Community freizugeben, genehmigte Plugins im gesamten Unternehmen zu verteilen und vorhandene Lösungen für häufige Entwicklungsherausforderungen zu nutzen.

Zum Hosten eines Marketplaces benötigen Sie lediglich ein Git-Repository, ein GitHub-Repository oder eine URL mit einer korrekt formatierten Datei.claude-plugin/marketplace.json. Weitere Informationen finden Sie in unserer Dokumentation.

Um Plugins von einem Marktplatz zu verwenden, führen Sie/plugin marketplace add user-or-org/repo-nameaus und suchen und installieren Sie Plugins über das Menü/plugin.

### Entdecken Sie neue Marktplätze

Plugin-Marktplätze erweitern die Best Practices, die unsere Community bereits entwickelt hat, und Community-Mitglieder ebnen den Weg. Der[Plugin-Marktplatz](https://www.aitmpl.com/plugins)von Ingenieur Dan Ávila beispielsweise bietet Plugins für die DevOps-Automatisierung, Dokumentationserstellung, Projektmanagement und Testsuites, während Ingenieur Seth Hobson in seinem[GitHub-Repository](https://github.com/wshobson/agents)über 80 spezialisierte Subagenten zusammengestellt hat, auf die Entwickler über Plugins sofortigen Zugriff haben.

Sie können auch einige[Beispiel-Plugins](https://github.com/anthropics/claude-code)ansehen, die wir für PR-Reviews, Sicherheitsleitfäden, die Entwicklung des[Claude Agent SDK](https://www.anthropic.com/engineering/building-agents-with-the-claude-agent-sdk)und sogar ein Meta-Plugin zur Erstellung neuer Plugins entwickelt haben.

### Erste Schritte

Plugins stehen jetzt für alle Claude-Code-Benutzer als öffentliche Betaversion zur Verfügung. Installieren Sie sie mit dem Befehl/plugin, und sie funktionieren in Ihrem Terminal und VS Code.

Lesen Sie unsere Dokumentation für[Erste Schritte](https://docs.claude.com/en/docs/claude-code/plugins-reference),[erstellen Sie eigene Plugins](https://docs.claude.com/en/docs/claude-code/plugins)oder[veröffentlichen Sie einen Marktplatz](https://docs.claude.com/en/docs/claude-code/plugin-marketplaces). Testen Sie diesen Multiagent-Workflow, den wir für die Entwicklung von Claude Code verwenden, um Plugins in Aktion zu sehen:

/plugin marketplace add anthropics/claude-code

```

```

```

```

![](https://cdn.prod.website-files.com/6889473510b50328dbb70ae6/6889473610b50328dbb70b58_placeholder.svg)

![](https://cdn.prod.website-files.com/6889473510b50328dbb70ae6/6889473610b50328dbb70b58_placeholder.svg)

![](https://cdn.prod.website-files.com/6889473510b50328dbb70ae6/6889473610b50328dbb70b58_placeholder.svg)

Häufig gestellte Fragen

## Ähnliche Beiträge

Weitere Produktneuheiten und Best Practices für Teams, die mit Claude arbeiten.

![](https://cdn.prod.website-files.com/68a44d4040f98a4adf2207b6/6903d2238ce207f9b2011d3f_e44a6b53398f189b9fd0d4f70516db614ac84db3-1000x1000.svg)

### Beobachtbarkeit für Entwickler, die Konnektoren entwickeln

![](https://cdn.prod.website-files.com/68a44d4040f98a4adf2207b6/6903d22d7d4c10df6024f7bc_ee580919acaba2ddc07425f7a7390c8962cadc94-1000x1000.svg)

### Steering Claude Code: CLAUDE.md files, skills, hooks, rules, subagents and more

![](https://cdn.prod.website-files.com/68a44d4040f98a4adf2207b6/6a025cf25f0694905405e054_Object-Scale.svg)

### Claude für die Rechtsbranche

![](https://cdn.prod.website-files.com/68a44d4040f98a4adf2207b6/6903d22e13864f88ea55c2d8_b5c98d26c46edc43193e7f7e28a00633a538bb9c-1000x1000.svg)

### Skills erklärt: Vergleich von Skills mit Prompts, Projekten, MCP und Subagenten

## Transformieren Sie mit Claude die Arbeitsweise Ihres Unternehmens

Entwickler-Newsletter abonnieren

Neues zu Produkten, Anleitungen, Community-Spotlights und mehr. Monatlich in Ihrem Posteingang.

Bitte geben Sie Ihre E-Mail-Adresse an, wenn Sie unseren monatlichen Entwickler-Newsletter erhalten möchten. Sie können sich jederzeit wieder abmelden.

---
**Source:** https://claude.com/de/blog/claude-code-plugins
*This is a mirror of the Claude.com blog post for local access and AI-assisted development.*
