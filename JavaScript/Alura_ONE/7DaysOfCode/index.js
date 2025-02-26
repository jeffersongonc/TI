let comparacaoUm = document.getElementById("comparacaoUm");
let comparacaoDois = document.getElementById("comparacaoDois");
let comparacaoTres = document.getElementById("comparacaoTres");

let numeroUm = 1;
let stringUm = '1';
let numeroTrinta = 30;
let stringTrinta = '30';
let numeroDez = 10;
let stringDez = '10';

function compararVariaveis( varUm, varDois){
    let textoVariaveis = '';
    let textoTipo = '';
    let tipoUm = typeof varUm;
    let tipoDois = typeof varDois;
    textoVariaveis = (varUm == varDois) ? " Os valores são iguais" : " Os valores são diferentes";
    textoTipo = (tipoUm == tipoDois) ? " e os tipos das variáveis são iguais." : " e os tipos das variáveis são diferentes.";
    
    return textoVariaveis + textoTipo;
}

comparacaoUm.innerHTML = comparacaoUm.innerHTML + compararVariaveis(numeroUm, stringUm);
comparacaoDois.innerHTML = comparacaoDois.innerHTML + compararVariaveis(numeroTrinta, stringTrinta);
comparacaoTres.innerHTML = comparacaoTres.innerHTML + compararVariaveis(numeroDez, stringDez);