# Skills erklärt: Vergleich von Skills mit Prompts, Projekten, MCP und Subagenten
---
![](https://cdn.prod.website-files.com/68a44d4040f98a4adf2207b6/6903d22e13864f88ea55c2d8_b5c98d26c46edc43193e7f7e28a00633a538bb9c-1000x1000.svg)

# Skills erklärt: Vergleich von Skills mit Prompts, Projekten, MCP und Subagenten

Skills sind ein immer leistungsfähigeres Tool zur Erstellung benutzerdefinierter KI-Workflows und Agenten, aber wo passen sie in den Claude-Stack? Wir erklären, welches Tool wann verwendet werden soll – und wie sie alle zusammenarbeiten.

- KategorieAgenten

- ProduktClaude AppsClaude Platform

- Datum5.3.2026

- Lesezeit5Min

- TeilenLink kopierenhttps://claude.com/blog/skills-explained

Seit der Einführung von[Skills](https://www.anthropic.com/news/skills)ist das Interesse daran gewachsen, wie die verschiedenen Komponenten des agentischen Ökosystems von Claude zusammenarbeiten.

Egal ob Sie anspruchsvolle Workflows in[Claude Code](https://www.claude.com/product/claude-code)entwickeln, Unternehmenslösungen mit der API erstellen oder Ihre Produktivität mit[Claude.ai](http://claude.ai)maximieren möchten – wenn Sie wissen, welches Tool Sie wann nutzen möchten, können Sie Ihre Arbeitsweise mit Claude verändern.

In diesem Leitfaden werden die einzelnen Bausteine dargestellt und erklärt, wann sie verwendet werden können, und es wird gezeigt, wie Sie sie für leistungsstarke agentische Workflows kombinieren.

## Ihre agentischen Bausteine verstehen

### Was sind Skills?

Skills sind Ordner mit Anweisungen, Skripten und Ressourcen, die Claude entdeckt und dynamisch lädt, wenn sie für eine Aufgabe relevant sind. Stellen Sie sich diese als spezielle Schulungshandbücher vor, in denen Claude Fachwissen in bestimmten Bereichen vermittelt wird – von der Arbeit mit Excel-Tabellen bis hin zur Einhaltung der Markenrichtlinien Ihres Unternehmens.

Funktionsweise von Skills:Wenn Claude auf eine Aufgabe stößt, durchsucht es verfügbare Skills nach relevanten Übereinstimmungen. Skills verwenden eine progressive Offenlegung: Metadaten werden zuerst geladen (~100 Tokens). Sie enthalten gerade genug Informationen, damit Claude weiß, wann ein Skill relevant ist. Vollständige Anweisungen werden bei Bedarf geladen (<5.000 Tokens), und gebündelte Dateien oder Skripte werden nur auf Anforderung geladen.

Wann Skills eingesetzt werden können:Wählen Sie Skills, wenn Claude zur konsistenten und effizienten Durchführung spezieller Aufgaben benötigt wird. Sie sind ideal für:

- Organisatorische Workflows: Markenrichtlinien, Compliance-Verfahren, Dokumentvorlagen

- Fachwissen:Excel-Formeln, PDF-Bearbeitung, Datenanalyse

- Persönliche Präferenzen:Notizsysteme, Programmiermuster, Forschungsmethoden

Beispiel:Erstellen Sie[einen Markenrichtlinien-Skill](https://github.com/anthropics/skills/tree/main/skills/brand-guidelines), der die Farbpalette, Typografieregeln und Layout-Spezifikationen Ihres Unternehmens enthält. Wenn Claude Präsentationen oder Dokumente erstellt, werden diese Standards automatisch angewendet, ohne dass Sie sie jedes Mal erklären müssen.

[Erfahren Sie mehr](https://support.claude.com/en/articles/12512176-what-are-skills)über Skills und sehen Sie sich[unsere wachsende Skills-Bibliothek](https://github.com/anthropics/skills)an.

### Was sind Prompts?

[Prompts](https://docs.claude.com/en/prompt-library/library)sind die Anweisungen, die Sie Claude während einer Unterhaltung in natürlicher Sprache geben. Sie sind kurzlebig, konversationsbasiert und reaktiv. Sie stellen Kontext und Richtung im Moment bereit.

Wann Prompts verwendet werden:Verwenden Sie Prompts für:

- Einmalige Anfragen: „Fasse diesen Artikel zusammen“

- Konversationsverfeinerung: „Gestalte den Tonfall professioneller“

- Direkter Kontext: „Analysiere diese Daten und identifiziere Trends

- Ad-hoc-Anweisungen: „Formatiere das als Aufzählung"

Beispiel:

Führe bitte eine umfassende Sicherheitsüberprüfung dieses Codes durch. Ich suche nach:

1. häufigen Schwachstellen, einschließlich:

- Injection-Fehler (SQL, Befehl, XSS usw.)

- Authentifizierungs- und Autorisierungsprobleme

- Vertrauliche Daten

- Sicherheitsfehlkonfigurationen

- Defekte Zugriffskontrolle

- Kryptografische Fehler

- Probleme mit der Eingabevalidierung

- Probleme mit der Fehlerbehandlung und Protokollierung

2. Gib für jedes gefundene Problem Folgendes an:

- Schweregrad (Kritisch/Hoch/Mittel/Niedrig)

- Position im Code (Zeilennummern oder Funktionsnamen)

- Erklärung, warum es ein Sicherheitsrisiko darstellt und wie es ausgenutzt werden könnte

- Spezifische Lösungsempfehlung nach Möglichkeit mit Codebeispielen

- Best Practices zur Vermeidung ähnlicher Probleme

3. Code-Kontext: [Beschreiben Sie die Aufgaben des Codes, die Sprache/das Framework und die Umgebung, in der es ausgeführt wird – z. B. „Dies ist eine Node.js-REST-API, die die Benutzerauthentifizierung übernimmt und Zahlungsdaten verarbeitet“]

4. Zusätzliche Überlegungen:

- Gibt es Schwachstellen in der OWASP-Liste der Top 10?

- Folgt der Code Best Practices für Sicherheit für [spezifisches Framework/Sprache]?

- Gibt es Abhängigkeiten mit bekannten Schwachstellen?

Priorisiere die Ergebnisse nach Schweregrad und potenziellen Auswirkungen.

Pro-Tipp:Prompts sind Ihre primäre Art der Interaktion mit Claude, aber die Unterhaltungen werden nicht gespeichert. Für sich wiederholende Workflows oder Fachwissen können Sie Prompts als Skills oder Projektanweisungen erfassen.

Wann stattdessen ein Skill verwendet wird:Wenn Sie wiederholt denselben Prompt in mehreren Unterhaltungen eingeben, ist es an der Zeit, einen Skill zu erstellen. Wandeln Sie wiederkehrende Anweisungen wie „Diesen Code mit OWASP-Standards auf Sicherheitsschwachstellen überprüfen“ oder „Diese Analyse mit Zusammenfassung, wichtigsten Ergebnissen und Empfehlungen formatieren“ in Skills um. So müssen Sie Prozeduren nicht jedes Mal neu erklären und können eine konsistente Ausführung sicherstellen.

Informieren Sie sich in unserer[Prompt-Bibliothek](https://docs.claude.com/en/prompt-library/library)mit[Best Practices](http://claude.com/blog/prompt-engineering-best-practices)oder[unserem intelligenten Prompt-Maker](https://claude.ai/public/artifacts/3796db7e-4ef1-4cab-b70c-d045778f23ec)über die ersten Schritte.

### Was sind Projekte?

[Projekte](https://support.claude.com/en/articles/9517075-what-are-projects)sind in allen kostenpflichtigen Claude-Plänen verfügbar und sind eigenständige Workspaces mit eigenem Chat-Verlauf und Wissensdatenbanken. Jedes Projekt enthält ein Kontextfenster mit 200.000 Ressourcen, in dem Sie Dokumente hochladen, Kontext angeben und benutzerdefinierte Anweisungen festlegen können, die für alle Unterhaltungen innerhalb dieses Projekts gelten.

Projekte funktionieren:Alles, was Sie in die Wissensdatenbank eines Projekts hochladen, ist in allen Chats innerhalb dieses Projekts verfügbar. Claude nutzt diesen Kontext automatisch, um fundiertere und relevantere Antworten bereitzustellen. Wenn Ihr Projektwissen sich den Kontextgrenzen nähert, aktiviert Claude nahtlos den Modus Retrieval Augmented Generation (RAG), um die Kapazität um das bis zu 10-Fache zu erweitern.

Wann Projekte verwendet werden:Wählen Sie Projekte, wenn Sie Folgendes benötigen:

- Beständiger Kontext:Hintergrundwissen, das jeder Unterhaltung zugute kommt

- Workspace-Organisation:Separate Kontexte für verschiedene Initiativen

- Teamzusammenarbeit:Gemeinsamer Wissensaustausch und Konversationsverlauf (bei Team- und Enterprise-Plänen)

- Benutzerdefinierte Anweisungen:Projektspezifischer Ton, Perspektive oder Ansatz

Beispiel:Erstellen Sie ein Projekt "Produkteinführung im 4. Quartal", das Marktforschung, Mitbewerberanalyse und Produktspezifikationen enthält. Jeder Chat in diesem Projekt hat Zugriff auf dieses Wissen, ohne dass Sie den Kontext erneut hochladen oder neu erklären müssen.

Wann Sie lieber ein Skill verwenden sollten:Durch Projekte erhält Claude einen spezifischen Kontext für eine bestimmte Arbeit – die Codebasis Ihres Unternehmens, eine Forschungsinitiative, ein laufendes Kundenprojekt. Skills bringen Claude bei, wie man etwas tut. In einem Projekt können alle Informationen zu Ihrer Produkteinführung enthalten sein, während ein Skill Claude die Schreibstandards oder den Codeüberprüfungsprozess Ihres Teams beibringen kann. Wenn Sie dieselben Anweisungen in mehrere Projekte kopieren, ist das ein Signal dafür, lieber einen Skill zu entwickeln.

[Erfahren Sie mehr](https://support.claude.com/en/articles/9517075-what-are-projects)über Projekte.

### Was sind Subagenten?

[Subagenten](https://docs.claude.com/en/docs/claude-code/sub-agents)sind spezielle KI-Assistenten mit eigenen Kontextfenstern, benutzerdefinierten Systemprompts und spezifischen Tool-Berechtigungen. In Claude Code und dem Claude Agenten SDK sind [Subagenten](https://docs.claude.com/en/docs/claude-code/sub-agents) verfügbar. Sie können gesonderte Aufgaben unabhängig voneinander verarbeiten und Ergebnisse an den Hauptagenten zurückgeben.

Funktionsweise von Subagenten:Jeder Subagent hat seine eigene Konfiguration. Sie definieren, was er tut, wie er Probleme löst und auf welche Tools er zugreifen kann. Claude delegiert Aufgaben automatisch basierend auf deren Beschreibungen an die entsprechenden Subagenten, oder Sie können explizit einen bestimmten Subagenten anfordern.

Wann Subagenten verwendet werden sollen:Subagenten verwenden Sie für:

- Aufgaben-Spezialisierung:Codeüberprüfung, Testerstellung, Sicherheitsaudits

- Kontextverwaltung:Konzentration auf das Hauptgespräch und spezialisierte Arbeiten auslagern

- Parallele Verarbeitung:Mehrere Subagenten können gleichzeitig an verschiedenen Aspekten arbeiten

- Tool-Einschränkung:Bestimmte Unteragenten auf sichere Vorgänge beschränken (z. B. schreibgeschützter Zugriff)

Beispiel:

```

```

Wann stattdessen ein Skill verwendet wird:Wenn mehrere Agenten oder Konversationen dasselbe Know-how benötigen – z. B. Verfahren zur Überprüfung der Sicherheit oder Datenanalysemethoden –, erstellen Sie einen Skill, anstatt dieses Wissen in einzelne Subagenten einzubetten. Skills sind übertragbar und wiederverwendbar, während Subagenten speziell für bestimmte Workflows entwickelt sind. Verwenden Sie Skills, um Fachwissen zu vermitteln, das jeder Agent nutzen kann. Verwenden Sie Subagenten, wenn Sie eine unabhängige Aufgabenausführung mit bestimmten Tool-Berechtigungen und Kontextisolierung benötigen.

[Mehr erfahren](https://code.claude.com/docs/en/sub-agents)über Subagenten.

### Was ist MCP?

![](https://cdn.prod.website-files.com/68a44d4040f98a4adf2207b6/69141f0993d68ff4c536f316_619a5262.png)

Das Model Context Protocol (MCP) ist ein offener Standard zur Verbindung von KI-Assistenten mit externen Systemen, in denen Daten gespeichert sind – Content-Repositorys, Geschäftstools, Datenbanken und Entwicklungsumgebungen.

Funktionsweise von MCP:MCP bietet eine standardisierte Möglichkeit, Claude mit Ihren Tools und Datenquellen zu verbinden. Anstatt für jede Datenquelle benutzerdefinierte Integrationen zu erstellen, können Sie ein einzelnes Protokoll als Basis verwenden und darauf aufbauen. MCP-Server stellen Daten und Funktionen bereit. MCP-Clients (wie Claude) stellen eine Verbindung zu diesen Servern her.

Wann MCP-Nutzung:Wählen Sie MCP, wenn Claude für folgende Zwecke benötigt wird:

- Zugriff auf externe Daten: Google Drive, Slack, GitHub, Datenbanken

- Geschäftstools nutzen: CRM-Systeme, Projektmanagementplattformen

- Verbindung zu Entwicklungsumgebungen: Lokale Dateien, IDEs, Versionskontrolle

- Integration in benutzerdefinierte Systeme: Ihre eigenen Tools und Datenquellen

Beispiel:Verknüpfung von Claude über MCP mit Google Drive Ihres Unternehmens. Claude kann jetzt Dokumente durchsuchen, Dateien lesen und auf interne Informationen verweisen, ohne manuelle Uploads - die Verbindung bleibt bestehen und wird automatisch aktualisiert.

Wann stattdessen ein Skill verwendet wird:MCP verbindet Claude mit Daten; Skills bringen Claude bei, was mit diesen Daten getan werden soll. Wenn Sie erklären möchten,wieein Tool verwendet wird oder Verfahren befolgt wird – z. B. „Bei Abfragen unserer Datenbank immer zuerst nach Datumsbereich filtern“ oder „Excel-Berichte mit diesen spezifischen Formeln formatieren“ – ist dies ein Skill. Wenn Sie Claude für denZugriffauf die Datenbank oder Excel-Dateien benötigen, ist dies MCP. Nutzen Sie beides gemeinsam: MCP für Konnektivität, Skills für Verfahrenswissen.

[Erfahren Sie mehr](https://www.anthropic.com/news/model-context-protocol)über MCP und lesen Sie die[Dokumentation](https://modelcontextprotocol.io/docs/develop/build-server)zur Erstellung eines MCP-Servers.

## Wie sie zusammenarbeiten

Die wahre Leistung entsteht, wenn Sie diese Bausteine kombinieren. Jedes Produkt erfüllt einen anderen Zweck und erstellt gemeinsam anspruchsvolle agentische Workflows.

### Vergleich: Auswahl des richtigen Tools

### Beispiel für einen agentischen Workflow: Recherchieragent

Wir möchten einen umfassenden Recherchieragent erstellen, der mehrere Bausteine kombiniert. Dieses Beispiel zeigt, wie ein Agent für die Wettbewerbsanalyse zusammengestellt und aktiviert wird.

Schritt 1: Projekt einrichten

Erstellen Sie ein Projekt "Competitive Intelligence" und laden Sie es hoch:

- Branchenberichte und Marktanalysen

- Produktdokumentation von Mitbewerbern

- Kundenfeedback aus Ihrem CRM

- Zusammenfassungen früherer Forschungen

Fügen Sie Projektanweisungen hinzu:

Analysiere die Konkurrenz im Rahmen unserer Produktstrategie. Konzentriere dich auf Differenzierungsmöglichkeiten und neue Markttrends. Präsentiere die Ergebnisse mit spezifischen Nachweisen und umsetzbaren Empfehlungen.

Schritt 2: Verknüpfung von Datenquellen über MCP

Aktivieren Sie einen MCP-Server für:

- Google Drive (für den Zugriff auf gemeinsame Forschungsdokumente)

- GitHub (zur Überprüfung von Open-Source-Repositorys von Mitbewerbern)

- Websuche (für Marktinformationen in Echtzeit)

Schritt 3: Spezielle Skills erstellen

Erstellen Sie einen Skill für die Wettbewerbsanalyse:

```

```

Schritt 4: Konfigurieren von Subagenten (nur Claude Code/SDK)

Erstellen Sie spezialisierte Subagenten:

market-researchersubagent:

```

```

technical-analystsubagent:

```

```

Schritt 5: Recherchieragenten aktivieren

Jetzt fragen Sie Claude: „Analysiere, wie unsere drei wichtigsten Konkurrenten ihre neuen KI-Funktionen einsetzen, und identifiziere Lücken, die wir nutzen können.“

Jetzt passiert Folgendes:

- Projektkontext wird geladen: Claude greift auf Ihre hochgeladenen Recherchedokumente zu und folgt den Projektanweisungen

- MCP-Verbindungen aktivieren: Claude durchsucht Google Drive nach aktuellen Mitbewerberbeschreibungen und ruft GitHub-Daten ab

- Skills aktivieren: Der Skill zur Wettbewerbsanalyse stellt den analytischen Rahmen bereit

- Subagenten ausführen(in Claude Code): Der Marktforscher sammelt Branchendaten, während der technische Analyst technische Implementierungen überprüft

- Prompts verfeinern: Sie stellen Anleitungen zur Verfügung: „Konzentriere dich insbesondere auf Unternehmenskunden im Gesundheitswesen“

Das Ergebnis:Eine umfassende Wettbewerbsanalyse, die aus mehreren Datenquellen stammt, Ihrem analytischen Framework folgt, spezialisiertes Know-how nutzt und während Ihres gesamten Rechercheprojekts Kontext beibehält.

## Häufige Fragen

#### Wie funktionieren Skills?

Skills nutzen die[progressive Offenlegung](https://www.anthropic.com/engineering/equipping-agents-for-the-real-world-with-agent-skills), um Claude effizient zu halten. Bei der Arbeit an Aufgaben durchsucht Claude zunächst Skill-Metadaten (Beschreibungen und Zusammenfassungen), um relevante Übereinstimmungen zu identifizieren. Wenn ein Skill übereinstimmt, lädt Claude die vollständigen Anweisungen. Wenn der Skill ausführbaren Code- oder Referenzdateien enthält, werden diese nur bei Bedarf geladen.

Diese Architektur bedeutet, dass Sie viele Skills zur Verfügung haben können, ohne das Kontextfenster von Claude zu überfordern. Claude greift genau dann auf die Daten zu, wenn sie benötigt werden.

#### Skills vs. Subagenten: Wann was verwendet werden sollte

Verwenden Sie Skills, wenn:Sie Funktionen möchten, die jede Claude-Instanz laden und verwenden kann. Skills sind wie Schulungsmaterialien: Sie helfen Claude dabei, bestimmte Aufgaben in allen Konversationen besser zu bewältigen.

Verwenden Sie Subagenten, wenn:Sie vollständige, eigenständige Agenten benötigen , die für bestimmte Zwecke entwickelt wurden und Workflows unabhängig voneinander verarbeiten. Subagenten sind wie spezialisierte Mitarbeiter mit eigenem Kontext und Tool-Berechtigungen.

Nutzen Sie sie gemeinsam, wenn:Sie Subagenten mit speziellem Know-how benötigen. Ein Subagent zur Codeüberprüfung kann beispielsweise Skills für sprachspezifische Best Practices nutzen und dabei die Unabhängigkeit eines Subagenten mit dem übertragbaren Know-how von Skills kombinieren.

#### Skills vs. Prompts: wann Sie was verwenden

Verwenden Sie Prompts wenn:Sie Anweisungen einmalig eingeben, einen unmittelbaren Kontext bereitstellen oder eine Konversation führen. Prompts sind reaktiv und kurzlebig.

Verwenden Sie Skills, wenn:Sie Verfahren oder Fachwissen haben, die Sie wiederholt benötigen. Skills sind proaktiv – Claude weiß, wann sie angewendet werden sollen – und werden über Unterhaltungen hinweg beibehalten.

Verwenden Sie sie gemeinsam:Prompts und Skills ergänzen sich auf natürliche Weise. Verwenden Sie Skills, um grundlegendes Know-how bereitzustellen, und geben Sie dann Prompts für jede Aufgabe spezifischen Kontext und Feinabstimmung an.

#### Skills vs. Projekte: wann Sie was verwenden

Verwenden Sie Projekte, wenn:Sie Hintergrundwissen und Kontext benötigen, der in alle Gespräche über eine bestimmte Initiative einfließen sollte. Projekte stellen statisches Referenzmaterial bereit, das immer geladen wird.

Verwenden Sie Skills, wenn:Sie prozedurales Wissen und ausführbaren Code benötigen, der nur bei Bedarf aktiviert wird. Skills bieten dynamisches Know-how, das nach Bedarf geladen wird und in Ihrem Kontextfenster gespeichert wird.

Nutzen Sie sie gemeinsam, wenn:Sie sowohl konsistenten Kontext als auch spezielle Funktionen benötigen. Beispiel: Ein Projekt zur Produktentwicklung mit Produktspezifikationen und Benutzerrecherchen in Kombination mit Skills zur Erstellung technischer Dokumentation und Analyse von Benutzerfeedbackdaten.

Hauptunterschied:Projekte sagen: „Hier ist alles,was man wissen muss." Skills sagen: „So macht man das.“ Projekte stellen eine Wissensdatenbank bereit, in der Sie arbeiten. Skills bieten Funktionen, die überall eingesetzt werden können – in jeder Unterhaltung, in jedem Projekt.

#### Können Subagenten Skills verwenden?

Ja. In Claude Code und dem Agenten-SDK können Unteragenten genau wie der Hauptagent auf Skills zugreifen und diese verwenden. Dadurch entstehen leistungsstarke Kombinationen, in denen spezialisierte Subagenten portables Know-how nutzen.

Beispielsweise kann Ihr Python-Entwickler-Subagent den Pandas-Analyse-Skill verwenden, um Datentransformationen gemäß den Konventionen Ihres Teams durchzuführen, während Ihr Dokumentations-Writer den Skill für technisches Schreiben verwendet, um die API-Dokumentation konsistent zu formatieren.

## Erste Schritte

Möchten Sie Skills erstellen? So klappt der Einstieg:

[Claude.ai](https://Claude.ai)-Benutzer:

- Skills in Einstellungen → Funktionen aktivieren

- Erstellen Sie Ihr erstes Projekt unter claude.ai/projects

- Kombinieren Sie Projektwissen mit Skills für Ihre nächste Analyseaufgabe

API-Entwickler:

- Entdecken Sie den Skills-Endpunkt in derDokumentation

- Lesen Sie unserenSkills-Leitfaden

Claude Code-Benutzer:

- Installation von Skills überPlugin-Marktplätze

- Lesen Sie unserenSkills-Leitfaden

## Agentische Skills

Nutzen Sie Skills mit Claude, um noch heute leistungsstärkere Anwendungen zu entwickeln.

![](https://cdn.prod.website-files.com/6889473510b50328dbb70ae6/6889473610b50328dbb70b58_placeholder.svg)

![](https://cdn.prod.website-files.com/68a44d4040f98a4adf2207b6/6915038fea2f5466c171c21f_Hand-NodeWeb.svg)

![](https://cdn.prod.website-files.com/68a44d4040f98a4adf2207b6/691503928e574d7dc8407b4a_Hand-NodeWeb-1.svg)

Häufig gestellte Fragen

## Ähnliche Beiträge

Weitere Produktneuheiten und Best Practices für Teams, die mit Claude arbeiten.

![](https://cdn.prod.website-files.com/68a44d4040f98a4adf2207b6/6903d2238ce207f9b2011d3f_e44a6b53398f189b9fd0d4f70516db614ac84db3-1000x1000.svg)

### Observability for developers building connectors

![](https://cdn.prod.website-files.com/68a44d4040f98a4adf2207b6/6a025cf25f0694905405e054_Object-Scale.svg)

### Claude für die Rechtsbranche

![](https://cdn.prod.website-files.com/68a44d4040f98a4adf2207b6/6903d22cf0b73a86025c5ba9_2174acb37a84767550abfe2588eb5648f941a897-1000x1000.svg)

### Das kann der Max Plan

![](https://cdn.prod.website-files.com/68a44d4040f98a4adf2207b6/6903d22d0099a66d72e05699_33ddc751e21fb4b116b3f57dd553f0bc55ea09d1-1000x1000.svg)

### Wir testen Claude in Chrome

## Transformieren Sie mit Claude die Arbeitsweise Ihres Unternehmens

Entwickler-Newsletter abonnieren

Neues zu Produkten, Anleitungen, Community-Spotlights und mehr. Monatlich in Ihrem Posteingang.

Bitte geben Sie Ihre E-Mail-Adresse an, wenn Sie unseren monatlichen Entwickler-Newsletter erhalten möchten. Sie können sich jederzeit wieder abmelden.

---
**Source:** https://claude.com/de/blog/skills-explained
*This is a mirror of the Claude.com blog post for local access and AI-assisted development.*
