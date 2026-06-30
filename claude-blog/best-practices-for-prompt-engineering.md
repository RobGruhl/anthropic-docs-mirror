# Best Practices für Prompt-Engineering
---
![](https://cdn.prod.website-files.com/68a44d4040f98a4adf2207b6/6909386cc7ad3ed2a7ec8eed_Object-ThoughtBubble.svg)

# Best Practices für Prompt-Engineering

Mit den Prompt-Engineering-Techniken des Teams von Claude erzielen Sie noch bessere KI-Ergebnisse.

- KategorieAgenten

- ProduktClaude Apps

- Datum10.11.2025

- Lesezeit5Min

- TeilenLink kopierenhttps://claude.com/blog/best-practices-for-prompt-engineering

[Kontext-Engineering](https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents)hat sich als immer wichtigerer Bestandteil von LLMs herausgestellt, wobei das Prompt-Engineering ein wesentlicher Baustein ist.

[Prompt-Engineering](https://docs.claude.com/en/docs/build-with-claude/prompt-engineering/claude-4-best-practices)ist die Strukturierung von Anweisungen, um bessere Ergebnisse aus den KI-Modellen zu erhalten. Es beschäftigt sich damit, wie man Abfragen formuliert, einen Stil spezifiziert, den Kontext bereitstellt und das Verhalten des Modells steuert, um seine Ziele zu erreichen.

Der Unterschied zwischen einer vagen Anweisung und einem gut erstellten Prompt kann darüber bestimmen, ob Sie generische Ergebnisse oder genau das erhalten, was Sie brauchen. Ein schlecht strukturierter Prompt erfordert möglicherweise mehrere Anläufe, um die Absicht zu klären, während ein gut formulierter Prompt beim ersten Mal das gewünschte Ergebnis erzielt.

Um Ihnen den Start zu erleichtern, haben wir einige Best Practices unseres Teams zusammengestellt, einschließlich praktischer Methoden, die Ihre Ergebnisse sofort verbessern können. Wir beginnen mit einfachen Gewohnheiten, die Sie direkt anwenden und später auf erweiterte Methoden für komplexe Projekte ausweiten können.

## So wenden Sie Prompt-Engineering an

Prompt-Engineering modifiziert quasi die Abfrage an Ihr LLM. Oft geht es darum, Informationen zur Abfrage hinzuzufügen, bevor Sie Ihre eigentliche Abfrage stellen. Aber zu wissen,welcheInformationen dierichtigensind, ist das Geheimnis für die Entwicklung eines großartigen und effektiven Prompts.

### Kerntechniken

Diese Prompt-Engineering-Techniken bilden die Grundlage für effektive KI-Interaktionen. Verwenden Sie sie konsequent, um sofortige Verbesserungen in der Antwortqualität zu erzielen.

#### Drücken Sie sich klar und deutlich aus

Moderne KI-Modelle reagieren außergewöhnlich gut auf klare, explizite Anweisungen. Gehen Sie nicht davon aus, dass das Modell sich herleitet, was Sie wollen, sondern geben Sie es konkret an. Verwenden Sie einfache Sprache, die genau sagt, was Sie wollen, ohne Mehrdeutigkeit.

Das Schlüsselprinzip: Sagen Sie dem Modell genau, was Sie haben möchten. Wenn Sie einen umfassenden Bericht wünschen, fragen Sie danach. Wenn Sie bestimmte Funktionen benötigen, listen Sie diese auf. Moderne Modelle wie Claude profitieren insbesondere von expliziten Anweisungen.

Beispiel: Erstellung eines Analyse-Dashboards

Vage: „Erstelle eine Analyse-Dashboard“

Explizit: „Erstellen ein Analyse-Dashboard. Fügen Sie so viele relevante Funktionen und Interaktionen wie möglich hinzu. Gehe über die Grundlagen hinaus, um eine Implementierung mit allen Funktionen zu erstellen."

Die zweite Version fordert explizit umfassende Funktionen und signalisiert, dass das Modell über das Minimum hinausgeht.

Best Practices:

- Führe Aktionsverben ein: „Schreiben“, „Analysieren“, „Generieren“, „Erstellen“

- Präambel überspringen und direkt zur Anfrage kommen

- Geben Sie an, was die Ergebnisse enthalten sollen, nicht nur woran gearbeitet werden soll

- Geben Sie genaue Angaben zu Qualität und Tiefe an

#### Kontext und Motivation liefern

Zu erklären,warumetwas wichtig ist, hilft KI-Modellen, Ihre Ziele besser zu verstehen und gezieltere Antworten zu liefern. Dies ist besonders effektiv bei neueren Modellen, die über die Ziele nachdenken können.

Beispiel: Formatierungseinstellungen

Weniger effektiv: „NIEMALS Bulletins verwenden“

Effektiver: „Ich bevorzuge Antworten in natürlicher Absätze, da ich Prosa leichter lesbar und konversationsfreundlicher finde. Bulletpoints wirken sich zu formell und listenähnlich für meinen legeren Lernstil an.“

Die zweite Version hilft dem Modell, die Gründe für die Regel zu verstehen, sodass bessere Entscheidungen über die Formatierung getroffen werden können.

Um den Kontext zu erläutern:

- Zweck oder Zielgruppe des Produkts erklären

- Klärung, warum bestimmte Einschränkungen bestehen

- Beschreibung, wie die Ergebnisse verwendet werden

- Angabe des Problems, das Sie lösen möchten

#### Spezifisch sein

Prompt-Engineering erfordert die Strukturierung Ihrer Anweisungen mit expliziten Richtlinien und Anforderungen. Je genauer man seine Wünsche formuliert, desto besser sind die Ergebnisse.

Beispiel: Essensplanung

Vague: „Einen Speiseplan für eine mediterrane Ernährung erstellen“

Spezifisch: „Entwickeln Sie einen mediterranen Ernährungsplan für die Behandlung von Prädiabetikern. 1.800 Kalorien täglich, Schwerpunkt auf Lebensmitteln mit niedrigem glykämischen Wert. Ich nenne Frühstück, Mittagessen, Abendessen und einen Snack mit vollständigen Nährwertangaben.“

Was macht einen Prompt spezifisch genug?

Anforderungen:

- Klare Einschränkungen (Wortzahl, Format, Zeitplan)

- Relevanter Kontext (wer ist die Zielgruppe, was ist das Ziel)

- Gewünschte Ausgabestruktur (Tabelle, Liste, Absatz)

- Anforderungen oder Einschränkungen (diätetische Anforderungen, Budgetlimits, technische Einschränkungen)

#### Beispiele verwenden

Beispiele sind nicht immer notwendig, aber sie eignen sich hervorragend, um Konzepte zu erklären oder bestimmte Formate zu demonstrieren. Beispiele, die auch als One-Shot-Prompt bezeichnet werden, zeigen statt zu erzählen, und verdeutlichen subtile Anforderungen, die schwer allein in Beschreibung auszudrücken sind.

Wichtiger Hinweis für moderne Modelle: Claude 4.x und ähnliche erweiterte Modelle achten sehr genau auf Details in Beispielen. Stellen Sie sicher, dass Ihre Beispiele an den Verhaltensweisen ausgerichtet sind, die Sie fördern möchten, und minimieren Sie alle Muster, die Sie vermeiden möchten.

Beispiel: Artikelzusammenfassung

Ohne Beispiel: „Fasse diesen Artikel zusammen“

```

```

Beispiele für diese Anwendung:

- Das gewünschte Format ist einfacher darzustellen als zu beschreiben

- Sie benötigen einen bestimmten Ton oder Stil

- Die Aufgabe beinhaltet subtile Muster oder Konventionen

- Einfache Anweisungen führten nicht zu konsistenten Ergebnissen

Pro-Tipp: Beginnen Sie mit einem Beispiel (einmalig). Füge nur dann weitere Beispiele hinzu, wenn das Ergebnis immer noch nicht deinen Anforderungen entspricht.

#### Claude die Erlaubnis geben, Unsicherheit auszudrücken

Geben Sie der KI die ausdrückliche Erlaubnis, Unsicherheit auszudrücken, anstatt zu raten. Dies reduziert Halluzinationen und erhöht die Zuverlässigkeit.

Beispiel: „Analysieren Sie diese Finanzdaten und identifizieren Sie Trends. Wenn die Daten nicht ausreichen, um Schlussfolgerungen zu ziehen, sollte man dies sagen, anstatt zu spekulieren.“

Diese einfache Ergänzung macht die Antworten vertrauenswürdiger, da das Modell die Einschränkungen berücksichtigen kann.

[Versuchen](https://claude.ai/)Sie es in Claude.

## Erweiterte Prompt-Engineering-Techniken

Diese Kerngewohnheiten bringen Sie ziemlich weit, aber Sie können immer noch Situationen finden, die anspruchsvollere Ansätze erfordern. Fortschrittliche Prompt-Engineering-Techniken eignen sich hervorragend, wenn Sie agentische Lösungen entwickeln, mit komplexen Datenstrukturen arbeiten oder mehrstufige Probleme lösen müssen.

### Antwort der KI im Voraus ausfüllen

Im Vorfeld können Sie die Antwort der KI erstellen, wobei Sie Format, Ton oder Struktur festlegen. Diese Technik ist besonders leistungsfähig, um Ausgabeformate durchzusetzen oder Präambel zu überspringen.

Für die Vorauszahlung:

- Sie benötigen die KI, um JSON, XML oder andere strukturierte Formate auszugeben

- Sie möchten die Präambel überspringen und direkt zum Inhalt kommen

- Sie müssen eine bestimmte Stimme oder Figur beibehalten

- Sie möchten steuern, wie die KI mit der Reaktion beginnt

Beispiel: Durchsetzung der JSON-Ausgabe

Claude könnte ohne Vorankündigung sagen: „Hier ist der angeforderte JSON: {...}“

Mit Vorabfüllen (API-Nutzung):

```

```

Die KI wird aus dem ersten Rang bestehen und nur gültiges JSON liefern.

Hinweis: In Chat-Oberflächen kann dies annähernd angegeben werden, indem es sehr explizit formuliert: „Ausgabe nur als JSON ohne Präambel. Beginnen Sie Ihre Antwort mit einem ersten Satz.“

### Denkkette

Bei der Gedankenkette (Chain of Thought, CoT) wird vor der Beantwortung eine Schritt-für-Schritt-Argumentation abgefragt. Diese Technik hilft bei komplexen analytischen Aufgaben, die vom strukturierten Denken profitieren.

Moderner Ansatz: Claude bietet eine[erweiterte Denkfunktion](https://www.anthropic.com/news/visible-extended-thinking), die strukturiertes Denken automatisiert. Wenn es möglich ist, ist erweitertes Denken in der Regel der manuellen Denkkette vorzuziehen. Das Verständnis des manuellen CoT bleibt jedoch nützlich, wenn kein erweitertes Denken verfügbar ist oder wenn Sie transparente Argumente benötigen, die Sie überprüfen können.

Wenn wir es in Gedanken verwenden:

- Erweitertes Denken ist nicht verfügbar (z. B. der kostenloseClaude.ai-Plan)

- Sie benötigen transparente Argumente, die Sie überprüfen können

- Die Aufgabe erfordert mehrere Analyseschritte

- Sie möchten sicherstellen, dass die KI bestimmte Faktoren berücksichtigt

Es gibt drei gängige Implementierungen der Gedankenkette:

Grundlegende Denkkette

Fügen Sie Ihren Anweisungen einfach „Schritt für Schritt denken“ hinzu.

```

```

Gedankengänge

Strukturieren Sie Ihren Prompt so, dass er bestimmte Reasoning-Phasen bereitstellt.

```

```

Strukturierte Denkkette

Verwenden Sie Tags, um die Gründe von der endgültigen Antwort zu trennen.

```

```

Hinweis: Selbst wenn erweitertes Denken verfügbar ist, kann ein explizites CoT-Prompt für komplexe Aufgaben immer noch von Vorteil sein. Die beiden Ansätze ergänzen sich, schließen sich nicht aus.

### Steuerung des Ausgabeformats

Für moderne KI-Modelle gibt es mehrere effektive Methoden, die Antwortformatierung zu kontrollieren:

1. Sagen Sie der KI, was SIE NICHT machen soll

Anstatt: „Verwenden Sie keinen Markdown in Ihrer Antwort“ Versuchen Sie: „Ihre Antwort sollte aus Prosabsätzen bestehen, die reibungslos fließen“

2. Stimmen Sie den Prompt-Stil an die gewünschte Ausgabe ab

Der Formatierungsstil, der in Ihrem Prompt verwendet wird, kann den Antwortstil der KI beeinflussen. Wenn Sie den Markdown minimieren möchten, reduzieren Sie den Markdown im Prompt

3. Geben Sie die Formatierungspräferenzen an

Zur detaillierten Kontrolle der Formatierung:

```

```

### Prompte Verkettung

Im Gegensatz zu den vorherigen Techniken kann das Prompt-Kettening nicht in einem einzigen Prompt implementiert werden. Die Kette zerlegt komplexe Aufgaben in kleinere sequentielle Schritte mit separaten Prompts. Jeder Prompt verarbeitet eine Stufe, und die Ausgabe wird in die nächste Anweisung eingearbeitet.

Dieser Ansatz tauscht die Latenz gegen eine höhere Genauigkeit aus, indem jede einzelne Aufgabe vereinfacht wird. Normalerweise würde diese Technik über Workflows oder programmgesteuert implementiert, aber Sie könnten die Prompts manuell bereitstellen, nachdem Sie die Antworten erhalten haben.

Beispiel: Forschungszusammenfassung

- Erster Prompt: „Fassen Sie dieses medizinische Papier zusammen, das Methodik, Ergebnisse und klinische Auswirkungen enthält.“

- Zweite Aufforderung: „Überprüfen Sie die obige Zusammenfassung auf Genauigkeit, Klarheit und Vollständigkeit. Geben Sie bewertetes Feedback.“

- Dritter Prompt: „Verbessern Sie die Zusammenfassung anhand des folgenden Feedbacks: [Feedback aus Schritt 2]“

Jede Stufe verbessert die Kenntnisse durch fokussierten Unterricht.

Wenn es das Prompt-Chaining verwendet:

- Sie haben eine komplexe Anfrage, die in mehrere Schritte aufgegliedert werden muss

- Sie benötigen eine iterative Verfeinerung

- Sie führen eine mehrstufige Analyse durch

- Zwischenvalidierung bietet Mehrwert

- Ein einziger Prompt liefert inkonsistente Ergebnisse

Nachteil: Die Verkettung erhöht die Latenz (mehrere API-Aufrufe), verbessert jedoch oft die Genauigkeit und Zuverlässigkeit für komplexe Aufgaben erheblich.

## Techniken, von denen Sie vielleicht gehört haben

Einige Prompt-Engineering-Techniken, die bei früheren KI-Modellen populär waren, sind bei Modellen wie Claude weniger notwendig. Sie finden sie jedoch möglicherweise immer noch in älteren Dokumentationen oder in bestimmten Situationen nützlich.

### XML-Tags zur Struktur

XML-Tags wurden einst empfohlen, um Prompts Struktur und Klarheit zu verleihen, insbesondere bei der Integration großer Datenmengen. Obwohl moderne Modelle Strukturen ohne XML-Tags besser verstehen, können sie in bestimmten Situationen immer noch nützlich sein.

Beispiel:

```

```

Wenn XML-Tags immer noch nützlich sind:

- Sie arbeiten mit extrem komplexen Prompts und mischen mehrere Content-Typen

- Sie müssen sich der Content-Grenzen absolut sicher sein

- Sie arbeiten mit älteren Modellversionen

Moderne Alternative: In den meisten Anwendungsfällen funktionieren klare Überschriften, Leerräume und explizite Sprache („Unter Verwendung der Athleteninformationen unten…“) mit weniger Overhead genauso gut.

### Rollenabfrage

Die Rollenabfrage definiert die Experten und ihre Perspektiven bei der Formulierung Ihrer Frage. Dies kann effektiv sein, aber moderne Modelle sind so ausgefeilt, dass eine aufwändige Rollenabfrage oft überflüssig ist.

Beispiel: „Sie sind Finanzberater. Analysieren Sie dieses Anlageportfolio..."

Wichtiger Vorbehalt: Überlasten Sie die Rolle nicht. „Sie sind ein hilfreicher Assistent“ ist oft besser als „Sie sind ein weltbekannter Experte, der nur technischen Fachjargon spricht und niemals Fehler macht.“ Zu spezifische Rollen können den Nutzen der KI einschränken.

Wenn die Rollenabfrage hilfreich sein könnte:

- Sie benötigen einen konsistenten Ton für viele Ausgaben

- Sie erstellen eine Bewerbung, die eine bestimmte Person benötigt

- Sie möchten Fachwissen für komplexe Themen zusammenstellen

Moderne Alternative: Oft ist es effektiver, die gewünschte Perspektive explizit anzugeben: „Analysieren Sie dieses Anlageportfolio und konzentrieren Sie sich auf die Risikotoleranz und das langfristige Wachstumspotenzial“, als eine Rolle zuzuweisen.

[Versuchen Sie](https://preview.claude.ai/new)es mit Claude.

## Alles zusammenfassen

Man hat die einzelnen Techniken isoliert betrachtet, aber ihre wahre Leistungsfähigkeit kommt zum Tragen, wenn man sie strategisch kombiniert. Prompt-Engineering verwendet nicht jede verfügbare Technik, sondern die Auswahl der richtigen Kombination für Ihre spezifischen Anforderungen.

Beispiel für die Kombination mehrerer Techniken:

```

```

Dieser Prompt kombiniert:

- Explizite Anweisungen (exakt zu extrahieren)

- Kontext (warum das Format wichtig ist)

- Beispielstruktur (Format)

- Erlaubnis zur Ausdrucksform der Unsicherheit (Null verwenden, wenn unsicher)

- Formatsteuerung (mit dem ersten Teil beginnen)

## Auswahl der richtigen Techniken

Nicht jeder Prompt benötigt jede Technik. Hier ist ein Entscheidungsrahmen:

Hier beginnen:

- Ist Ihre Anfrage klar und explizit? Wenn nicht, dann erst Klarheit schaffen

- Ist die Aufgabe einfach? Nur Kerntechniken verwenden (spezifisch, klar und im Kontext angeben)

- Benötigt die Aufgabe eine bestimmte Formatierung? Beispiele oder Vorfüllen verwenden

- Ist die Aufgabe komplex? Zersetzen (Ketten)

- Muss es begründet werden? Verwenden Sie erweitertes Denken (falls verfügbar) oder Denkkette

‍Leitfaden zur Auswahl von Techniken:

## Fehlerbehebung bei Prompt-Problemen

Selbst gut gemeinte Prompts können unerwartete Ergebnisse liefern. Hier sind häufige Probleme und wie sie behoben werden:

- Problem: Die Antwort ist zu allgemein→ Lösung: Fügen Sie Spezifischkeiten, Beispiele oder explizite Anforderungen hinzu, um umfassende Ergebnisse zu erzielen. Bitten Sie die KI, „über die Grundlagen hinauszugehen“.

- Problem: Die Antwort ist offtopic oder verfehlt den Punkt→ Lösung: Geben Sie Ihr tatsächliches Ziel an. Geben Sie den Kontext an, warum Sie fragen.

- Problem: Antwortformat ist inkonsistent→ Lösung: Fügen Sie Beispiele hinzu (wenige) oder verwenden Sie das Prefill zur Steuerung des Beginns der Antwort.

- Problem: Aufgabe ist zu komplex, die Ergebnisse sind unzuverlässig→ Lösung: Mehrere Prompts erstellen (Ketten), Jeder Prompt sollte eine Aufgabe erfüllen.

- Problem: KI enthält unnötige Präambel→ Lösung: Vorfüllen verwenden oder explizit fragen: „Überspringen Sie die Präambel und kommen Sie direkt zur Antwort.“

- Problem: KI erfindet Informationen→ Lösung: Erlauben Sie explizit die Angabe, „Ich weiß nicht“ zu sagen, wenn es unsicher ist.

- Problem: KI schlägt Änderungen vor, wenn sie implementiert werden sollten→ Lösung: Geben Sie die Aktion an: „Ändern Sie diese Funktion“ anstatt „Können Sie Änderungen vorschlagen?“

Pro-Tipp: Starten Sie einfach und fügen Sie Komplexität hinzu, wenn es nötig ist. Testen Sie jede Ergänzung, um zu sehen, ob sie die Ergebnisse tatsächlich verbessert.

## Häufige Fehler zu vermeiden

Lernen Sie aus diesen häufigen Fallen, um Zeit zu sparen und Ihre Prompts zu verbessern:

- Nicht übertreiben: Länger, komplexere Prompts sind NICHT immer besser.

- Vergessen Sie nicht, dass erweiterte Techniken nicht helfen, wenn Ihr Kernprompt unklar oder vage ist.

- Gehen Sie nicht davon aus, dass die KI Gedanken liest: Geben Sie genau an, was Sie möchten. Wenn die Dinge mehrdeutig sind, kann die KI falsch interpretieren.

- Verwenden Sie nicht alle Techniken gleichzeitig: Wählen Sie Techniken aus, die Ihre spezifischen Herausforderungen erfüllen.

- Vergessen Sie nicht, es zu wiederholen: Der erste Prompt funktioniert selten perfekt. Testen und verfeinern.

- Verlassen Sie sich nicht auf veraltete Techniken: XML-Tags und umfangreiche Rollenabfragen sind bei modernen Modellen weniger notwendig. Beginnen Sie mit klaren Anweisungen.

## Prompt-Engineering

### Mit langen Inhalten arbeiten

Eine der Herausforderungen bei der Implementierung von Prompt-Engineering besteht darin, dass es durch die Verwendung zusätzlicher Token Kontext schafft. Beispiele, mehrere Prompts, detaillierte Anweisungen – sie alle verbrauchen Tokens, und das Kontextmanagement ist eine Fähigkeit für sich.

Prompt-Engineering sollte verwendet werden, wenn es sinnvoll ist und die Verwendung rechtfertigt. Eine umfassende Anleitung zur effektiven Verwaltung von Kontext finden Sie in unserem Blogbeitrag über[Kontext Engineering](https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents).

Verbesserungen der Kontextbewusstsein: Moderne KI-Modelle, einschließlich Claude 4.x, haben die Funktionen zur Kontextbewusstsein deutlich verbessert, um historische Probleme zu lösen, bei denen die Modelle Schwierigkeiten hatten, alle Teile des langen Kontexts gleichermaßen zu berücksichtigen.

Warum Aufgabenaufteilung immer noch hilft: Selbst mit diesen Verbesserungen bleibt die Aufteilung großer Aufgaben in kleinere, diskrete Teile eine wertvolle Technik – nicht aufgrund von Kontextbeschränkungen, sondern weil das Modell sich so darauf konzentriert, seine Arbeit innerhalb eines sehr spezifischen Rahmens und Anforderungen optimal zu erbringen. Eine fokussierte Aufgabe mit klaren Grenzen führt zu qualitativ hochwertigeren Ergebnissen als der Versuch, mehrere Ziele auf einmal zu erreichen.

Strategie: Strukturieren Sie Ihre Informationen bei langen Zusammenhängen klar und deutlich mit den wichtigsten Details am Anfang oder am Ende. Bei komplexen Aufgaben sollte man überlegen, ob die Aufteilung in zielgerichtete Teilaufgaben die Qualität und Zuverlässigkeit jeder Komponente verbessern würde.

### Wie sieht ein guter Prompt aus?

Prompt-Engineering ist eine Fähigkeit, und es dauert ein paar Versuche, bis Sie es beherrschen. Der einzige Weg, um zu wissen, ob es richtig ist, ist, es zu testen. Der erste Schritt ist, es selbst auszuprobieren. Sie sehen sofort die Unterschiede zwischen Abfragen mit und ohne die hier beschriebenen Prompting-Techniken.

Um Ihre Prompt-Engineering-Fähigkeiten wirklich zu verbessern, müssen Sie die Effektivität Ihrer Prompts objektiv messen. Die gute Nachricht ist, dass es genau das ist, was in unserem Prompt-Engineering-Kurs auf[anthropic.skilljar.com](https://anthropic.skilljar.com/claude-with-the-anthropic-api)behandelt wird.

Tipps zur Bewertung:

- Entspricht das Ergebnis Ihren spezifischen Anforderungen?

- Sie haben das Ergebnis in einem Versuch erhalten oder benötigen mehrere Iterationen?

- Ist das Format über mehrere Versuche hinweg einheitlich?

- Vermeiden Sie die oben genannten Fehler?

## Letzte Worte

Prompt-Engineering bedeutet letztendlich Kommunikation: Es muss die Sprache gesprochen werden, die es der KI ermöglicht, Ihre Absicht am besten zu verstehen. Beginnen Sie mit den Kerntechniken, die bereits zu Beginn dieses Leitfadens behandelt wurden. Verwenden Sie sie konstant, bis sie zur zweiten Natur werden. Nur in fortschrittlichen Techniken integriert, wenn sie ein bestimmtes Problem lösen.

Denken Sie daran: Der beste Prompt ist nicht der längste oder komplexeste. Es ist es, das Ihre Ziele zuverlässig erreicht, mit der erforderlichen Mindeststruktur. Während Sie üben, entwickeln Sie eine Intuition für die Techniken, die für die jeweilige Situation geeignet sind.

Die Verlagerung zum Kontext-Engineering mindert nicht die Bedeutung des Prompt Engineering. Prompt-Engineering ist ein grundlegender Baustein im Kontext-Engineering. Jeder gut gestaltete Prompt wird Teil des größeren Kontexts, der das KI-Verhalten prägt und mit dem Konversationsverlauf, angehängten Dateien und Systemanweisungen zusammenarbeitet, um bessere Ergebnisse zu erzielen.

[Claude ist noch heute dabei](https://preview.claude.ai/new).

## Zusätzliche Ressourcen

- Prompt-Engineering Dokumentation

- Interaktives Prompt-Engineering-Tutorial

- Prompt-Engineering-Kurs

- Leitfaden für Kontext

![](https://cdn.prod.website-files.com/6889473510b50328dbb70ae6/6889473610b50328dbb70b58_placeholder.svg)

![](https://cdn.prod.website-files.com/6889473510b50328dbb70ae6/6889473610b50328dbb70b58_placeholder.svg)

![](https://cdn.prod.website-files.com/6889473510b50328dbb70ae6/6889473610b50328dbb70b58_placeholder.svg)

Häufig gestellte Fragen

## Ähnliche Beiträge

Weitere Produktneuheiten und Best Practices für Teams, die mit Claude arbeiten.

![](https://cdn.prod.website-files.com/68a44d4040f98a4adf2207b6/6903d229e73ca2d0d73d78f7_682ac293884c9d4ee4ebe2355a2f6c4ecfdd9c1b-1000x1000.svg)

### Getting started with loops

![](https://cdn.prod.website-files.com/68a44d4040f98a4adf2207b6/6903d2238ce207f9b2011d3f_e44a6b53398f189b9fd0d4f70516db614ac84db3-1000x1000.svg)

### Beobachtbarkeit für Entwickler, die Konnektoren entwickeln

![](https://cdn.prod.website-files.com/68a44d4040f98a4adf2207b6/6903d22d7d4c10df6024f7bc_ee580919acaba2ddc07425f7a7390c8962cadc94-1000x1000.svg)

### Steering Claude Code: CLAUDE.md files, skills, hooks, rules, subagents and more

![](https://cdn.prod.website-files.com/68a44d4040f98a4adf2207b6/6a025cf25f0694905405e054_Object-Scale.svg)

### Claude für die Rechtsbranche

## Transformieren Sie mit Claude die Arbeitsweise Ihres Unternehmens

Entwickler-Newsletter abonnieren

Neues zu Produkten, Anleitungen, Community-Spotlights und mehr. Monatlich in Ihrem Posteingang.

Bitte geben Sie Ihre E-Mail-Adresse an, wenn Sie unseren monatlichen Entwickler-Newsletter erhalten möchten. Sie können sich jederzeit wieder abmelden.

---
**Source:** https://claude.com/de/blog/best-practices-for-prompt-engineering
*This is a mirror of the Claude.com blog post for local access and AI-assisted development.*
