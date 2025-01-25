//O principal objetivo deste desafio é fortalecer suas habilidades em lógica de programação. Aqui você deverá desenvolver a lógica para resolver o problema.
let listaNomes = [];
let listaAmigos = [];
let nomes = document.getElementById("amigo");

function gerarNumeroAleatorio(base){
    return parseInt(Math.random()*base)
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

function exibirNomes(tagPai, tagFilho, valor){
    let ul = document.getElementById(tagPai);
    let li = document.createElement(tagFilho);
    
    li.textContent = valor;
    ul.appendChild(li);
}

function adicionarAmigo(){
    if (nomes.value.trim() != "" && !listaNomes.includes(nomes.value.toUpperCase())){
        listaNomes.push(nomes.value.toUpperCase());
        exibirNomes("listaAmigos", "li", nomes.value.toUpperCase());
    }
    limparTag("amigo", "text");
    limparTag("resultado", "ul");   
}

function sortearAmigo(){
    let quantidade = listaNomes.length;
    
    limparTag("resultado", "ul");
    if (quantidade < 2) {
        exibirNomes("resultado", "li", "Insira ao menos 2 nomes");
    }
    else{
        exibirNomes("resultado", "li", `Seu amigo secreto é: ${listaNomes[gerarNumeroAleatorio(listaNomes.length)]}`)
    }
}
