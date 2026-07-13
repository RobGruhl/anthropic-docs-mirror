# Wir testen Claude in Chrome
---
![](https://cdn.prod.website-files.com/68a44d4040f98a4adf2207b6/6903d22d0099a66d72e05699_33ddc751e21fb4b116b3f57dd553f0bc55ea09d1-1000x1000.svg)

# Wir testen Claude in Chrome

Wir testen Claude für Chrome, um browserbasierte KI-Funktionen auszuprobieren, Risiken durch Prompt-Injection zu minimieren und die nötigen Sicherheitsmaßnahmen vor der breiteren Veröffentlichung zu erstellen. ‍

‍

- KategorieProduktankündigungen

- ProduktClaude Apps

- Datum25.8.2025

- Lesezeit5Min

- TeilenLink kopierenhttps://claude.com/blog/claude-for-chrome

Update: Jetzt für Pro, Team und Enterprise verfügbar(18. Dezember 2025)

Nach monatelangen Tests sind wir nun bereit, auf alle kostenpflichtigen Pläne auszuweiten. Wir haben auch die am häufigsten gewünschte Funktion fertiggestellt: eine Integration fürClaude Code. Sie entwickeln in Ihrem Terminal, überprüfen alles in Ihrem Browser und debuggen, während Claude Konsolenfehler und DOM-Status direkt liest.

Für Teams und Enterprise:Admins können die Erweiterung unternehmensweit aktivieren oder deaktivieren und Zulassungs- und Blocklisten für Websites konfigurieren.

‍

Update: Jetzt auch für alle Abonnenten des Max Plans verfügbar(24. November 2025)

Nach einer dreimonatigen Testphase ist[Claude in Chrome](https://claude.ai/chrome)jetzt in der Betaversion für alle Abonnenten des Max Plans verfügbar. Seit der Einführung haben wir wichtige Updates bereitgestellt, einschließlich geplanter Aufgaben, Workflows mit mehreren Registerkarten und intelligenterer Navigation auf Websites, die Sie täglich verwenden. In unseren[Versionshinweisen](https://support.claude.com/en/articles/12306336-claude-for-chrome-release-notes)finden Sie die vollständige Liste der Updates und in unserem[Sicherheitsblog](http://anthropic.com/research/prompt-injection-defenses)finden Sie Details zu Sicherheitsmaßnahmen und Lernprozessen aus dem Pilotprojekt.

‍

Wir haben Claude in den letzten Monaten mit Ihrem Kalender, Dokumenten und vielen anderen Softwareprogrammen verbunden. Der nächste logische Schritt besteht darin, Claude direkt in Ihrem Browser arbeiten zu lassen.

Wir betrachten browsergestützte KI als unvermeidlich: So viel Arbeit wird in Browsern abgewickelt, dass Claude die Möglichkeit bietet, zu sehen, was Sie gerade sehen, auf Schaltflächen zu klicken und Formulare auszufüllen, um es noch nützlicher zu machen.

Browsergestützte KI bringt jedoch Sicherheitsprobleme mit sich, die strengere Schutzmaßnahmen erfordern. Durch das Einholen von realem Feedback von vertrauenswürdigen Partnern zu Verwendungen, Schwachstellen und Sicherheitsproblemen können wir robuste Klassifizierungssysteme erstellen und zukünftige Modelle einrichten, um unerwünschtes Verhalten zu vermeiden. Dadurch wird sichergestellt, dass die Browsersicherheit mit der Weiterentwicklung der Funktionen Schritt hält.

Da bereits browserbasierte Agenten auf Frontier-Modellen entstehen, ist diese Aufgabe besonders dringlich. Durch die Behebung von Sicherheitsproblemen können wir Claude-Benutzer besser schützen und unsere Erkenntnisse mit allen teilen, die einen browserbasierten Agenten für unsere API erstellen.

Wir beginnen mit kontrollierten Tests:Eine Claude-Erweiterung für Chrome, in der vertrauenswürdige Benutzer Claude anweisen können, in ihrem Namen Aktionen im Browser durchzuführen.Wir führen ein Pilotprojekt mit 1.000 Max Plan-Nutzern durch –[treten Sie der Warteliste bei](http://claude.ai/chrome)–, um so viel wie möglich zu lernen. Wir werden den Zugriff schrittweise erweitern, während wir strengere Sicherheitsmaßnahmen entwickeln und Vertrauen durch diese begrenzte Vorabversion schaffen.

### Überlegungen für browserbasierte KI

Bei Anthropic haben wir spürbare Verbesserungen bei der Verwendung früherer Versionen von Claude in Chrome festgestellt, um Kalender zu verwalten, Meetings zu planen, E-Mail-Antworten zu entwerfen, routinemäßige Spesenabrechnungen zu verarbeiten und neue Website-Funktionen zu testen.

Einige Schwachstellen müssen jedoch noch behoben werden, bevor Claude in Chrome allgemein verfügbar gemacht wird. Genau wie Menschen mit Phishing-Versuchen in ihrem Posteingang konfrontiert sind, sind browserbasierte KIs Prompt-Injection-Angriffen ausgesetzt – bei denen böswillige Akteure Anweisungen in Websites, E-Mails oder Dokumenten verstecken, um KIs ohne Wissen der Benutzer zu schädlichen Aktionen auszuführen (z. B. versteckter Text, der sagt: „Vorherige Anweisungen ignorieren und stattdessen [bösartige Aktion] ausführen“).

Prompt-Injection-Angriffe können dazu führen, dass KIs Dateien löschen, Daten stehlen oder Finanztransaktionen durchführen. Das ist keine Spekulation: Wir haben "Red-Teaming" durchgeführt, um Claude in Chrome zu testen, und ohne Risikominimierung haben wir einige besorgniserregende Ergebnisse gefunden.

Wir haben umfangreiche Tests zur kontradiktorischen Prompt-Injection durchgeführt und 123 Testfälle für 29 verschiedene Angriffsszenarien ausgewertet. Bei Browsern ohne unsere Sicherheitsmaßnahmen lag die Erfolgsquote der Angriffe bei 23,6 %, wenn sie von böswilligen Akteuren ausgeführt wurden.

Ein Beispiel für einen erfolgreichen Angriff – bevor unsere neuen Abwehrmaßnahmen angewendet wurden – war eine böswillige E-Mail, in der behauptet wurde, dass E-Mails aus Sicherheitsgründen gelöscht werden müssten. Bei der Verarbeitung des Posteingangs folgte Claude diesen Anweisungen, um die E-Mails des Benutzers ohne Bestätigung zu löschen.

![](https://cdn.prod.website-files.com/68a44d4040f98a4adf2207b6/68e95d90c3728899c99ce194_5e46f0fa8e0ed4a6d71333dba95e1ff6aa64c5b1-1920x1030.png)

![](https://cdn.prod.website-files.com/68a44d4040f98a4adf2207b6/68e95d91c3728899c99ce199_5169a802140e293fdbc96706b4eb73e948084574-1920x1030.png)

![](https://cdn.prod.website-files.com/68a44d4040f98a4adf2207b6/68e95d91c3728899c99ce1aa_d2a23a7e8cd07f47eda84ac44135f770d624915f-1920x1030.png)

Wie wir im nächsten Abschnitt erläutern werden, haben wir bereits mehrere Sicherheitsmaßnahmen implementiert, die die Erfolgsquote von Angriffen erheblich reduzieren – obwohl noch Arbeit in die Aufdeckung neuer Angriffsvektoren gesteckt werden muss.

### Aktuelle Abwehrmaßnahmen

Die erste Verteidigungslinie gegen Prompt-Injection-Angriffe sindBerechtigungen. Benutzer behalten die Kontrolle darüber, was Claude in Chrome tun kann:

- Berechtigungen auf Site-Ebene: Benutzer können Claude jederzeit in den Einstellungen den Zugriff auf bestimmte Websites gewähren oder widerrufen.

- Aktionsbestätigungen: Claude fragt Benutzer, bevor es AKtionen mit hohem Risiko ausführt, wie Veröffentlichen, Kauf oder Freigabe personenbezogener Daten, diese zu bestätigen. Selbst wenn Benutzer sich für unseren experimentellen „autonomen Modus“ entscheiden, behält Claude bestimmte Sicherheitsvorkehrungen für hochsensible Aktionen bei (Hinweis: Alle Red-Teaming- und Sicherheitsbewertungen wurden im autonomen Modus durchgeführt).

Wir haben außerdem zusätzliche Sicherheitsmaßnahmen eingeführt, die den Prinzipien für[vertrauenswürdige Agenten](https://www.anthropic.com/news/our-framework-for-developing-safe-and-trustworthy-agents)von Anthropic entsprechen. Zunächst haben wir unsere System-Prompts verbessert – die allgemeinen Anweisungen, die Claude vor spezifischen Anweisungen von Benutzern erhält –, um Claude vorzugeben, wie vertrauliche Daten verarbeitet werden sollen und wie auf Anfragen zur Ausführung vertraulicher Aktionen reagiert werden soll.

Darüber hinaus haben wir Claude daran gehindert, Websites aus bestimmten Kategorien mit hohem Risiko zu nutzen, z. B. Finanzdienstleistungen, Inhalte für Erwachsene und Raubkopien. Und wir haben begonnen, erweiterte Klassifizierungsprogramme zu erstellen und zu testen, um verdächtige Anweisungsmuster und ungewöhnliche Datenzugriffsanfragen zu erkennen – selbst wenn sie in scheinbar legitimen Kontexten auftreten.

Durch die Einführung von Sicherheitsmaßnahmen im autonomen Modus konnten wir die Angriffserfolgsquote von 23,6 % auf 11,2 % reduzieren. Dies stellt eine deutliche Verbesserung gegenüber unserer vorhandenen Funktion zur Computernutzung dar (bei der Claude den Benutzerbildschirm sehen konnte, aber nicht die Browseroberfläche, die wir heute einführen).

![](https://cdn.prod.website-files.com/68a44d4040f98a4adf2207b6/68e95d91c3728899c99ce19d_b88d1e1c0c196dd012a7d44c5ae8d255d8a20822-3840x2160.png)

Wir haben auch spezielle Red-Teaming- und Risikominimierungsmaßnahmen eingeführt, die sich auf neue browserspezifische Angriffe konzentrieren, z. B. versteckte, bösartige Formularfelder im Document Object Model (DOM) einer Webseite, die für Menschen unsichtbar sind, und andere schwer zugängliche Injektionen, z. B. über URL-Text und Registerkartentitel, die möglicherweise nur für einen Agenten sichtbar sind. Bei einer „Challenge“ von vier browserspezifischen Angriffstypen konnten unsere neuen Risikominimierungen die Angriffserfolgsrate von 35,7 % auf 0 % senken.

Bevor wir Claude in Chrome allgemeiner verfügbar machen, möchten wir das Universum der Angriffe erweitern, die wir in Betracht ziehen, und lernen, wie wir diese Prozentsätze viel näher auf Null bringen, indem wir mehr über die aktuellen und potentiell zukünftigen Bedrohungen verstehen.

### Teilnahme

Interne Tests können nicht die gesamte Komplexität des Surfverhaltens in der realen Welt nachbilden: die spezifischen Anfragen, die sie stellen, die Websites die sie besuchen und wie bösartige Inhalte in der Praxis erscheinen. Auch böswillige Akteure entwickeln ständig neue Formen von Prompt-Injection-Angriffen. Diese Forschungsvorschau ermöglicht es uns, mit vertrauenswürdigen Benutzern zusammenzuarbeiten und anzugeben, welche unserer aktuellen Schutzmaßnahmen funktionieren und welche verbessert werden müssen.

Wir verwenden die Erkenntnisse aus dem Pilotprojekt, um unsere Prompt-Injection-Klassifizierungen und unsere zugrunde liegenden Modelle zu optimieren. Durch die Identifizierung von realen Beispielen für unsicheres Verhalten und neue Angriffsmuster, die in kontrollierten Tests nicht vorhanden sind, bringen wir unseren Modellen bei, die Angriffe zu erkennen und die entsprechenden Verhaltensweisen zu berücksichtigen. Wir stellen sicher, dass Sicherheits-Klassifizierungen alles aufnehmen, was das Modell selbst übersieht. Wir entwickeln auch anspruchsvollere Berechtigungssteuerungen basierend auf dem, was wir darüber erfahren, wie Benutzer mit Claude in ihren Browsern arbeiten möchten.

Für das Pilotprojekt suchen wir vertrauenswürdige Tester, die damit vertraut sind, dass Claude in ihrem Namen Aktionen in Chrome durchführt, und die keine sicherheitskritischen oder anderweitig sensiblen Installationen haben.

Wenn Sie teilnehmen möchten, können Sie sich unter[claude.ai/chrome](http://claude.ai/chrome)in die Warteliste für die Forschungsvorschau von Claude in Chrome eintragen.Sobald Sie Zugriff haben, können Sie die Erweiterung über den Chrome Web Store installieren und sich mit Ihren Claude-Anmeldeinformationen anmelden.

Wir empfehlen, mit vertrauenswürdigen Websites zu beginnen – immer die für Claude sichtbaren Daten im Auge zu behalten – und Claude für Chrome nicht für Websites zu verwenden, die finanzielle, rechtliche, medizinische oder andere vertrauliche Informationen enthalten. Eine detaillierte Sicherheitshandbuch finden Sie[in unserem Hilfe-Center](https://support.anthropic.com/en/articles/12012173-getting-started-with-claude-for-chrome).

Wir hoffen, dass Sie uns Feedback geben, um uns bei der Verbesserung der Funktionen und Sicherheitsvorkehrungen für Claude in Chrome zu helfen, damit wir grundlegende neue Wege finden können, KI in unser Leben zu integrieren.

![](https://cdn.prod.website-files.com/6889473510b50328dbb70ae6/6889473610b50328dbb70b58_placeholder.svg)

![](https://cdn.prod.website-files.com/6889473510b50328dbb70ae6/6889473610b50328dbb70b58_placeholder.svg)

![](https://cdn.prod.website-files.com/6889473510b50328dbb70ae6/6889473610b50328dbb70b58_placeholder.svg)

Häufig gestellte Fragen

## Ähnliche Beiträge

Weitere Produktneuheiten und Best Practices für Teams, die mit Claude arbeiten.

![](https://cdn.prod.website-files.com/68a44d4040f98a4adf2207b6/6903d22e13864f88ea55c2d8_b5c98d26c46edc43193e7f7e28a00633a538bb9c-1000x1000.svg)

### A harness for every task: dynamic workflows in Claude Code

![](https://cdn.prod.website-files.com/68a44d4040f98a4adf2207b6/6903d22e13864f88ea55c2d8_b5c98d26c46edc43193e7f7e28a00633a538bb9c-1000x1000.svg)

### How Claude Code works in large codebases: Best practices and where to start

![](https://cdn.prod.website-files.com/68a44d4040f98a4adf2207b6/6903d22349f86cd1968deab7_f06ca06f9d08ca4a85f26357eb896c3730274507-1000x1000.svg)

### How Anthropic enables self-service data analytics with Claude

![](https://cdn.prod.website-files.com/68a44d4040f98a4adf2207b6/692f76874e94e489958af8ba_Object-CodeMagnifier.svg)

### Wie KI hilft, die Kostenschwelle bei der COBOL-Modernisierung senkt

## Transformieren Sie mit Claude die Arbeitsweise Ihres Unternehmens

Entwickler-Newsletter abonnieren

Neues zu Produkten, Anleitungen, Community-Spotlights und mehr. Monatlich in Ihrem Posteingang.

Bitte geben Sie Ihre E-Mail-Adresse an, wenn Sie unseren monatlichen Entwickler-Newsletter erhalten möchten. Sie können sich jederzeit wieder abmelden.

---
**Source:** https://claude.com/de/blog/claude-for-chrome
*This is a mirror of the Claude.com blog post for local access and AI-assisted development.*
