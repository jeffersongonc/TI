let perguntasDiaDois = document.getElementById('perguntasDiaDois');
let respostaDiaDois = document.getElementById('respostaDiaDois');
let respostaExtra = document.getElementById('respostaExtra');
function perguntas(event){
    event.preventDefault();
    const nomeUsuario = nome();
    const idadeUsuario = idade();
    const linguagemUsuario = linguagem(); 
    if (nomeUsuario && idadeUsuario && linguagemUsuario){
        respostaDiaDois.innerHTML = `Olá <strong>${nomeUsuario}</strong>, você tem ${idadeUsuario} anos e já está aprendendo ${linguagemUsuario}!`;
        extra = perguntaExtra(linguagemUsuario);
        return respostaExtra.innerHTML = extra;
    }
    else{
        return respostaDiaDois.innerHTML = 'Todos os dados devem ser preenchidos!';
    }
        
}
function nome(){
    return prompt("Qual o seu nome?");
}
function idade(){
    return prompt("Qual a sua idade?");
}
function linguagem(){
    return prompt("Qual linguagem de programação você está estudando?");
}
function perguntaExtra(pLinguagem){
    let resposta;
    do{
        resposta = prompt(`Você gosta de estudar ${pLinguagem}? Responda com o número 1 para SIM ou 2 para NÃO`);
        if (resposta == 1){
            return "Muito bom! Continue estudando e você terá muito sucesso!";
        } 
        if (resposta == 2){
            return "Ahh que pena... Já tentou aprender outras linguagens?";
        }
    } while (resposta != '1' || resposta != '2');
}
perguntasDiaDois.addEventListener('click', perguntas);

