# VueJs Tutorial

```
# install
 nodeenv env
# activate 
  . env/bin/activate
```

## Create New Project
- npm install -g @vue/cli
- vue create todo-app

## Vue User Interface

- vue ui

## Modi per utilizzare VueJS

```
a. Utilizzo di CDN includendo il tag <script> nel file HTML;
b. Installazione tramite package manager (npm o yarn);
c. Utilizzo di @vue/cli per inizializzare il progetto.
```

## Example Vue project structure

```
todo-app
├── node_modules
├── public
│ ├── favicon.ico
│ └── index.html
├── src
│ ├── App.vue
│ ├── assets
│ │ └── logo.png
│ ├── components
│ │ └── HelloWorld.vue
│ └── main.js
├── README.md
├── babel.config.js
├── package.json
└── yarn.lock
```

# Shell

Vue command line interface for project maneagement and creation

```bash
 vue cli 
```

Vue run node client server without building and automate the dependency fixing.

```bash
node run serve --fix
```

```bash
vue ui
```

# Data Interpolation

```html
<p> {{ my_variabile }} </p>
<p> {{ my_function( ) }} </p>
```

# Vue components

### Basic syntax

v-{nomedirettiva}:{nomeargomento}

Il motore di Vue implementa il cosiddetto one way data flow come modalità con la quale i componenti comunicano tra di loro. In particolare, questo significa che le prop passate ad un componente possono essere modificate dall’esterno, ma non dal componente stesso, in quanto il flusso di dati è monodirezionale, dall’alto al basso. Se per qualche ragione cercassimo di modificare il valore di una prop all’interno di un componente, Vue lancierà un warning in console.
Gli sviluppatori di Vue hanno imposto questo comportamento come schermatura per potenziali errori incontrollati, che potrebbero verificarsi implementando un doppio flusso di modifica. Nel caso in cui servisse implementare un componente che applichi una modifica verso l’alto, gli stessi sviluppatori suggeriscono un approccio basato sugli eventi custom.

# opzione data( ) - Vue.component

l’opzione data non può più essere un oggetto, ma deve essere una funzione

```
//questo è la modalità ERRATA
Vue.component('mio-componente', {
  data: {
    name: 'Alberto',
    age: 99
  }
});
//questo è la modalità CORRETTA
Vue.component('mio-componente', {
  data: function() {
    return {
      name: 'Alberto',
      age: 99
    };
  }
});
```

# template componente

## Modi di definire il template:

## 1\. Stringa

```
Vue.component('mio-componente', {
  template: '<b>Io sono il corpo del componente</b>'
});
```

## 2\. Nodo Esterno

il template può essere contenuto all’interno di un tag `<template>` o di un tag `<script>` con type text/x-template

```
<mio-componente></mio-componente>
<template id="mio-componente-template">
  <b>Io sono il corpo del componente</b>
</template>

Vue.component('mio-componente', {
  template: '#mio-componente-template'
});

```

## 3\. Template inline

Definire un template inline all’interno del nodo stesso del componente. Questa è una modalità che permette di avere diverse istanziazioni dello stesso componente ma con template differenti. Per poter utilizzare uesta modalità è necessario l’utilizzo dell’attributo inline-template.

```
<mio-componente inline-template>
  <b>Io sono il corpo del componente</b>
</mio-componente>

Vue.component('mio-componente', {
  template: '#mio-componente-template'
});
```

## opzione props

Le props rappresentano le proprietà esterne che permettono di configurare un componente.
Dato che ciascun componente ha uno scope di esecuzione isolato, qualsiasi tipologia di dato esterno che deve essere reso accessibile dentro il componente, deve essere passato tramite appunto una prop.
Le proprietà devono essere definite a priori tramite appunto l’opzione props. Inoltre, se necessario, è possibile definire il loro tipo (String, Boolean, Number…), l’eventuale obbligatorietà (required) o un valore di default.

## Example form v-model + v-bind

```html
<template>
<div id="vue">
  <input type="radio" v-model="mese" v-bind:value="'marzo'"> Marzo
  <input type="radio" v-model="mese" v-bind:value="'aprile'"> Aprile
  <input type="radio" v-model="mese" v-bind:value="'maggio'"> Maggio
  <br/>
  <input type="checkbox" v-model="tv" v-bind:true-value="'si'" v-bind:false-value="'no'">tv
  <input type="checkbox" v-model="sauna" v-bind:true-value="'si'" v-bind:false-value="'no'">sauna
  <br/><br/>
  {{ mese }} - {{ tv }} - {{ sauna }}
</div>
</template>

<script>
new Vue({
  el: '#vue',
  data: {
    mese: 'marzo',
    tv: 'si',
    sauna: 'no'
  }
})
</script>

```

