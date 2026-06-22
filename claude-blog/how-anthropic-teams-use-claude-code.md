# Wie Anthropic-Teams Claude Code verwenden
---
![](https://cdn.prod.website-files.com/68a44d4040f98a4adf2207b6/6903d223de65e7dcca8267d8_ea364001be6bf6d2e86b58109ead6a779d5771a7-1000x1000.svg)

# Wie Anthropic-Teams Claude Code verwenden

Teams bei Anthropic nutzen Claude Code für alles – von der Fehlersuche in der Produktion über die Navigation unbekannter Codebasen bis hin zur Erstellung benutzerdefinierter Automatisierungstools. So geht's.

- KategorieKI für Unternehmen

- ProduktClaude Code

- Datum24.7.2025

- Lesezeit5Min

- TeilenLink kopierenhttps://claude.com/blog/how-anthropic-teams-use-claude-code

Tools für agentisches Coding wie[Claude Code](https://www.anthropic.com/claude-code)helfen Entwicklern dabei, Workflows zu beschleunigen, sich wiederholende Aufgaben zu automatisieren und komplexe Programmierprojekte in Angriff zu nehmen. Da sich der Bereich weiterentwickelt, erfahren wir täglich etwas über neue Anwendungen durch die Nutzer, einschließlich unserer eigenen Mitarbeiter.

Um mehr Informationen darüber zu erhalten, haben wir uns mit Mitarbeitern in Anthropic unterhalten, um herauszufinden, wie sie Claude Code bei der Arbeit nutzen.

Während viele ihrer Anwendungsfälle vorhersehbar waren – Debugging, Navigation in Codebasen, Verwaltung von Workflows – haben uns andere überrascht. Anwälte haben Telefonstruktursysteme erstellt. Marketingexperten generierten in Sekundenschnelle Hunderte von Anzeigenvariationen. Datenwissenschaftler haben komplexe Visualisierungen ohne Kenntnisse von JavaScript erstellt.

Das Muster wurde klar: agentisches Coding dient nicht nur zur Beschleunigung der herkömmlichen Entwicklung. Die Grenze zwischen technischer und nichttechnischer Arbeit verschwimmt und jeder, der ein Problem beschreiben kann, wird zu jemandem, der eine Lösung erstellen kann.

Folgendes haben wir in Erfahrung gebracht.

### Navigation und Verständnis der Codebasis

Teams im gesamten Unternehmen nutzen Claude Code, um neuen und langjährigen Mitarbeitern den Einstieg in unsere Codebasen zu erleichtern.

Neue Data Scientists in unserem Infrastrukturteam speisen ihre gesamte Codebasis in Claude Code  ein, um schnell produktiv zu sein. Claude liest die[CLAUDE.md](http://claude.md)-Dateien der Codebasis, identifiziert relevante Dateien, erklärt Datenpipeline-Abhängigkeiten und zeigt, welche vorgelagerten Quellen in Dashboards eingespeist werden und ersetzen herkömmliche Datenkatalog-Tools.

Unser Produktentwicklungsteam nutzt Claude Code als erste Anlaufstelle für Programmieraufgaben. Sie bitten es, herauszufinden, welche Dateien auf Fehlerbehebungen, Funktionen oder Analysen untersucht werden sollen, wodurch der zeitaufwändige Prozess der manuellen Erfassung von Kontext vor der Erstellung neuer Funktionen entfällt.

### Testen und Codeüberprüfung

Tools für agentisches Coding sind besonders beliebt wegen ihrer Fähigkeit, zwei kritische, aber mühsame Programmieraufgaben zu automatisieren: das Schreiben von Unit-Tests und die Überprüfung von Code.

Das Produktdesign-Team verwendet Claude Code zum Schreiben umfassender Tests für neue Funktionen. Sie haben Pull-Request-Kommentare über GitHub-Aktionen automatisiert, wobei Claude Formatierungsprobleme und das Refactoring von Testfällen automatisch übernimmt.

Das Sicherheitstechnik-Team hat seinen Workflow von "Designdokument → Janky Code → refactor → aufgeben von Tests" umgewandelt und kann Claude um Pseudocode bitten, ihn durch die testgesteuerte Entwicklung führen und regelmäßig einchecken. Dadurch wird zuverlässiger, testbarer Code.

Agentisches Coding kann auch zur Übersetzung von Tests in andere Programmiersprachen verwendet werden. Wenn das Inferenz-Team beispielsweise Funktionen in unbekannten Sprachen wie Rust testen muss, erklärt es, was getestet werden soll, und Claude schreibt die Logik in der systemeigenen Sprache der Codebasis

### Debugging und Fehlerbehebung

Produktionsprobleme erfordern eine schnelle Lösung, aber der Versuch, unter Druck unbekannten Code zu analysieren, führt oft zu Verzögerungen. Für viele Teams im Unternehmen beschleunigt Claude Code die Diagnose und Korrekturen durch die Analyse von Stack-Traces, Dokumentation und Systemverhalten in Echtzeit.

Bei Vorfällen speist das Security Engineering-Team Claude Code Stack-Traces und Dokumentationen in den Kontrollfluss durch die Codebasis ein. Probleme, die normalerweise 10 bis 15 Minuten manuell scannen würden, werden jetzt 3-mal schneller gelöst.

Mit Claude Code gewann das Produktengineering-Team das Vertrauen, Fehler in unbekannten Codebasen zu beheben. Sie fragen Claude: „Können Sie diesen Fehler beheben? Dies ist das Verhalten, das ich sehe", und überprüfen Sie die vorgeschlagene Lösung, ohne dass andere Engineering-Teams um Unterstützung bitten müssen.

Als Kubernetes-Cluster die Planung von Pods stoppte, verwendete das Dateninfrastruktur-Team Claude Code zur Diagnose des Problems. Sie gaben Dashboard-Screenshots ein und Claude führte sie Menü für Menü durch die Benutzeroberfläche von Google Cloud, bis sie feststellten, dass die IP-Adressen nicht mehr verfügbar waren. Claude stellte dann die genauen Befehle bereit, um einen neuen IP-Pool zu erstellen und dem Cluster hinzuzufügen, was ihnen bei einem Systemausfall 20 Minuten wertvolle Zeit einspart.

### Prototyping und Funktionsentwicklung

Die Erstellung neuer Funktionen erfordert traditionell tiefgreifendes technisches Wissen und erhebliche Zeitinvestition. Claude Code ermöglicht die schnelle Prototypenerstellung und sogar die vollständige Anwendungsentwicklung, sodass Teams unabhängig von ihrem Programmierwissen Ideen schnell validieren können.

Mitglieder des Produktdesign-Teams würden Figma-Designdateien an Claude Code weiterleiten und dann autonome Schleifen einrichten, in denen Claude Code den Code für die neue Funktion schreibt, Tests ausführt und kontinuierlich iteriert. Sie stellen Claude abstrakte Probleme zu, lassen es autonom arbeiten und überprüfen dann die Lösungen, bevor sie endgültige Verfeinerungen vornehmen. In einem Fall ließ Claude Vim-Key-Bindungen mit minimaler Überprüfung durch Menschen selbst erstellen.

Mit Claude Code entdeckte das Produktdesign-Team eine unerwartete Nutzung: Zuordnung von Fehlerzuständen, Logikabläufen und Systemstatus zur Identifizierung von Randfällen während des Designs, anstatt sie während der Entwicklung zu entdecken. Dies verbessert die anfängliche Designqualität grundlegend und erspart später stundenlange Debugging.

Obwohl Data Scientists nicht fließend mit TypeScript sprechen, verwenden sie Claude Code zur Erstellung ganzer React-Anwendungen zur Visualisierung der RL-Modellleistung. Nach einmaliger Eingabe in einer Sandbox-Umgebung schreibt das Tool ganze TypeScript-Visualisierungen von Grund auf neu, ohne den Code selbst zu verstehen. Wenn die Aufgabe so einfach ist, nimmt der Mitarbeiter kleine Anpassungen vor und versucht es erneut, wenn der erste Prompt nicht ausreicht, wenn er die Aufgabe so einfach ist und es nicht ausreicht.

### Dokumentation und Wissensmanagement

Technische Dokumentationen sind oft verteilt auf Wikis, Codekommentare und Kopfzeilen der Teammitglieder. Claude Code konsolidiert dieses Wissen über MCP- und CLAUDE.md-Dateien in zugänglichen Formaten und stellt so jedem Fachmann zur Verfügung, der es benötigt.

Mitglieder von Inferenzteams ohne ML-Hintergrund verlassen sich auf Claude, um modellspezifische Funktionen zu erläutern. Was normalerweise eine Stunde dauert, dauert jetzt 10 bis 20 Minuten – eine 80 % weniger Forschungszeit.

Das Security Engineering-Team kann Claude mehrere Dokumentationsquellen einbeziehen, um Markdown-Runbooks und Fehlerbehebungshandbücher zu erstellen. Diese komprimierten Dokumente werden zum Kontext für das Debuggen echter Produktionsprobleme, was oft effizienter ist als das Durchsuchen vollständiger Wissensdatenbanken.

### Automatisierung und Workflow-Optimierung

Mit Tools für agentisches Coding können Teams benutzerdefinierte Automatisierungen erstellen, die normalerweise spezielle Entwicklerressourcen oder teure Software erfordern würden.

Das Growth Marketing-Team hat einen agentischen Workflow entwickelt, der CSV-Dateien mit Hunderten von Anzeigen verarbeitet, Performance-Unterschiede identifiziert und neue Variationen innerhalb einer strikten Zeichenbegrenzung generiert. Mithilfe von zwei speziellen Subagenten generiert das System Hunderte von neuen Anzeigen in Minuten statt Stunden.

Sie entwickelten außerdem ein Figma-Plugin, das Frames identifiziert und programmgesteuert bis zu 100 Anzeigenvariationen generiert, indem Überschriften und Beschreibungen getauscht werden. Dadurch wird der stundenlange Zeitaufwand für das Einfügen von Kopien auf eine halbe Sekunde pro Anzeigenstapel reduziert.

In einem besonders einzigartigen Anwendungsfall erstellte das Rechtsteam Prototypen von "Telefonbaumsystemen", um Teammitgliedern die Verbindung mit dem richtigen Anwalt in Anthropic zu erleichtern. Dabei wurde gezeigt, wie Abteilungen ohne herkömmliche Entwicklungsressourcen benutzerdefinierte Tools erstellen können.

### Neue Möglichkeiten mit Claude Code

Diese Berichte zeigen ein Muster: Claude Code funktioniert am besten, wenn Sie sich auf die Workflows konzentrieren, die es erweitern kann. Die erfolgreichsten Teams sehen Claude Code eher als Gedankenpartner als als als als Code-Generator.

Sie erkunden Möglichkeiten, erstellen schnell Prototypen und teilen ihre Erkenntnisse mit technischen und nichttechnischen Benutzern. Dieser Ansatz der Zusammenarbeit zwischen Mensch und KI eröffnet Möglichkeiten, die wir erst zu verstehen beginnen.

![](https://cdn.prod.website-files.com/6889473510b50328dbb70ae6/6889473610b50328dbb70b58_placeholder.svg)

![](https://cdn.prod.website-files.com/6889473510b50328dbb70ae6/6889473610b50328dbb70b58_placeholder.svg)

![](https://cdn.prod.website-files.com/6889473510b50328dbb70ae6/6889473610b50328dbb70b58_placeholder.svg)

Häufig gestellte Fragen

Erste Schritte mit Claude Code.

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
**Source:** https://claude.com/de/blog/how-anthropic-teams-use-claude-code
*This is a mirror of the Claude.com blog post for local access and AI-assisted development.*
