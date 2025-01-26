//O principal objetivo deste desafio é fortalecer suas habilidades em lógica de programação. Aqui você deverá desenvolver a lógica para resolver o problema.
let listaSorteio = [];
let listaAmigos = [];
let nomes = document.getElementById("amigo");

function gerarNumeroAleatorio(base){
    return parseInt(Math.random()*base);
}
function limparTag(tag, tipo){
    let campo = document.getElementById(tag);
    
    switch (tipo) {
        case "ul":
            campo.innerHTML = "";    
            break;
        default:
            campo.value = "";
            break;
    }
}

function alterarMensagemInicial(tag, valor){
    let campo = document.querySelector(tag);

    campo.innerHTML = valor;
}

alterarMensagemInicial("h2", "Digite o seu nome");

function exibirNomes(tagPai, tagFilho, valor){
    let ul = document.getElementById(tagPai);
    let li = document.createElement(tagFilho);
    
    li.textContent = valor;
    ul.appendChild(li);
}

function adicionarAmigo(){
    if (nomes.value.trim() != "" && !listaAmigos.includes(nomes.value.toUpperCase())){
        listaAmigos.push(nomes.value.toUpperCase());
        exibirNomes("listaAmigos", "li", nomes.value.toUpperCase());
    }
    limparTag("amigo", "text");
    limparTag("resultado", "ul");
    listaAmigos.length > 0 ? alterarMensagemInicial("h2", "Digite o nome dos seus amigos") : alterarMensagemInicial("h2", "Digite o seu nome");
}

function definirAmigoSecreto(){
    let listaBase = listaAmigos.slice();
    for (let i in listaAmigos){
        let escolha = gerarNumeroAleatorio(listaAmigos.length);
        while (listaAmigos[i] == listaBase[escolha] || listaSorteio.includes(listaBase[escolha])){
            escolha = gerarNumeroAleatorio(listaAmigos.length);
        }
        listaSorteio.push(listaBase[escolha]);
    }
    console.log(listaAmigos);
    console.log(listaSorteio);    
}

function sortearAmigo(){
    let quantidade = listaAmigos.length;
    
    limparTag("resultado", "ul");
    if (quantidade < 2) {
        exibirNomes("resultado", "li", "Insira ao menos 2 nomes");
    }
    else{
        definirAmigoSecreto();
        exibirNomes("resultado", "li", `Seu amigo secreto é: ${listaSorteio[0]}`);
    }
}
