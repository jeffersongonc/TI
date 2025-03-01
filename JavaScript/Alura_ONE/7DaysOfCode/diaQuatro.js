let perguntasDiaQuatro = document.getElementById("perguntasDiaQuatro");
let respostaDiaQuatro = document.getElementById("respostaDiaQuatro");
let valorMinimo = 0;
let valorMaximo;
let valorEscolhido;
let tentativas = 3;
function escolherMaximo(){
    let fValor;
    do{
        fValor = parseInt(prompt("Digite o valor máximo?"));
    }while (fValor < 1 || isNaN(fValor));
    return fValor;
}
function pergunta(event){
    event.preventDefault();
    valorMaximo = escolherMaximo();
    valorEscolhido = Math.floor(Math.random() * (valorMaximo-valorMinimo+1) + valorMinimo);
    let valorChute;
    let acertouChute = false;
    for (i=0; i<tentativas; i++){
        valorChute = prompt(`Tente adivinhar o valor. Tentativa ${i+1}/${tentativas}: Digite um valor entre ${valorMinimo} e ${valorMaximo}?`)
        if (valorChute == valorEscolhido){
            acertouChute = true;
            break;
        }
    }
    let mensagem;
    if (acertouChute){
        mensagem = `Você acertou! O valor correto era o ${valorChute}.`;
    } else{
        mensagem = `Você não acertou! O Valor correto era ${valorEscolhido}.`;
    }
    respostaDiaQuatro.innerHTML = mensagem;
}
perguntasDiaQuatro.addEventListener('click', pergunta);