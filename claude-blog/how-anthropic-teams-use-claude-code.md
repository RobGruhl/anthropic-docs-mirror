# Come i team di Anthropic utilizzano Claude Code
---
![](https://cdn.prod.website-files.com/68a44d4040f98a4adf2207b6/6903d223de65e7dcca8267d8_ea364001be6bf6d2e86b58109ead6a779d5771a7-1000x1000.svg)

# Come i team di Anthropic utilizzano Claude Code

I team di Anthropic utilizzano Claude Code per qualsiasi attività, dal debug dei problemi di produzione o la navigazione nelle codebase sconosciute fino alla creazione di strumenti di automazione personalizzati. Scopri come.

- CategoriaIA aziendale

- ProdottoClaude Code

- Data24/7/25

- Tempo di lettura5min

- CondividiCopia linkhttps://claude.com/blog/how-anthropic-teams-use-claude-code

Gli strumenti di programmazione di tipo agentico come[Claude Code](https://claude.com/it/product/claude-code)aiutano chi sviluppa ad accelerare i flussi di lavoro, automatizzare le attività ripetitive e affrontare progetti di programmazione complessi. Con l'evolversi del settore, ogni giorno scopriamo nuove applicazioni, sia dagli utenti, sia dai nostri stessi dipendenti.

Per saperne di più, abbiamo parlato con diversi dipendenti di Anthropic per capire come utilizzano Claude Code per svolgere il proprio lavoro.

Sebbene molti dei casi d'uso fossero prevedibili (debug, navigazione nelle codebase, gestione dei flussi di lavoro), altri ci hanno sorpreso. In campo legale, sono stati creati sistemi ad albero telefonico. Nel campo del marketing, sono state generate centinaia di varianti pubblicitarie in pochi secondi. Nel campo della scienza dei dati, sono state create visualizzazioni complesse senza conoscere JavaScript.

La tendenza è chiara: la programmazione agentica non sta semplicemente accelerando lo sviluppo tradizionale, sta dissolvendo il confine tra lavoro tecnico e non tecnico, trasformando chiunque sia in grado di descrivere un problema in una persona capace di progettare una soluzione.

Ecco cosa abbiamo appreso.

### Navigazione e comprensione della codebase

I team di tutta l'azienda utilizzano Claude Code per aiutare le nuove persone assunte, ma anche i dipendenti di lunga data, a familiarizzare con le codebase.

I nuovi data scientist del nostro Infrastructure team forniscono a Claude Code l'intera codebase per diventare produttivi rapidamente. Claude legge i file[CLAUDE.md](http://claude.md)della codebase, identifica quelli pertinenti, spiega le dipendenze della pipeline dei dati e mostra quali fonti a monte alimentano le dashboard, sostituendo gli strumenti tradizionali di catalogazione dei dati.

Il nostro Product Engineering team ritiene che Claude Code sia il "primo step" per qualsiasi attività di programmazione. Claude viene usato per individuare quali file esaminare ai fini della correzione dei bug, dello sviluppo di nuove funzionalità o dell'analisi, saltando così il lungo processo di raccolta manuale delle informazioni di contesto necessario prima di sviluppare nuove funzionalità.

### Test e revisione del codice

Gli strumenti di codifica agentici sono particolarmente apprezzati per la loro capacità di automatizzare due attività di programmazione critiche ma noiose: la scrittura di test unitari e la revisione del codice.

Il Product Design team utilizza Claude Code per scrivere test completi per le nuove funzionalità. Inoltre, ha automatizzato i commenti alle pull request tramite GitHub Actions e usa Claude per gestire automaticamente i problemi di formattazione e il refactoring dei casi di test.

Il team di Security Engineering ha trasformato il proprio flusso di lavoro passando da un modello "progettazione della documentazione → codice approssimativo → rifattorizzazione → rinuncia ai test" a una procedura in cui viene chiesto a Claude lo pseudocodice, lo si guida attraverso lo sviluppo guidato dai test e si effettuano controlli periodici. Ciò crea un codice più affidabile e verificabile.

La programmazione agentica può anche essere utilizzata per tradurre i test in altri linguaggi di programmazione. Ad esempio, quando l'Inference team ha bisogno di testare funzionalità in linguaggi meno familiari come Rust, spiega cosa vuole testare e Claude scrive la logica nel linguaggio nativo della codebase.

### Debug e risoluzione dei problemi

I problemi di produzione richiedono una risoluzione rapida, ma cercare di ragionare sui codici meno conosciuti quando si è sotto pressione porta spesso a ritardi. Per molti team all'interno dell'azienda, Claude Code consente di accelerare la diagnosi e le correzioni analizzando le tracce dello stack, la documentazione e il comportamento del sistema in tempo reale.

Durante gli incidenti, il Security Engineering team fornisce a Claude Code le tracce dello stack e la documentazione per tracciare il flusso di controllo attraverso la codebase. I problemi che in genere richiedevano 10-15 minuti di scansione manuale ora vengono risolti 3 volte più rapidamente.

Con Claude Code, il Product Engineering team ha acquisito la sicurezza necessaria per affrontare i bug in codebase poco familiari. Le persone del team chiedono a Claude: "Puoi risolvere questo bug? Questo è il comportamento che sto osservando" ed esaminano la soluzione proposta senza dover fare affidamento sull'assistenza di altri team tecnici.

In un caso, quando i cluster Kubernetes hanno smesso di pianificare i pod, il Data Infrastructure team ha utilizzato Claude Code per fare una diagnosi del problema. Una volta ottenuti gli screenshot della dashboard, Claude ha guidato le persone attraverso l'interfaccia utente di Google Cloud, menu per menu, fino a quando non è stato possibile individuare dove avveniva l'esaurimento degli indirizzi IP dei pod. Claude ha quindi fornito i comandi esatti per creare un nuovo pool IP in modo da aggiungerlo al cluster, facendo risparmiare 20 minuti di tempo prezioso durante l'interruzione del sistema.

### Prototipazione e sviluppo di funzionalità

Lo sviluppo di nuove funzionalità richiede tradizionalmente conoscenze tecniche approfondite e un investimento in termini di tempo piuttosto significativo. Claude Code consente la prototipazione rapida e persino lo sviluppo completo di applicazioni, permettendo ai team di validare le idee rapidamente indipendentemente dalle loro competenze di programmazione.

I membri del Product Design team, ad esempio, hanno fornito i file di design Figma a Claude Code e quindi impostato cicli autonomi in cui Claude Code scriveva il codice per la nuova funzionalità, eseguiva i test e iterava in modo continuo. Hanno fornito a Claude problemi astratti, hanno lasciato che Claude lavorasse in modo autonomo, poi hanno esaminato le soluzioni prima delle ottimizzazioni finali. In un caso, hanno fatto progettare a Claude delle combinazioni di tasti Vim per Claude con una revisione umana minima.

Con Claude Code, il Product Design team ha scoperto un utilizzo inaspettato: mappare stati di errore, flussi logici e stati del sistema per identificare i casi limite durante la fase di progettazione, anziché scoprirli in fase di sviluppo. Ciò ha migliorato enormemente la qualità iniziale dei progetti e consentito di risparmiare ore di debugging in seguito.

Nonostante non conoscano bene il linguaggio TypeScript, i data scientist utilizzano Claude Code per progettare intere applicazioni React destinate alla visualizzazione delle prestazioni dei modelli RL. Dopo un singolo prompt in un ambiente sandbox, lo strumento scrive intere visualizzazioni in TypeScript da zero senza che sia necessario comprendere il codice. Data la semplicità del compito, se il primo prompt non è sufficiente, è possibile apportare piccole modifiche e riprovare.

### Documentazione e gestione delle conoscenze

La documentazione tecnica spesso si trova dispersa tra wiki, commenti nel codice e nella mente delle persone del team. Claude Code consolida il bagaglio di conoscenze tramite MCP e file CLAUDE.md in formati accessibili, rendendo le competenze disponibili a tutti coloro che ne hanno bisogno.

I membri del team di inferenza privi di competenze in ML si affidano a Claude per capire le funzioni specifiche del modello. Quello che normalmente richiedeva un'ora di ricerca su Google ora richiede 10-20 minuti: una riduzione dell'80% del tempo di ricerca.

Il Security Engineering team chiede a Claude di elaborare molteplici fonti di documentazione per creare runbook in markdown e guide alla risoluzione dei problemi. Questi documenti condensati diventano il contesto per il debug di problemi reali in produzione, il che è spesso più efficiente rispetto alla ricerca all'interno di basi di conoscenza complete.

### Automazione e ottimizzazione del flusso di lavoro

Gli strumenti di programmazione agentici aiutano i team a creare automazioni personalizzate che tradizionalmente richiederebbero risorse di sviluppo dedicate o software costosi.

Il Growth Marketing team ha sviluppato un flusso di lavoro agentico che elabora file CSV contenenti centinaia di annunci, identifica quelli con prestazioni insufficienti e genera nuove varianti nel rispetto di rigidi limiti di caratteri. Utilizzando due sottoagenti specializzati, il sistema genera centinaia di nuovi annunci in pochi minuti quando prima erano necessarie diverse ore.

Il team ha inoltre sviluppato un plugin Figma che identifica i frame e genera programmaticamente fino a 100 varianti di annunci scambiando titoli e descrizioni, riducendo ore di copia e incolla a un mezzo secondo di lavoro per ogni gruppo di annunci.

In un caso d'uso particolarmente unico, il team legale ha creato prototipi di sistemi ad "albero telefonico" per aiutare le persone del team a mettersi in contatto con l'avvocato giusto presso Anthropic, dimostrando come i dipartimenti possano creare strumenti personalizzati senza le tradizionali risorse di sviluppo.

### Sbloccare nuove possibilità con Claude Code

Queste storie rivelano un pattern: Claude Code funziona meglio quando ci si concentra sui flussi di lavoro umani che può potenziare. I team di maggior successo trattano Claude Code come un vero e proprio partner e non come un semplice generatore di codice.

Esplorano le possibilità, creano prototipi rapidamente e condividono le scoperte tra utenti tecnici e non tecnici. Questo approccio collaborativo tra esseri umani e IA crea opportunità che oggi abbiamo appena iniziato a comprendere.

## Costruire un'IA affidabile nell'azienda

La guida di Anthropic su come iniziare, scalare e avere successo, basata su esempi reali e best practice.

![](https://cdn.prod.website-files.com/6889473510b50328dbb70ae6/6889473610b50328dbb70b58_placeholder.svg)

![](https://cdn.prod.website-files.com/68a44d4040f98a4adf2207b6/68e9140968560c6fe367e267_Hand-City-light.svg)

![](https://cdn.prod.website-files.com/68a44d4040f98a4adf2207b6/68e9140d1a23dfc2e7405210_Hand-City-dark.svg)

FAQ

Comincia a usare Claude Code.

## Articoli correlati

Accedi alle altre novità sui prodotti e scopri le best practice per i team che programmano con Claude.

![](https://cdn.prod.website-files.com/68a44d4040f98a4adf2207b6/6903d2238ce207f9b2011d3f_e44a6b53398f189b9fd0d4f70516db614ac84db3-1000x1000.svg)

### Come Brex migliora la qualità del codice e la produttività con Claude Code

## Trasforma le operazioni della tua azienda con Claude

Ricevi la newsletter sullo sviluppo

Aggiornamenti sui prodotti, guide utili, informazioni sulla community e molto altro. Ogni mese nella tua e-mail.

Inserisci il tuo indirizzo e-mail per ricevere la newsletter mensile sullo sviluppo. Puoi annullare l'iscrizione in qualsiasi momento.

---
**Source:** https://claude.com/it/blog/how-anthropic-teams-use-claude-code
*This is a mirror of the Claude.com blog post for local access and AI-assisted development.*