## v-model

```
<input type="text" v-model="myText"> {{ myText }}
```

Questo esempio, inserito correttamente in un contesto Vue, permette di avere il contenuto di myText, associato con il valore presente nel campo di testo. v-model è totalmente agnostica dalla tipologia di input utilizzata.

```
select v-model="blog.author"
	option v-for='autor in autors
select

data
	blog:{
	author:
	}
	authors:['c','f']
```	

## v-on : gestione Eventi

v-on : aggancia un listener di eventi all’elemento. Il tipo di evento è indicato dall’argomento.
L’espressione può essere un nome di metodo, un’istruzione inline.
Per esempio se vogliamo agganciare un evento click  ad un pulsante la sintassi è
la forma abbreviata è la seguente

```html
// Examples

<button @click="submitForm">

<button @click="alert('Button clicked!')">Click<button>

<a href="#" @click.prevent="onClick">an anchor</a>

<input @keyup.enter="submit">

or
<button v-on:click="onClickButton">Click<button>
    <div v-on:click="updateData()" >
```

I modificatori dedicati agli eventi basati sulla tastiera sono: .enter, .tab, .delete, .esc, .space, .up, .down, .left, .right, .ctrl, code>.alt, .shift e .meta.
Sono disponibili anche modificatori speculari, ma basati sugli eventi del mouse: .left, .right e .middle

## v-show

```html
    <div v-if="showMovies">
      <li v-for="movie in movies">{{ movie }}</li>
```

## v-for

v-for : che effettua il rendering dell’elemento più volte in base ai dati di origine.
Utilizza una sintassi del tipo alias in expression per fornire un alias per l’elemento
corrente su cui si sta iterando;

```html
    <div v-if="showMovies">
      <li v-for="movie in movies">{{ movie }}</li>
```

## v-if

v-if : questa direttiva permette di effettuare il rendering di un componente
o di un elemento del DOM basandosi su una condizione specifica
(solitamente riguardante uno specifico valore dei nostri dati);

```html
    <div v-if="showMovies">
      <li v-for="movie in movies">{{ movie }}</li>
        
        or
    <div v-if ="'isAbilited'===true">

```

## v-bind

v-bind : Associa dinamicamente uno o più attributi, o una proprietà, del componente ad un’espressione;
<br>

# Come passare i dati tra i componenti in Vue.js

A meno che tu non stia creando l'intera app Vue in un componente (il che non avrebbe alcun senso), incontrerai situazioni in cui devi condividere i dati tra i componenti.

Alla fine di questo tutorial, conoscerai tre modi per farlo.

1. Usando gli oggetti di scena per condividere i dati da genitore a figlio,
2. Emissione di eventi personalizzati per condividere dati da figlio a genitore,
3. Utilizzo di Vuex per creare uno stato condiviso a livello di app.

tre modi diversi per condividere i dati tra i componenti in VueJS: oggetti di scena, eventi personalizzati e un negozio Vuex.

# VUEX
## Vue components
- state
- mutations
- actions
- getters

``` javascript

const store = new Vuex.Store({
	state:{
		loading : 'loading'
		todo : []
	}
	mutations:{
		SET_LOADING_STATUS(state, status){
			sate.loadingStatus = status
		},
		SET_TODO(state, todo){
		state.todo = todo
		}
	
	}
	actions:{
		fetchTodos(context){
		context.commit('SET_LOADING_STATUS','loading')
		axios.get('/api/todo').then( responde => {
	    context.commit('SET_LOADING_STATUS','loading')
		context.commit('SET_TODO',response.data.todo)
			
		})
		getters:{}

		}
	}
})

```


**Vuex**  è un’estensione per le applicazioni scritte in Vue che permette di avere quello che gli autori chiamano  *state management pattern*, ovvero un modello per applicazioni a stato centralizzato.

Il modello base di Vue prevede che ciascun componente sia composto dai seguenti blocchi logici:

- lo  **stato**, che rappresenta il contesto dei dati utilizzati dall’applicazione (concretizzato dall’oggetto  `data`);
- la  **vista**, che permette, tramite un mapping dichiarativo, di rappresentare lo stato all’utente tramite un’interfaccia (concretizzata tramite template HTML);
- le  **azioni**, che permettono di modificare lo stato reagendo alle interazioni che gli utenti fanno tramite la vista (concretizzata tramite eventi e metodi).

Per quanto questo modello sia funzionale e permette di avere modularità, esso è particolarmente rigido in applicazioni di una certa entità nelle quali spesso molti componenti condividono e necessitano di modificare un unico stato globale. Vuex permette di isolare questo  `stato`  in un’unica entità singleton, a disposizione di qualsiasi componente, a prescindere dal livello di gerarchia nel quale esso si trova.

Vuex, in concreto, è composto da un modello teorico di regole e di best practice da seguire e da una parte di software che funge da estensione di Vue e che permette di implementare il modello teorico con facilità. In questa prima lezione cercheremo di introdurre gli aspetti teorici, fondamentali per capire questo modello, mentre nella lezione successiva implementeremo un’applicazione Vuex da zero.

## Stato e store

Il concetto principale di una applicazione Vuex è lo  `store`. Esso rappresenta il contenitore dello stato globale dell’applicazione. Le caratteristiche che rendono gli store funzionali sono principalmente due:

- la  **reattività**: qualsiasi componente che utilizza un dato contenuto nello store viene notificato di eventuali cambi tramite le funzionalità già apprese in Vue;
- l’**immutabilità**: gli store non sono modificabili direttamente ma solamente tramite delle azioni specifiche, chiamate  *mutation*  in modo da garantirne la consistenza e la tracciabilità.

Nonostante lo stato viene reso globale tramite gli store, non è detto che ciascun componente non possa avere anche uno stato locale. Se esistono proprietà strettamente correlate ad un singolo componente, è corretto che esse rimangano locali. Inoltre la natura globale dello store, non limita la modularità in quanto è possibile scomporre lo store in sotto moduli indipendenti.

## Mutation

Come abbiamo introdotto prima, lo stato viene alterato tramite le  **mutation**. A loro volta, esse non vengono invocate direttamente ma vengono “committate” in uno store, come se fossero degli eventi che vengono scatenati, tramite il metodo  `store.commit("mutationName")`. Ovviamente, oltre al nome della mutation, se necessario, è possibile passare parametri aggiuntivi.

Il comportamento delle mutation viene definito direttamente all’interno dello store, proprio come se fossero dei listener sull’evento stesso.

Secondo gli sviluppatori di Vuex, è buona pratica quella di definire delle costanti per i nomi delle mutation, in modo da avere maggior controllo sulle invocazioni, per sfruttare eventuali tool di  *linting*  e per riuscire ad avere un file contentente la definizione di tutte le mutation disponibili nell’applicazione.

Ulteriore regola suggerita è quella della  **sincronia**. Le funzioni associate alle mutation devono essere sincrone. Una volta committate sullo store esse devono risolversi subito.

## Action

Le action sono simile alle mutation, tranne per il fatto che esse possono contenere codice asincrono e che vengono invocate tramite il metodo  `store.dispatch(actionName)`. Esse rappresentano un’azione scatanata da un comportamento di un utente e possono corrispondere ad una o più mutation.

Data l’asincronia del loro comportamento, il metodo  `dispatch`  ritorna una  <ins>Promise</ins>, in modo da poter gestire correttamente i valori di ritorno.

Seppur a prima vista esse possano sembrare ridondanti rispetto alle mutation, le action sono particolarmente diverse. Eventuali dubbi verranno risolti grazie all’implementazione di una applicazione reale, cosa che avverrà nel prossimo capitolo.

```
export default new Vuex.Store({
 state: {
   user: {
     username: 'matt',
     fullName: 'Matt Maribojoc'
   }
 },

getters: {
   firstName: state => {
     return state.user.fullName.split(' ')[0]
   },
   
   lastName (state, getters) {
     return state.user.fullName.replace(getters.firstName, '');
		}

 }

mutations: {
   changeName (state, payload) {
     state.user.fullName = payload
   }
},


 actions: {}
});


mounted () {
   console.log(this.$store.state.user.username);
}


```


Mutations,
possiamo chiamare questo metodo dal nostro componente usando il store.commitmetodo, con il nostro carico utile come secondo argomento
```
this.$store.commit("changeName", "New Name");
```

```
this.$store.commit("changeName", {
       newName: "New Name 1",
});
 
     // or
 
 this.$store.commit({
       type: "changeName",
       newName: "New Name 2"
});
```

AZIONI

In Vuex, le azioni sono abbastanza simili alle mutazioni perché le usiamo per cambiare lo stato. Tuttavia, le azioni non cambiano i valori stessi. Invece, le azioni commettono mutazioni. Inoltre, mentre le mutazioni Vuex devono essere sincrone, le azioni no. Usando le azioni, ad esempio, possiamo chiamare una mutazione dopo una chiamata API.
